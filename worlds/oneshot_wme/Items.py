import logging
from BaseClasses import Item, ItemClassification
from .Types import ItemData, LocData, OneShotItem
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import OneShotWorld

ITEM_ID_BASE = 7_770_000


def create_itempool(world: "OneShotWorld") -> List[Item]:
    itempool: List[Item] = []
    starting_zone = world.options.StartingZone.value

    # Always include key items
    for name in key_items.keys():
        if name == "Photo of Niko":
            for i in range(0, 9):
                itempool.append(create_item(world, name))
        elif name == "Barrens Key" and starting_zone == 1:
            continue  # precollected based on StartingZone option
        elif name == "Glen Key" and starting_zone == 2:
            continue  # precollected based on StartingZone option
        elif name == "Refuge Key" and starting_zone == 3:
            continue  # precollected based on StartingZone option
        elif name == "Bottle of Dye" and not world.options.IncludeCrafts:
            itempool.append(OneShotItem(name, ItemClassification.useful, item_table[name].ap_code, world.player))
        else:
            itempool.append(create_item(world, name))

    # Craft items only if crafts enabled
    if world.options.IncludeCrafts:
        for name in craft_items.keys():
            itempool.append(create_item(world, name))

    # Collectibles
    if world.options.IncludeWallpapers:
        for name in wallpaper_items.keys():
            itempool.append(create_item(world, name))

    if world.options.IncludeFriends:
        for name in profile_items.keys():
            itempool.append(create_item(world, name))

    if world.options.IncludeThemes:
        for name in theme_items.keys():
            itempool.append(create_item(world, name))

    if world.options.IncludeExternalFiles:
        for name in file_items.keys():
            itempool.append(create_item(world, name))

    # Place victory at the goal location
    victory = create_item(world, "Victory")
    goal = world.options.GameGoal.value
    if goal == 0:
        world.multiworld.get_location("Leave", world.player).place_locked_item(victory)
    elif goal == 1:
        world.multiworld.get_location("Victory?", world.player).place_locked_item(victory)
#    else:
#        world.multiworld.get_location("Solstice", world.player).place_locked_item(victory)

    # Fill remaining locations with junk
    remaining = get_total_locations(world) - len(itempool)
    if remaining > 0:
        itempool += create_junk_items(world, remaining)

    return itempool


def create_item(world: "OneShotWorld", name: str) -> Item:
    data = item_table[name]
    return OneShotItem(name, data.classification, data.ap_code, world.player)


def create_junk_items(world: "OneShotWorld", count: int) -> List[Item]:
    trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []

    trap_list: Dict[str, int] = {}
    if trap_chance > 0:
        trap_list["Spooky Popup Trap"] = world.options.SpookyPopupTrapWeight.value
        trap_list["Crash Trap"]        = world.options.CrashTrapWeight.value

    for i in range(count):
        if (trap_chance > 0
                and world.random.randint(1, 100) <= trap_chance
                and any(v > 0 for v in trap_list.values())):
            name = world.random.choices(
                list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]
            junk_pool.append(create_item(world, name))
        else:
            junk_pool.append(create_item(world, "Pancake"))

    return junk_pool


