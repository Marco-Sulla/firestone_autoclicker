import pyautogui as p
from pyautogui import ImageNotFoundException
from pyscreeze import ImageNotFoundException as ImageNotFoundException2
from pathlib import Path
import time
import sys
import logging
import random
import configparser
import argparse

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
level = logging.ERROR
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
advice_up_x = int(coordinates_conf["advice_up_x"])
advice_up_y = int(coordinates_conf["advice_up_y"])
advice_down_x = int(coordinates_conf["advice_down_x"])
advice_down_y = int(coordinates_conf["advice_down_y"])

center_left_x = int(coordinates_conf["center_left_x"])
center_left_y = int(coordinates_conf["center_left_y"])
center_right_x = int(coordinates_conf["center_right_x"])
center_right_y = int(coordinates_conf["center_right_y"])

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
claim_green_big_path = image_dir / f"claim_green_big{image_ext}"
claim_dark_green_2_path = image_dir / f"claim_dark_green_2{image_ext}"
claim_dark_green_3_path = image_dir / f"claim_dark_green_3{image_ext}"
claim_dark_green_4_path = image_dir / f"claim_dark_green_4{image_ext}"
claim_dark_green_5_path = image_dir / f"claim_dark_green_5{image_ext}"
claim_rewards_path = image_dir / f"claim_rewards{image_ext}"
claim_map_path = image_dir / f"claim_map{image_ext}"
claim_research_path = image_dir / f"claim_research{image_ext}"

start_path = image_dir / f"start{image_ext}"
free_path = image_dir / f"free{image_ext}"
free_orange_path = image_dir / f"free_orange{image_ext}"
check_in_path = image_dir / f"check_in{image_ext}"
n5_path = image_dir / f"5{image_ext}"
n5_red_path = image_dir / f"5_red{image_ext}"
manual_path = image_dir / f"manual{image_ext}"
manual2_path = image_dir / f"manual2{image_ext}"
arcane_crystal_path = image_dir / f"arcane_crystal{image_ext}"
exit_guild_path = image_dir / f"exit_guild{image_ext}"
daily_missions_path = image_dir / f"daily_missions{image_ext}"
open_path = image_dir / f"open{image_ext}"
liberate_path = image_dir / f"liberate{image_ext}"
fight_path = image_dir / f"fight{image_ext}"
ok_path = image_dir / f"ok{image_ext}"
train_free_path = image_dir / f"train_free{image_ext}"
get_game_tokens_path = image_dir / f"get_game_tokens{image_ext}"

machine_advice_path = image_dir / f"machine_advice{image_ext}"
machine_claim_loot_path = image_dir / f"machine_claim_loot{image_ext}"

quest_advice_path = image_dir / f"quest_advice{image_ext}"
quest_daily_path = image_dir / f"quest_daily{image_ext}"
quest_weekly_path = image_dir / f"quest_weekly{image_ext}"

pickaxe_advice_path = image_dir / f"pickaxe_advice{image_ext}"

crystal_advice_path = image_dir / f"crystal_advice{image_ext}"
crystal_hit_path = image_dir / f"crystal_hit{image_ext}"
crystal_hit_2_path = image_dir / f"crystal_hit_2{image_ext}"

map_advice_path = image_dir / f"map_advice{image_ext}"
map_advice_1_path = image_dir / f"map_advice_1{image_ext}"
map_advice_2_path = image_dir / f"map_advice_2{image_ext}"
map_advice_3_path = image_dir / f"map_advice_3{image_ext}"
map_advice_4_path = image_dir / f"map_advice_4{image_ext}"
map_advice_5_path = image_dir / f"map_advice_5{image_ext}"
map_advice_6_path = image_dir / f"map_advice_6{image_ext}"
map_advice_7_path = image_dir / f"map_advice_7{image_ext}"
map_advice_8_path = image_dir / f"map_advice_8{image_ext}"
map_mission_war_path = image_dir / f"map_mission_war{image_ext}"
map_mission_adventure_path = image_dir / f"map_mission_adventure{image_ext}"
map_mission_scout_path = image_dir / f"map_mission_scout{image_ext}"
map_mission_monster_path = image_dir / f"map_mission_monster{image_ext}"
map_mission_dragon_path = image_dir / f"map_mission_dragon{image_ext}"
map_mission_naval_path = image_dir / f"map_mission_naval{image_ext}"
map_mission_naval_2_path = image_dir / f"map_mission_naval_2{image_ext}"
map_mission_cave_path = image_dir / f"map_mission_cave{image_ext}"

