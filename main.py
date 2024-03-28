from flask import Flask
from flask import render_template


app=Flask(__name__)  #app=object


@app.route("/home")

def home():
    return render_template("home.html")


@app.route("/about")
def about_us():
    return render_template("about.html")



if __name__=="__main__":#port=backend
    app.run(port=1000,debug=True)