from flask import Flask, jsonify
from flask import render_template,request,redirect
import os

app = Flask(__name__)


@app.route("/")       
def index():
    return """
    <html>
    <body>
        <h1>Welcome to my Web Server!!</h1>
    <ul>
        <li><a href='/updatefortoday'>Update for Today</a></li>
        <li><a href='/share'>Share Today's Update</a></li>
        <li><a href='/clearnotepadtxt'>Clear Note</a></li>
    </ul>
    </body>
    </html>
    """

@app.route("/favicon.ico") 
def favicon():
    return app.send_static_file("favicon.ico")
    
    
@app.route("/updatefortoday", methods=['GET', "POST"])
def updatefortoday():
    if request.method == 'POST': 
        content = request.form.get("content", "")
        with open("today_update.txt", "a") as f:
            f.write(content)
        return f"<p>Update Saved</p><a href='/'> Go Home</a>"
        
    return """
    <html>
        <head>
            <title> Update for Today </title>
        </head>
        <body>
            <form action="/updatefortoday" method = "post">
            <textarea name = "content" rows ="10" cols="50"></textarea><br/>
            <input type = "submit" value = "submit"/>
            </form>
        </body>
    </html> """
    
@app.route("/share", methods=['GET'])
def share():
    try: 
        with open("today_update.txt", 'r') as f:
                content = f.read()
    except FileNotFoundError:
        content = "No update found"
    return f"<pre>{content}</pre><a href='/'> Go Home</a>"
            

@app.route("/clearnotepadtxt", methods=['GET'])
def clear_notepad_txt():
    open("today_update.txt", "w").close()
    return "<p>Note cleared</p><a href='/'> Go Home</a>"


if __name__ == '__main__':
    app.run()