shop_advice_path = image_dir / f"shop_advice{image_ext}"
shop_advice_1_path = image_dir / f"shop_advice_1{image_ext}"
shop_advice_2_path = image_dir / f"shop_advice_2{image_ext}"
shop_advice_3_path = image_dir / f"shop_advice_3{image_ext}"
shop_advice_4_path = image_dir / f"shop_advice_4{image_ext}"
shop_advice_5_path = image_dir / f"shop_advice_5{image_ext}"
shop_advice_6_path = image_dir / f"shop_advice_6{image_ext}"
shop_advice_7_path = image_dir / f"shop_advice_7{image_ext}"
shop_advice_8_path = image_dir / f"shop_advice_8{image_ext}"
shop_advice_9_path = image_dir / f"shop_advice_9{image_ext}"
shop_advice_10_path = image_dir / f"shop_advice_10{image_ext}"
shop_advice_11_path = image_dir / f"shop_advice_11{image_ext}"
shop_advice_12_path = image_dir / f"shop_advice_12{image_ext}"
bundles_advice_path = image_dir / f"bundles_advice{image_ext}"

tavern_advice_path = image_dir / f"tavern_advice{image_ext}"
tavern_get_5_tokens_path = image_dir / f"tavern_get_5_tokens{image_ext}"

alchemist_advice_path = image_dir / f"alchemist_advice{image_ext}"
alchemist_blood_path = image_dir / f"alchemist_blood{image_ext}"
alchemist_coin_path = image_dir / f"alchemist_coin{image_ext}"
alchemist_dust_path = image_dir / f"alchemist_dust{image_ext}"

engineer_advice_path = image_dir / f"engineer_advice{image_ext}"

oracle_advice_path = image_dir / f"oracle_advice{image_ext}"
rituals_path = image_dir / f"rituals{image_ext}"
oracle_gift_advice_path = image_dir / f"oracle_gift_advice{image_ext}"


guardian_advice_1_5_path = image_dir / f"guardian_advice_1_5{image_ext}"
guardian_advice_3_2_path = image_dir / f"guardian_advice_3_2{image_ext}"
guardian_advice_3_3_path = image_dir / f"guardian_advice_3_3{image_ext}"
guardian_advice_3_4_path = image_dir / f"guardian_advice_3_4{image_ext}"
guardian_advice_3_5_path = image_dir / f"guardian_advice_3_5{image_ext}"
guardian_1_5_path = image_dir / f"guardian_1_5{image_ext}"
guardian_2_5_path = image_dir / f"guardian_2_5{image_ext}"
guardian_3_1_path = image_dir / f"guardian_3_1{image_ext}"
guardian_3_2_path = image_dir / f"guardian_3_2{image_ext}"
guardian_3_3_path = image_dir / f"guardian_3_3{image_ext}"
guardian_3_4_path = image_dir / f"guardian_3_4{image_ext}"
guardian_3_5_path = image_dir / f"guardian_3_5{image_ext}"
guardian_4_1_path = image_dir / f"guardian_4_1{image_ext}"

events_1_path = image_dir / f"events_1{image_ext}"
events_2_path = image_dir / f"events_2{image_ext}"
events_3_path = image_dir / f"events_3{image_ext}"
events_4_path = image_dir / f"events_4{image_ext}"
events_5_path = image_dir / f"events_5{image_ext}"
events_6_path = image_dir / f"events_6{image_ext}"
events_7_path = image_dir / f"events_7{image_ext}"
decorated_heroes_path = image_dir / f"decorated_heroes{image_ext}"

research_advice_path = image_dir / f"research_advice{image_ext}"
research_box_path = image_dir / f"research_box{image_ext}"
research_path = image_dir / f"research{image_ext}"
research_no_slot_path = image_dir / f"research_no_slot{image_ext}"

main_screen = True


