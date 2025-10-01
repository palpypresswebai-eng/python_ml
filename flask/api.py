from flask import Flask, jsonify, request

app = Flask(__name__)
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "welcome to the sample to do list"

@app.route('/items',methods=['GET'])
def items():
    return jsonify(items)

if __name__=='__main__':
    app.run(debug=True)