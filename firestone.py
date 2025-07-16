#!/usr/bin/env python

import pyautogui as p
from pyautogui import ImageNotFoundException
from pyautogui import FailSafeException
from pyscreeze import ImageNotFoundException as ImageNotFoundException2
from pathlib import Path
import time
import sys
import logging
import random
import configparser
import argparse
import json

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
prestige_conf = config["prestige"]
hero_conf = config["hero"]

home_x = int(coordinates_conf["home_x"])
home_y = int(coordinates_conf["home_y"])
delta_x = int(coordinates_conf["delta_x"])
delta_y = int(coordinates_conf["delta_y"])
advice_up_x = int(coordinates_conf["advice_up_x"])
advice_up_y = int(coordinates_conf["advice_up_y"])
advice_down_x = int(coordinates_conf["advice_down_x"])
advice_down_y = int(coordinates_conf["advice_down_y"])

center_left_x = int(coordinates_conf["center_left_x"])
center_left_x_battle_pass = int(coordinates_conf["center_left_x_battle_pass"])
center_left_y = int(coordinates_conf["center_left_y"])
center_right_x = int(coordinates_conf["center_right_x"])
center_right_x_research = int(coordinates_conf["center_right_x_research"])
center_right_x_battle_pass = int(coordinates_conf["center_right_x_battle_pass"])
center_right_delta_x_init_battle_pass = int(coordinates_conf["center_right_delta_x_init_battle_pass"])
center_right_y = int(coordinates_conf["center_right_y"])

map_x = int(coordinates_conf["map_x"])
map_y = int(coordinates_conf["map_y"])
map_delta_y = int(coordinates_conf["map_delta_y"])

preferred_heroes = json.loads(prestige_conf["preferred_heroes"])

power_prestige = hero_conf["power_prestige"]
power_farming = hero_conf["power_farming"]

image_ext = ".png"

guild_expedition_advice_path = (
    image_dir / 
    f"guild_expedition_advice{image_ext}"
)

guild_path = image_dir / f"guild{image_ext}"
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
claim_map_path = image_dir / f"claim_map{image_ext}"
claim_research_path = image_dir / f"claim_research{image_ext}"
claim_rewards_path = image_dir / f"claim_rewards{image_ext}"

start_path = image_dir / f"start{image_ext}"
free_path = image_dir / f"free{image_ext}"
free_orange_path = image_dir / f"free_orange{image_ext}"
check_in_path = image_dir / f"check_in{image_ext}"
manual_path = image_dir / f"manual{image_ext}"
manual2_path = image_dir / f"manual2{image_ext}"
manual_chaos_path = image_dir / f"manual_chaos{image_ext}"
manual_green_path = image_dir / f"manual_green{image_ext}"
arcane_crystal_path = image_dir / f"arcane_crystal{image_ext}"
exit_guild_path = image_dir / f"exit_guild{image_ext}"
daily_missions_path = image_dir / f"daily_missions{image_ext}"
open_path = image_dir / f"open{image_ext}"
liberate_path = image_dir / f"liberate{image_ext}"
fight_path = image_dir / f"fight{image_ext}"
ok_path = image_dir / f"ok{image_ext}"
train_free_path = image_dir / f"train_free{image_ext}"
get_game_tokens_path = image_dir / f"get_game_tokens{image_ext}"
research_maxed_path = image_dir / f"research_maxed{image_ext}"
research_in_progress_path = image_dir / f"research_in_progress{image_ext}"
research_is_locked_path = image_dir / f"research_is_locked{image_ext}"
mission_rewards_path = image_dir / f"mission_rewards{image_ext}"
close_buy_path = image_dir / f"close_buy{image_ext}"
save_and_exit_path = image_dir / f"save_and_exit{image_ext}"
rewards_path = image_dir / f"rewards{image_ext}"

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
map_mission_war_path = image_dir / f"map_mission_war{image_ext}"
map_mission_adventure_path = image_dir / f"map_mission_adventure{image_ext}"
map_mission_scout_path = image_dir / f"map_mission_scout{image_ext}"
map_mission_monster_path = image_dir / f"map_mission_monster{image_ext}"
map_mission_dragon_path = image_dir / f"map_mission_dragon{image_ext}"
map_mission_naval_path = image_dir / f"map_mission_naval{image_ext}"
map_mission_cave_path = image_dir / f"map_mission_cave{image_ext}"
map_squad_available_path = image_dir / f"map_squad_available{image_ext}"

shop_advice_path = image_dir / f"shop_advice{image_ext}"
daily_reward_advice_path = image_dir / f"daily_reward_advice{image_ext}"

tavern_advice_path = image_dir / f"tavern_advice{image_ext}"
tavern_get_5_tokens_path = image_dir / f"tavern_get_5_tokens{image_ext}"
tavern_card_path = image_dir / f"tavern_card{image_ext}"
token_button_path = image_dir / f"token_button{image_ext}"

alchemist_advice_path = image_dir / f"alchemist_advice{image_ext}"
alchemist_blood_path = image_dir / f"alchemist_blood{image_ext}"
alchemist_coin_path = image_dir / f"alchemist_coin{image_ext}"
alchemist_dust_path = image_dir / f"alchemist_dust{image_ext}"

engineer_advice_path = image_dir / f"engineer_advice{image_ext}"