def locateAllOnScreenAndFilterNear(path, confidence=0.9, delta=4):
        locations_original = p.locateAllOnScreen(str(path), confidence=confidence)
        points = []
        locations = []
        
        for i, location in enumerate(locations_original):
            point_new = p.center(location)
            add = True
            
            for point in points:
                if (
                    abs(point.x - point_new.x) <= delta and 
                    abs(point.y - point_new.y) <= delta
                ):
                    add = False
                    break
            
            if add:
                points.append(point_new)
                locations.append(location)
        
        return locations


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
            time.sleep(0.5)
    else:
        point = p.locateCenterOnScreen(str(image), confidence=confidence)
        click(point)
    
def click_on_image_no_exc(*args, **kwargs):
    res = True
    
    try:
        click_on_image(*args, **kwargs)
    except ImageNotFoundException:
        res = False
    
    return res


def is_main_screen(main_screen=None):
    if main_screen is False:
        return main_screen
    
    res = True
    
    try:
        p.locateOnScreen(str(guild_path), confidence=0.9)
    except ImageNotFoundException:
        res = False
    
    return res


def move_random_around_home():
    p.moveTo(
        home_x + random.randint(0, delta_x), 
        home_y + random.randint(0, delta_y)
    )


def scroll_right():
    p.moveTo(center_left_x, center_left_y)
    p.dragTo(center_right_x, center_right_y, duration=5)


def scroll_left():
    p.moveTo(center_right_x, center_right_y)
    p.dragTo(center_left_x, center_left_y, duration=5)


