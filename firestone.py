import pyautogui as p
from pyautogui import ImageNotFoundException
from pathlib import Path
import time
import sys
import logging
import random
import configparser

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
level = logging.INFO
logger.setLevel(level)
handler.setLevel(level)
handler.setFormatter(formatter)
logger.addHandler(handler)

curr_path = Path(__file__)
curr_dir = curr_path.parent
image_dir = curr_dir / "image"
ini_path = curr_dir / "firestone.ini"

config = configparser.ConfigParser()
config.read(ini_path)
config.sections()
coordinates_conf = config['coordinates']

home_x = int(coordinates_conf["home_x"])
home_y = int(coordinates_conf["home_y"])
delta_x = int(coordinates_conf["delta_x"])
delta_y = int(coordinates_conf["delta_y"])

guild_path = image_dir / "guild.png"
guild_expedition_path = image_dir / "guild_expedition.png"
guild_expedition_advice_path = image_dir / "guild_expedition_advice.png"
guild_start_expedition_path = image_dir / "guild_start_expedition.png"
guild_shop_path = image_dir / "guild_shop.png"
guild_supplies_path = image_dir / "guild_supplies.png"

green_claim_path = image_dir / "green_claim.png"
dark_green_claim_path = image_dir / "dark_green_claim.png"
machine_advice_path = image_dir / "machine_advice.png"
machine_claim_loot_path = image_dir / "machine_claim_loot.png"
quest_advice_path = image_dir / "quest_advice.png"
quest_weekly_path = image_dir / "quest_weekly.png"
pickaxe_advice_path = image_dir / "pickaxe_advice.png"
crystal_advice_path = image_dir / "crystal_advice.png"
hit_the_crystal_path = image_dir / "hit_the_crystal.png"

main_screen = True

def click_on_image(image):
	screen = p.screenshot()
	point = p.locateCenterOnScreen(str(image), confidence=0.9)
	p.moveTo(*point)
	time.sleep(0.2)
	p.click()


def get_main_screen(main_screen):
	if not main_screen:
		for _ in range(5):
			p.press('esc')

	p.moveTo(home_x + random.randint(0, delta_x), home_y + random.randint(0, delta_y))

	return True


def do_guild_expedition_2(main_screen):
	main_screen = get_main_screen(main_screen)
	
	try:
		click_on_image(guild_path)
	except ImageNotFoundException:
		pass
	else:
		main_screen = False

	time.sleep(0.2)

	try:
		click_on_image(guild_expedition_path)
		time.sleep(0.2)
		click_on_image(guild_start_expedition_path)
	except ImageNotFoundException:
		pass

	return main_screen


def do_guild_expedition(main_screen):
	main_screen = get_main_screen(main_screen)
	
	try:
		click_on_image(guild_expedition_advice_path)
	except ImageNotFoundException:
		logger.debug("No guild expedition advice")
		return main_screen
	else:
		main_screen = False

	time.sleep(0.4)
	
	did_something = False

	try:
		click_on_image(green_claim_path)
		time.sleep(1)
	except ImageNotFoundException:
		logger.debug("No guild expedition to claim")
	else:
		logger.info("Guild expedition claimed")
		did_something = True

	try:
		click_on_image(guild_start_expedition_path)
	except ImageNotFoundException:
		logger.debug("No guild expedition to start")
	else:
		logger.info("Guild expedition started")
		did_something = True

	if not did_something:
		logger.error("Failed to claim or start a guild expedition")

	return main_screen


def do_machine(main_screen):
	main_screen = get_main_screen(main_screen)
	
	try:
		click_on_image(machine_advice_path)
	except ImageNotFoundException:
		logger.debug("No machine advice")
		return main_screen
	else:
		main_screen = False

	time.sleep(0.2)

	try:
		click_on_image(machine_claim_loot_path)
	except ImageNotFoundException:
		logger.debug("No machine loot")
	else:
		logger.info("Machine loot claimed")

	return main_screen


