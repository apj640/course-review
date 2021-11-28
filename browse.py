from flask import render_template
from flask.views import MethodView
import crmodel


class Browse(MethodView):
    def get(self):
        """
        Accepts GET requests and displays all reviews from database.
        """
        model = crmodel.get_model()
        reviews = [dict(author=row[0], dept=row[1], crnum=row[2],
                        qtr=row[3], year=row[4], instructor=row[5], review=row[6], rating=row[7]) for row in model.select()]
        return render_template('browse.html', reviews=reviews)
