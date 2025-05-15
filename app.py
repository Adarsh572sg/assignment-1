from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        name = request.form["name1"]
        age = request.form.get("age")
        if age.isdigit():
            age = int(age)
            if age < 17:
                result = f"Hello, {name}! Age restriction: You are Not Allowed"
            else:
                result = f"Hello, {name}! Permission Granted: You are Eligible"
        else:
            result = "Please enter a valid age"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
