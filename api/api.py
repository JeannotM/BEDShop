import os
from flask import Flask, send_from_directory
from flask_restful import Api
from resources import *

# ============================================================================================
# =================================================================== INITIALIZATION =========
# ============================================================================================

# Create a new Flask application
app = Flask(__name__)
# Add a secret key. Important for hashing (e.g. with login handling)
app.secret_key = os.getenv('SECRET')
# Create a new API
api = Api(app, prefix=os.getenv('API_PREFIX'))

# ============================================================================================
# =============================================================== FRONTEND REDIRECTS =========
# ============================================================================================

@app.route('/')
def index():
    """Redirects the base url '/' to the webshop/index.html file

    Returns:
        string: file content
    """
    return send_from_directory('../webshop', 'index.html')

@app.route('/<path:path>')
def shop(path):
    """Redirects all requests to the front end (webshop)

    Args:
        path (path): path to requested file

    Returns:
        string: file content
    """
    return send_from_directory('../webshop', path)
    
# ============================================================================================
# =================================================================== ERROR HANDLING =========
# ============================================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Returns a JSON on 404
    
    Returns:
        object: error message
    """
    return {'message': 'resource not found'}, 404
    
# ============================================================================================
# ======================================================================== ENDPOINTS =========
# ============================================================================================

api.add_resource(Categories, '/categories')

# ============================================================================================
# ================================================================ START APPLICATION =========
# ============================================================================================

if __name__ == '__main__':
    app.run(debug=True)
