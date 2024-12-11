from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    expenses = 0
    income = 0
    error_message = None

    if request.method == "POST":
        try:
            income = int(request.form.get("mon_inc", 0))
            housing = int(request.form.get("house", 0))
            trans = int(request.form.get("trans", 0))
            education = int(request.form.get("edu", 0))
            personal = int(request.form.get("per", 0))
            expenses = housing + trans + education + personal
        except ValueError:
            error_message = "Invalid input, please ensure all inputs are numeric."

    if income < expenses:
        message = "You have to look after your expensens"
    else:
        message = "Your Income and Expense ratio looks okay!"

    return render_template("index.html", expenses=expenses, income=income, error_message=error_message, message=message)

if __name__ == "__main__":
    app.run(debug=True)