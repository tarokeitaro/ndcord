# ndcord
Simple Discord Rich Presence for Navidrome

## How it works?
This python script takes Json data from Navidrome Rest API and then sends it to a Discord developer app via [pypresence](https://github.com/qwertyquerty/pypresence "pypresence").

## How to start?
### Get Discord client_id
Create your new application in the [Discord Developer Portal](https://discord.com/developers/applications "Discord Developer Portal"), and get `client_id`.

### Clone This Repository
Clone or download this repository.
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

### Download Requirements
This project requires the libraries `pypresence` and `requests`.
```bash
pip install requests
```
Currently, this project depends on the latest development version of pypresence.
```bash
pip install https://github.com/qwertyquerty/pypresence/archive/master.zip
```
### Change secret.json
Fill in according to the data you have and this is mandatory!

**Important**. The `"server"` field must include `/` at the *end* of the URL.
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

![image](https://github.com/tarokeitaro/ndcord/assets/42670754/a432c43e-2af2-4c0f-be53-cc1390321325)

To stop this program, click `ctrl + C`