oracle_advice_path = image_dir / f"oracle_advice{image_ext}"
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
guardian_4_2_path = image_dir / f"guardian_4_2{image_ext}"
guardian_4_3_path = image_dir / f"guardian_4_3{image_ext}"
guardian_4_4_path = image_dir / f"guardian_4_4{image_ext}"
guardian_4_5_path = image_dir / f"guardian_4_5{image_ext}"

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

chaos_advice_path = image_dir / f"chaos_advice{image_ext}"
chaos_hit_path = image_dir / f"chaos_hit{image_ext}"

arena_advice_path = image_dir / f"arena_advice{image_ext}"
arena_fight_start_path = image_dir / f"arena_fight_start{image_ext}"
arena_fight_path = image_dir / f"arena_fight{image_ext}"

upgrade_path = image_dir / f"upgrade{image_ext}"
next_milestone_path = image_dir / f"next_milestone{image_ext}"
confirm_path = image_dir / f"confirm{image_ext}"
start_now_path = image_dir / f"start_now{image_ext}"
upgrade_hero_path = image_dir / f"upgrade_hero{image_ext}"
upgrade_max_path = image_dir / f"upgrade_max{image_ext}"
epic_prestige_path = image_dir / f"epic_prestige{image_ext}"
firestone_advice_path = image_dir / f"firestone_advice{image_ext}"
boss_path = image_dir / f"boss{image_ext}"

treasure_tab_path = image_dir / f"treasure_tab{image_ext}"
common_chest_path = image_dir / f"common_chest{image_ext}"
common_chest_button_path = image_dir / f"common_chest_button{image_ext}"
uncommon_chest_path = image_dir / f"uncommon_chest{image_ext}"
uncommon_chest_button_path = image_dir / f"uncommon_chest_button{image_ext}"
rare_chest_path = image_dir / f"rare_chest{image_ext}"
rare_chest_button_path = image_dir / f"rare_chest_button{image_ext}"
wooden_chest_path = image_dir / f"wooden_chest{image_ext}"
wooden_chest_button_path = image_dir / f"wooden_chest_button{image_ext}"
iron_chest_path = image_dir / f"iron_chest{image_ext}"
iron_chest_button_path = image_dir / f"iron_chest_button{image_ext}"
golden_chest_path = image_dir / f"golden_chest{image_ext}"
golden_chest_button_path = image_dir / f"golden_chest_button{image_ext}"
comet_chest_path = image_dir / f"comet_chest{image_ext}"
comet_chest_button_path = image_dir / f"comet_chest_button{image_ext}"
lunar_chest_path = image_dir / f"lunar_chest{image_ext}"
lunar_chest_button_path = image_dir / f"lunar_chest_button{image_ext}"
solar_chest_path = image_dir / f"solar_chest{image_ext}"
solar_chest_button_path = image_dir / f"solar_chest_button{image_ext}"
mistery_box_path = image_dir / f"mistery_box{image_ext}"
mistery_box_button_path = image_dir / f"mistery_box_button{image_ext}"
oracle_gift_path = image_dir / f"oracle_gift{image_ext}"
oracle_gift_button_path = image_dir / f"oracle_gift_button{image_ext}"

awake_advice_path = image_dir / f"awake_advice{image_ext}"
awake_button_path = image_dir / f"awake_button{image_ext}"

mailbox_path = image_dir / f"mailbox{image_ext}"

emblem_market_path = image_dir / f"emblem_market{image_ext}"
gear_tab_path = image_dir / f"gear_tab{image_ext}"
gear_tab_2_path = image_dir / f"gear_tab_2{image_ext}"
jewel_tab_path = image_dir / f"jewel_tab{image_ext}"
jewel_tab_path = image_dir / f"jewel_tab{image_ext}"
jewel_tab_2_path = image_dir / f"jewel_tab_2{image_ext}"
soulstone_tab_path = image_dir / f"soulstone_tab{image_ext}"
soulstone_tab_2_path = image_dir / f"soulstone_tab_2{image_ext}"
emblem_of_courage_path = image_dir / f"emblem_of_courage{image_ext}"
emblem_of_valor_path = image_dir / f"emblem_of_valor{image_ext}"
emblem_of_brotherhood_path = image_dir / f"emblem_of_brotherhood{image_ext}"

battle_pass_path = image_dir / f"battle_pass{image_ext}"


def locateAllOnScreen(path, confidence=0.9):
    return p.locateAllOnScreen(str(path), confidence=confidence)


def locateAllOnScreenAndFilterNear(path, confidence=0.9, delta=4):
    try:
        locations_original = locateAllOnScreen(path, confidence=confidence)
    
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
    except ImageNotFoundException2:
        raise ImageNotFoundException
    
    return locations


def click(point):
    p.moveTo(*point)
    time.sleep(0.2)
    p.click()


def click_on_location(location):
    point = p.center(location)
    click(point)


def click_on_image(image, all=False, confidence=0.9):
    if all:
        try:
            locations = locateAllOnScreen(image, confidence=confidence)
        
            for location in locations:
                click_on_location(location)
                time.sleep(0.5)
        except ImageNotFoundException2:
            raise ImageNotFoundException
    else:
        point = p.locateCenterOnScreen(str(image), confidence=confidence)
        click(point)


def locateOnScreen(path, confidence=0.9):
    try:
        p.locateOnScreen(str(path), confidence=confidence)
    except ImageNotFoundException:
        return False
    
    return True


def dragTo(*args, duration=None, **kwargs):
    if duration is None:
        duration = 5
    
    p.dragTo(*args, duration=duration, **kwargs)


def is_main_screen(main_screen=None):
    if main_screen is False:
        return main_screen
    
    return locateOnScreen(guild_path)


