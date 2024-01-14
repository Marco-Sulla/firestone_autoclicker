import pyautogui as p
from pyautogui import ImageNotFoundException
from pyscreeze import ImageNotFoundException as ImageNotFoundException2
from pathlib import Path
import time
import sys
import logging
import random
import configparser

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
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
coordinates_conf = config["coordinates"]

home_x = int(coordinates_conf["home_x"])
home_y = int(coordinates_conf["home_y"])
delta_x = int(coordinates_conf["delta_x"])
delta_y = int(coordinates_conf["delta_y"])

image_ext = ".png"

guild_path = image_dir / f"guild{image_ext}"

guild_expedition_advice_path = (
    image_dir / 
    f"guild_expedition_advice{image_ext}"
)

guild_start_expedition_path = image_dir / f"guild_start_expedition{image_ext}"
guild_shop_path = image_dir / f"guild_shop{image_ext}"
guild_supplies_path = image_dir / f"guild_supplies{image_ext}"
guild_supplies_2_path = image_dir / f"guild_supplies_2{image_ext}"

claim_green_path = image_dir / f"claim_green{image_ext}"
claim_dark_green_path = image_dir / f"claim_dark_green{image_ext}"
claim_dark_green_2_path = image_dir / f"claim_dark_green_2{image_ext}"
claim_rewards_path = image_dir / f"claim_rewards{image_ext}"

start_path = image_dir / f"start{image_ext}"
free_path = image_dir / f"free{image_ext}"
check_in_path = image_dir / f"check_in{image_ext}"
n1500_path = image_dir / f"1500{image_ext}"
n5_path = image_dir / f"5{image_ext}"
n5_red_path = image_dir / f"5_red{image_ext}"

machine_advice_path = image_dir / f"machine_advice{image_ext}"
machine_claim_loot_path = image_dir / f"machine_claim_loot{image_ext}"

quest_advice_path = image_dir / f"quest_advice{image_ext}"
quest_daily_path = image_dir / f"quest_daily{image_ext}"
quest_weekly_path = image_dir / f"quest_weekly{image_ext}"

pickaxe_advice_path = image_dir / f"pickaxe_advice{image_ext}"

crystal_advice_path = image_dir / f"crystal_advice{image_ext}"
crystal_hit_path = image_dir / f"crystal_hit{image_ext}"

map_advice_1_path = image_dir / f"map_advice_1{image_ext}"
map_advice_2_path = image_dir / f"map_advice_2{image_ext}"
map_advice_3_path = image_dir / f"map_advice_3{image_ext}"
map_advice_4_path = image_dir / f"map_advice_4{image_ext}"
map_advice_5_path = image_dir / f"map_advice_5{image_ext}"
map_advice_6_path = image_dir / f"map_advice_6{image_ext}"
map_advice_7_path = image_dir / f"map_advice_7{image_ext}"
map_mission_war_path = image_dir / f"map_mission_war{image_ext}"
map_mission_adventure_path = image_dir / f"map_mission_adventure{image_ext}"
map_mission_scout_path = image_dir / f"map_mission_scout{image_ext}"
map_mission_monster_path = image_dir / f"map_mission_monster{image_ext}"
map_mission_dragon_path = image_dir / f"map_mission_dragon{image_ext}"

shop_advice_1_path = image_dir / f"shop_advice_1{image_ext}"
shop_advice_2_path = image_dir / f"shop_advice_2{image_ext}"
shop_advice_3_path = image_dir / f"shop_advice_3{image_ext}"
shop_advice_4_path = image_dir / f"shop_advice_4{image_ext}"
shop_advice_5_path = image_dir / f"shop_advice_5{image_ext}"
shop_daily_rewards_path = image_dir / f"shop_daily_rewards{image_ext}"

tavern_advice_path = image_dir / f"tavern_advice{image_ext}"


main_screen = True


def click(point):
    p.moveTo(*point)
    time.sleep(0.2)
    p.click()


def click_on_image(image, all=False, confidence=0.9):
    if all:
        locations = p.locateAllOnScreen(str(image), confidence=confidence)
        
        for location in locations:
            point = p.center(location)
            click(point)
            time.sleep(0.2)
    else:
        point = p.locateCenterOnScreen(str(image), confidence=confidence)
        click(point)


def get_main_screen(main_screen, arg_is_fire):
    if not main_screen:
        for _ in range(5):
            p.press("esc")

    if arg_is_fire:
        p.moveTo(
            home_x + random.randint(0, delta_x), 
            home_y + random.randint(0, delta_y)
        )

    return True


