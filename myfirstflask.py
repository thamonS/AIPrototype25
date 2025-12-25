from flask import Flask,  flash, redirect, request, render_template, make_response, url_for
import json
import sys 
#import pandas as pd

app = Flask(__name__)

@app.route("/")  #บอกว่าเรียกใช้ web ไหน
def helloworld():
    return "Hello, World!"

@app.route("/name")  #บอกว่าเรียกใช้ web ไหน
def name():
    return "Thamon Siriprahmanakul"

@app.route('/receive_get',methods=['GET']) #เพื่อรับ GET message
def web_service_API_GET():

    msg = request.args.get('msg')
    name = request.args.get('name')

    print(f'the input message from GET is {msg} from {name}.')

    return f'{msg} from {name} received!'

@app.route('/request',methods=['POST']) 
def web_service_API_POST():

    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload) # ทำ json

    print(inmessage)
    
    
    json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
    return json_data


if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5001)#host='0.0.0.0' = run on internet ,port=5001



# #web service
# ##api post
# @app.route('/request',methods=['POST']) 
# def web_service_API():

#     payload = request.data.decode("utf-8")
#     inmessage = json.loads(payload) # ทำ json

#     print(inmessage)
    
    
#     json_data = json.dumps({'y': 'received!'}) # ส่งกลับไปว่าได้รับเเล้ววว
#     return json_data



# @app.route("/")  #บอกว่าเรียกใช้ web ไหน
# def helloworld():
#     return "Hello, World!"

# @app.route("/name")  #บอกว่าเรียกใช้ web ไหน
# def hellonat():
#     return "Hello, Nat!"

# @app.route("/home", methods=['POST','GET']) # methods=['POST'] ต้องเปิดเพื่อให้รับข้อความ
# def homefn():
#     if request.method == "GET":
#        print('we are in home(GET)', file=sys.stdout)

#        namein = request.args.get('fname')
#        print(namein, file=sys.stdout)
#        return render_template("home.html",name=namein)

#     elif request.method == "POST":
#         print('we are in home(POST)', file=sys.stdout)
#         namein = request.form.get('fname') #เก็บ input
#         lastnamein = request.form.get('lname')
#         print(namein, file=sys.stdout)
#         print(lastnamein, file=sys.stdout)
#         #return render_template("home.html",name = f"{first_name} {last_name}")
#         return render_template("home.html",name=namein)

# @app.route('/upload', methods=['GET', 'POST'])  # เริ่มเเรก Get ไป return
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('filename')
#         return render_template("home.html",name= 'upload completed')

#     return '''  
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''