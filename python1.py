from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:吳咏壎<br>"
    X += "<a href=/mis>資訊管理導論</a><br>"
    X += "<a href=/today>日期時間</a><br>"
    X += "<a href=/welcome?nick=吳咏壎>傳送使用者暱稱</a><br>"
    X += "<a href=/S>我的個人網頁</a><br>"
    X += "<a href=/account>使用表單方式傳值</a><br>"
    return X

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/S")
def S():
    return render_template("S.html")

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime=str(now))

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

if __name__ == "__main__":
    app.run()
    serve(app, host='0.0.0.0', port=8080)

