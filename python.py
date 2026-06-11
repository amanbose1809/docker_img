from flask import Flask
app=Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return "flask app running on port:5500 of python"

app.run(port=5500,host="0.0.0.0")
