import requests
import parse_utils


def send_push_notification(msg):
    return parse_utils.send_push(msg)