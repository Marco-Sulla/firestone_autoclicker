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
claim_dark_green_path = image_dir / f"claim_dark_green{image_ext}"
claim_dark_green_2_path = image_dir / f"claim_dark_green_2{image_ext}"
claim_dark_green_3_path = image_dir / f"claim_dark_green_3{image_ext}"
claim_dark_green_4_path = image_dir / f"claim_dark_green_4{image_ext}"
claim_dark_green_5_path = image_dir / f"claim_dark_green_5{image_ext}"
claim_rewards_path = image_dir / f"claim_rewards{image_ext}"
claim_map_path = image_dir / f"claim_map{image_ext}"

start_path = image_dir / f"start{image_ext}"
free_path = image_dir / f"free{image_ext}"
check_in_path = image_dir / f"check_in{image_ext}"
n1500_path = image_dir / f"1500{image_ext}"
n5_path = image_dir / f"5{image_ext}"
n5_red_path = image_dir / f"5_red{image_ext}"
manual_path = image_dir / f"manual{image_ext}"
manual2_path = image_dir / f"manual2{image_ext}"
arcane_crystal_path = image_dir / f"arcane_crystal{image_ext}"
exit_guild_path = image_dir / f"exit_guild{image_ext}"
daily_missions_path = image_dir / f"daily_missions{image_ext}"
open_path = image_dir / f"open{image_ext}"
liberate_path = image_dir / f"liberate{image_ext}"
ok_path = image_dir / f"ok{image_ext}"
train_free_path = image_dir / f"train_free{image_ext}"

machine_advice_path = image_dir / f"machine_advice{image_ext}"
machine_claim_loot_path = image_dir / f"machine_claim_loot{image_ext}"

quest_advice_path = image_dir / f"quest_advice{image_ext}"
quest_daily_path = image_dir / f"quest_daily{image_ext}"
quest_weekly_path = image_dir / f"quest_weekly{image_ext}"

pickaxe_advice_path = image_dir / f"pickaxe_advice{image_ext}"

crystal_advice_path = image_dir / f"crystal_advice{image_ext}"
crystal_hit_path = image_dir / f"crystal_hit{image_ext}"
crystal_hit_2_path = image_dir / f"crystal_hit_2{image_ext}"

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

shop_advice_1_path = image_dir / f"shop_advice_1{image_ext}"
shop_advice_2_path = image_dir / f"shop_advice_2{image_ext}"
shop_advice_3_path = image_dir / f"shop_advice_3{image_ext}"
shop_advice_4_path = image_dir / f"shop_advice_4{image_ext}"
shop_advice_5_path = image_dir / f"shop_advice_5{image_ext}"
shop_advice_6_path = image_dir / f"shop_advice_6{image_ext}"
shop_daily_rewards_path = image_dir / f"shop_daily_rewards{image_ext}"

tavern_advice_path = image_dir / f"tavern_advice{image_ext}"

alchemist_advice_path = image_dir / f"alchemist_advice{image_ext}"
alchemist_blood_path = image_dir / f"alchemist_blood{image_ext}"
alchemist_coin_path = image_dir / f"alchemist_coin{image_ext}"
alchemist_dust_path = image_dir / f"alchemist_dust{image_ext}"

engineer_advice_path = image_dir / f"engineer_advice{image_ext}"

oracle_advice_path = image_dir / f"oracle_advice{image_ext}"
rituals_path = image_dir / f"rituals{image_ext}"
oracle_gift_advice_path = image_dir / f"oracle_gift_advice{image_ext}"


guardian_advice_1_path = image_dir / f"guardian_advice_1{image_ext}"
guardian_1_5_path = image_dir / f"guardian_1_5{image_ext}"
guardian_2_5_path = image_dir / f"guardian_2_5{image_ext}"
guardian_3_1_path = image_dir / f"guardian_3_1{image_ext}"

main_screen = True


