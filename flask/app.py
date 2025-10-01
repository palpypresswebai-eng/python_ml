
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to over 1st flaskk" 

@app.route("/about")
def about():
    return "welcome to over about page" 


if __name__=="__main__":
    app.run(debug=True)


