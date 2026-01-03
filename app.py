from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["POST"])
def report():
    title = request.form.get("title")
    description = request.form.get("description")

    return f"Issue received: {title} - {description}"

if __name__ == "__main__":
    app.run(debug=True)
