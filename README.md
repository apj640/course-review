# course-review
This project was implemented for Portland State's CS430P Internet, Web and Cloud Systems class. It is a simple
course review site built with HTML, Python, Gunicorn, Jinja2 and Flask with a Google Cloud Datastore backend. 
I modeled this project after an example from our instructor, Wu-Chang Feng, and modified it for course reviews. 
The original source can be viewed [here](https://github.com/wu4f/cs430-src). It is currently deployed as a Docker 
container on Google Cloud Run, and can be accessed [here](https://hw4-qu2dd6bijq-uw.a.run.app/).

## Instructions
To build and run locally:

1. Clone the repository.
2. Navigate to the project directory:
        cd course-review
3. Create a virtual environment
        python -m venv env
        source env/bin/activate
4. Install dependencies
        pip install -r requirements.txt
6. Run
        python app.py
7. In your browser, navigate to http://localhost:5000
