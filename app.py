from flask import Flask, request, jsonify
app = Flask(__name__)

# Defining the API route
@app.route('/occurrence/api' , methods = ['GET'])
def num_of_occurrence():
    input = request.args.get("arg", default="", type=str)
    
    # Initializing dictionary (Using Characters in input String as keys and 0 as default
    # value for all keys)
    occurrence = {}.fromkeys([char for char in input],0)
    
    # Check if the input is empty string
    if len(occurrence) == 0:
        return jsonify ({"message": "Your input is empty, please provide a String"})

    # Iterating over characters in input string and update #of_occurrence for the current char in 
    # the dictionary by increasing the value by one
    for char in input:
        occurrence[char] += 1
    return jsonify({"Characters Occurrences": occurrence})

if __name__ == "__main__":
    app.run(port=5000, host= '0.0.0.0')
