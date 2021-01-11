from flask import Flask, redirect, url_for, render_template, request, session, abort, flash
from reddit import run

app = Flask(__name__,
            static_url_path='', 
            static_folder='',
            template_folder='')
app.secret_key = "PASSWORD"

@app.route('/', methods=['GET', 'POST'])
def home():
    url = ''
    try:
        subreddit = request.args.get('subreddit')
        url = run(subreddit)
    finally:
        return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)