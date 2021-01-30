import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def home():    
   return "Default Home Function Return"

@app.route('/second', methods = ['GET'])
def home2():    
   return "Second Function Return"

app.run(debug=True)
