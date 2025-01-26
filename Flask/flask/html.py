from flask import Flask,render_template
### WSGI Application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this flask"
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)