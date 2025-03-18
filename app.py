from flask import Flask, send_file
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/stocks')
def show_stock():
    stock_data = """
Product Name: Urea Fertilizer
Quantity: 50 bags
Description: High-quality nitrogen fertilizer

Product Name: DAP Fertilizer
Quantity: 30 bags
Description: Phosphate-rich fertilizer for crops
    """
    return f"<pre>{stock_data}</pre>"

@app.route('/add_item', methods=['POST'])
def add_item():
    # Your code to add item to the stock
    return redirect(url_for('show_stock'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
