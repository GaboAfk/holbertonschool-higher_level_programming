from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
    
def read_csv(csv_file_path):
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

def read_sql(sql_file_path):
    con = sqlite3.connect(sql_file_path)
    cur = con.cursor()
    res = cur.execute("SELECT * from Products")
    data = res.fetchall()
    #print("data SQL")
    #print(data)
    con.close()
    products_list = []
    for row in data:
        #[
        # (1, 'Laptop', 'Electronics', 799.99),
        # (2, 'Coffee Mug', 'Home Goods', 15.99)
        #]
        products_list.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products_list

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
            product_list = read_csv("products.csv")
        elif source == "sql":
            product_list = read_sql("products.db")
            #print("product_list SQL")
            #print(product_list)
        else:
            return render_template("product_display.html", error="Wrong source")
    except (json.decoder.JSONDecodeError, FileNotFoundError, sqlite3.OperationalError) as e:
        if source == "sql":
            print(f"error loading products.db: {e}")
        else:
            print(f"error loading products.{source}: {e}")

    if id is not None:
        product_id = None
        for items in product_list:
            if items.get("id") == int(id):
                product_id = [items]
                break
        if product_id is None:
                return render_template("product_display.html", error="Product not found")
        else:
            product_list = product_id

    return render_template("product_display.html", product_list=product_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)