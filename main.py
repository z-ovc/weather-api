from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temprature = 23
    return {"station":station,
            "date":date,
            "temprature":temprature}

if __name__=="__main__":
    app.run(debug=True)