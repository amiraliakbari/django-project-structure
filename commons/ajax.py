# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse


def json_response(array):
    return HttpResponse(json.dumps(array), mimetype='application/json')


def xml_response(xml):
    return HttpResponse(xml, mimetype='application/xml')
