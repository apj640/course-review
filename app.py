"""
A simple course review flask app.
"""
import flask, os
from flask.views import MethodView
from index import Index
from create import Create
from browse import Browse
app = flask.Flask(__name__)

app.add_url_rule('/', view_func=Index.as_view('index'), methods=["GET"])
app.add_url_rule('/create', view_func=Create.as_view('create'),
                 methods=["GET", "POST"])
app.add_url_rule(
    '/browse', view_func=Browse.as_view('browse'), methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
