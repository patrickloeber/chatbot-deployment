import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Prompt three most commonly asked FAQs
samples = "Welcome to DiGiCOR. I am DiGiCOR Chatbot, and I can help answer your simple queries. <br>  1. If you wish to compare our systems model side by side filtering to your specifications, visit DiGiCOR Applicator. <br> 2. If you wish to obtain pricing, simply ask to speak to a live agent"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "DiGiCOR Chatbot"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
 
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.85:      #Increasing specifisity to reduce incorrect classifications
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return f"I'm sorry, but I cannot understand your query. {samples} "


if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

