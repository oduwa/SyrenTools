from flask import Flask, flash, request, redirect, render_template
import json
from create_mixtape import mixtape
from push import send_push_notification
application = Flask(__name__)


@application.route("/")
def home():
    return render_template('mixtape_creator.html')


@application.route("/push")
def push():
    return render_template('push.html')


@application.route("/create_mixtape", methods=['POST', 'GET'])
def create_mixtape():
    name = request.form["mixtape_name"]
    cover_img_url = request.form["img"]
    tracks = [request.form[key] for key in sorted(request.form.keys()) if key.startswith("track_")]
    print(tracks)
    return json.dumps(mixtape(name, "Syren", "Syren", tracks, [], cover_img_url))


@application.route("/handle_push", methods=['POST', 'GET'])
def handle_push():
    push_text = request.form["push_message"]
    return json.dumps(send_push_notification(push_text))


if __name__ == "__main__":
    application.debug = True
    application.run(use_reloader=False)