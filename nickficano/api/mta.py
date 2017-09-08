# -*- coding: utf-8 -*-
from flask import Blueprint, abort, request
import os
import requests
import xmltodict
from .mta_realtime import MtaSanitizer
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


@route(bp, '/get_by_route/<route_id>')
def get_by_route(route_id):
    stations = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            'stations.json')
    mta_api_key = "f651ffb45bdd555375328b81b33f6296"
    mta_sanitizer = MtaSanitizer(mta_api_key, stations)
    try:
        data = mta_sanitizer.get_by_route(route_id)
    except KeyError:
        abort(404)
    return data


@route(bp, '/get_by_location')
def get_by_location():
    stations = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            'stations.json')
    mta_api_key = "f651ffb45bdd555375328b81b33f6296"
    mta_sanitizer = MtaSanitizer(mta_api_key, stations)
    location = (float(request.args['lat']), float(request.args['lon']))

    try:
        data = mta_sanitizer.get_by_point(location, 5)
    except KeyError:
        abort(404)
    return data
