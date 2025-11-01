from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Thanks {name}! We got your email: {email}"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
