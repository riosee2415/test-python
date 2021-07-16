from flask import Flask, render_template

app = Flask(__name__)
app.config["KEY"] = "pythondeploytestkey"


@app.route("/")
def home():

    image_path = "https://newsimg.sedaily.com/2021/01/21/22HCCECXD7_2.jpg"

    title = "Enaak Extra"
    content = "So good and delicious snack! if you eat, you will retry it!"

    return render_template("home.html", t=title, c=content, i=image_path)


app.run(debug=True)