def locateAllOnScreenAndFilterNear(path, confidence=0.9):
        locations_original = p.locateAllOnScreen(str(path), confidence=confidence)
        points = []
        locations = []
        
        for i, location in enumerate(locations_original):
            point_new = p.center(location)
            add = True
            
            for point in points:
                if (
                    abs(point.x - point_new.x) <= 4 and 
                    abs(point.y - point_new.y) <= 4
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


def is_main_screen(main_screen=None):
    if main_screen is False:
        return main_screen
    
    res = True
    
    try:
        p.locateOnScreen(str(guild_path))
    except ImageNotFoundException:
        res = False
    
    return res


def get_main_screen(main_screen, arg_is_fire):
    if not main_screen:
        for _ in range(15):
            p.press("esc")
        
        try:
            click_on_image(exit_guild_path)
        except ImageNotFoundException:
            logger.debug("Unable to exit guid")
        else:
            logger.error("Exit from guild with success")

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
        time.sleep(2)

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
    
    try:
        click_on_image(daily_missions_path)
    except ImageNotFoundException:
        logger.debug("No daily missions advice")
        return main_screen
    
    time.sleep(0.5)
    
    try:
        click_on_image(open_path)
    except ImageNotFoundException:
        logger.debug("Failed to find daily missions open button")
        return main_screen
    
    time.sleep(0.5)
    
    for i in range(9):
        try:
            click_on_image(liberate_path)
        except ImageNotFoundException:
            logger.debug("Failed to find a liberate mission")
            break
        
        max_time = 60
        start_time = time.time()
        
        while True:
            try:
                click_on_image(ok_path)
            except ImageNotFoundException:
                pass
            else:
                time.sleep(0.5)
                break
            
            if time.time() - start_time >= max_time:
                logger.error(
                    "Failed to find ok button, or liberate missions lasts" + 
                    f" more than {max_time} seconds"
                )
            
            time.sleep(0.2)
        
    logger.info(f"Liberated {i+1} areas")
    
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

    time.sleep(0.2)

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


def do_map_mission(mission_path, mission_type):
    mission_started = False
    
    try:
        locations = locateAllOnScreenAndFilterNear(mission_path, confidence=0.7)
        
        for i, location in enumerate(locations):
            point = p.center(location)
            click(point)
            time.sleep(0.5)
            
            try:
                click_on_image(start_path)
            except ImageNotFoundException:
                logger.debug(f"Failed to start the {mission_type} mission")
                p.press("esc")
                time.sleep(0.5)
                
                try:
                    p.locateOnScreen(str(guild_path))
                except ImageNotFoundException:
                    pass
                else:
                    main_screen = click_on_map(None)
                    
                    if main_screen is None:
                        return
                    
            else:
                logger.info(f"Mission of type {mission_type} started")
                mission_started = True
                time.sleep(0.2)
    except ImageNotFoundException2 as e:
        logger.debug("No {mission_type} missions")
    
    if not mission_started:
        logger.debug(f"Failed to start any mission of type {mission_type}")
    

def click_on_map(main_screen):
    
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
                                try:
                                    click_on_image(map_advice_8_path)
                                except ImageNotFoundException:
                                    logger.debug("No map advice")
                                    return None
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

    time.sleep(0.2)
    
    
    i = 0
    
    while True:
        try:
            click_on_image(claim_map_path, confidence=0.7)
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
    
    do_map_mission(map_mission_cave_path, "cave")
    do_map_mission(map_mission_naval_path, "naval")
    do_map_mission(map_mission_naval_2_path, "naval")
    do_map_mission(map_mission_monster_path, "monster")
    do_map_mission(map_mission_dragon_path, "dragon")
    do_map_mission(map_mission_war_path, "war")
    do_map_mission(map_mission_scout_path, "scout")
    do_map_mission(map_mission_adventure_path, "adventure")

    return main_screen


def do_shop(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        logger.debug("Clicking on shop advice 1")
        click_on_image(shop_advice_1_path, confidence=0.95)
    except ImageNotFoundException:
        logger.debug("No shop advice")
        return main_screen
        
        # try:
        #     logger.debug("Clicking on shop advice 2")
        #     click_on_image(shop_advice_2_path, confidence=0.98)
        # except ImageNotFoundException:
        #     try:
        #         logger.debug("Clicking on shop advice 3")
        #         click_on_image(shop_advice_3_path, confidence=0.98)
        #     except ImageNotFoundException:
        #         try:
        #             logger.debug("Clicking on shop advice 4")
        #             click_on_image(shop_advice_4_path, confidence=1)
        #         except ImageNotFoundException:
        #             try:
        #                 logger.debug("Clicking on shop advice 5")
        #                 click_on_image(shop_advice_5_path, confidence=0.99)
        #             except ImageNotFoundException:
        #                 try:
        #                     logger.debug("Clicking on shop advice 5")
        #                     click_on_image(shop_advice_6_path, confidence=1)
        #                 except ImageNotFoundException:
        #                     logger.debug("No shop advice")
        #                     return main_screen
        #                 else:
        #                     main_screen = False
        #             else:
        #                 main_screen = False
        #         else:
        #             main_screen = False
        #     else:
        #         main_screen = False
        # else:
        #     main_screen = False
    else:
        main_screen = False
    
    time.sleep(0.2)

    try:
        click_on_image(free_path, confidence=0.7)
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

    time.sleep(2)
    
    try:
        click_on_image(n1500_path, confidence=0.7)
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


def do_alchemist(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(alchemist_advice_path)
    except ImageNotFoundException:
        logger.debug("No alchemist advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    for i in range(3):
        try:
            click_on_image(claim_dark_green_4_path, confidence=0.7)
            time.sleep(0.5)
        except ImageNotFoundException:
            try:
                click_on_image(claim_dark_green_5_path)
                time.sleep(0.5)
            except ImageNotFoundException:
                break
    
    try:
        click_on_image(alchemist_blood_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No alchemist blood experiment to start")
    else:
        logger.info("Alchemist blood experiment started")
        time.sleep(0.5)
    
    try:
        click_on_image(alchemist_dust_path, confidence=0.7)
    except ImageNotFoundException:
        logger.debug("No alchemist dust experiment to start")
    else:
        logger.info("Alchemist dust experiment started")
        time.sleep(0.5)
    
    try:
        click_on_image(alchemist_coin_path)
    except ImageNotFoundException:
        logger.debug("No alchemist coin experiment to start")
    else:
        logger.info("Alchemist coin experiment started")
        time.sleep(0.5)
    
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
        logger.debug("Failed to claim engineer")
    else:
        logger.info("Engineer claimed")
    
    return main_screen


def do_oracle(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(oracle_advice_path)
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
    
    i = 0
    
    for _ in range(3):
        try:
            click_on_image(claim_dark_green_3_path, confidence=0.95)
        except ImageNotFoundException:
            break
        else:
            i += 1
    
    if not i:
        logger.error("Failed to claim any rituals")
    
    try:
        click_on_image(start_path)
    except ImageNotFoundException:
        logger.error("Unable to start ritual")
    else:
        logger.info("Started ritual")
    
    return main_screen



train_free_path_confidence = 0.95



def do_guardian_specific(guardian_path, guardian_num, guardian_level):
        try:
            click_on_image(guardian_path)
        except ImageNotFoundException:
            logger.error(
                f"Unable to find guardian {guardian_num} " + 
                f"level {guardian_level}"
            )
        else:
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
        
        return False


def do_guardian(main_screen, arg_is_fire):
    main_screen = get_main_screen(main_screen, arg_is_fire)
    
    try:
        click_on_image(guardian_advice_1_path)
    except ImageNotFoundException:
        logger.debug("No guardian advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.2)
    
    try:
        click_on_image(train_free_path, confidence=train_free_path_confidence)
    except ImageNotFoundException:
        done = do_guardian_specific(guardian_1_5_path, 1, 5)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_2_5_path, 2, 5)
        
        if done:
            return main_screen
        
        done = do_guardian_specific(guardian_3_1_path, 3, 1)
        
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
        click_on_image(free_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No oracle gift")
    
    return main_screen

def check(main_screen, arg_is_fire):
    main_screen = do_guild_expedition(main_screen, arg_is_fire)
    main_screen = do_machine(main_screen, arg_is_fire)
    main_screen = do_quest(main_screen, arg_is_fire)
    main_screen = hit_the_crystal(main_screen, arg_is_fire)
    main_screen = get_pickaxes(main_screen, arg_is_fire, from_advice=True)
    main_screen = do_map(main_screen, arg_is_fire)
    main_screen = do_shop(main_screen, arg_is_fire)
    main_screen = do_tavern(main_screen, arg_is_fire)
    main_screen = do_alchemist(main_screen, arg_is_fire)
    main_screen = do_engineer(main_screen, arg_is_fire)
    main_screen = do_oracle(main_screen, arg_is_fire)
    main_screen = do_guardian(main_screen, arg_is_fire)
    main_screen = do_oracle_gift(main_screen, arg_is_fire)
    
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

wait_sec = 40 if arg_is_fire else 3
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
        main_screen_real = is_main_screen(main_screen)
        
        if main_screen_real:
            time.sleep(0.2)
            p.moveTo(advice_down_x, advice_down_y)
            p.dragTo(advice_up_x, advice_up_y, duration=3)
            time.sleep(4)
            main_screen = check(main_screen, arg_is_fire)
            main_screen_real = is_main_screen(main_screen)
            
            if main_screen_real:
                time.sleep(0.2)
                p.moveTo(advice_up_x, advice_up_y)
                p.dragTo(advice_down_x, advice_down_y, duration=3)
                time.sleep(4)
                prev_time = time.time()
    
    main_screen_real = is_main_screen(main_screen)
    
    if arg_is_fire and main_screen_real:    
        p.click(interval=0.2)
