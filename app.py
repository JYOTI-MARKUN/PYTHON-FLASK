from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") # static routes
@app.route("/home") 
def home_page():
    return render_template('home.html')  # it handels all our request and direct them into html page

@app.route("/about/<username>")  # dynamic routes
def about_page(username):
    return f"<h1> This is the about page of {username} </h1>"




if __name__ == "__main__":
    app.run(debug = True)