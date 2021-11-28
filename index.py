from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        """
        Accepts GET requests and displays landing page.
        """
        return render_template('index.html')
