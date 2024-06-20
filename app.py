from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/influencer')
def influencer():
    return render_template("Influencer.html")

@app.route('/templates/Influencer.html')
def influencers():
    return render_template("Influencer.html")

@app.route('/sponsor')
def sponsor():
    return render_template("sponsor.html")

@app.route('/templates/sponsor.html')
def sponsors():
    return render_template("sponsor.html")


@app.route('/templates/index.html')
def index():
    return render_template("index.html")

@app.route('/templates/form.html')
def form():
    return render_template("form.html")

if __name__=="__main__":
    app.run()