# firestone_autoclicker

Features:
* auto-prestige
* claims and starts guild expeditions
* does map missions
* claims and starts oracle rituals
* does machine daily missions
* claim and starts the firestone researches
* fights in the arena
* gets the free pickaxes and hit the crystal
* gets daily and weekly rewards
* spends the beer in the tavern
* uses the free train on the guardians
* hits the chaos
* and something more

## Steps to make it working from source code

### For Windows

1. Install Python: https://www.python.org/downloads/windows/
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

If you want auto-prestige, `python firestone.py -p`

If you want to make the guardian hit for faster restart after prestige, `python firestone.py fire`

If you want to start also dust researches in Alchemist, `python firestone.py -d`

If you want to disable automatic Tavern, `python firestone.py -t`

If you want to automate claming in events (only Decorated Heroes for now), `python firestone.py -e`

`python firestone.py pre` is equivalent to `python firestone.py fire -p`
