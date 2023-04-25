from flask import Flask, render_template
# localhost:5000

app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("index.html",
                            rows = 8,
                            columns = 8)

@app.route("/<row>")
def checkerboard_more(row):
    return render_template("index.html",
                            rows = int(row),
                            columns = 8)

@app.route("/<row>/<col>")
def checkerboard_extra(row, col):
    return render_template("index.html",
                            rows = int(row),
                            columns = int(col),
                            color_odd = "red",
                            color_even = "black")

@app.route("/<row>/<col>/<color1>/<color2>")
def checkerboard_colors(row, col, color1, color2):
    return render_template("index.html",
                            rows = int(row),
                            columns = int(col),
                            color_odd = color1,
                            color_even = color2)

if __name__ == "__main__":
    app.run(debug=True)