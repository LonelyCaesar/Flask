# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # 假設我們從資料夾渲染 index.html
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 這裡處理表單提交的邏輯
    username = request.form.get('username') # 讀取HTTP request
    return f"感謝註冊，{username}！"

if __name__ == '__main__':
    app.run(debug=True)