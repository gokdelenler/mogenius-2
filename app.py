import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("git clone https://gokdelenler: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@github.com/gokdelenler/grup2 ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
