# Set model backend to be sqlite3
model_backend = 'sqlite3'
#model_backend = 'datastore'

""" 
Model backend can be changed later by commenting out previous line, 
setting model_backend to appropriate value and adding an elif
condition to the following conditional to import correct model
"""

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
elif model_backend == 'datastore':
    from .model_datastore import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

# Return the appropriate model


def get_model():
    return appmodel
