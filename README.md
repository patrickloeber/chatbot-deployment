# Chatbot Training and Deployment

Objective: We are planning to deploy a new chatbot for our FAQ Page. 
           The chatbot should be able to identify certain key phrasings from user input, 
           such as the make and models of a specific product on our site, and often, 
           multiple products names will appear in a single input. 
           Our advanced search function currently yields the relevant results according to user queries. 
           We are looking to implement a chatbot that can aid user navigation via the chatbot by providing dynamic links to our advanced search page
           (comprising a list of filtered/relevant products according to user queries). 
           We have a specific format for our dynamic link generation but in order to construct it, 
           and we require the extraction of the aforementioned key phrases and entity recognition in order to amalgamate them into the required link structure.
           
Project Chatbot: https://docs.google.com/spreadsheets/d/17QFaHgvD6dlTbNiOdj4rlE-T3I7H9fXXHaNJVZ4-A0Y/edit?usp=sharing

Research: https://docs.google.com/document/d/11yLE81vcrzVn15s2jeLP5cnzcMiyKryaz84i_KLOtL4/edit?usp=sharing

Various approaches to DiGiCOR chatbot prototypes, ranked from best (1) to worst (7):
1. IBM Watson Assistant and Discovery
2. Amazon Lex
3. Wit.ai with Messenger
4. Python Libraries (NLTK/ Spacy)
5. Alterra.ai with Messenger
6. DialogFlow with Google AutoML
7. Microsoft Azure Cognitive Services for Language

Conclusion: Based on assessments of key features/functionality, IBM Watson Assistant (Plus) is the chosen approach as approved by Roham, Richard and Cathy.
            Begin by setting up the IBM Cloud Account (requires a credit/debit card, ask Cathy/Roham for it), there should be no immediate charge. 
            Start training the chatbot intents and utterances using IBM Watson Assistant Lite. Request for approval for Plus Subscription when required.
            Live Agent Handover, Dynamic Link Generation and FAQ training can all be handled by IBM Watson Assistant (Provides entity recognition and key-phrase extraction).
            Watson Discovery (optional extension) is a powerful search engine that performs web scraping for the site to yield potential relevant responses to unclear user input.
Guidelines: Develop your roadmap as required. 
            Training and Testing should take 2- 3 weeks.
Assistance: IBM Support - $250/month
            OutThought Consultant - $1800/day
