import logging
from BaseClasses import Item, ItemClassification
from .Types import ItemData, OneShotItem
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import OneShotWorld

ITEM_ID_BASE = 7_770_000


def create_itempool(world: "OneShotWorld") -> List[Item]:
    itempool: List[Item] = []

    # Always include key items
    for name in key_items.keys():
        if name == "Photo of Niko":
            for i in range(0, 9):
                itempool.append(create_item(world, name))
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
    else:
        world.multiworld.get_location("Solstice", world.player).place_locked_item(victory)

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
    "Solstice Protocol":       ItemData(ITEM_ID_BASE + 704, ItemClassification.progression),

    # Starter House
#    "Television Remote":       ItemData(ITEM_ID_BASE + 2, ItemClassification.progression),
    "Lightbulb":               ItemData(ITEM_ID_BASE + 1,  ItemClassification.progression),
    "Bottle of Alcohol":       ItemData(ITEM_ID_BASE + 3,  ItemClassification.useful),
    "Dry Branch":              ItemData(ITEM_ID_BASE + 4,  ItemClassification.useful),
    "Basement Key":            ItemData(ITEM_ID_BASE + 7,  ItemClassification.useful),

    # Barrens
    "Camera":                  ItemData(ITEM_ID_BASE + 8,  ItemClassification.useful),
    "Screwdriver":             ItemData(ITEM_ID_BASE + 9,  ItemClassification.useful),
    "Broken Battery":          ItemData(ITEM_ID_BASE + 12, ItemClassification.useful),
    "Metal Rod":               ItemData(ITEM_ID_BASE + 19, ItemClassification.useful),
    "Sponge":                  ItemData(ITEM_ID_BASE + 20, ItemClassification.useful),
    "Empty Syringe":           ItemData(ITEM_ID_BASE + 21, ItemClassification.useful),
    "Amber":                   ItemData(ITEM_ID_BASE + 23, ItemClassification.progression),
    "Strange Journal":         ItemData(ITEM_ID_BASE + 24, ItemClassification.progression),
    "Gas Mask":                ItemData(ITEM_ID_BASE + 47, ItemClassification.useful),
    "Rubber Gloves":           ItemData(ITEM_ID_BASE + 48, ItemClassification.useful),

    # Glen
    "Feather":                 ItemData(ITEM_ID_BASE + 25, ItemClassification.progression),
    "Bottle of Dye":           ItemData(ITEM_ID_BASE + 26, ItemClassification.useful),
    "Tube of Water":           ItemData(ITEM_ID_BASE + 27, ItemClassification.useful),
    "Seed":                    ItemData(ITEM_ID_BASE + 28, ItemClassification.useful),
    "Wool":                    ItemData(ITEM_ID_BASE + 29, ItemClassification.useful),
    "Novelty T-Shirt":         ItemData(ITEM_ID_BASE + 50, ItemClassification.useful),


    # Refuge
    "Die":                     ItemData(ITEM_ID_BASE + 31, ItemClassification.progression),
    "Magnets":                 ItemData(ITEM_ID_BASE + 36, ItemClassification.useful),
    "Metal Can":               ItemData(ITEM_ID_BASE + 37, ItemClassification.useful),
    "Scissors":                ItemData(ITEM_ID_BASE + 38, ItemClassification.useful),
    "Weird Film":              ItemData(ITEM_ID_BASE + 39, ItemClassification.progression),
    "Concave Lens":            ItemData(ITEM_ID_BASE + 40, ItemClassification.useful),
    "Convex Lens":             ItemData(ITEM_ID_BASE + 41, ItemClassification.useful),
    "Thin Lens":               ItemData(ITEM_ID_BASE + 42, ItemClassification.useful),
    "Thick Lens":              ItemData(ITEM_ID_BASE + 43, ItemClassification.useful),
    "Kips Library Card":       ItemData(ITEM_ID_BASE + 46, ItemClassification.useful),
    "Glitter Glue":            ItemData(ITEM_ID_BASE + 44, ItemClassification.useful),
    "Photo of Niko":           ItemData(ITEM_ID_BASE + 45, ItemClassification.useful),
    "Photo of Niko (Blink)":   ItemData(ITEM_ID_BASE + 66, ItemClassification.filler),
    "Water Pill":              ItemData(ITEM_ID_BASE + 56, ItemClassification.useful),
    "Dirt":                    ItemData(ITEM_ID_BASE + 55, ItemClassification.useful),



    # Tower / solstice
    "Memory Card":             ItemData(ITEM_ID_BASE + 75, ItemClassification.progression),
    "Memory Card (Backup)":    ItemData(ITEM_ID_BASE + 76, ItemClassification.progression),
    "Music Box":               ItemData(ITEM_ID_BASE + 78, ItemClassification.progression),
    "Charged Battery (Green)": ItemData(ITEM_ID_BASE + 77, ItemClassification.progression),
}