def do_quest(main_screen):
	main_screen = get_main_screen(main_screen)
	
	try:
		click_on_image(quest_advice_path)
	except ImageNotFoundException:
		logger.debug("No quest advice")
		return main_screen
	else:
		main_screen = False

	time.sleep(0.2)

	did_something = False

	try:
		click_on_image(green_claim_path)
	except ImageNotFoundException:
		logger.debug("No daily quest to claim")
	else:
		logger.info("Daily quest claimed")
		did_something = True

	time.sleep(0.2)

	try:
		click_on_image(quest_weekly_path)
	except ImageNotFoundException:
		logger.error("Failed to find weekly quest button")

	time.sleep(0.2)

	try:
		click_on_image(green_claim_path)
	except ImageNotFoundException:
		logger.debug("No weekly quest to claim")
	else:
		logger.info("Weekly quest claimed")
		did_something = True


	if not did_something:
		logger.error("Failed to claim a daily or weekly quest")

	return main_screen


def get_pickaxes(main_screen, from_advice=False):
	main_screen = get_main_screen(main_screen)
	
	if from_advice:
		try:
			click_on_image(pickaxe_advice_path)
		except ImageNotFoundException:
			logger.debug("No pickaxe advice")
			return main_screen
		else:
			main_screen = False
	else:
		try:
			click_on_image(guild_path)
		except ImageNotFoundException:
			logger.error("Failed to find guild")
			return main_screen
		else:
			main_screen = False

		time.sleep(0.2)

		try:
			click_on_image(guild_shop_path)
		except ImageNotFoundException:
			logger.error("Failed to find guild shop")
			return main_screen

		time.sleep(0.2)

		try:
			click_on_image(guild_supplies_path)
		except ImageNotFoundException:
			logger.error("Failed to find guild supplies")
			return main_screen

	time.sleep(0.2)

	try:
		click_on_image(dark_green_claim_path)
	except ImageNotFoundException:
		logger.error("Failed to get pickaxes")

	return main_screen


def hit_the_crystal(main_screen):
	main_screen = get_main_screen(main_screen)
	
	try:
		click_on_image(crystal_advice_path)
	except ImageNotFoundException:
		logger.debug("No crystal advice")
		return main_screen
	else:
		main_screen = False

	time.sleep(0.2)
	hits = 1

	while True:
		try:
			click_on_image(hit_the_crystal_path)
			logger.info(f"Hit the crystal number {hits}")
			time.sleep(2)
		except ImageNotFoundException:
			logger.debug("Crystal hit finished")
			break

		hits += 1

	return main_screen


def check(main_screen):
	main_screen = do_guild_expedition(main_screen)
	main_screen = do_machine(main_screen)
	main_screen = do_quest(main_screen)
	main_screen = hit_the_crystal(main_screen)
	main_screen = get_main_screen(main_screen)
	main_screen = get_pickaxes(main_screen, from_advice=True)

	return main_screen


p.keyDown('alt')
time.sleep(0.2)
p.press('tab')
time.sleep(0.2)
p.keyUp('alt')

time.sleep(0.5)

fire_arg = "fire"
possible_args = (fire_arg, )

try:
	arg = sys.argv[1]

	if arg not in possible_args:
		raise ValueError(f"argument must be one of this values: {possible_args}")
except IndexError:
	arg = None

arg_is_fire = arg == fire_arg

wait_sec = 20 if arg_is_fire else 3
wait_sec_packaxes = 4800

prev_time = time.time() - wait_sec - 2
prev_time_pickaxes = prev_time

while True:
	if arg_is_fire:	
		p.click(interval=0.2)

	curr_time = time.time()

	if curr_time - prev_time_pickaxes >= wait_sec_packaxes:
		main_screen = get_pickaxes(main_screen)
		prev_time_pickaxes = time.time()

	if curr_time - prev_time >= wait_sec:
		main_screen = check(main_screen)
		prev_time = time.time()
