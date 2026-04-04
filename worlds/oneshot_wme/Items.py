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
        itempool.append(create_item(world, name))

    # Starting zone skips — precollect keys for zones the player skips
    starting_zone = world.options.StartingZone.value
    if starting_zone == 2:  # Glen start — skip Barrens
        world.multiworld.push_precollected(create_item(world, "Barrens Key"))
    elif starting_zone == 3:  # Refuge start — skip Barrens and Glen
        world.multiworld.push_precollected(create_item(world, "Barrens Key"))
        world.multiworld.push_precollected(create_item(world, "Glen Key"))

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
    "Tower Key":               ItemData(ITEM_ID_BASE + 703, ItemClassification.progression),
    "Solstice Protocol":       ItemData(ITEM_ID_BASE + 704, ItemClassification.progression),

    # Starter House
    "Lightbulb":               ItemData(ITEM_ID_BASE + 1,  ItemClassification.progression),
    "Basement Key":            ItemData(ITEM_ID_BASE + 7,  ItemClassification.progression),

    # Barrens
    "Amber":                   ItemData(ITEM_ID_BASE + 23, ItemClassification.progression),
    "Crowbar":                 ItemData(ITEM_ID_BASE + 19, ItemClassification.progression),

    # Glen
    "Feather":                 ItemData(ITEM_ID_BASE + 25, ItemClassification.progression),
    "Feather Pen":             ItemData(ITEM_ID_BASE + 30, ItemClassification.progression),
    "Clover":                  ItemData(ITEM_ID_BASE + 58, ItemClassification.progression),

    # Refuge
    "Die":                     ItemData(ITEM_ID_BASE + 31, ItemClassification.progression),
    "Weird Film":              ItemData(ITEM_ID_BASE + 39, ItemClassification.progression),

    # Tower / late game
    "Memory Card":             ItemData(ITEM_ID_BASE + 75, ItemClassification.progression),
    "Glowing Journal":         ItemData(ITEM_ID_BASE + 74, ItemClassification.progression),
    "Charged Battery (Green)": ItemData(ITEM_ID_BASE + 77, ItemClassification.progression),
}