# ── Craft items (only when IncludeCrafts enabled) ─────────────────────────────
craft_items = {
    # Starter House
    "Wet Branch":              ItemData(ITEM_ID_BASE + 5,  ItemClassification.useful),
    "Torch":                   ItemData(ITEM_ID_BASE + 6,  ItemClassification.useful),
    "Empty Bottle":            ItemData(ITEM_ID_BASE + 11, ItemClassification.useful),

    # Barrens
    "Empty Battery":           ItemData(ITEM_ID_BASE + 13, ItemClassification.useful),
    "Charged Battery":         ItemData(ITEM_ID_BASE + 14, ItemClassification.useful),
    "Bottle of Smoke":         ItemData(ITEM_ID_BASE + 15, ItemClassification.useful),
    "Bottle of Acid":          ItemData(ITEM_ID_BASE + 16, ItemClassification.useful),
    "Wet Sponge":              ItemData(ITEM_ID_BASE + 17, ItemClassification.useful),
    "Crowbar":                 ItemData(ITEM_ID_BASE + 18, ItemClassification.useful),
    "Filled Syringe":          ItemData(ITEM_ID_BASE + 22, ItemClassification.useful),
    "Lens":                    ItemData(ITEM_ID_BASE + 10, ItemClassification.useful),

    # Glen
    "Feather Pen":             ItemData(ITEM_ID_BASE + 30, ItemClassification.progression),

    # Refuge
    "Button (?)":              ItemData(ITEM_ID_BASE + 32, ItemClassification.useful),
    "Magnetized (?) Button":   ItemData(ITEM_ID_BASE + 33, ItemClassification.useful),
    "Taped Button":            ItemData(ITEM_ID_BASE + 34, ItemClassification.progression),
    "Photo of Niko (Sticky)":  ItemData(ITEM_ID_BASE + 54, ItemClassification.progression),
    "Nikos Library Card":      ItemData(ITEM_ID_BASE + 51, ItemClassification.useful),
    "Medicated Water":         ItemData(ITEM_ID_BASE + 57, ItemClassification.progression),
}

# ── External TWM file items (only when IncludeExternalFiles enabled) ──────────
file_items = {
    "Outpost PC File":          ItemData(ITEM_ID_BASE + 800, ItemClassification.useful),
    "Clover App":               ItemData(ITEM_ID_BASE + 801, ItemClassification.progression),
    "Prototype Files":          ItemData(ITEM_ID_BASE + 802, ItemClassification.useful),
    "Cedric Files":             ItemData(ITEM_ID_BASE + 803, ItemClassification.useful),
    "Rue Files":                ItemData(ITEM_ID_BASE + 804, ItemClassification.useful),
}

# ── Collectible wallpapers ────────────────────────────────────────────────────
wallpaper_items = {
    "Wallpaper: Outpost":           ItemData(ITEM_ID_BASE + 401, ItemClassification.filler),
    "Wallpaper: Factory":           ItemData(ITEM_ID_BASE + 402, ItemClassification.filler),
    "Wallpaper: Navigate":          ItemData(ITEM_ID_BASE + 403, ItemClassification.filler),
    "Wallpaper: Courtyard":         ItemData(ITEM_ID_BASE + 404, ItemClassification.filler),
    "Wallpaper: Calamus and Alula": ItemData(ITEM_ID_BASE + 405, ItemClassification.filler),
    "Wallpaper: Catwalks":          ItemData(ITEM_ID_BASE + 406, ItemClassification.filler),
    "Wallpaper: Library Stroll":    ItemData(ITEM_ID_BASE + 407, ItemClassification.filler),
    "Wallpaper: Secret RAM Club":   ItemData(ITEM_ID_BASE + 408, ItemClassification.filler),
    "Wallpaper: Lamplighter":       ItemData(ITEM_ID_BASE + 409, ItemClassification.filler),
    "Wallpaper: Cafe":              ItemData(ITEM_ID_BASE + 410, ItemClassification.filler),
    "Wallpaper: Maize":             ItemData(ITEM_ID_BASE + 411, ItemClassification.filler),
    "Wallpaper: Tower":             ItemData(ITEM_ID_BASE + 412, ItemClassification.filler),
    "Wallpaper: Prophets":          ItemData(ITEM_ID_BASE + 413, ItemClassification.filler),
    "Wallpaper: Memory":            ItemData(ITEM_ID_BASE + 414, ItemClassification.filler),
    "Wallpaper: Reflection":        ItemData(ITEM_ID_BASE + 415, ItemClassification.filler),
    "Wallpaper: From Niko":         ItemData(ITEM_ID_BASE + 416, ItemClassification.filler),
}

