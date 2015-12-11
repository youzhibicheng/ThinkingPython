from flask import Flask, render_template
from flask.ext.babel import Babel, gettext as _

app = Flask(__name__)

@app.route('/')
def hello():
    day = "Saturday"
    return render_template('index_normal.html', day=day)

if __name__ == '__main__':
    app.debug = True
    app.run()