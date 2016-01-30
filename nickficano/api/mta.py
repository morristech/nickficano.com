# -*- coding: utf-8 -*-
from flask import Blueprint
import requests
import xmltodict
from . import route

bp = Blueprint('mta', __name__, url_prefix='/mta')


@route(bp, '/status')
def get_status():
    url = "http://web.mta.info/status/serviceStatus.txt"
    resp = requests.get(url)
    mta_data = xmltodict.parse(resp.text)
    api = {}
    subway = (
        mta_data
        .get('service', {})
        .get('subway', {})
        .get('line', [])
    )
    for ln in subway:
        lines = list(ln['name'])
        status = ln['status']
        for l in lines:
            api[l] = status
    return api