def move_random_around_home():
    p.moveTo(
        home_x + random.randint(0, delta_x), 
        home_y + random.randint(0, delta_y)
    )


def scroll_right(scope=None):
    if scope == "battle_pass":
        left_x = center_left_x_battle_pass
    else:
        left_x = center_left_x
    
    p.moveTo(left_x, center_left_y)
    dragTo(center_right_x, center_right_y)
    time.sleep(0.5)


def scroll_left(scope=None, first_time=False):
    if scope == "research":
        right_x = center_right_x_research
    elif scope == "battle_pass":
        right_x = center_right_x_battle_pass
        
        if first_time:
            right_x += center_right_delta_x_init_battle_pass
    else:
        right_x = center_right_x
    
    if scope == "battle_pass":
        left_x = center_left_x_battle_pass
    else:
        left_x = center_left_x
    
    p.moveTo(right_x, center_right_y)
    dragTo(left_x, center_left_y)
    time.sleep(0.5)


def press_power(do_prestige, main_screen_real):
    if main_screen_real:
        if do_prestige:
            p.press(power_prestige)
        else:
            p.press(power_farming)


def close_save_and_exit():
    if locateOnScreen(
        save_and_exit_path, 
        confidence=0.8
    ):
        p.press("esc")
        
        return True
    
    return False


def get_main_screen(main_screen, arg_is_fire, do_prestige):
    guild_detected = False
    
    if not main_screen:
        try:
            click_on_image(close_buy_path)
        except ImageNotFoundException:
            pass
        else:
            time.sleep(1)
        
        for _ in range(15):
            p.press("esc")
            
            if locateOnScreen(guild_path):
                guild_detected = True
                main_screen = True
                break
                
        close_save_and_exit()
        
        try:
            click_on_image(exit_guild_path)
        except ImageNotFoundException:
            logger.debug("Unable to exit guild")
        else:
            logger.info("Exit from guild with success")
    
    if guild_detected:
        main_screen_real = True
    else:
        # TODO  is this really needed?
        main_screen_real = is_main_screen(main_screen)
    
    if arg_is_fire and main_screen_real:
        move_random_around_home()
        p.click(interval=0.5)
    
    press_power(do_prestige, main_screen_real)

    return main_screen_real


