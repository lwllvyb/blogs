from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def foo():
   #data = json.loads(request.data)
   os.popen("/bin/sh ./redeploy_blog.sh")
   return "OK"

if __name__ == '__main__':
   app.run("0.0.0.0")
