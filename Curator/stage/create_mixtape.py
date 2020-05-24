import soundcloud
import requests
import parse_utils
from settings import SOUNDCLOUD_CLIENT_KEY

client = soundcloud.Client(client_id=SOUNDCLOUD_CLIENT_KEY)


def track_from_url(song_url):
    def is_valid_response(res):
        return "id" in res and "title" in res and "artwork_url" in res and \
               "stream_url" in res and "duration" in res
    request_url = 'https://api.soundcloud.com/resolve?url={}&client_id={}'.format(song_url, SOUNDCLOUD_CLIENT_KEY)
    response = requests.get(request_url).json()
    if is_valid_response(response):
        return ":??:".join(map(str, [response["id"],
                                    response["title"],
                                    response["artwork_url"],
                                    '{}?client_id={}'.format(response["stream_url"], SOUNDCLOUD_CLIENT_KEY),
                                    response["duration"]]))
    else:
        print("WARNING: NO TRACK DATA FOUND FOR {}".format(song_url))
        return None


def mixtape(name, creator, owner, url_list, tags, cover_img_url):
    track_list = [track_from_url(url) for url in url_list]
    new_mixtape = {"hasBeenSeen":True,
                   "seen": True,
                   "tapeFromMessageBeenOpened": True,
                   "tracks": [track for track in track_list if track is not None],
                   "name": name,
                   "creator": creator,
                   "owner": owner,
                   "tags": tags,
                   "coverImageURL": cover_img_url
                   }
    return parse_utils.save_object("Mixtape",new_mixtape)
