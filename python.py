from flask import Flask
app=flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return "welcome to flask app"

app.run(port=5500,host="0.0.0.0",debug=True)
