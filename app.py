from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Are you Hanpee"

@app.route("/option1")
def op1():
    return "I am hanpee"
if __name__=="__main__":
    app.run()