def do_guild_expedition(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(guild_expedition_advice_path)
    except ImageNotFoundException:
        logger.debug("No guild expedition advice")
        return main_screen
    
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


def do_machine(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(machine_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No machine advice")
        return main_screen
    
    main_screen = False
    time.sleep(1)
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
            
            did_something = True
            n += 1
            max_time = 120
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
                        "Failed to find ok button, or liberate missions " + 
                        f"lasts more than {max_time} seconds"
                    )
                    
                    break
                
                time.sleep(0.5)
        
        scroll_left()
        time.sleep(1)
    
    logger.info(f"Liberated {n} areas")
    
    if not did_something:
        logger.error("Unable to claim loot or liberate any area")
    
    return main_screen


def do_quest(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(quest_advice_path)
    except ImageNotFoundException:
        logger.debug("No quest advice")
        return main_screen
    
    main_screen = False
    time.sleep(1)
    did_something = False
    
    try:
        click_on_image(quest_daily_path)
    except ImageNotFoundException:
        logger.error("Failed to find daily quest button")
    else:
        time.sleep(0.5)

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
        time.sleep(0.5)

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


def get_pickaxes(main_screen, arg_is_fire, do_prestige, from_advice=False):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    if from_advice:
        try:
            click_on_image(pickaxe_advice_path)
        except ImageNotFoundException:
            logger.debug("No pickaxe advice")
            return main_screen
        
        main_screen = False
    else:
        # TODO this for is really needed?
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

        time.sleep(2)

        try:
            click_on_image(guild_shop_path, confidence=0.7)
        except ImageNotFoundException:
            logger.error("Failed to find guild shop")
            return main_screen

        time.sleep(1)

        try:
            click_on_image(guild_supplies_path)
        except ImageNotFoundException:
            if not locateOnScreen(guild_supplies_2_path):
                logger.error("Failed to find guild supplies")
                return main_screen

    time.sleep(1)

    try:
        click_on_image(claim_dark_green_2_path, confidence=0.8)
    except ImageNotFoundException:
        logger.error("Failed to get pickaxes")
    else:
        logger.info("Piackaxes claimed")
        
        main_screen = hit_crystal(
            main_screen, 
            arg_is_fire, 
            do_prestige, 
            from_advice=False
        )

    return main_screen


def hit_crystal(main_screen, arg_is_fire, do_prestige, from_advice=True):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    if from_advice:
        try:
            click_on_image(crystal_advice_path)
        except ImageNotFoundException:
            logger.debug("No crystal advice")
            return main_screen
        
        main_screen = False
    else:
        try:
            click_on_image(guild_path)
        except ImageNotFoundException:
            logger.error("Failed to find guild")
            return main_screen
        
        main_screen = False
        time.sleep(2)
        
        try:
            click_on_image(arcane_crystal_path, confidence=0.7)
        except ImageNotFoundException:
            logger.error("Failed to find arcane crystal")
            return main_screen
        
        
    time.sleep(1)
    
    
    hits = 0

    for _ in range(100):
        if not locateOnScreen(manual_path, confidence=0.6):
            break
        
        # TODO what works now?
        if not locateOnScreen(manual2_path, confidence=0.6):
            break
        
        logger.info("Crystal hit finished")
        
        try:
            click_on_image(crystal_hit_path)
        except ImageNotFoundException:
            try:
                # TODO what works now?
                click_on_image(crystal_hit_2_path)
            except ImageNotFoundException:
                break
        
        time.sleep(3)


        hits += 1
    
    logger.info(f"Hit the crystal {hits} times")
    
    return main_screen


def do_map_mission(mission_path, mission_type, confidence=0.7):
    missions_started = 0
    
    try:
        locations = locateAllOnScreenAndFilterNear(
            mission_path, 
            confidence=confidence,
        )
    except ImageNotFoundException as e:
        logger.debug("No {mission_type} missions")
        return bool(missions_started)
        
    for i, location in enumerate(locations):
        click_on_location(location)
        time.sleep(0.5)
        already_sleeped = 0
        mission_started = False
        
        try:
            click_on_image(free_orange_path)
            missions_started += 1
            mission_started = True
        except ImageNotFoundException:
            try:
                click_on_image(start_path)
                missions_started += 1
                mission_started = True
            except ImageNotFoundException:
                logger.debug(f"Failed to start the {mission_type} mission")
                p.press("esc")
                already_sleeped = 0.5
                time.sleep(already_sleeped)
                
                if locateOnScreen(guild_path):
                    main_screen = click_on_map(None)
                    
                    if main_screen is None:
                        logger.warning(
                            "Guild button detected, but no map advice"
                        )
                        
                        return bool(missions_started)
        else:
            time.sleep(2)
            p.press("esc")
        
        if not locateOnScreen(map_squad_available_path):
            return None
        
        time.sleep(1 - already_sleeped)
    
    if missions_started:
        logger.info(
            f"Started {missions_started} missions of type {mission_type}"
        )
    else:
        logger.debug(f"Failed to start any mission of type {mission_type}")
    
    return bool(missions_started)
    

def click_on_map(main_screen):
    try:
        click_on_image(map_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No map advice")
        return None
    
    return False


def do_map(main_screen, arg_is_fire, do_prestige, repeat=True):
    if repeat:
        main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
        main_screen_map = click_on_map(main_screen)
        
        if main_screen_map is None:
            return main_screen
        
        main_screen = main_screen_map

        time.sleep(1)
    
    i = 0
    
    for _ in range(100):
        try:
            click_on_image(claim_map_path, confidence=0.8)
        except ImageNotFoundException:
            if i:
                time.sleep(1)
                p.press("esc")
                move_random_around_home()
            break
        
        i += 1
        time.sleep(0.5)
    
    if not locateOnScreen(map_squad_available_path):
        return main_screen
    
    time.sleep(2)
    
    done = bool(i)
    done2 = do_map_mission(map_mission_cave_path, "cave")
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    done2 = do_map_mission(map_mission_naval_path, "naval")
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    done2 = do_map_mission(map_mission_monster_path, "monster")
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    done2 = do_map_mission(map_mission_dragon_path, "dragon")
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    done2 = do_map_mission(map_mission_scout_path, "scout")
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    done2 = do_map_mission(map_mission_war_path, "war", confidence=0.65)
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    
    done2 = do_map_mission(
        map_mission_adventure_path, 
        "adventure", 
        confidence=0.65
    )
    
    if done2 is None:
        return main_screen
    
    done = done2 or done
    
    if not done:
        logger.error("Unable to start or claim any map mission")
    
    return main_screen


def do_shop(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    logger.debug("Clicking on shop advice")
    
    try:
        click_on_image(shop_advice_path)
    except ImageNotFoundException:
        logger.debug("No shop advice")
        return main_screen
    
    main_screen = False
    
    time.sleep(1)

    try:
        click_on_image(free_path, confidence=0.6)
    except ImageNotFoundException:
        logger.error("Failed to get shop free gift")
        
    return main_screen


def do_daily_reward(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(daily_reward_advice_path)
    except ImageNotFoundException:
        logger.debug("No daily shop reward advice")
        return main_screen
    
    main_screen = False
    
    time.sleep(1)
    
    try:
        click_on_image(check_in_path, confidence=0.7)
    except ImageNotFoundException:
        logger.error(
            "Failed to find daily reward check in button in shop"
        )
    else:
        logger.info("Claimed daily reward in shop")
        
    return main_screen


def do_tavern(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
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
        
        locations = locateAllOnScreen(token_button_path)
        
        try:
            location = tuple(locations)[-1]
        except ImageNotFoundException2:
            log_func(f"Unable to find any token button in the tavern")
            return main_screen
        
        click_on_location(location)
        time.sleep(1)
        
        try:
            click_on_image(tavern_card_path)
        except ImageNotFoundException:
            logger.error("Failed to discover tavern cards")
        
        time.sleep(6)
        
        try:
            click_on_image(get_game_tokens_path)
        except ImageNotFoundException:
            logger.error("Failed to get game tokens")
            return main_screen
        
        time.sleep(0.5)
    
    return main_screen


def do_alchemist(main_screen, arg_is_fire, spend_dust, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(alchemist_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No alchemist advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(0.5)
    
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


def do_engineer(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(engineer_advice_path)
    except ImageNotFoundException:
        logger.debug("No engineer advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(1)
    
    try:
        click_on_image(claim_green_big_path)
    except ImageNotFoundException:
        logger.error("Failed to claim engineer")
    else:
        logger.info("Engineer claimed")
    
    return main_screen


def do_oracle(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(oracle_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No oracle advice")
        return main_screen
    else:
        main_screen = False
    
    time.sleep(0.5)
    claimed = True
    
    try:
        click_on_image(claim_dark_green_3_path, confidence=0.94)
    except ImageNotFoundException:
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



train_free_path_confidence = 0.8



def do_guardian_specific(
    guardian_path, 
    guardian_num, 
    guardian_level, 
    confidence=0.8
):
        try:
            click_on_image(guardian_path, confidence=confidence)
        except ImageNotFoundException as e:
            logger.debug(
                f"Unable to find guardian {guardian_num} " + 
                f"level {guardian_level}."
            )
            
            return None
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


def do_guardians_type(level, data):
    guardian_not_found = True
    
    for path, type, confidence in data:
        if confidence is None:
            confidence = 0.9
        
        done = do_guardian_specific(path, type, level, confidence=confidence)
        
        if done:
            return True
        
        if done is not None:
            guardian_not_found = False
    
    if guardian_not_found:
        logger.error(f"Guardian of level {level} not found")
    
    return False


def do_guardian(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(guardian_advice_3_5_path, confidence=0.8)
    except ImageNotFoundException:
        try:
            click_on_image(guardian_advice_3_4_path)
        except ImageNotFoundException:
            try:
                click_on_image(guardian_advice_3_3_path)
            except ImageNotFoundException:
                try:
                    click_on_image(guardian_advice_3_2_path)
                except ImageNotFoundException:
                    try:
                        click_on_image(guardian_advice_1_5_path)
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

    time.sleep(2)
    
    try:
        click_on_image(train_free_path, confidence=train_free_path_confidence)
    except ImageNotFoundException:
        done = do_guardians_type(2, ((guardian_2_5_path, 5, None),))
        
        if done:
            return main_screen
        
        done = do_guardians_type(3, (
            (guardian_3_5_path, 5, 0.7),
            (guardian_3_4_path, 4, 0.7),
            (guardian_3_3_path, 3, 0.65),
            (guardian_3_2_path, 2, 0.7),
            (guardian_3_1_path, 1, None),
        ))
        
        if done:
            return main_screen
        
        done = do_guardians_type(1, ((guardian_1_5_path, 5, 0.7),))
        
        if done:
            return main_screen
        
        done = do_guardians_type(4, (
            (guardian_4_5_path, 5, 0.7),
            (guardian_4_4_path, 4, 0.7),
            (guardian_4_3_path, 3, 0.7),
            (guardian_4_2_path, 2, 0.7),
            (guardian_4_1_path, 1, 0.7),
        ))
        
        if done:
            return main_screen
            
        logger.error("No free train")
    else:
        logger.info("Free train on current guardian")
    
    return main_screen


def do_oracle_gift(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(oracle_gift_advice_path, confidence=0.8)
    except ImageNotFoundException:
        logger.debug("No oracle gift advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(1)
    
    try:
        click_on_image(free_path, confidence=0.75)
    except ImageNotFoundException:
        logger.error("No oracle gift")
    
    return main_screen


def do_event(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(events_1_path)
    except ImageNotFoundException:
        try:
            click_on_image(events_2_path, confidence=0.95)
        except ImageNotFoundException:
            try:
                click_on_image(events_3_path)
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
        click_on_image(decorated_heroes_path)
    except ImageNotFoundException:
        logger.error("No Decorated Heroes event")
        return main_screen

    time.sleep(0.5)
    
    try:
        click_on_image(claim_dark_green_3_path, all=True)
    except ImageNotFoundException:
        logger.debug("Unable to claim all on Decorated Heroes")
    
    return main_screen


def do_research(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(research_advice_path, confidence=0.8)
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
            click_on_image(claim_research_path)
        except ImageNotFoundException:
            break
        else:
            time.sleep(0.5)
    
    passes = 3
    did_something = False
    
    for j in range(passes):
        try:
            locations = locateAllOnScreenAndFilterNear(
                research_box_path, 
                confidence=0.33,
                delta=100
            )
            
            random.shuffle(locations)
            
            for i, location in enumerate(locations):
                click_on_location(location)
                time.sleep(0.5)
                
                try:
                    click_on_image(research_path)
                except ImageNotFoundException:
                    press_esc = locateOnScreen(research_maxed_path)
                    
                    if not press_esc:
                        press_esc = locateOnScreen(research_in_progress_path)
                    
                    if not press_esc:
                        press_esc = locateOnScreen(research_is_locked_path)
                    
                    if press_esc:
                        p.press("esc")
                        time.sleep(1)
                else:
                    did_something = True
                    time.sleep(1)
                    
                    if locateOnScreen(research_no_slot_path):
                        return main_screen
            
            if j != passes - 1:
                scroll_left("research")
                time.sleep(1)
        except ImageNotFoundException:
            pass
    
    if not did_something:
        logger.error("Unable to start any research")
    
    return main_screen


def hit_chaos(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(chaos_advice_path)
    except ImageNotFoundException:
        logger.debug("No chaos advice")
        return main_screen
    else:
        main_screen = False
        
        
    time.sleep(2.5)
    
    
    hits = 0

    for _ in range(100):
        try:
            click_on_image(chaos_hit_path)
        except ImageNotFoundException:
            break
        
        if not locateOnScreen(manual_chaos_path):
            break
        
        time.sleep(5)


        hits += 1
        
    logger.info(f"Hit chaos {hits} times")
    
    return main_screen


def do_arena(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(arena_advice_path)
    except ImageNotFoundException:
        logger.debug("No arena advice")
        return main_screen
    else:
        main_screen = False

    time.sleep(2)
            
    max_time = 120
    
    for n in range(100):
        try:
            fight_locations = locateAllOnScreenAndFilterNear(
                arena_fight_path,
                confidence=0.8,
            )
        except ImageNotFoundException:
            logger.error("Unable to find any fight button")
            break
        
        fight_location = fight_locations[-1]
        click_on_location(fight_location)
        time.sleep(2)
        
        try:
            click_on_image(arena_fight_start_path)
        except ImageNotFoundException:
            logger.debug("Unable to find arena start fight button")
            break
        
        time.sleep(0.5)
        start_time = time.time()
        
        while True:
            try:
                fight_locations = locateAllOnScreenAndFilterNear(
                    arena_fight_path
                )
            except ImageNotFoundException:
                pass
            else:
                break
            
            try:
                click_on_image(ok_path)
            except ImageNotFoundException:
                pass
            else:
                time.sleep(0.5)
                break
            
            if time.time() - start_time >= max_time:
                logger.error(
                    "Failed to find ok button, or arena fight lasts" + 
                    f" more than {max_time} seconds"
                )
                
                break
        
        time.sleep(0.5)
    
    logger.info(f"Fighted in arena {n} times")
    
    if n == 0:
        logger.error("Unable to do any fight in arena")
    
    return main_screen


def prestige(main_screen, arg_is_fire, do_prestige):
    get_main_screen(main_screen, arg_is_fire, do_prestige)
    p.press("u")
    main_screen = False
    time.sleep(2)
    
    for _ in range(100):
        if locateOnScreen(upgrade_max_path, confidence=0.77):
            logger.debug("Max heroes upgrade multiplier found")
            break
        
        try:
            click_on_image(upgrade_path, confidence=0.8)
        except ImageNotFoundException:
            try:
                click_on_image(next_milestone_path, confidence=0.8)
            except ImageNotFoundException:
                logger.error("Unable to cycle heroes upgrade multipliers")
                break
        
        time.sleep(0.2)
    
    for _ in range(10000):
        try:
            locations = locateAllOnScreenAndFilterNear(
                upgrade_hero_path, 
                confidence = 0.5,
                delta = 10,
            )
        except ImageNotFoundException:
            logger.debug("No upgrades for heroes")
            break
        else:
            if len(locations) != 7:
                break
            
            for hero_pos in preferred_heroes:
                click_on_location(locations[hero_pos-1])
                time.sleep(0.2)
            
            logger.debug(f"Upgraded heroes")
    
    if not locateOnScreen(boss_path):
        return main_screen
    
    try:
        click_on_image(firestone_advice_path)
    except ImageNotFoundException:
        logger.debug("Unable to find prestige advice")
    else:
        time.sleep(0.5)
        main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
        time.sleep(0.5)
    
        try:
            click_on_image(firestone_advice_path)
        except ImageNotFoundException:
            logger.debug("Unable to find prestige advice")
        else:
            main_screen = False
            time.sleep(0.5)
            
            try:
                click_on_image(epic_prestige_path)
            except ImageNotFoundException:
                logger.error("Unable to find epic prestige button")
            else:
                time.sleep(0.5)
                
                try:
                    click_on_image(confirm_path)
                except ImageNotFoundException:
                    logger.error("Unable to find confirm prestige button")
                else:
                    logger.info("Prestige done!")
                
                for _ in range(100):
                    try:
                        click_on_image(start_now_path)
                    except ImageNotFoundException:
                        pass
                    else:
                        break
                    
                    time.sleep(0.2)
                else:
                    logger.error("Unable to find 'Start now' button")
                    
                        
    
    return main_screen


wait_time_bag_opened = 0.5


def open_chest(
    chest_path, 
    chest_button_path, 
    chest_name, 
    main_screen, 
    arg_is_fire, 
    do_prestige,
    not_last=True,
):
    try:
        click_on_image(chest_path)
    except ImageNotFoundException:
        logger.debug(f"No {chest_name} in the bag")
    else:
        time.sleep(0.5)
        locations = locateAllOnScreen(chest_button_path)
        
        try:
            location = tuple(locations)[-1]
        except ImageNotFoundException2:
            logger.error(f"Unable to find any {chest_name} button")
        else:
            click_on_location(location)
            time.sleep(2)
        
            for _ in range(60):
                main_screen = get_main_screen(
                    main_screen, 
                    arg_is_fire, 
                    do_prestige
                )
                
                if main_screen:
                    break
                
                time.sleep(1)
            
            if not_last:
                time.sleep(1)
                p.press("b")
                main_screen = False
                time.sleep(wait_time_bag_opened)
                
    return main_screen


def open_chests(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    time.sleep(0.5)
    p.press("b")
    main_screen = False
    time.sleep(wait_time_bag_opened)
    
    try:
        click_on_image(treasure_tab_path)
    except ImageNotFoundException:
        logger.error("Unable to find treasure tab in the bag")
    
    main_screen = open_chest(
        common_chest_path, 
        common_chest_button_path, 
        "common chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        uncommon_chest_path, 
        uncommon_chest_button_path, 
        "uncommon chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        rare_chest_path, 
        rare_chest_button_path, 
        "rare chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        wooden_chest_path, 
        wooden_chest_button_path, 
        "wooden chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        iron_chest_path, 
        iron_chest_button_path, 
        "iron chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        golden_chest_path, 
        golden_chest_button_path, 
        "golden chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        comet_chest_path, 
        comet_chest_button_path, 
        "comet chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        lunar_chest_path, 
        lunar_chest_button_path, 
        "lunar chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        solar_chest_path, 
        solar_chest_button_path, 
        "solar chest", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        mistery_box_path, 
        mistery_box_button_path, 
        "mistery box", 
        main_screen, 
        arg_is_fire, 
        do_prestige
    )
    
    main_screen = open_chest(
        oracle_gift_path, 
        oracle_gift_button_path, 
        "oracle's gift", 
        main_screen, 
        arg_is_fire, 
        do_prestige,
        False
    )
    
    return main_screen


def awake(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(awake_advice_path)
    except ImageNotFoundException:
        logger.debug("No awake advice")
        return main_screen
        
    main_screen = False
    time.sleep(1)
    did_something = False
    
    for _ in range(60):
        try:
            click_on_image(awake_button_path)
        except ImageNotFoundException:
            logger.debug("No hero to awake")
            break
        else:
            if not locateOnScreen(manual_green_path):
                break
            
            logger.info("Hero awaken")
            did_something = True
            time.sleep(4.5)

    if not did_something:
        logger.error("Failed to awake any hero")

    return main_screen


def open_mailbox(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(mailbox_path)
    except ImageNotFoundException:
        logger.error("Unable to find mailbox")
        return main_screen
    
    main_screen = False
    time.sleep(0.5)
    claimed = False

    try:
        click_on_image(claim_green_path)
    except ImageNotFoundException:
        logger.debug("No message to claim")
    else:
        logger.info("Message claimed")
        p.press("esc")
        claimed = True
    
    p.press("esc")
    
    if claimed:
        close_save_and_exit()

    return main_screen


max_emblem_buttons = 4


def spend_emblem(
    tab_path, 
    tab_2_path, 
    name, 
    emblem_path, 
    emblem_name,
    tab_confidence=0.9,
):
    tab_active = False
    
    try:
        click_on_image(tab_path, confidence=tab_confidence)
        tab_active = True
    except ImageNotFoundException:
        try:
            click_on_image(tab_2_path, confidence=tab_confidence)
            tab_active = True
        except ImageNotFoundException:
            logger.debug(f"No active {name} tab found")
    
    if tab_active:
        time.sleep(0.5)
        
        try:
            locations = locateAllOnScreenAndFilterNear(emblem_path)
        except ImageNotFoundException:
            logger.error(f"Unable to find any emblem of {emblem_name} button")
        else:
            if len(locations) != max_emblem_buttons:
                logger.error(
                    f"Unable to find {max_emblem_buttons} emblem of " + 
                    f"{emblem_name} buttons"
                )
            else:
                click_on_location(locations[0])
                logger.info(f"Acquired {name} chests from merchant")
                time.sleep(0.5)


def spend_emblems(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    p.press("x")
    
    main_screen = False
    time.sleep(1)

    try:
        click_on_image(emblem_market_path)
    except ImageNotFoundException:
        logger.debug("No active emblem market")
        return main_screen
    
    time.sleep(0.5)
    
    spend_emblem(
        gear_tab_path, 
        gear_tab_2_path, 
        "gear", 
        emblem_of_courage_path, 
        "courage",
    )
    
    spend_emblem(
        jewel_tab_path, 
        jewel_tab_2_path, 
        "jewel", 
        emblem_of_valor_path, 
        "valor",
        tab_confidence=0.91,
    )
    
    
    spend_emblem(
        soulstone_tab_path, 
        soulstone_tab_2_path, 
        "soulstone", 
        emblem_of_brotherhood_path, 
        "brotherhood",
        tab_confidence=0.91,
    )
    
    return main_screen


def do_battle_pass(main_screen, arg_is_fire, do_prestige):
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    try:
        click_on_image(battle_pass_path, confidence=0.905)
    except ImageNotFoundException:
        logger.debug("No battle pass advice")
        return main_screen
    
    main_screen = False
    time.sleep(1)
    did_something = False
    
    try:
        click_on_image(rewards_path)
    except ImageNotFoundException:
        logger.error("Unable to find rewards tab in battle pass")
        return main_screen
        
    time.sleep(1)
    
    screens_n = 6
    
    for _ in range(screens_n):
        scroll_right("battle_pass")
    
    time.sleep(1)
    done = False
    
    for i in range(screens_n):
        found_claim = False
        
        try:
            locations = locateAllOnScreenAndFilterNear(
                claim_dark_green_3_path, 
            )
        except ImageNotFoundException as e:
            pass
        else:
            for location in locations:
                click_on_location(location)
                time.sleep(0.5)
            
            done = True
            
        first_time = not bool(i)
        scroll_left("battle_pass", first_time)
        
        if i != screens_n -1:
            time.sleep(1)
    
    if not done:
        logger.error("No claim button found in battle pass")
    
    return main_screen


def check(
    main_screen, 
    arg_is_fire, 
    spend_dust, 
    events, 
    no_tavern,
    do_prestige,
    first_time,
):
    if first_time:
        main_screen = open_mailbox(main_screen, arg_is_fire, do_prestige)
    
    main_screen = do_research(main_screen, arg_is_fire, do_prestige)
    main_screen = do_guardian(main_screen, arg_is_fire, do_prestige)
    main_screen = do_engineer(main_screen, arg_is_fire, do_prestige)
    
    main_screen = do_alchemist(
        main_screen, 
        arg_is_fire, 
        spend_dust, 
        do_prestige
    )
    
    main_screen = do_guild_expedition(main_screen, arg_is_fire, do_prestige)
    main_screen = do_quest(main_screen, arg_is_fire, do_prestige)
    
    main_screen = get_pickaxes(
        main_screen, 
        arg_is_fire, 
        do_prestige, 
        from_advice=True
    )
    
    main_screen = hit_crystal(main_screen, arg_is_fire, do_prestige)
    
    main_screen = do_shop(main_screen, arg_is_fire, do_prestige)
    main_screen = do_daily_reward(main_screen, arg_is_fire, do_prestige)
    
    if not no_tavern:
        main_screen = do_tavern(main_screen, arg_is_fire, do_prestige)
    
    main_screen = do_oracle(main_screen, arg_is_fire, do_prestige)
    main_screen = do_oracle_gift(main_screen, arg_is_fire, do_prestige)
    main_screen = do_map(main_screen, arg_is_fire, do_prestige)
    main_screen = hit_chaos(main_screen, arg_is_fire, do_prestige)
    
    if events and first_time:
        main_screen = do_event(main_screen, arg_is_fire, do_prestige)
    
    if do_prestige and first_time:
        main_screen = prestige(main_screen, arg_is_fire, do_prestige)
    
    if first_time:
        main_screen = spend_emblems(main_screen, arg_is_fire, do_prestige)
        main_screen = open_chests(main_screen, arg_is_fire, do_prestige)
    

    main_screen = do_battle_pass(main_screen, arg_is_fire, do_prestige)
    main_screen = do_machine(main_screen, arg_is_fire, do_prestige)
    main_screen = do_machine(main_screen, arg_is_fire, do_prestige)
    main_screen = do_arena(main_screen, arg_is_fire, do_prestige)
    main_screen = awake(main_screen, arg_is_fire, do_prestige)
    
    main_screen = get_main_screen(main_screen, arg_is_fire, do_prestige)
    
    return main_screen


parser = argparse.ArgumentParser(
    prog='firestone.py',
    description='Automates the Firestone idle game',
)

parser.add_argument(
    "command",
    choices=("fire", "pre"),
    nargs="?",
    help="Make the guardian attack. 'pre' is equivalent to 'fire -p'",
)

parser.add_argument(
    "-p", 
    "--prestige", 
    action="store_true", 
    help="Enables auto-upgrade of heroes and auto-prestige"
)

parser.add_argument(
    "-k", 
    "--decorated", 
    action="store_true", 
    help="Equivalent of -t -e -d, or -ted"
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


p.keyDown("alt")
time.sleep(0.2)
p.press("tab")
time.sleep(0.2)
p.keyUp("alt")

time.sleep(0.5)

wait_sec_pickaxes = 5737
safe_delta_sec = 300


def main():
    p.FAILSAFE = True
    args = parser.parse_args()
    arg_is_fire = False
    spend_dust = args.spend_dust
    no_tavern = args.no_tavern
    events = args.events
    do_prestige = args.prestige
    decorated = args.decorated

    if args.command == "fire":
        arg_is_fire = True
    elif args.command == "pre":
        arg_is_fire = True
        do_prestige = True

    if decorated:
        no_tavern = True
        events = True
        spend_dust = True

    wait_sec = 100 if arg_is_fire else 3
    prev_time_safe = time.time()
    prev_time_pickaxes = 0
    prev_time = 0
    main_screen = is_main_screen()
    
    while True:
        if time.time() - prev_time_safe >= safe_delta_sec:
            main_screen = get_main_screen(
                main_screen, 
                arg_is_fire, 
                do_prestige
            )
            
            prev_time_safe = time.time()
        
        if time.time() - prev_time_pickaxes >= wait_sec_pickaxes:
            main_screen = get_pickaxes(main_screen, arg_is_fire, do_prestige)
            prev_time_pickaxes = time.time()
            
            main_screen = get_main_screen(
                main_screen, 
                arg_is_fire, 
                do_prestige
            )
        
        main_screen = is_main_screen()
        
        if time.time() - prev_time >= wait_sec and main_screen:
            main_screen = check(
                main_screen, 
                arg_is_fire, 
                spend_dust, 
                events,
                no_tavern,
                do_prestige,
                True,
            )
            
            main_screen_real = is_main_screen(main_screen)
            
            if main_screen_real:
                duration_advice = 3
                p.moveTo(advice_down_x, advice_down_y)
                dragTo(advice_up_x, advice_up_y, duration=duration_advice)
                press_power(do_prestige, main_screen_real)
                time.sleep(4)
                
                main_screen = check(
                    main_screen, 
                    arg_is_fire, 
                    spend_dust, 
                    events,
                    no_tavern,
                    do_prestige,
                    False,
                )
                
                main_screen_real = is_main_screen(main_screen)
                
                if main_screen_real:
                    p.moveTo(advice_up_x, advice_up_y)
                    
                    dragTo(
                        advice_down_x, 
                        advice_down_y, 
                        duration=duration_advice
                    )
                    
                    press_power(do_prestige, main_screen_real)
                    time.sleep(4)
                    prev_time = time.time()
        
        main_screen_real = is_main_screen()
        
        if arg_is_fire and main_screen_real: 
            move_random_around_home()
            p.click(interval=0.4)
            press_power(do_prestige, main_screen_real)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except FailSafeException:
        try:
            p.FAILSAFE = False
            move_random_around_home()
            main()
        except KeyboardInterrupt:
            pass
