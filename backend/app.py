from flask import Flask,jsonify,request,send_file
from flask_cors import CORS,cross_origin
from checkthesite.check import Checker
import os

app =  Flask(__name__)
CORS(app)
checker = Checker()

@app.route('/',methods = ["GET","POST"])
def home():
    return 'Hello'

@app.route('/check',methods= ['GET'])
@cross_origin()
def checkTheSite():
        print("GET")
        response = jsonify({'data':'asdhajkshdkajs'})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

@app.route("/check",methods=["POST"])
@cross_origin()
def check():
    name = request.get_json()['name']
    url = request.get_json()['url']
    if(not url==""):
        checker.checkTheSite(url,name)
    res = os.walk(f'screenshots/{name}/')
    files = {}
    for folder,sub_folder,file in res:
        if folder in files:
            files[folder] = files[folder] + (file)
        else:
            files[folder] = file
    
    print(files)
    response = files
    
    return jsonify(response)

@app.route("/img/screenshots/<username>/<foldername>/<filename>",methods=["GET"])
@cross_origin()
def serve_image(username,foldername,filename):
     print(username,foldername,filename)
     return send_file(f"screenshots/{username}/{foldername}/{filename}")
     

if __name__=='__main__':
    app.run(debug=True)