# ── Key items (always in pool) ────────────────────────────────────────────────
key_items = {
    # Region access keys
    "Barrens Key":             ItemData(ITEM_ID_BASE + 700, ItemClassification.progression),
    "Glen Key":                ItemData(ITEM_ID_BASE + 701, ItemClassification.progression),
    "Refuge Key":              ItemData(ITEM_ID_BASE + 702, ItemClassification.progression),
#    "Solstice Protocol":       ItemData(ITEM_ID_BASE + 704, ItemClassification.progression),

    # Starter House
#    "Television Remote":       ItemData(ITEM_ID_BASE + 2, ItemClassification.progression),
    "Lightbulb":               ItemData(ITEM_ID_BASE + 1,  ItemClassification.progression),
    "Bottle of Alcohol":       ItemData(ITEM_ID_BASE + 3,  ItemClassification.progression),
    "Dry Branch":              ItemData(ITEM_ID_BASE + 4,  ItemClassification.progression),
    "Basement Key":            ItemData(ITEM_ID_BASE + 7,  ItemClassification.progression),

    # Barrens
    "Camera":                  ItemData(ITEM_ID_BASE + 8,  ItemClassification.progression),
    "Screwdriver":             ItemData(ITEM_ID_BASE + 9,  ItemClassification.progression),
    "Broken Battery":          ItemData(ITEM_ID_BASE + 12, ItemClassification.progression),
    "Metal Rod":               ItemData(ITEM_ID_BASE + 19, ItemClassification.progression),
    "Sponge":                  ItemData(ITEM_ID_BASE + 20, ItemClassification.progression),
    "Empty Syringe":           ItemData(ITEM_ID_BASE + 21, ItemClassification.progression),
    "Amber":                   ItemData(ITEM_ID_BASE + 23, ItemClassification.progression),
    "Strange Journal":         ItemData(ITEM_ID_BASE + 24, ItemClassification.progression),
    "Gas Mask":                ItemData(ITEM_ID_BASE + 47, ItemClassification.progression),
    "Rubber Gloves":           ItemData(ITEM_ID_BASE + 48, ItemClassification.progression),

    # Glen
    "Feather":                 ItemData(ITEM_ID_BASE + 25, ItemClassification.progression),
    "Bottle of Dye":           ItemData(ITEM_ID_BASE + 26, ItemClassification.progression),
    "Tube of Water":           ItemData(ITEM_ID_BASE + 27, ItemClassification.progression),
    "Seed":                    ItemData(ITEM_ID_BASE + 28, ItemClassification.progression),
    "Wool":                    ItemData(ITEM_ID_BASE + 29, ItemClassification.progression),
    "Novelty T-Shirt":         ItemData(ITEM_ID_BASE + 50, ItemClassification.progression),


    # Refuge
    "Die":                     ItemData(ITEM_ID_BASE + 31, ItemClassification.progression),
    "Magnets":                 ItemData(ITEM_ID_BASE + 36, ItemClassification.progression),
    "Metal Can":               ItemData(ITEM_ID_BASE + 37, ItemClassification.progression),
    "Scissors":                ItemData(ITEM_ID_BASE + 38, ItemClassification.progression),
    "Weird Film":              ItemData(ITEM_ID_BASE + 39, ItemClassification.progression),
    "Concave Lens":            ItemData(ITEM_ID_BASE + 40, ItemClassification.progression),
    "Convex Lens":             ItemData(ITEM_ID_BASE + 41, ItemClassification.progression),
    "Thin Lens":               ItemData(ITEM_ID_BASE + 42, ItemClassification.progression),
    "Thick Lens":              ItemData(ITEM_ID_BASE + 43, ItemClassification.progression),
    "Kip's Library Card":      ItemData(ITEM_ID_BASE + 46, ItemClassification.progression),
    "Glitter Glue":            ItemData(ITEM_ID_BASE + 44, ItemClassification.progression),
    "Photo of Niko":           ItemData(ITEM_ID_BASE + 45, ItemClassification.progression),
    "Photo of Niko (Blink)":   ItemData(ITEM_ID_BASE + 66, ItemClassification.filler),
    "Water Pill":              ItemData(ITEM_ID_BASE + 56, ItemClassification.progression),
    "Dirt":                    ItemData(ITEM_ID_BASE + 55, ItemClassification.progression),



    # Tower / solstice
#    "Memory Card":             ItemData(ITEM_ID_BASE + 75, ItemClassification.progression),
#    "Memory Card (Backup)":    ItemData(ITEM_ID_BASE + 76, ItemClassification.progression),
#    "Music Box":               ItemData(ITEM_ID_BASE + 78, ItemClassification.progression),
#    "Charged Battery (Green)": ItemData(ITEM_ID_BASE + 77, ItemClassification.progression),
}

# ── Craft items (only when IncludeCrafts enabled) ─────────────────────────────
craft_items = {
    # Starter House
    "Wet Branch":              ItemData(ITEM_ID_BASE + 5,  ItemClassification.progression),
    "Torch":                   ItemData(ITEM_ID_BASE + 6,  ItemClassification.progression),
    "Empty Bottle":            ItemData(ITEM_ID_BASE + 11, ItemClassification.progression),

    # Barrens
    "Empty Battery":           ItemData(ITEM_ID_BASE + 13, ItemClassification.progression),
    "Charged Battery":         ItemData(ITEM_ID_BASE + 14, ItemClassification.progression),
    "Bottle of Smoke":         ItemData(ITEM_ID_BASE + 15, ItemClassification.progression),
    "Bottle of Acid":          ItemData(ITEM_ID_BASE + 16, ItemClassification.progression),
    "Wet Sponge":              ItemData(ITEM_ID_BASE + 17, ItemClassification.progression),
    "Crowbar":                 ItemData(ITEM_ID_BASE + 18, ItemClassification.progression),
    "Filled Syringe":          ItemData(ITEM_ID_BASE + 22, ItemClassification.progression),
    "Lens":                    ItemData(ITEM_ID_BASE + 10, ItemClassification.progression),

    # Glen
    "Feather Pen":             ItemData(ITEM_ID_BASE + 30, ItemClassification.progression),

    # Refuge
    "Button (?)":              ItemData(ITEM_ID_BASE + 32, ItemClassification.progression),
    "Magnetized (?) Button":   ItemData(ITEM_ID_BASE + 33, ItemClassification.progression),
    "Taped Button":            ItemData(ITEM_ID_BASE + 34, ItemClassification.progression),
#    "Photo of Niko (Sticky)":  ItemData(ITEM_ID_BASE + 54, ItemClassification.progression),
    "Niko's Library Card":      ItemData(ITEM_ID_BASE + 51, ItemClassification.progression),
    "Medicated Water":         ItemData(ITEM_ID_BASE + 57, ItemClassification.progression),
}

