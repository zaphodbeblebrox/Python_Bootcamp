from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<color>")
def index(color):
    users = ["Matt", "Brittany", "Sam", "Rishad", "Catrina", "Dana"]
    return render_template("index.html", 
                            monkey = "its a chimp",
                            print_this = False, 
                            users_list=users, 
                            color_value=color)

@app.route("/hi")
def teamwork():
    return "<h1>Success<h1>"



if __name__ == "__main__":
    app.run(debug=True)