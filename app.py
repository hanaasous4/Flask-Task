from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def num_of_occurrence():
    input = request.args.get("arg", default="", type=str)
    occursence = {}.fromkeys([char for char in input],0)
    for char in input:
        occursence[char] += 1
    return occursence

if __name__ == "__main__":
    app.run(port=5000)
