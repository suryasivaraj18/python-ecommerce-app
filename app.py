from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "ecommerce-secret-key"

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Headphones", "price": 2000},
    {"id": 3, "name": "Keyboard", "price": 1500},
    {"id": 4, "name": "Mouse", "price": 800}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", [])

    for product in products:
        if product["id"] == product_id:
            cart.append(product)
            break

    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    total = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart=cart_items, total=total)

@app.route("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("success.html")

@app.route("/health")
def health():
    return {"status": "UP"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
