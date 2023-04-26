from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

if __name__== "__main__":
    app.run(debug=True,port=8000) # port will set the web site port to someK number