# ── External TWM file items (only when IncludeExternalFiles enabled) ──────────
file_items = {
    "Outpost PC File":          ItemData(ITEM_ID_BASE + 800, ItemClassification.progression),
    "Clover App":               ItemData(ITEM_ID_BASE + 801, ItemClassification.progression),
#    "Prototype Files":          ItemData(ITEM_ID_BASE + 802, ItemClassification.progression),
#    "Cedric Files":             ItemData(ITEM_ID_BASE + 803, ItemClassification.progression),
#    "Rue Files":                ItemData(ITEM_ID_BASE + 804, ItemClassification.progression),
}

# ── Collectible wallpapers (AP items use 1100+ range)
wallpaper_items = {
    "Wallpaper: Outpost":           ItemData(ITEM_ID_BASE + 1100, ItemClassification.filler),
    "Wallpaper: Factory":           ItemData(ITEM_ID_BASE + 1101, ItemClassification.filler),
    "Wallpaper: Navigate":          ItemData(ITEM_ID_BASE + 1102, ItemClassification.filler),
    "Wallpaper: Courtyard":         ItemData(ITEM_ID_BASE + 1103, ItemClassification.filler),
    "Wallpaper: Calamus and Alula": ItemData(ITEM_ID_BASE + 1104, ItemClassification.filler),
    "Wallpaper: Catwalks":          ItemData(ITEM_ID_BASE + 1105, ItemClassification.filler),
    "Wallpaper: Library Stroll":    ItemData(ITEM_ID_BASE + 1106, ItemClassification.filler),
    "Wallpaper: Secret RAM Club":   ItemData(ITEM_ID_BASE + 1107, ItemClassification.filler),
    "Wallpaper: Lamplighter":       ItemData(ITEM_ID_BASE + 1108, ItemClassification.filler),
    "Wallpaper: Cafe":              ItemData(ITEM_ID_BASE + 1109, ItemClassification.filler),
    "Wallpaper: Maize":             ItemData(ITEM_ID_BASE + 1110, ItemClassification.filler),
    "Wallpaper: Tower":             ItemData(ITEM_ID_BASE + 1111, ItemClassification.filler),
#    "Wallpaper: Prophets":          ItemData(ITEM_ID_BASE + 1112, ItemClassification.filler),
#    "Wallpaper: Memory":            ItemData(ITEM_ID_BASE + 1113, ItemClassification.filler),
#    "Wallpaper: Reflection":        ItemData(ITEM_ID_BASE + 1114, ItemClassification.filler),
#    "Wallpaper: From Niko":         ItemData(ITEM_ID_BASE + 1115, ItemClassification.filler),
}

