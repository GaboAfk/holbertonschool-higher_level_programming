from flask import Flask, render_template, request
import json
import csv

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

def read_json(json_file_path):
        with open(json_file_path) as f:
            return json.load(f)
    
def read_cvs(csv_file_path):
    with open(csv_file_path) as f:
        readfile = csv.DictReader(f)
        product_list = []
        for row in readfile:
            product_list.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return product_list

#@app.route("/products/<source>")
#@app.route("/products/<source>/<id>")
@app.route("/products")
def products():
#def products(source, id=None):
    source = request.args.get("source")
    id = request.args.get("id")

    product_list = []
    #print("llegue aca\n\n\n\n")
    try:
        if source == "json":
            product_list = read_json("products.json")
            #print("product_list JSON")
            #print(product_list)
        elif source == "csv":
            product_list = read_cvs("products.csv")
            #print("product_list CSV")
            #print(product_list)
        else:
            return render_template("product_display.html", error="Wrong source")
    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(f"error loading products.{source}: {e}")

    if id is not None:
        product_id = None
        for items in product_list:
            if items.get("id") == int(id):
                product_id = [items]
                break
        if product_id is None:
                return render_template("product_display.html", error="Product ID not found")
        else:
            product_list = product_id

    return render_template("product_display.html", product_list=product_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)