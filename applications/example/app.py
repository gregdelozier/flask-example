from flask import Blueprint, render_template, redirect, url_for

app = Blueprint("example", __name__, url_prefix="/example", template_folder="templates")


@app.route("/")
def get_index():
    return render_template("example.html")

@app.route("/redirect")
def get_redirect():
    return redirect(url_for('example.get_index'))
    
