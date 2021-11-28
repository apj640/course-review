from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import crmodel


class Create(MethodView):
    def get(self):
        """
        Accepts GET requests, and displays form
        to create a course review.
        """
        return render_template('create.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to browse when completed.
        """
        model = crmodel.get_model()
        model.insert(request.form['author'],  request.form['dept'], request.form['crnum'],
                     request.form['qtr'], request.form['year'], request.form['instructor'],
                     request.form['review'], request.form['rating'])
        return redirect(url_for('browse'))
