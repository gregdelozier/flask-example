from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html")


# register application blueprints
from applications.example.app import app as example

app.register_blueprint(example)

# start the server if necessary
if __name__ == "__main__":
    app.run(debug=True)
