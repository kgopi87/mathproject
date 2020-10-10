import flask
from Authorization.Authentication import Auth
from . import routes

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@routes.route('/auth', methods=['GET'])
def token():
    return Auth().gettoken()
