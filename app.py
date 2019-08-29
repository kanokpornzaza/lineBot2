from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    return "นางสาวกนกพร ลาวเวียง  เลขที่ 11 ชั้น ม.4/6"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    #user user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    user= decoded['originalDetectIntent']['data']['payload']['replyToken']
    #userText = decoded['queryResult']['intent']['displayName']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
    if (userText == 'คิดถึงเค้าไหม') :
        sendText(user,'คิดถึงมากเลยครับ')
    elif (userText == 'เป็นยังไงบ้าง') :
        sendText(user,'สบายดีครับ')
    else :
        sendText(user,'ติดงานอยู่')  
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
