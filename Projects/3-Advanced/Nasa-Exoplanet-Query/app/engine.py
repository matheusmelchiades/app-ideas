from flask import Flask, render_template
from app.database import Database

app = Flask(__name__)
database = Database()


@app.route('/')
def index():
    payload = {
        'title': 'PLANETS',
        'fields': [
            'Year of discovery',
            'Discovery method',
            'Host name',
            'Discovery Facility'
        ],
        'data': database.find()
    }

    return render_template('index.html', **payload)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404-not-found.html'), 404
