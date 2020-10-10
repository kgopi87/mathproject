import flask
from Authorization.Authentication import Auth
from flask import request, jsonify
from . import routes

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Maths - Multiplication
@routes.route('/maths/v1/multi', methods=['GET', 'POST'])
def multi():
    if not Auth().checktoken(request.headers.get('Auth')):
        return jsonify(ErrorMessage="Authentication has failed which is given in request headers"), 401

    if request.method == 'GET':
        if 'id1' and 'id2' in request.args:
            id1 = int(request.args['id1'])
            id2 = int(request.args['id2'])
        else:
            return jsonify("Error: No id field provided. Please specify an id."), 500

        ans = id1 * id2
        jsonObj = jsonify(id1=id1, id2=id2, Multipled=ans)
        app.logger.debug("Multiplication completed")

        return jsonObj

    if request.method == 'POST':
        if request.is_json:
            requestbody = request.get_json()
            id1 = int(requestbody['id1'])
            id2 = int(requestbody['id2'])
        else:
            return jsonify("Specified request body doesn't type is not JSON"), 500

        ans = id1 * id2
        jsonObj = jsonify(Multipled=ans)
        app.logger.debug("Multiplication completed")

        return jsonObj