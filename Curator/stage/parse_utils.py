import json, httplib, urllib
from settings import SERVER_APP_ID, SERVER_REST_KEY, SERVER_URL, SERVER_HOST, SERVER_PORT, SERVER_MASTER_KEY


def save_object(classname, obj):
    connection = httplib.HTTPConnection(SERVER_HOST, SERVER_PORT)
    connection.connect()
    connection.request('POST', '/parse/classes/{}'.format(classname), json.dumps(obj), {
                           "X-Parse-Application-Id": SERVER_APP_ID,
                           "X-Parse-REST-API-Key": SERVER_REST_KEY,
                           "Content-Type": "application/json"
                       })
    return json.loads(connection.getresponse().read())


def send_push(msg):
    connection = httplib.HTTPConnection(SERVER_HOST, SERVER_PORT)
    connection.connect()
    connection.request('POST', '/parse/push', json.dumps({
        "channels": [
            "global"
        ],
        "data": {
            "alert": msg,
            "badge": "Increment",
            "push_type": "alert"
        }
    }), {
                           "X-Parse-Application-Id": SERVER_APP_ID,
                           "X-Parse-REST-API-Key": SERVER_REST_KEY,
                           "X-Parse-Master-Key": SERVER_MASTER_KEY,
                           "Content-Type": "application/json"
                       })
    result = json.loads(connection.getresponse().read())
    return result
