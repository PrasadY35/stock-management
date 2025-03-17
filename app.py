from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Use Railway's dynamic port
    app.run(debug=True, host="0.0.0.0", port=port)