# ── Friend profiles (AP items use 1300+ range)
profile_items = {
    "Profile: ProphetBot":        ItemData(ITEM_ID_BASE + 1300, ItemClassification.filler),
    "Profile: Silver":            ItemData(ITEM_ID_BASE + 1301, ItemClassification.filler),
    "Profile: Rowbot":            ItemData(ITEM_ID_BASE + 1302, ItemClassification.filler),
    "Profile: Shepherd":          ItemData(ITEM_ID_BASE + 1303, ItemClassification.filler),
    "Profile: Magpie":            ItemData(ITEM_ID_BASE + 1304, ItemClassification.filler),
    "Profile: Calamus":           ItemData(ITEM_ID_BASE + 1305, ItemClassification.filler),
    "Profile: Alula":             ItemData(ITEM_ID_BASE + 1306, ItemClassification.filler),
    "Profile: Maize":             ItemData(ITEM_ID_BASE + 1307, ItemClassification.filler),
    "Profile: Ling":              ItemData(ITEM_ID_BASE + 1308, ItemClassification.filler),
    "Profile: Watcher":           ItemData(ITEM_ID_BASE + 1309, ItemClassification.filler),
    "Profile: Mason":             ItemData(ITEM_ID_BASE + 1310, ItemClassification.filler),
    "Profile: Lamplighter":       ItemData(ITEM_ID_BASE + 1311, ItemClassification.filler),
    "Profile: Kelvin":            ItemData(ITEM_ID_BASE + 1312, ItemClassification.filler),
    "Profile: Kip":               ItemData(ITEM_ID_BASE + 1313, ItemClassification.filler),
    "Profile: George":            ItemData(ITEM_ID_BASE + 1314, ItemClassification.filler),
#    "Profile: Prototype":         ItemData(ITEM_ID_BASE + 1315, ItemClassification.filler),
#    "Profile: Cedric":            ItemData(ITEM_ID_BASE + 1316, ItemClassification.filler),
#    "Profile: Rue":               ItemData(ITEM_ID_BASE + 1317, ItemClassification.filler),
#    "Profile: The World Machine": ItemData(ITEM_ID_BASE + 1318, ItemClassification.filler),
#    "Profile: The Author":        ItemData(ITEM_ID_BASE + 1319, ItemClassification.filler),
#    "Profile: Niko":              ItemData(ITEM_ID_BASE + 1320, ItemClassification.filler),
}

# ── Desktop themes (AP items use 1200+ range)
theme_items = {
    "Theme: Blue":    ItemData(ITEM_ID_BASE + 1200, ItemClassification.filler),
    "Theme: Cyan":    ItemData(ITEM_ID_BASE + 1201, ItemClassification.filler),
    "Theme: Green":   ItemData(ITEM_ID_BASE + 1202, ItemClassification.filler),
    "Theme: Yellow":  ItemData(ITEM_ID_BASE + 1203, ItemClassification.filler),
    "Theme: Red":     ItemData(ITEM_ID_BASE + 1204, ItemClassification.filler),
    "Theme: Pink":    ItemData(ITEM_ID_BASE + 1205, ItemClassification.filler),
    "Theme: Orange":  ItemData(ITEM_ID_BASE + 1206, ItemClassification.filler),
    "Theme: White":   ItemData(ITEM_ID_BASE + 1207, ItemClassification.filler),
    "Theme: Rainbow": ItemData(ITEM_ID_BASE + 1208, ItemClassification.filler),
}

badge_items = {
        "Badge: Chaotic Evil": ItemData(ITEM_ID_BASE + 1400, ItemClassification.filler),
        "Badge: Shock": ItemData(ITEM_ID_BASE + 1401, ItemClassification.filler),
#        "Badge: Extreme Bartering": ItemData(ITEM_ID_BASE + 1402, ItemClassification.filler),
        "Badge: Ram Whisperer": ItemData(ITEM_ID_BASE + 1403, ItemClassification.filler),
        "Badge: We Ride at Dawn": ItemData(ITEM_ID_BASE + 1404, ItemClassification.filler),
        "Badge: Secret": ItemData(ITEM_ID_BASE + 1405, ItemClassification.filler),
        "Badge: Bookworm": ItemData(ITEM_ID_BASE + 1406, ItemClassification.filler),
        "Badge: Pancakes": ItemData(ITEM_ID_BASE + 1407, ItemClassification.filler),
        "Badge: Rebirth": ItemData(ITEM_ID_BASE + 1408, ItemClassification.filler),
        "Badge: OneShot": ItemData(ITEM_ID_BASE + 1409, ItemClassification.filler),
        }

# ── Filler and traps ──────────────────────────────────────────────────────────
filler_items = {
    "Pancake":           ItemData(ITEM_ID_BASE + 900, ItemClassification.filler),
    "Spooky Popup Trap": ItemData(ITEM_ID_BASE + 901, ItemClassification.trap),
    "Crash Trap":        ItemData(ITEM_ID_BASE + 902, ItemClassification.trap),
}

# ── Victory ───────────────────────────────────────────────────────────────────
victory_item = {
    "Victory": ItemData(ITEM_ID_BASE + 999, ItemClassification.progression),
}

item_table = {
    **key_items,
    **craft_items,
    **file_items,
    **wallpaper_items,
    **profile_items,
    **theme_items,
    **badge_items,
    **filler_items,
    **victory_item,
}
