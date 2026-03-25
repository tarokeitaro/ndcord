# ndcord
Simple Discord Rich Presence for Navidrome

> ## Disclaimer
> 
> Due to a lack of API support for currently playing songs from Navidrome / Subsonic, ndcord might run into some known issues:
> - Wrong now playing timestamp when pausing or repeating a song
> - When an ongoing song starts playing again, it does not show the presence UNTIL the next song is played.

## How does it work?
<img width="246" height="91" alt="image" src="https://github.com/user-attachments/assets/49e8bcdc-1f91-43ea-9798-f9fd1c155044" />
<img width="139" height="53" alt="image" src="https://github.com/user-attachments/assets/c793e343-0ea5-4a95-85e4-26bf903e6df1" />


ndcord takes JSON data from Navidrome Rest API and then sends it to an app using Discord Developer Portal via [pypresence](https://github.com/qwertyquerty/pypresence "pypresence"). 

It is designed to have a similar Spotify Discord presence look and feel, including:
- Album art from Navidrome itself (public, https-based server) or iTunes Store (http-based server).
- Progress bar (read [Disclaimer](#disclaimer))
- Artist name as Discord status instead of "Navidrome"


## How to start?
### Get Discord `client_id`
Create your new application in [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal"), and get `client_id`.

### Clone the Repository
Clone or download the repository.
```bash
git clone https://github.com/tarokeitaro/ndcord.git
```

### Virtual Environment (Optional)
If you don't want to disturb your global python environment, you can create a virtual environment.
```bash
python -m venv env
```
Then enter the virtual environment.

**Linux/MacOS**
```bash
source env/bin/activate
```
**Windows Command Prompt**
```bash
source env\Scripts\activate.bat
```
**Windows PowerShell**
```bash
source env\Scripts\Activate.ps1
```

### Requirements
This script requires `pypresence` and `requests`. Install these libraries via `pip`.
```bash
pip install requests
```
Currently, this script depends on the latest development version of `pypresence`.
```bash
pip install https://github.com/qwertyquerty/pypresence/archive/master.zip
```
### Edit `secret.json`
Fill in the data you have accordingly and this is mandatory!

**Important:** The `"server"` field must include `/` at the *end* of the URL.
```json
{
    "client_id": "xxxxxxxxxxxxxxxxxxx",
    "server": "https://your.ndhost.here/",
    "username": "john",
    "password": "john123"
}
```

### Start ndcord!
Just do this!
```bash
python ndcord.py
```
To stop the script, press `Ctrl + C`