def do_guild_expedition(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
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
        click_on_image(claim_green_path)
    except ImageNotFoundException:
        logger.debug("No guild expedition to claim")
    else:
        logger.info("Guild expedition claimed")
        did_something = True
        time.sleep(1)

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


def do_machine(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(machine_advice_path, confidence=0.8)
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


def do_quest(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
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
        click_on_image(quest_daily_path)
    except ImageNotFoundException:
        logger.error("Failed to find daily quest button")
    else:
        time.sleep(0.2)

        try:
            click_on_image(claim_green_path)
        except ImageNotFoundException:
            logger.debug("No daily quest to claim")
        else:
            logger.info("Daily quest claimed")
            did_something = True
            time.sleep(2)

    try:
        click_on_image(quest_weekly_path)
    except ImageNotFoundException:
        logger.error("Failed to find weekly quest button")
    else:
        time.sleep(0.2)

        try:
            click_on_image(claim_green_path)
        except ImageNotFoundException:
            logger.debug("No weekly quest to claim")
        else:
            logger.info("Weekly quest claimed")
            did_something = True


    if not did_something:
        logger.error("Failed to claim a daily or weekly quest")

    return main_screen


def get_pickaxes(main_screen, arg_is_fire, from_advice=False):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    if from_advice:
        try:
            click_on_image(pickaxe_advice_path)
        except ImageNotFoundException:
            logger.debug("No pickaxe advice")
            return main_screen
        else:
            main_screen = False
    else:
        for _ in range(10):
            guild_found = False
            
            try:
                click_on_image(guild_path)
            except ImageNotFoundException:
                time.sleep(0.5)
            else:
                main_screen = False
                guild_found = True
                break
        
        if not guild_found:
            logger.error("Failed to find guild")
            return main_screen

        time.sleep(0.2)

        try:
            click_on_image(guild_shop_path, confidence=0.8)
        except ImageNotFoundException:
            logger.error("Failed to find guild shop")
            return main_screen

        time.sleep(0.2)

        try:
            click_on_image(guild_supplies_path)
        except ImageNotFoundException:
            try:
                p.locateOnScreen(guild_supplies_2_path)
            except ImageNotFoundException:
                logger.error("Failed to find guild supplies")
                return main_screen

    time.sleep(0.2)

    try:
        click_on_image(claim_dark_green_2_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get pickaxes")
    else:
        logger.info("Piackaxes claimed")

    return main_screen


def hit_the_crystal(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
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
            click_on_image(crystal_hit_path)
            logger.info(f"Hit the crystal number {hits}")
            time.sleep(3)
        except ImageNotFoundException:
            logger.info("Crystal hit finished")
            break

        hits += 1

    return main_screen


def do_map_mission(mission_path, mission_type):
    mission_started = False
    
    try:
        locations = p.locateAllOnScreen(str(mission_path), confidence=0.7)
        
        for i, location in enumerate(locations):
            point = p.center(location)
            click(point)
            time.sleep(0.2)
            
            try:
                click_on_image(start_path)
            except ImageNotFoundException:
                logger.debug(f"Failed to start the {mission_type} mission")
                p.press("esc")
            else:
                logger.info(f"Mission of type {mission_type} started")
                mission_started = True
                time.sleep(0.2)
    except ImageNotFoundException2 as e:
        logger.debug("No {mission_type} missions")
    
    if not mission_started:
        logger.debug(f"Failed to start any mission of type {mission_type}")
    


def do_map(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(map_advice_1_path, confidence=0.95)
    except ImageNotFoundException:
        try:
            click_on_image(map_advice_2_path)
        except ImageNotFoundException:
            try:
                click_on_image(map_advice_3_path)
            except ImageNotFoundException:
                try:
                    click_on_image(map_advice_4_path)
                except ImageNotFoundException:
                    try:
                        click_on_image(map_advice_5_path)
                    except ImageNotFoundException:
                        try:
                            click_on_image(map_advice_6_path)
                        except ImageNotFoundException:
                            try:
                                click_on_image(map_advice_7_path)
                            except ImageNotFoundException:
                                logger.debug("No map advice")
                                return main_screen
                            else:
                                main_screen = False
                        else:
                            main_screen = False
                    else:
                        main_screen = False
                else:
                    main_screen = False
            else:
                main_screen = False
        else:
            main_screen = False
    else:
        main_screen = False

    time.sleep(0.2)
    
    
    i = 0
    
    while True:
        try:
            click_on_image(claim_dark_green_path, confidence=0.8)
        except ImageNotFoundException:
            break
        
        i += 1
        
        time.sleep(2)
        
        try:
            click_on_image(claim_rewards_path, confidence=0.7)
        except ImageNotFoundException:
            logger.error("Unable to confirm map reward claim")
        
        time.sleep(0.2)
        
    logger.info(f"{i} map loots claimed")
    
    time.sleep(2)
    
    do_map_mission(map_mission_monster_path, "monster")
    do_map_mission(map_mission_war_path, "war")
    do_map_mission(map_mission_scout_path, "scout")
    do_map_mission(map_mission_adventure_path, "adventure")
    do_map_mission(map_mission_dragon_path, "dragon")

    return main_screen


def do_shop(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        logger.debug("Clicking on shop advice 1")
        click_on_image(shop_advice_1_path, confidence=0.95)
    except ImageNotFoundException:
        try:
            logger.debug("Clicking on shop advice 2")
            click_on_image(shop_advice_2_path, confidence=0.98)
        except ImageNotFoundException:
            try:
                logger.debug("Clicking on shop advice 3")
                click_on_image(shop_advice_3_path, confidence=0.98)
            except ImageNotFoundException:
                try:
                    logger.debug("Clicking on shop advice 4")
                    click_on_image(shop_advice_4_path, confidence=1)
                except ImageNotFoundException:
                    try:
                        logger.debug("Clicking on shop advice 5")
                        click_on_image(shop_advice_5_path, confidence=0.99)
                    except ImageNotFoundException:
                        logger.debug("No shop advice")
                        return main_screen
                    else:
                        main_screen = False
                else:
                    main_screen = False
            else:
                main_screen = False
        else:
            main_screen = False
    else:
        main_screen = False
    
    time.sleep(0.2)

    try:
        click_on_image(free_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get shop free gift")
    
    time.sleep(0.2)
    
    try:
        click_on_image(shop_daily_rewards_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to find daily rewards button")
        
        return main_screen
    else:
        logger.info("Claimed daily shop reward")
    
    try:
        click_on_image(check_in_path)
    except ImageNotFoundException:
        logger.error(
            "Failed to find daily shop check in daily rewards button"
        )
    else:
        logger.info("Claimed weekly shop reward")
        
    return main_screen


def do_tavern(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(tavern_advice_path)
    except ImageNotFoundException:
        logger.debug("No tavern advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(1)
    
    try:
        click_on_image(n1500_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get 5 tavern tokens")
        return main_screen
    
    time.sleep(2)
    p.press("esc")
    
    try:
        click_on_image(n5_path)
    except ImageNotFoundException:
        logger.error("Failed to bet 5 tavern tokens")
        return main_screen
    
    time.sleep(1)
    
    try:
        click_on_image(n5_red_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get 5 tavern cards")
    
    time.sleep(5)
    
    return main_screen
    


def check(main_screen, arg_is_fire):
    main_screen = do_guild_expedition(main_screen, arg_is_fire)
    # main_screen = do_machine(main_screen, arg_is_fire)
    main_screen = do_quest(main_screen, arg_is_fire)
    main_screen = hit_the_crystal(main_screen, arg_is_fire)
    main_screen = get_pickaxes(main_screen, arg_is_fire, from_advice=True)
    main_screen = do_map(main_screen, arg_is_fire)
    main_screen = do_shop(main_screen, arg_is_fire)
    main_screen = do_tavern(main_screen, arg_is_fire)
    
    main_screen = get_main_screen(main_screen, arg_is_fire)

    return main_screen


p.keyDown("alt")
time.sleep(0.2)
p.press("tab")
time.sleep(0.2)
p.keyUp("alt")

time.sleep(0.5)

fire_arg = "fire"
possible_args = (fire_arg, )

try:
    arg = sys.argv[1]

    if arg not in possible_args:
        raise ValueError(
            f"argument must be one of this values: {possible_args}"
        )
except IndexError:
    arg = None

arg_is_fire = arg == fire_arg

wait_sec = 20 if arg_is_fire else 3
wait_sec_packaxes = 5737

now = time.time()
prev_time = now - wait_sec - 2
prev_time_pickaxes = now - wait_sec_packaxes - 2

while True:
    curr_time = time.time()

    if curr_time - prev_time_pickaxes >= wait_sec_packaxes:
        main_screen = get_pickaxes(main_screen, arg_is_fire)
        prev_time_pickaxes = time.time()

    if curr_time - prev_time >= wait_sec:
        main_screen = check(main_screen, arg_is_fire)
        prev_time = time.time()
    
    if arg_is_fire:    
        p.click(interval=0.2)
