import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/items")
def items():
    try:
        item_list = []
        with open("items.json") as f:
            data = json.load(f)
        if isinstance(data, dict) and "items" in data:
            item_list = data["items"]
    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(f"error loading items.json: {e}")
    return render_template("items.html", item_list=item_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)