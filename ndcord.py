import requests
from pypresence import Presence
import time, json

with open('secret.json') as f:
    secret_data = json.load(f)

client_id = secret_data.get('client_id', "")
server = secret_data.get('server', "")
username = secret_data.get('username', "")
password = secret_data.get('password', "")

RPC = Presence(client_id)
RPC.connect()

def get_now_playing_data(username, password):
    try:
        url = f"{server}rest/getNowPlaying.view?u={username}&p={password}&v=1.13.0&c=ndcord&f=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        now_playing_entries = data.get("subsonic-response", {}).get("nowPlaying", {}).get("entry", [])
        for entry in now_playing_entries:
            if entry.get("username") == username:
                return entry

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")

    return None

def update_presence(username):
    now_playing_data = get_now_playing_data(username, password)

    if now_playing_data:
        title = now_playing_data.get("title", "")
        artist = now_playing_data.get("artist", "")

        RPC.update(
            state=f"By: {artist}",
            details=title,
            large_image='navidrome',
            large_text='Navidrome Streaming Service',
            # Remove this if you don't want to include the button
            buttons=[{
                "label": "Listen Now!",
                "url": f"{server}"
            }],
            ### End of the button
        )

try:
    while True:
        update_presence(username)
        time.sleep(15)
except KeyboardInterrupt:
    RPC.close()
    print("")
    print("ndcord is terminated.")