def get_main_screen(main_screen, arg_is_fire):
    if not main_screen:
        for _ in range(15):
            p.press("esc")
        
        try:
            click_on_image(exit_guild_path)
        except ImageNotFoundException:
            logger.debug("Unable to exit guild")
        else:
            logger.info("Exit from guild with success")

    main_screen_real = is_main_screen(main_screen)
    
    if arg_is_fire and main_screen_real:
        move_random_around_home()
        p.click(interval=0.5)

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
        time.sleep(2)

    try:
        click_on_image(guild_start_expedition_path)
    except ImageNotFoundException:
        logger.debug("No guild expedition to start")
    else:
        logger.info("Guild expedition started")
        did_something = True

    if not did_something:
        logger.error(
            "Failed to claim or start a guild expedition (maybe finished " + 
            "for now?)"
        )

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

    time.sleep(0.5)
    
    did_something = False
    
    try:
        click_on_image(machine_claim_loot_path)
    except ImageNotFoundException:
        logger.debug("No machine loot")
    else:
        logger.info("Machine loot claimed")
        did_something = True
    
    try:
        click_on_image(daily_missions_path)
    except ImageNotFoundException:
        logger.debug("No daily missions advice")
        return main_screen
    
    time.sleep(1)
    
    try:
        click_on_image(open_path, confidence=0.95)
    except ImageNotFoundException:
        logger.debug("Failed to find daily missions open button")
        return main_screen
    
    time.sleep(0.5)
    
    scroll_right()
    scroll_right()
    
    time.sleep(1)
    
    n = 0
    
    for j in range(2):
        for i in range(5):
            try:
                click_on_image(liberate_path)
            except ImageNotFoundException:
                try:
                    click_on_image(fight_path)
                except ImageNotFoundException:
                    logger.debug("Failed to find a liberate or fight mission")
                    break
            
            max_time = 60
            start_time = time.time()
            
            while True:
                try:
                    click_on_image(ok_path)
                except ImageNotFoundException:
                    pass
                else:
                    did_something = True
                    time.sleep(0.5)
                    break
                
                if time.time() - start_time >= max_time:
                    logger.error(
                        "Failed to find ok button, or liberate missions lasts" + 
                        f" more than {max_time} seconds"
                    )
                    
                    break
                
                n += 1
                time.sleep(0.2)
        
        scroll_left()
        time.sleep(1)
    
    logger.info(f"Liberated {n} areas")
    
    if not did_something:
        logger.error("Unable to claim loot or liberate any area")
    
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
        click_on_image(quest_weekly_path, confidence=0.8)
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

        time.sleep(1)

        try:
            click_on_image(guild_shop_path, confidence=0.7)
        except ImageNotFoundException:
            logger.error("Failed to find guild shop")
            return main_screen

        time.sleep(0.2)

        try:
            click_on_image(guild_supplies_path)
        except ImageNotFoundException:
            try:
                p.locateOnScreen(str(guild_supplies_2_path))
            except ImageNotFoundException:
                logger.error("Failed to find guild supplies")
                return main_screen

    time.sleep(0.5)

    try:
        click_on_image(claim_dark_green_2_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get pickaxes")
    else:
        logger.info("Piackaxes claimed")
        main_screen = hit_the_crystal(main_screen, arg_is_fire, from_advice=False)

    return main_screen


def hit_the_crystal(main_screen, arg_is_fire, from_advice=True):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    if from_advice:
        try:
            click_on_image(crystal_advice_path)
        except ImageNotFoundException:
            logger.debug("No crystal advice")
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
        
        time.sleep(0.5)
        
        try:
            click_on_image(arcane_crystal_path)
        except ImageNotFoundException:
            logger.error("Failed to find arcane crystal")
            return main_screen
        
        
    time.sleep(0.2)
    
    
    hits = 1

    while True:
        try:
            p.locateOnScreen(str(manual_path), confidence=0.6)
        except ImageNotFoundException:
            try:
                p.locateOnScreen(str(manual2_path), confidence=0.6)
            except ImageNotFoundException:
                logger.info("Crystal hit finished")
                break
        try:
            click_on_image(crystal_hit_path, confidence=0.9)
        except ImageNotFoundException:
            try:
                click_on_image(crystal_hit_2_path)
            except ImageNotFoundException:
                logger.info("Crystal hit finished")
                break
        
        logger.info(f"Hit the crystal number {hits}")
        time.sleep(3)


        hits += 1
    
    return main_screen


def do_map_mission(mission_path, mission_type, confidence=0.7):
    mission_started = False
    
    try:
        locations = locateAllOnScreenAndFilterNear(
            mission_path, 
            confidence=confidence,
        )
        
        for i, location in enumerate(locations):
            point = p.center(location)
            click(point)
            time.sleep(0.5)
            mission_started = True
            
            try:
                click_on_image(start_path)
            except ImageNotFoundException:
                try:
                    click_on_image(free_orange_path)
                except ImageNotFoundException:
                    logger.debug(f"Failed to start the {mission_type} mission")
                    mission_started = False
                    p.press("esc")
                    
                    try:
                        p.locateOnScreen(str(guild_path))
                    except ImageNotFoundException:
                        pass
                    else:
                        main_screen = click_on_map(None)
                        
                        if main_screen is None:
                            return mission_started
            time.sleep(1)
            
    except ImageNotFoundException2 as e:
        logger.debug("No {mission_type} missions")
    
    if mission_started:
        logger.info(f"Mission of type {mission_type} started")
    else:
        logger.debug(f"Failed to start any mission of type {mission_type}")
    
    return mission_started
    

def click_on_map(main_screen):
    try:
        click_on_image(map_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No map advice")
        return None
    else:
        main_screen = False
    
    return main_screen


def do_map(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    main_screen_map = click_on_map(main_screen)
    
    if main_screen_map is None:
        return main_screen
    else:
        main_screen = main_screen_map

    time.sleep(1)
    
    
    i = 0
    
    while True:
        try:
            click_on_image(claim_map_path, confidence=0.8)
        except ImageNotFoundException:
            break
        
        i += 1
        
        time.sleep(2)
        
        try:
            click_on_image(claim_rewards_path, confidence=0.7)
        except ImageNotFoundException:
            logger.error("Unable to confirm map reward claim")
            break
        
        time.sleep(0.2)
    
    if i:
        logger.info(f"{i} map loots claimed")
    
    time.sleep(2)
    
    done = bool(i)
    done = do_map_mission(map_mission_cave_path, "cave") or done
    done = do_map_mission(map_mission_naval_path, "naval") or done
    done = do_map_mission(map_mission_naval_2_path, "naval") or done
    done = do_map_mission(map_mission_monster_path, "monster") or done
    done = do_map_mission(map_mission_dragon_path, "dragon") or done
    done = do_map_mission(map_mission_war_path, "war", confidence=0.65) or done
    done = do_map_mission(map_mission_scout_path, "scout") or done
    done = do_map_mission(map_mission_adventure_path, "adventure", confidence=0.65) or done
    
    if not done:
        logger.error("Unable to start or claim any map mission")

    return main_screen


def do_shop(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    logger.debug("Clicking on shop advice")
    
    try:
        click_on_image(shop_advice_path)
    except ImageNotFoundException:
        logger.debug("No shop advice")
        return main_screen
    
    main_screen = False
    
    time.sleep(0.5)

    try:
        click_on_image(free_path, confidence=0.6)
    except ImageNotFoundException:
        logger.error("Failed to get shop free gift")
        
    return main_screen


def do_bundle(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    logger.debug("Clicking on shop bundles advice")
    
    try:
        click_on_image(bundles_advice_path)
    except ImageNotFoundException:
        logger.debug("No shop bundles advice")
        return main_screen
    
    main_screen = False
    
    time.sleep(0.5)
    
    try:
        click_on_image(check_in_path, confidence=0.7)
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

    time.sleep(2)
    
    for i in range(100):
        if i == 0:
            log_func = logger.error
        else:
            log_func = logger.debug
        
        try:
            click_on_image(tavern_get_5_tokens_path, confidence=0.7)
        except ImageNotFoundException:
            
            log_func("Failed to get 5 tavern tokens")
            
            return main_screen
        
        time.sleep(2)
        p.press("esc")
        time.sleep(1)
        
        try:
            click_on_image(n5_path)
        except ImageNotFoundException:
            log_func("Failed to bet 5 tavern tokens")
            return main_screen
        
        time.sleep(1)
        
        try:
            click_on_image(n5_red_path, confidence=0.8)
        except ImageNotFoundException:
            logger.error("Failed to get 5 tavern cards")
        
        time.sleep(6)
        
        try:
            click_on_image(get_game_tokens_path)
        except ImageNotFoundException:
            logger.error("Failed to get game tokens")
            return main_screen
        
        time.sleep(0.5)
    
    return main_screen


def do_alchemist(main_screen, arg_is_fire, spend_dust):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(alchemist_advice_path)
    except ImageNotFoundException:
        logger.debug("No alchemist advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    done = False
    
    for i in range(3):
        try:
            click_on_image(claim_dark_green_4_path, confidence=0.7)
            time.sleep(0.5)
            done = True
        except ImageNotFoundException:
            try:
                click_on_image(claim_dark_green_5_path)
                time.sleep(0.5)
                done = True
            except ImageNotFoundException:
                try:
                    click_on_image(free_orange_path)
                    done = True
                except ImageNotFoundException:
                    break
    
    try:
        click_on_image(alchemist_blood_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No alchemist blood experiment to start")
    else:
        logger.info("Alchemist blood experiment started")
        time.sleep(0.5)
        done = True
    
    if spend_dust:
        try:
            click_on_image(alchemist_dust_path, confidence=0.7)
        except ImageNotFoundException:
            logger.debug("No alchemist dust experiment to start")
        else:
            logger.info("Alchemist dust experiment started")
            time.sleep(0.5)
            done = True
    
    try:
        click_on_image(alchemist_coin_path)
    except ImageNotFoundException:
        logger.debug("No alchemist coin experiment to start")
    else:
        logger.info("Alchemist coin experiment started")
        time.sleep(0.5)
        done = True
        
    if not done:
        logger.error("Unable to claim or start any Alchemist experiment")
    
    return main_screen


def do_engineer(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(engineer_advice_path)
    except ImageNotFoundException:
        logger.debug("No engineer advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    try:
        click_on_image(claim_green_big_path)
    except ImageNotFoundException:
        logger.error("Failed to claim engineer")
    else:
        logger.info("Engineer claimed")
    
    return main_screen


def do_oracle(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(oracle_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No oracle advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    try:
        click_on_image(rituals_path)
    except ImageNotFoundException:
        logger.debug("Failed to find rituals")
        return main_screen
    
    time.sleep(0.5)
    claimed = True
    
    try:
        click_on_image(claim_dark_green_3_path, all=True, confidence=0.94)
    except ImageNotFoundException2:
        claimed = False
    
    if claimed:
        logger.info("Claimed ritual")
        time.sleep(0.5)
    
    try:
        click_on_image(start_path)
    except ImageNotFoundException:
        if claimed:
            logger.warning("Unable to start ritual, probably no one for now")
        else:
            logger.error("Unable to claim or start any ritual")
    else:
        if not claimed:
            logger.warning("Unable to start ritual, probably all started")
        logger.info("Started ritual")
    
    return main_screen



train_free_path_confidence = 0.9



def do_guardian_specific(
    guardian_path, 
    guardian_num, 
    guardian_level, 
    confidence=0.9
):
        try:
            click_on_image(guardian_path, confidence=confidence)
        except ImageNotFoundException:
            logger.error(
                f"Unable to find guardian {guardian_num} " + 
                f"level {guardian_level}"
            )
        else:
            time.sleep(1)
            
            try:
                click_on_image(
                    train_free_path, 
                    confidence=train_free_path_confidence
                )
            except ImageNotFoundException:
                logger.debug(
                    f"No free train on guardian {guardian_num}" + 
                    f"level {guardian_level}"
                )
            else:
                logger.info(
                    f"Free train on guardian {guardian_num}" + 
                    f"level {guardian_level}"
                )
                
                return True
        
        time.sleep(1)
        
        return False


def do_guardian(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(guardian_advice_1_5_path)
    except ImageNotFoundException:
        try:
            click_on_image(guardian_advice_3_2_path)
        except ImageNotFoundException:
            try:
                click_on_image(guardian_advice_3_3_path)
            except ImageNotFoundException:
                try:
                    click_on_image(guardian_advice_3_4_path)
                except ImageNotFoundException:
                    try:
                        click_on_image(
                            guardian_advice_3_5_path, 
                            confidence=0.8,
                        )
                    except ImageNotFoundException:
                        logger.debug("No guardian advice")
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

    time.sleep(1)
    
    try:
        click_on_image(train_free_path, confidence=train_free_path_confidence)
    except ImageNotFoundException:
        done = do_guardian_specific(guardian_1_5_path, 1, 5, confidence=0.7)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_2_5_path, 2, 5)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_1_path, 3, 1)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_2_path, 3, 2, confidence=0.7)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_3_path, 3, 3, confidence=0.65)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_5_path, 3, 5, confidence=0.7)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_4_path, 3, 4, confidence=0.7)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_4_1_path, 4, 1, confidence=0.7)
        
        if done:
            return main_screen
            
        logger.error("No free train")
    else:
        logger.info("Free train on current guardian")
    
    return main_screen


def do_oracle_gift(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(oracle_gift_advice_path)
    except ImageNotFoundException:
        logger.debug("No oracle gift advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    try:
        click_on_image(free_path, confidence=0.75)
    except ImageNotFoundException:
        logger.error("No oracle gift")
    
    return main_screen


def do_event(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(events_1_path)
    except ImageNotFoundException:
        try:
            click_on_image(events_2_path, confidence=0.95)
        except ImageNotFoundException:
            try:
                click_on_image(events_3_path, confidence=0.9)
            except ImageNotFoundException:
                try:
                    click_on_image(events_4_path, confidence=0.95)
                except ImageNotFoundException:
                    try:
                        click_on_image(events_5_path)
                    except ImageNotFoundException:
                        try:
                            click_on_image(events_6_path)
                        except ImageNotFoundException:
                            try:
                                click_on_image(events_7_path)
                            except ImageNotFoundException:
                                logger.debug("No events advice")
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

    time.sleep(1)
    
    try:
        click_on_image(decorated_heroes_path, confidence=0.9)
    except ImageNotFoundException:
        logger.error("No Decorated Heroes event")
        return main_screen

    time.sleep(0.5)
    
    try:
        click_on_image(claim_dark_green_3_path, all=True)
    except ImageNotFoundException2:
        logger.debug("Unable to claim all on Decorated Heroes")
    
    return main_screen


def do_research(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(research_advice_path, confidence=0.9)
    except ImageNotFoundException:
        logger.debug("No research advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.5)
    
    scroll_right()
    scroll_right()
    
    time.sleep(1)
    
    for _ in range(10):
        try:
            click_on_image(claim_research_path, confidence=0.9)
        except ImageNotFoundException:
            break
        else:
            time.sleep(0.5)
    
    passes = 2
    
    for j in range(passes):
        try:
            locations = locateAllOnScreenAndFilterNear(
                research_box_path, 
                confidence=0.3,
                delta=100
            )
            
            for i, location in enumerate(locations):
                point = p.center(location)
                click(point)
                time.sleep(0.5)
                
                try:
                    click_on_image(research_path, confidence=0.9)
                except ImageNotFoundException:
                    pass
                else:
                    time.sleep(1)
                    
                    try:
                        p.locateOnScreen(
                            str(research_no_slot_path), 
                            confidence=0.9,
                        )
                    except ImageNotFoundException:
                        pass
                    else:
                        return main_screen
            
            if j != passes - 1:
                scroll_left()
                time.sleep(1)
        except ImageNotFoundException2:
            pass
    
    return main_screen

def check(main_screen, arg_is_fire, spend_dust, events):
    main_screen = do_guild_expedition(main_screen, arg_is_fire)
    main_screen = do_machine(main_screen, arg_is_fire)
    main_screen = do_quest(main_screen, arg_is_fire)
    main_screen = hit_the_crystal(main_screen, arg_is_fire)
    main_screen = get_pickaxes(main_screen, arg_is_fire, from_advice=True)
    main_screen = do_map(main_screen, arg_is_fire)
    main_screen = do_shop(main_screen, arg_is_fire)
    main_screen = do_bundle(main_screen, arg_is_fire)
    
    if not no_tavern:
        main_screen = do_tavern(main_screen, arg_is_fire)
    
    main_screen = do_alchemist(main_screen, arg_is_fire, spend_dust)
    main_screen = do_engineer(main_screen, arg_is_fire)
    main_screen = do_oracle(main_screen, arg_is_fire)
    main_screen = do_guardian(main_screen, arg_is_fire)
    main_screen = do_oracle_gift(main_screen, arg_is_fire)
    main_screen = do_oracle_gift(main_screen, arg_is_fire)
    main_screen = do_research(main_screen, arg_is_fire)
    
    if events:
        main_screen = do_event(main_screen, arg_is_fire)
    
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    return main_screen

parser = argparse.ArgumentParser(
    prog='firestone.py',
    description='Automates the Firestone idle game',
)

parser.add_argument(
    "command", 
    choices=("fire",), 
    nargs="?",
    help="Make the guardian attack",
)

parser.add_argument(
    "-d", 
    "--spend-dust", 
    action="store_true", 
    help="Enables the auto-clicking on dust researches in Alchemist"
)

parser.add_argument(
    "-t", 
    "--no-tavern", 
    action="store_true", 
    help="Disables auto-clicking on the Tavern"
)

parser.add_argument(
    "-e", 
    "--events", 
    action="store_true", 
    help="Enables auto-clicking on the Events (for now only Decorated Heroes)"
)

args = parser.parse_args()


p.keyDown("alt")
time.sleep(0.2)
p.press("tab")
time.sleep(0.2)
p.keyUp("alt")

time.sleep(0.5)

arg_is_fire = args.command == "fire"
spend_dust = args.spend_dust
no_tavern = args.no_tavern
events = args.events

wait_sec = 100 if arg_is_fire else 3
wait_sec_packaxes = 5737

now = time.time()
prev_time = now - wait_sec - 2
prev_time_pickaxes = now - wait_sec_packaxes - 2
prev_time_safe = now
safe_delta_sec = 300

while True:
    curr_time = time.time()
    
    if curr_time - prev_time_safe >= safe_delta_sec:
        main_screen = is_main_screen(main_screen)
        prev_time_safe = time.time()
        
    
    if curr_time - prev_time_pickaxes >= wait_sec_packaxes:
        main_screen = get_pickaxes(main_screen, arg_is_fire)
        prev_time_pickaxes = time.time()

    if curr_time - prev_time >= wait_sec:
        main_screen = check(main_screen, arg_is_fire, spend_dust, events)
        main_screen_real = is_main_screen(main_screen)
        
        if main_screen_real:
            p.moveTo(advice_down_x, advice_down_y)
            p.dragTo(advice_up_x, advice_up_y, duration=3)
            time.sleep(4)
            main_screen = check(main_screen, arg_is_fire, spend_dust, events)
            main_screen_real = is_main_screen(main_screen)
            
            if main_screen_real:
                p.moveTo(advice_up_x, advice_up_y)
                p.dragTo(advice_down_x, advice_down_y, duration=3)
                time.sleep(4)
                prev_time = time.time()
    
    main_screen_real = is_main_screen(main_screen)
    
    if arg_is_fire and main_screen_real: 
        move_random_around_home()
        
        p.click(interval=0.4)
