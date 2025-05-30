# firestone_autoclicker

Features:
* claim and starts the firestone researches
* claims and starts alchemist researches (dust ones disabled by default)
* does map missions
* claims and starts oracle rituals
* claims and starts guild expeditions
* does machine daily missions
* if activated, upgrade preferred heroes (configurable in `firestone.ini`) and auto-prestige. Useful after prestiging
* auto-press preferred leader power (configurable in `firestone.ini`)
* fights in the arena
* gets the free pickaxes and hit the crystal
* claim daily and weekly quests
* spends the beer in the tavern
* uses the free train on the guardians
* hits the chaos
* open chests (apart chests that can contain sigils)
* gets daily rewards
* awake heroes
* claim reward from last message in the mailbox
* auto-claim stars in Decorated Heroes (if activated)

## Steps to make it working from source code

### For Windows

1. Install Python: https://www.python.org/downloads/windows/ (tested with Python 3.10)
2. Install git: https://git-scm.com/download/win
3. open a cmd: https://www.google.com/search?channel=fs&client=ubuntu-sn&q=windows+open+cmd
4. clone the repo with `git clone https://github.com/Marco-Sulla/firestone_autoclicker`
5. do `cd firestone_autoclicker`
6. `python -m venv venv`
7. `venv\Scripts\activate`
8. `pip install -r requirements.txt`
9. (optional) make sure the window with Firestone is the next one you access clicking alt+tab
10. `python firestone.py`
11. enjoy!

The game uses primarily image recognition, but it needs some x and y coordinates on the screen. You can customize them and other options in the file `firestone.ini`

If you want auto-upgrade of heroes and auto-prestige, `python firestone.py -p`

If you want to make the guardian hit for faster restart after prestige, `python firestone.py fire`

If you want to start also dust researches in Alchemist, `python firestone.py -d`

If you want to disable automatic Tavern, `python firestone.py -t` (useful for Decorated Heroes)

`python firestone.py pre` is equivalent to `python firestone.py fire -p`

If you want to claim starts in Decorated Heroes event, `python firestone.py -e` (only for laziness. Unclaimed stars in Decorated Heroes are sent in the mailbox anyway)
