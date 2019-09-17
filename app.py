from flask import Flask, render_template
from static.python.elem_list import elem_list

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage"""

    return render_template('index.html')


@app.route('/lists')
def lists():
    """Return lists page"""
    e_list = elem_list()

    return render_template('lists.html', e_list=e_list)


@app.route('/search')
def search():
    """Return search page"""

    return render_template('search.html')
