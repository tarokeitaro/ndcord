from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
from datetime import datetime
import time, json, re, requests

with open('secret.json') as f:
    secret_data = json.load(f)

# Basic information, getting from secret.json
client_id = secret_data.get('client_id', "")
server = secret_data.get('server', "")
username = secret_data.get('username', "")
password = secret_data.get('password', "")

RPC = Presence(client_id)
RPC.connect()
RPC.clear()

# Output when ndcord is running
print(f"[{datetime.now()}]\tndcord is running.")

# Get now playing data from Subsonic/Navidrome API
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
        print(f"[{datetime.now()}]\tConnection error: {e}")
    
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}]\tRequest exception: {e}")

    return None

last_state = None
last_song_id = None
song_start_ms = None
song_end_ms = None

# Update Discord presence
def update_presence(username):
    global last_song_id, song_start_ms, song_end_ms, last_state
    now_playing_data = get_now_playing_data(username, password)

    if now_playing_data:
        # Get currently playing song data
        title = now_playing_data.get("title", "")
        artist = now_playing_data.get("artist", "")
        song_id = now_playing_data.get("id", "")
        album = now_playing_data.get("album", "Unknown Album")
        # Get the album cover of the currently playing song. Using the iTunes album cover if the server is not publicly accessed. Fallback to navidrome default cover if nothing is found.
        try:
            if re.search(r":\d+", server):
                coverArt = requests.get(f"https://itunes.apple.com/search?term={title}+{artist}&entity=song&limit=1")
                art_url = json.loads(coverArt.text)["results"][0]["artworkUrl100"].replace("100x100bb.jpg", "600x600bb.jpg")
            else:
                coverArt = now_playing_data.get("coverArt")
                art_url = f"{server}rest/getCoverArt.view?id={coverArt}&u={username}&p={password}&v=1.16.1&c=ndcord&f=json"
        except Exception as e:
            art_url = "unknown"

        # Implementation of progress bar in Discord presence
        duration_ms = int(now_playing_data.get("duration", 0) or 0) * 1000
        duration = int(now_playing_data.get("duration", 0) or 0)
        mins, secs = divmod(duration, 60)

        if song_id != last_song_id:
            song_start_ms = int(time.time())
            song_end_ms = song_start_ms + duration
            last_song_id = song_id

        # Data for Discord presence
        RPC.update(
            activity_type=ActivityType.LISTENING,
            status_display_type=StatusDisplayType.STATE,
            state=artist,
            details=title,
            start=song_start_ms,
            end=song_end_ms,
            large_image=art_url,
            
            # Uncomment this if you want to include the button
            # buttons=[{
            #    "label": "Listen Now!",
            #    "url": f"{server}"
            # }],
            # end of the button
        )
        last_state = "playing"

    else:
        if last_state != "stopped":
            RPC.clear()
            last_state = "stopped"
            last_song_id = None
            song_start_ms = None
            song_end_ms = None
while True:
    try:
        update_presence(username)
        time.sleep(0.5)

    # Output error
    except Exception as e:
        print(f"[{datetime.now()}]\t{e}")
from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
from datetime import datetime
import time, json, re, requests

with open('secret.json') as f:
    secret_data = json.load(f)

# Basic information, getting from secret.json
client_id = secret_data.get('client_id', "")
server = secret_data.get('server', "")
username = secret_data.get('username', "")
password = secret_data.get('password', "")

RPC = Presence(client_id)
RPC.connect()
RPC.clear()

# Output when ndcord is running
print(f"[{datetime.now()}]\tndcord is running.")

# Get now playing data from Subsonic/Navidrome API
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
        print(f"[{datetime.now()}]\tConnection error: {e}")
    
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}]\tRequest exception: {e}")

    return None

last_state = None
last_song_id = None
song_start_ms = None
song_end_ms = None

# Update Discord presence
def update_presence(username):
    global last_song_id, song_start_ms, song_end_ms, last_state
    now_playing_data = get_now_playing_data(username, password)

    if now_playing_data:
        # Get currently playing song data
        title = now_playing_data.get("title", "")
        artist = now_playing_data.get("artist", "")
        song_id = now_playing_data.get("id", "")
        album = now_playing_data.get("album", "Unknown Album")
        # Get the album cover of the currently playing song. Using the iTunes album cover if the server is not publicly accessed. Fallback to navidrome default cover if nothing is found.
        try:
            if re.search(r":\d+", server):
                coverArt = requests.get(f"https://itunes.apple.com/search?term={title}+{artist}&entity=song&limit=1")
                art_url = json.loads(coverArt.text)["results"][0]["artworkUrl100"].replace("100x100bb.jpg", "600x600bb.jpg")
            else:
                coverArt = now_playing_data.get("coverArt")
                art_url = f"{server}rest/getCoverArt.view?id={coverArt}&u={username}&p={password}&v=1.16.1&c=ndcord&f=json"
        except Exception as e:
            art_url = "unknown"

        # Implementation of progress bar in Discord presence
        duration_ms = int(now_playing_data.get("duration", 0) or 0) * 1000
        duration = int(now_playing_data.get("duration", 0) or 0)
        mins, secs = divmod(duration, 60)

        if song_id != last_song_id:
            song_start_ms = int(time.time())
            song_end_ms = song_start_ms + duration
            last_song_id = song_id

        # Data for Discord presence
        RPC.update(
            activity_type=ActivityType.LISTENING,
            status_display_type=StatusDisplayType.STATE,
            state=artist,
            details=title,
            start=song_start_ms,
            end=song_end_ms,
            large_image=art_url,
            
            # Uncomment this if you want to include the button
            # buttons=[{
            #    "label": "Listen Now!",
            #    "url": f"{server}"
            # }],
            # end of the button
        )
        last_state = "playing"

    else:
        if last_state != "stopped":
            RPC.clear()
            last_state = "stopped"
            last_song_id = None
            song_start_ms = None
            song_end_ms = None
while True:
    try:
        update_presence(username)
        time.sleep(0.5)

    # Output error
    except Exception as e:
        print(f"[{datetime.now()}]\t{e}")
        while True:
            try:
                time.sleep(2)
                RPC = Presence(client_id)
                RPC.connect()
                break
            except:
                pass

    # Ctrl-C interaction
    except KeyboardInterrupt:
        RPC.close()
        print()
        print(f"[{datetime.now()}]\tndcord is terminated.")
        break

    # Ctrl-C interaction
    except KeyboardInterrupt:
        RPC.close()
        print()
        print(f"[{datetime.now()}]\tndcord is terminated.")
        break
