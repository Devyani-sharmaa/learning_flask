from flask import Flask
from flask import render_template


app=Flask(__name__)  #app=object


@app.route("/home")

def home():
    return render_template("home.html")


@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/services")
def service():
    return render_template("services.html")

@app.route("/contact")
def cn():
    return render_template("MYHTML/contact.html")


if __name__=="__main__":#port=backend
    app.run(port=4000,debug=True)