# ── Friend profiles ───────────────────────────────────────────────────────────
profile_items = {
    "Profile: ProphetBot":        ItemData(ITEM_ID_BASE + 426, ItemClassification.filler),
    "Profile: Silver":            ItemData(ITEM_ID_BASE + 427, ItemClassification.filler),
    "Profile: Rowbot":            ItemData(ITEM_ID_BASE + 428, ItemClassification.filler),
    "Profile: Shepherd":          ItemData(ITEM_ID_BASE + 429, ItemClassification.filler),
    "Profile: Magpie":            ItemData(ITEM_ID_BASE + 430, ItemClassification.filler),
    "Profile: Calamus":           ItemData(ITEM_ID_BASE + 431, ItemClassification.filler),
    "Profile: Alula":             ItemData(ITEM_ID_BASE + 432, ItemClassification.filler),
    "Profile: Maize":             ItemData(ITEM_ID_BASE + 433, ItemClassification.filler),
    "Profile: Ling":              ItemData(ITEM_ID_BASE + 434, ItemClassification.filler),
    "Profile: Watcher":           ItemData(ITEM_ID_BASE + 435, ItemClassification.filler),
    "Profile: Mason":             ItemData(ITEM_ID_BASE + 436, ItemClassification.filler),
    "Profile: Lamplighter":       ItemData(ITEM_ID_BASE + 437, ItemClassification.filler),
    "Profile: Kelvin":            ItemData(ITEM_ID_BASE + 438, ItemClassification.filler),
    "Profile: Kip":               ItemData(ITEM_ID_BASE + 439, ItemClassification.filler),
    "Profile: George":            ItemData(ITEM_ID_BASE + 440, ItemClassification.filler),
    "Profile: Prototype":         ItemData(ITEM_ID_BASE + 446, ItemClassification.filler),
    "Profile: Cedric":            ItemData(ITEM_ID_BASE + 447, ItemClassification.filler),
    "Profile: Rue":               ItemData(ITEM_ID_BASE + 448, ItemClassification.filler),
    "Profile: The World Machine": ItemData(ITEM_ID_BASE + 449, ItemClassification.filler),
    "Profile: The Author":        ItemData(ITEM_ID_BASE + 450, ItemClassification.filler),
    "Profile: Niko":              ItemData(ITEM_ID_BASE + 451, ItemClassification.filler),
}

# ── Desktop themes ────────────────────────────────────────────────────────────
theme_items = {
    "Theme: Blue":    ItemData(ITEM_ID_BASE + 461, ItemClassification.filler),
    "Theme: Cyan":    ItemData(ITEM_ID_BASE + 462, ItemClassification.filler),
    "Theme: Green":   ItemData(ITEM_ID_BASE + 463, ItemClassification.filler),
    "Theme: Yellow":  ItemData(ITEM_ID_BASE + 464, ItemClassification.filler),
    "Theme: Red":     ItemData(ITEM_ID_BASE + 465, ItemClassification.filler),
    "Theme: Pink":    ItemData(ITEM_ID_BASE + 466, ItemClassification.filler),
    "Theme: Orange":  ItemData(ITEM_ID_BASE + 467, ItemClassification.filler),
    "Theme: White":   ItemData(ITEM_ID_BASE + 468, ItemClassification.filler),
    "Theme: Rainbow": ItemData(ITEM_ID_BASE + 469, ItemClassification.filler),
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
    **filler_items,
    **victory_item,
}
