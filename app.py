from flask import Flask, request
app = Flask(__name__)

# Defining the API route
@app.route('/')
def num_of_occurrence():
    input = request.args.get("arg", default="", type=str)
    # Initializing dictionary (Using Characters in input String as keys and 0 as default
    # value for all keys)
    occursence = {}.fromkeys([char for char in input],0)
    # Iterating over characters in input string and update #of_occurrence for the current char in 
    # the dictionary by increasing the value by one
    for char in input:
        occursence[char] += 1
    return occursence

if __name__ == "__main__":
    app.run(port=5000, host= '0.0.0.0')
