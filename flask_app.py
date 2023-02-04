import json
from flask import Flask , jsonify,request

app = Flask(__name__)

@app.route(rule = '/', methods = ['GET'])
def main():
    return "Hello world"

    
if __name__ == '__main__':
    app.run(host ="127.0.0.1",port="8080",debug = True)