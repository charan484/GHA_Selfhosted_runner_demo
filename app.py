from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>GitHub Actions Demo</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 100px;
            background-color: #f4f4f4;
        }
        .card {
            background: white;
            padding: 30px;
            width: 400px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        h1 {
            color: green;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>GitHub Actions CI/CD Demo</h1>
        <p>Python Flask Application</p>
        <p>Successfully deployed using Docker & GitHub Actions 🚀</p>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
