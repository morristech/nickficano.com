import requests
from flask import Blueprint

from . import route


bp = Blueprint('disturbed', __name__, url_prefix='/down/with')


@route(bp, '/the/sickness')
def down_with_the_sickness():
    url = (
        'http://api.bandsintown.com/artists/Disturbed/events.json?'
        'api_version=2.0&app_id=js_www.disturbed1.com&extended=true'
        '&widget_version=1.5.2'
    )
    resp = requests.get(url)
    return resp.json()
