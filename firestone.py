import pyautogui as p
from pyautogui import ImageNotFoundException
from pathlib import Path
import time

curr_path = Path(__file__)
curr_dir = curr_path.parent
image_dir = curr_dir / "image"

guild_path = image_dir / "guild.png"
guild_expedition_path = image_dir / "guild_expedition.png"


def click_on_image(image):
	screen = p.screenshot()
	point = p.locateCenterOnScreen(str(image), confidence=0.9)
	p.click(*point)


p.keyDown('alt')
time.sleep(0.2)
p.press('tab')
time.sleep(0.2)
p.keyUp('alt')

time.sleep(0.5)

for _ in range(5):
	p.press('esc')

try:
	click_on_image(guild_path)
except ImageNotFoundException:
	pass

time.sleep(0.1)

click_on_image(guild_expedition_path)
