from flask import Flask, send_file, request, redirect
import csv
import os

app = Flask(__name__)

STOCK_FILE = 'stock.csv'

# Initialize CSV if it doesn't exist
try:
    with open(STOCK_FILE, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Quantity", "Description"])
except FileExistsError:
    pass

@app.route('/')
def index():
    return send_file('index.html')  # Serve from main directory

@app.route('/add_stock', methods=['POST'])
def add_stock():
    name = request.form['name']
    quantity = request.form['quantity']
    description = request.form['description']

    if name and quantity and description:
        with open(STOCK_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, quantity, description])
    return redirect('/stocks')

@app.route('/stocks')
def stocks():
    try:
        with open(STOCK_FILE, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        data = [["No Data", "No Data", "No Data"]]

    with open("stocks.html", "r") as file:
        html_template = file.read()

    table_rows = ""
    for row in data[1:]:
        table_rows += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
    
    html_template = html_template.replace("<!-- DATA_PLACEHOLDER -->", table_rows)
    return html_template

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
