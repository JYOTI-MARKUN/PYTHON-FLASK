from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") # static routes
@app.route("/home") 
def home_page():
    return render_template('home.html')  # it handels all our request and direct them into html page

@app.route('/market')
def market_page():
    item_list = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('Market.html',Items = item_list)


@app.route("/about/<username>")  # dynamic routes
def about_page(username):
    return f"<h1> This is the about page of {username} </h1>"




if __name__ == "__main__":
    app.run(debug = True)