# ── Craft items (only when IncludeCrafts enabled) ─────────────────────────────
craft_items = {
    # Starter House
    "Television Remote":       ItemData(ITEM_ID_BASE + 2,  ItemClassification.useful),
    "Bottle of Alcohol":       ItemData(ITEM_ID_BASE + 3,  ItemClassification.progression),
    "Dry Branch":              ItemData(ITEM_ID_BASE + 4,  ItemClassification.progression),
    "Wet Branch":              ItemData(ITEM_ID_BASE + 6,  ItemClassification.progression),
    "Torch":                   ItemData(ITEM_ID_BASE + 8,  ItemClassification.progression),
    "Empty Bottle":            ItemData(ITEM_ID_BASE + 11, ItemClassification.useful),

    # Barrens
    "Camera":                  ItemData(ITEM_ID_BASE + 9,  ItemClassification.progression),
    "Screwdriver":             ItemData(ITEM_ID_BASE + 10, ItemClassification.progression),
    "Lens":                    ItemData(ITEM_ID_BASE + 12, ItemClassification.progression),
    "Broken Battery":          ItemData(ITEM_ID_BASE + 13, ItemClassification.progression),
    "Empty Battery":           ItemData(ITEM_ID_BASE + 14, ItemClassification.progression),
    "Charged Battery":         ItemData(ITEM_ID_BASE + 15, ItemClassification.progression),
    "Bottle of Smoke":         ItemData(ITEM_ID_BASE + 16, ItemClassification.progression),
    "Bottle of Acid":          ItemData(ITEM_ID_BASE + 17, ItemClassification.progression),
    "Wet Sponge":              ItemData(ITEM_ID_BASE + 18, ItemClassification.progression),
    "Metal Rod":               ItemData(ITEM_ID_BASE + 20, ItemClassification.useful),
    "Sponge":                  ItemData(ITEM_ID_BASE + 21, ItemClassification.progression),
    "Empty Syringe":           ItemData(ITEM_ID_BASE + 22, ItemClassification.progression),
    "Filled Syringe":          ItemData(ITEM_ID_BASE + 24, ItemClassification.progression),
    "Strange Journal":         ItemData(ITEM_ID_BASE + 26, ItemClassification.useful),

    # Glen
    "Bottle of Dye":           ItemData(ITEM_ID_BASE + 27, ItemClassification.progression),
    "Tube of Water":           ItemData(ITEM_ID_BASE + 28, ItemClassification.useful),
    "Seed":                    ItemData(ITEM_ID_BASE + 29, ItemClassification.useful),
    "Wool":                    ItemData(ITEM_ID_BASE + 32, ItemClassification.useful),

    # Refuge
    "Button (?)":              ItemData(ITEM_ID_BASE + 33, ItemClassification.progression),
    "Magnetized (?) Button":   ItemData(ITEM_ID_BASE + 34, ItemClassification.progression),
    "Taped Button":            ItemData(ITEM_ID_BASE + 35, ItemClassification.progression),
    "You Tried":               ItemData(ITEM_ID_BASE + 36, ItemClassification.useful),
    "Magnets":                 ItemData(ITEM_ID_BASE + 37, ItemClassification.progression),
    "Metal Can":               ItemData(ITEM_ID_BASE + 38, ItemClassification.progression),
    "Scissors":                ItemData(ITEM_ID_BASE + 40, ItemClassification.progression),
    "Concave Lens":            ItemData(ITEM_ID_BASE + 41, ItemClassification.progression),
    "Convex Lens":             ItemData(ITEM_ID_BASE + 42, ItemClassification.progression),
    "Thin Lens":               ItemData(ITEM_ID_BASE + 43, ItemClassification.progression),
    "Thick Lens":              ItemData(ITEM_ID_BASE + 44, ItemClassification.progression),
    "Glitter Glue":            ItemData(ITEM_ID_BASE + 45, ItemClassification.progression),
    "Photo of Niko":           ItemData(ITEM_ID_BASE + 46, ItemClassification.progression),
    "Kip's Library Card":      ItemData(ITEM_ID_BASE + 47, ItemClassification.progression),
    "Gas Mask":                ItemData(ITEM_ID_BASE + 48, ItemClassification.progression),
    "Rubber Gloves":           ItemData(ITEM_ID_BASE + 49, ItemClassification.progression),
    "Boots":                   ItemData(ITEM_ID_BASE + 50, ItemClassification.useful),
    "Novelty T-Shirt":         ItemData(ITEM_ID_BASE + 51, ItemClassification.useful),
    "\"Kip\"'s Library Card":  ItemData(ITEM_ID_BASE + 52, ItemClassification.progression),
    "Library Card (Sticky)":   ItemData(ITEM_ID_BASE + 53, ItemClassification.progression),
    "Photo of Niko (Sticky)":  ItemData(ITEM_ID_BASE + 54, ItemClassification.progression),
    "Dirt":                    ItemData(ITEM_ID_BASE + 55, ItemClassification.progression),
    "Water Pill":              ItemData(ITEM_ID_BASE + 56, ItemClassification.progression),
    "Medicated Water":         ItemData(ITEM_ID_BASE + 57, ItemClassification.progression),
    "Empty Tube":              ItemData(ITEM_ID_BASE + 59, ItemClassification.useful),
    "Bottle of Pond Water":    ItemData(ITEM_ID_BASE + 60, ItemClassification.progression),
    "Photo of Niko (1)":       ItemData(ITEM_ID_BASE + 61, ItemClassification.progression),
    "Photo of Niko (2)":       ItemData(ITEM_ID_BASE + 62, ItemClassification.useful),
    "Photo of Niko (3)":       ItemData(ITEM_ID_BASE + 63, ItemClassification.useful),
    "Photo of Niko (4)":       ItemData(ITEM_ID_BASE + 64, ItemClassification.useful),
    "Photo of Niko (5)":       ItemData(ITEM_ID_BASE + 65, ItemClassification.useful),
    "Photo of Niko (Blink)":   ItemData(ITEM_ID_BASE + 66, ItemClassification.useful),
    "Photo of Niko (7)":       ItemData(ITEM_ID_BASE + 67, ItemClassification.useful),
    "Photo of Niko (8)":       ItemData(ITEM_ID_BASE + 68, ItemClassification.useful),
    "Photo of Niko (9)":       ItemData(ITEM_ID_BASE + 69, ItemClassification.useful),
    "Photo of Niko (10)":      ItemData(ITEM_ID_BASE + 70, ItemClassification.useful),
}

# ── External TWM file items (only when IncludeExternalFiles enabled) ──────────
file_items = {
    "Outpost PC File":         ItemData(ITEM_ID_BASE + 800, ItemClassification.useful),
    "Prototype File":          ItemData(ITEM_ID_BASE + 801, ItemClassification.useful),
    "Cedric File":             ItemData(ITEM_ID_BASE + 802, ItemClassification.useful),
    "Rue File":                ItemData(ITEM_ID_BASE + 803, ItemClassification.useful),
}

