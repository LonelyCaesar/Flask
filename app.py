from flask import Flask
from flask import render_template

#建立Flask類別的實體(instance)
app = Flask(__name__)

# 配對網址和執行的函數
@app.route("/page")
def home():
    lst = [
          {"name":"aaa","age":99},
          {"name":"bbb","age":88},
          {"name":"ccc","age":77},
    ]
    return render_template("index.html", name=lst)
    
if __name__ == "__main__":
	app.run(debug=True)