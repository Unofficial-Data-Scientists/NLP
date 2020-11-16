from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__,static_url_path='',static_folder='./static')
CORS(app)

#Loading all the endpoints written in endpoints dir
from q_a_api.endpoints.ml_endpoints import predict

def main():    
    app.run(debug=False)
    print("Server started")