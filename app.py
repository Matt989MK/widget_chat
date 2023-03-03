from flask import Flask, render_template
from database import get_company_info
from werkzeug.debug import DebuggedApplication
import database as db
from database import init_app
app = Flask(__name__)
db.init_app(app)
app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE='database.db',
)
app.debug = True
import logging
logging.basicConfig(level=logging.DEBUG)
@app.route('/')
def home():
    info = get_company_info()
    return render_template('home.html', info=info)

@app.errorhandler(500)
def internal_server_error(error):
    return 'Internal Server Error: {}'.format(error), 500



if __name__ == '__main__':
    app.run(debug=True)