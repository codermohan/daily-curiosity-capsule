from flask import Flask, render_template
import datetime
import hashlib

app = Flask(__name__)

def get_daily_curiosity():
    with open("curiosities.txt") as file:
        curiosities = file.readlines()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    index = int(hashlib.md5(date_str.encode()).hexdigest(), 16) % len(curiosities)
    return curiosities[index].strip()

@app.route("/")
def home():
    curiosity = get_daily_curiosity()
    return render_template("index.html", curiosity=curiosity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
