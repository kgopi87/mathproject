from flask import render_template, Flask
from Maths import *


app = Flask(__name__)
app.template_folder = "html"
app.config["DEBUG"] = True
app.register_blueprint(routes)


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


if __name__ == '__main__':
    # Flask Application Run
    app.run()
