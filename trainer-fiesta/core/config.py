# software version
VERSION = "v1.0"

# define status and core variables
loop_status = False
slimes_counter = -1
START_KEY = "PAGE UP"
PAUSE_KEY = "PAGE DOWN"
STOP_KEY = "END"

# define screen regions
REGION_HEALTH = (1774, 156, 81, 5)
REGION_MANA = (1773, 171, 82, 3)
REGION_BATTLE = (1746, 362, 172, 164)
REGION_SLIME_ON_BATTLE = (1754, 408)
REGION_FOOD = (1592, 654)
REGION_UH = (1592, 350)
REGION_PLAYER = (1255, 246)
REGION_BATTLE_NAME = (1744,361,65,17)

# bar percentages
HEAL_BELOW_HP = 60
CAST_SPELL_ABOVE_MANA = 80

# spells for mana training
SPELLS = {
    "exura": "F1",
    "utevo lux": "F3",
    "adura vita": "F10"
}

# spell to cast 
SPELL = "exura"

# image paths
TARGETING_SLIME_IMG = "trainer-fiesta/assets/images/targeting_slime.PNG"
FULL_HP_SLIME_IMG = "trainer-fiesta/assets/images/full_hp_slime.PNG"
BATTLE_NAME_IMG = "trainer-fiesta/assets/images/battle_name.PNG"
