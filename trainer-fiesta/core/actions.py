from pyautogui import screenshot, moveTo, click, locateOnScreen
from keyboard import add_hotkey, press_and_release
from time import sleep, strftime, localtime
from numpy import array, mean
from core.config import *
from sys import exit
import os

def start_loop():
    global loop_status
    loop_status = True
    log("STARTED!")

def pause_loop():
    global loop_status
    loop_status = False
    log("PAUSED!")
    log("PRESS PAGE UP TO RESUME")

def stop_loop():
    log("EXITING...")
    os._exit(0)  

# register keys to turn on/off the trainer
add_hotkey(START_KEY, start_loop)
add_hotkey(PAUSE_KEY, pause_loop)
add_hotkey(STOP_KEY, stop_loop)

def get_bar_percentage(region, threshold=0.45):
    """Calculate the filled percentage of a status bar based on a grayscale screenshot."""
    bar = screenshot(region=region).convert("L")  # convert to grayscale
    arr = array(bar)
    bw = arr >= int(threshold * 255)
    width = bw.shape[1]
    fill_width = sum(mean(bw[:, col]) > 0.5 for col in range(width))
    return (fill_width / width) * 100

def log(message):
    """Prints a log message with a timestamp."""
    timestamp = strftime("%H:%M:%S", localtime())
    print(f"{timestamp}: {message}")

def use_uh():
    """Uses an Ultimate Healing Rune if health is below HEAL_BELOW_HP."""
    health_percentage = get_bar_percentage(REGION_HEALTH)
    if health_percentage > HEAL_BELOW_HP:
        return
    
    log(f"Health: {health_percentage:.1f}% - Using one Ultimate Healing Rune...")
    moveTo(REGION_UH)
    click(REGION_UH, button='right')
    moveTo(REGION_PLAYER)
    click(REGION_PLAYER, button='left')
    sleep(1)

def cast_spell(spell_name):
    """Casts a spell if mana is above CAST_SPELL_ABOVE_MANA."""
    mana_percentage = get_bar_percentage(REGION_MANA)
    if mana_percentage < CAST_SPELL_ABOVE_MANA:
        return
    
    eat_food()
    spell_key = SPELLS.get(spell_name)
    log(f"Mana: {mana_percentage:.1f}% - Casting {spell_name}...")
    press_and_release(spell_key)
    sleep(1)

def eat_food():
    """Eat food."""
    moveTo(REGION_FOOD)
    for _ in range(2):
        click(REGION_FOOD, button='right')

def attack_next_slime(slimes_counter):
    """Attacks the next slime if found in the battle region."""
    targeting_slime = locateOnScreen(TARGETING_SLIME_IMG, confidence=0.9, region=REGION_BATTLE)
    full_hp_slime = locateOnScreen(FULL_HP_SLIME_IMG, confidence=0.9, region=REGION_BATTLE)
    if full_hp_slime and not targeting_slime:
        sleep(2)
        moveTo(REGION_SLIME_ON_BATTLE)
        click(REGION_SLIME_ON_BATTLE, button="left")
        sleep(0.5)
        eat_food()
        slimes_counter += 1
        log(f"Slimes killed: {slimes_counter}")
    return slimes_counter

def main():
    """Main function."""
    log("-------------------")
    log(f"TRAINER-FIESTA {VERSION}")
    log("-------------------")
    log(f"{START_KEY}   → Start")
    log(f"{PAUSE_KEY} → Pause")
    log(f"{STOP_KEY}       → Exit")
    log("-------------------")
    global slimes_counter
    while True:
        if loop_status:
            slimes_counter = attack_next_slime(slimes_counter)
            use_uh()
            cast_spell(SPELL)

            battle = locateOnScreen(BATTLE_NAME_IMG, confidence=0.9, region=REGION_BATTLE_NAME)
            if not battle:
                log("Battle not found...")
                log("Exiting the trainer.")
                exit(0)
