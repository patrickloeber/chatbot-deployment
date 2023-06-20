from chat import get_response
import sys

# Access command-line arguments
args = sys.argv[1:]

# Check if any arguments were provided
if len(args) > 0:
    process_var = args[0]
    print(get_response(args[0]))
else:
    print("No command-line argument provided.")
