from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Please success"

@app.route("/option1")
def op1():
    return "Lets go"
if __name__=="__main__":
    app.run()