# ── Collectible wallpapers ────────────────────────────────────────────────────
wallpaper_items = {
    "Wallpaper: Outpost":           ItemData(ITEM_ID_BASE + 401, ItemClassification.useful),
    "Wallpaper: Factory":           ItemData(ITEM_ID_BASE + 402, ItemClassification.useful),
    "Wallpaper: Navigate":          ItemData(ITEM_ID_BASE + 403, ItemClassification.useful),
    "Wallpaper: Courtyard":         ItemData(ITEM_ID_BASE + 404, ItemClassification.useful),
    "Wallpaper: Calamus and Alula": ItemData(ITEM_ID_BASE + 405, ItemClassification.useful),
    "Wallpaper: Catwalks":          ItemData(ITEM_ID_BASE + 406, ItemClassification.useful),
    "Wallpaper: Library Stroll":    ItemData(ITEM_ID_BASE + 407, ItemClassification.useful),
    "Wallpaper: Secret RAM Club":   ItemData(ITEM_ID_BASE + 408, ItemClassification.useful),
    "Wallpaper: Lamplighter":       ItemData(ITEM_ID_BASE + 409, ItemClassification.useful),
    "Wallpaper: Cafe":              ItemData(ITEM_ID_BASE + 410, ItemClassification.useful),
    "Wallpaper: Maize":             ItemData(ITEM_ID_BASE + 411, ItemClassification.useful),
    "Wallpaper: Tower":             ItemData(ITEM_ID_BASE + 412, ItemClassification.useful),
    "Wallpaper: Prophets":          ItemData(ITEM_ID_BASE + 413, ItemClassification.useful),
    "Wallpaper: Memory":            ItemData(ITEM_ID_BASE + 414, ItemClassification.useful),
    "Wallpaper: Reflection":        ItemData(ITEM_ID_BASE + 415, ItemClassification.useful),
    "Wallpaper: From Niko":         ItemData(ITEM_ID_BASE + 416, ItemClassification.useful),
}

# ── Friend profiles ───────────────────────────────────────────────────────────
profile_items = {
    "Profile: ProphetBot":        ItemData(ITEM_ID_BASE + 426, ItemClassification.useful),
    "Profile: Silver":            ItemData(ITEM_ID_BASE + 427, ItemClassification.useful),
    "Profile: Rowbot":            ItemData(ITEM_ID_BASE + 428, ItemClassification.useful),
    "Profile: Shepherd":          ItemData(ITEM_ID_BASE + 429, ItemClassification.useful),
    "Profile: Magpie":            ItemData(ITEM_ID_BASE + 430, ItemClassification.useful),
    "Profile: Calamus":           ItemData(ITEM_ID_BASE + 431, ItemClassification.useful),
    "Profile: Alula":             ItemData(ITEM_ID_BASE + 432, ItemClassification.useful),
    "Profile: Maize":             ItemData(ITEM_ID_BASE + 433, ItemClassification.useful),
    "Profile: Ling":              ItemData(ITEM_ID_BASE + 434, ItemClassification.useful),
    "Profile: Watcher":           ItemData(ITEM_ID_BASE + 435, ItemClassification.useful),
    "Profile: Mason":             ItemData(ITEM_ID_BASE + 436, ItemClassification.useful),
    "Profile: Lamplighter":       ItemData(ITEM_ID_BASE + 437, ItemClassification.useful),
    "Profile: Kelvin":            ItemData(ITEM_ID_BASE + 438, ItemClassification.useful),
    "Profile: Kip":               ItemData(ITEM_ID_BASE + 439, ItemClassification.useful),
    "Profile: George":            ItemData(ITEM_ID_BASE + 440, ItemClassification.useful),
    "Profile: Prototype":         ItemData(ITEM_ID_BASE + 446, ItemClassification.useful),
    "Profile: Cedric":            ItemData(ITEM_ID_BASE + 447, ItemClassification.useful),
    "Profile: Rue":               ItemData(ITEM_ID_BASE + 448, ItemClassification.useful),
    "Profile: The World Machine": ItemData(ITEM_ID_BASE + 449, ItemClassification.useful),
    "Profile: The Author":        ItemData(ITEM_ID_BASE + 450, ItemClassification.useful),
    "Profile: Niko":              ItemData(ITEM_ID_BASE + 451, ItemClassification.useful),
}

# ── Desktop themes ────────────────────────────────────────────────────────────
theme_items = {
    "Theme: Blue":    ItemData(ITEM_ID_BASE + 461, ItemClassification.useful),
    "Theme: Cyan":    ItemData(ITEM_ID_BASE + 462, ItemClassification.useful),
    "Theme: Green":   ItemData(ITEM_ID_BASE + 463, ItemClassification.useful),
    "Theme: Yellow":  ItemData(ITEM_ID_BASE + 464, ItemClassification.useful),
    "Theme: Red":     ItemData(ITEM_ID_BASE + 465, ItemClassification.useful),
    "Theme: Pink":    ItemData(ITEM_ID_BASE + 466, ItemClassification.useful),
    "Theme: Orange":  ItemData(ITEM_ID_BASE + 467, ItemClassification.useful),
    "Theme: White":   ItemData(ITEM_ID_BASE + 468, ItemClassification.useful),
    "Theme: Rainbow": ItemData(ITEM_ID_BASE + 469, ItemClassification.useful),
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
