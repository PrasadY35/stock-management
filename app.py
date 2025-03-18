from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# CSV File Path
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
    return render_template('index.html')

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
    
    return render_template('stocks.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
