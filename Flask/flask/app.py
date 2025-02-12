from flask import Flask
#wsgi
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this flask"

if __name__=="__main__":
    app.run(debug=True)