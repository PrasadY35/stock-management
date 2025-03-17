\from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serve stock page

@app.route('/stocks')
def show_stock():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Stock List</title>
</head>
<body>
    <h1>📦 Available Stock</h1>
    <pre id="stock-page">
        <script>
            document.write(localStorage.getItem("stockPage") || "No stock available.");
        </script>
    </pre>
</body>
</html>
"""  # This dynamically loads stock data from localStorage

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Railway provides PORT env variable
    app.run(debug=True, host="0.0.0.0", port=port)
