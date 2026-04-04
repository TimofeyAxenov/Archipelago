from typing import Dict, TYPE_CHECKING
from .Types import LocData

if TYPE_CHECKING:
    from . import OneShotWorld

LOC_ID_BASE = 7_771_000


def did_include_crafts(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeCrafts)

def did_include_themes(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeThemes)

def did_include_friends(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeFriends)

def did_include_wallpapers(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeWallpapers)

def did_include_files(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeExternalFiles)

def did_include_badges(world: "OneShotWorld") -> bool:
    return bool(world.options.IncludeBadges)


def get_total_locations(world: "OneShotWorld") -> int:
    total = 0
    for name in location_table:
        if name in event_locations:
            continue
        if is_valid_location(world, name):
            total += 1
    return total


def get_location_names() -> Dict[str, int]:
    return {name: data.ap_code for name, data in location_table.items()
            if data.ap_code is not None}


def is_valid_location(world: "OneShotWorld", name: str) -> bool:
    if name in event_locations:
        return False
    if name in crafts_locations and not did_include_crafts(world):
        return False
    if name in themes_locations and not did_include_themes(world):
        return False
    if name in friends_locations and not did_include_friends(world):
        return False
    if name in wallpapers_locations and not did_include_wallpapers(world):
        return False
    if name in files_locations and not did_include_files(world):
        return False
    if name in badges_locations and not did_include_badges(world):
        return False
    return True


# ── Starter House ─────────────────────────────────────────────────────────────
starter_house_locations = {
    "PC Room Floor":        LocData(LOC_ID_BASE + 1,  "Starter House"),
    "Left Room":            LocData(LOC_ID_BASE + 2,  "Starter House"),
    "Floorboards":          LocData(LOC_ID_BASE + 3,  "Starter House"),
    "Fridge":               LocData(LOC_ID_BASE + 4,  "Starter House"),
    "Basement":             LocData(LOC_ID_BASE + 5,  "Starter House"),
}

# ── Barrens ───────────────────────────────────────────────────────────────────
barrens_locations = {
    "Outpost Box":          LocData(LOC_ID_BASE + 10, "Barrens"),
    "House Floor":          LocData(LOC_ID_BASE + 11, "Barrens"),
    "House Bed":            LocData(LOC_ID_BASE + 12, "Barrens"),
    "Silver House Shelf":   LocData(LOC_ID_BASE + 13, "Barrens"),
    "Mines":                LocData(LOC_ID_BASE + 14, "Barrens"),
    "Vault Mask":           LocData(LOC_ID_BASE + 15, "Barrens"),
    "Infirmary":            LocData(LOC_ID_BASE + 16, "Barrens"),
    "Factory Floor":        LocData(LOC_ID_BASE + 17, "Barrens"),
    "Amber":                LocData(LOC_ID_BASE + 18, "Barrens"),
    "Rowbot":               LocData(LOC_ID_BASE + 19, "Barrens"),
    "Vault Journal":        LocData(LOC_ID_BASE + 20, "Barrens"),
    "Wet Sponge":           LocData(LOC_ID_BASE + 21, "Barrens"),
}

# ── Glen ──────────────────────────────────────────────────────────────────────
glen_locations = {
    "Calamus Camp":         LocData(LOC_ID_BASE + 30, "Glen"),
    "Ruins Feather":        LocData(LOC_ID_BASE + 31, "Glen"),
    "Magpie Trade Ink":     LocData(LOC_ID_BASE + 32, "Glen"),
    "Magpie Trade Shirt":   LocData(LOC_ID_BASE + 33, "Glen"),
    "Ram Quest Reward":     LocData(LOC_ID_BASE + 34, "Glen"),
    "Maize Seed":           LocData(LOC_ID_BASE + 35, "Glen"),
    "Dye Vial":             LocData(LOC_ID_BASE + 36, "Glen"),
    "Pond Water":           LocData(LOC_ID_BASE + 37, "Glen"),
}

# ── Refuge ────────────────────────────────────────────────────────────────────
refuge_locations = {
    "George Die":           LocData(LOC_ID_BASE + 50, "Refuge"),
    "Kip Library Card":     LocData(LOC_ID_BASE + 51, "Refuge"),
    "Photo of Niko":        LocData(LOC_ID_BASE + 52, "Refuge"),
    "Magnets":              LocData(LOC_ID_BASE + 53, "Refuge"),
    "Metal Can":            LocData(LOC_ID_BASE + 54, "Refuge"),
    "Scissors":             LocData(LOC_ID_BASE + 55, "Refuge"),
    "Glitter Glue":         LocData(LOC_ID_BASE + 56, "Refuge"),
    "Gas Mask":             LocData(LOC_ID_BASE + 57, "Refuge"),
    "Rubber Gloves":        LocData(LOC_ID_BASE + 58, "Refuge"),
    "Weird Film":           LocData(LOC_ID_BASE + 59, "Refuge"),
    "Lenses":               LocData(LOC_ID_BASE + 60, "Refuge"),
    "Dirt Bag":             LocData(LOC_ID_BASE + 61, "Refuge"),
    "Water Pill":           LocData(LOC_ID_BASE + 62, "Refuge"),
}

# ── Tower ─────────────────────────────────────────────────────────────────────
tower_locations = {
    "Clover App":           LocData(LOC_ID_BASE + 80, "Tower"),
}

# ── Crafts ────────────────────────────────────────────────────────────────────
crafts_locations = {
    "TV":                    LocData(LOC_ID_BASE + 100, "Starter House"),
    "Wet Branch Craft":      LocData(LOC_ID_BASE + 101, "Starter House"),
    "Empty Bottle Craft":    LocData(LOC_ID_BASE + 102, "Starter House"),
    "Factory Press":         LocData(LOC_ID_BASE + 103, "Barrens"),
    "Gas Vent":              LocData(LOC_ID_BASE + 104, "Barrens"),
    "Swamp Bubble":          LocData(LOC_ID_BASE + 105, "Barrens"),
    "Bottle of Water Craft": LocData(LOC_ID_BASE + 106, "Barrens"),
    "Acid Craft":            LocData(LOC_ID_BASE + 107, "Barrens"),
    "Lens Craft":            LocData(LOC_ID_BASE + 108, "Barrens"),
    "Battery Craft":         LocData(LOC_ID_BASE + 109, "Barrens"),
    "Battery Charge":        LocData(LOC_ID_BASE + 110, "Barrens"),
    "Feather Pen Craft":     LocData(LOC_ID_BASE + 111, "Glen"),
    "Button Craft":          LocData(LOC_ID_BASE + 112, "Refuge"),
    "Magnetized Button":     LocData(LOC_ID_BASE + 113, "Refuge"),
    "Taped Button":          LocData(LOC_ID_BASE + 114, "Refuge"),
    "Niko Library Card":     LocData(LOC_ID_BASE + 115, "Refuge"),
    "Sticky Card Craft":     LocData(LOC_ID_BASE + 116, "Refuge"),
    "Sticky Photo Craft":    LocData(LOC_ID_BASE + 117, "Refuge"),
    "Medicated Water Craft": LocData(LOC_ID_BASE + 118, "Refuge"),
}

# ── External TWM files ────────────────────────────────────────────────────────
files_locations = {
    "Outpost PC File":       LocData(LOC_ID_BASE + 200, "Barrens"),
    "Prototype File":        LocData(LOC_ID_BASE + 202, "Solstice"),
    "Cedric File":           LocData(LOC_ID_BASE + 203, "Solstice"),
    "Rue File":              LocData(LOC_ID_BASE + 204, "Solstice"),
}

# ── Wallpapers ────────────────────────────────────────────────────────────────
wallpapers_locations = {
    "Wallpaper: Outpost":           LocData(LOC_ID_BASE + 300, "Barrens"),
    "Wallpaper: Factory":           LocData(LOC_ID_BASE + 301, "Barrens"),
    "Wallpaper: Navigate":          LocData(LOC_ID_BASE + 302, "Glen"),
    "Wallpaper: Courtyard":         LocData(LOC_ID_BASE + 303, "Glen"),
    "Wallpaper: Calamus and Alula": LocData(LOC_ID_BASE + 304, "Glen"),
    "Wallpaper: Catwalks":          LocData(LOC_ID_BASE + 305, "Refuge"),
    "Wallpaper: Library Stroll":    LocData(LOC_ID_BASE + 306, "Refuge"),
    "Wallpaper: Secret RAM Club":   LocData(LOC_ID_BASE + 307, "Refuge"),
    "Wallpaper: Lamplighter":       LocData(LOC_ID_BASE + 308, "Refuge"),
    "Wallpaper: Cafe":              LocData(LOC_ID_BASE + 309, "Refuge"),
    "Wallpaper: Maize":             LocData(LOC_ID_BASE + 310, "Refuge"),
    "Wallpaper: Tower":             LocData(LOC_ID_BASE + 311, "Tower"),
    "Wallpaper: Prophets":          LocData(LOC_ID_BASE + 312, "Solstice"),
    "Wallpaper: Memory":            LocData(LOC_ID_BASE + 313, "Solstice"),
    "Wallpaper: Reflection":        LocData(LOC_ID_BASE + 314, "Solstice"),
    "Wallpaper: From Niko":         LocData(LOC_ID_BASE + 315, "Solstice"),
}

# ── Friend profiles ───────────────────────────────────────────────────────────
friends_locations = {
    "Profile: ProphetBot":        LocData(LOC_ID_BASE + 400, "Barrens"),
    "Profile: Silver":            LocData(LOC_ID_BASE + 401, "Barrens"),
    "Profile: Rowbot":            LocData(LOC_ID_BASE + 402, "Barrens"),
    "Profile: Shepherd":          LocData(LOC_ID_BASE + 403, "Glen"),
    "Profile: Magpie":            LocData(LOC_ID_BASE + 404, "Glen"),
    "Profile: Calamus":           LocData(LOC_ID_BASE + 405, "Glen"),
    "Profile: Alula":             LocData(LOC_ID_BASE + 406, "Glen"),
    "Profile: Maize":             LocData(LOC_ID_BASE + 407, "Glen"),
    "Profile: Ling":              LocData(LOC_ID_BASE + 408, "Glen"),
    "Profile: Watcher":           LocData(LOC_ID_BASE + 409, "Refuge"),
    "Profile: Mason":             LocData(LOC_ID_BASE + 410, "Refuge"),
    "Profile: Lamplighter":       LocData(LOC_ID_BASE + 411, "Refuge"),
    "Profile: Kelvin":            LocData(LOC_ID_BASE + 412, "Refuge"),
    "Profile: Kip":               LocData(LOC_ID_BASE + 413, "Refuge"),
    "Profile: George":            LocData(LOC_ID_BASE + 414, "Refuge"),
    "Profile: Prototype":         LocData(LOC_ID_BASE + 420, "Solstice"),
    "Profile: Cedric":            LocData(LOC_ID_BASE + 421, "Solstice"),
    "Profile: Rue":               LocData(LOC_ID_BASE + 422, "Solstice"),
    "Profile: The World Machine": LocData(LOC_ID_BASE + 423, "Solstice"),
    "Profile: The Author":        LocData(LOC_ID_BASE + 424, "Solstice"),
    "Profile: Niko":              LocData(LOC_ID_BASE + 425, "Solstice"),
}

# ── Desktop themes ────────────────────────────────────────────────────────────
themes_locations = {
    "Theme: Blue":    LocData(LOC_ID_BASE + 500, "Barrens"),
    "Theme: Cyan":    LocData(LOC_ID_BASE + 501, "Barrens"),
    "Theme: Green":   LocData(LOC_ID_BASE + 502, "Glen"),
    "Theme: Yellow":  LocData(LOC_ID_BASE + 503, "Glen"),
    "Theme: Red":     LocData(LOC_ID_BASE + 504, "Refuge"),
    "Theme: Pink":    LocData(LOC_ID_BASE + 505, "Refuge"),
    "Theme: Orange":  LocData(LOC_ID_BASE + 506, "Refuge"),
    "Theme: White":   LocData(LOC_ID_BASE + 507, "Tower"),
    "Theme: Rainbow": LocData(LOC_ID_BASE + 508, "Tower"),
}

# ── Badges ────────────────────────────────────────────────────────────────────
badges_locations = {
    "Badge: Chaotic Evil":      LocData(LOC_ID_BASE + 600, "Barrens"),
    "Badge: Shock":             LocData(LOC_ID_BASE + 601, "Barrens"),
    "Badge: Extreme Bartering": LocData(LOC_ID_BASE + 602, "Glen"),
    "Badge: Ram Whisperer":     LocData(LOC_ID_BASE + 603, "Glen"),
    "Badge: Pancakes":          LocData(LOC_ID_BASE + 604, "Refuge"),
    "Badge: We Ride at Dawn":   LocData(LOC_ID_BASE + 605, "Refuge"),
    "Badge: Secret":            LocData(LOC_ID_BASE + 606, "Refuge"),
    "Badge: Bookworm":          LocData(LOC_ID_BASE + 607, "Refuge"),
    "Badge: Rebirth":           LocData(LOC_ID_BASE + 608, "Endgame"),
    "Badge: OneShot":           LocData(LOC_ID_BASE + 609, "Endgame"),
    "Badge: Return":            LocData(LOC_ID_BASE + 610, "Solstice"),
}

# ── Event locations ───────────────────────────────────────────────────────────
event_locations = {
    "Leave":    LocData(None, "Tower"),
    "Victory?": LocData(None, "Endgame"),
    "Solstice": LocData(None, "Solstice"),
}

location_table = {
    **starter_house_locations,
    **barrens_locations,
    **glen_locations,
    **refuge_locations,
    **tower_locations,
    **crafts_locations,
    **files_locations,
    **wallpapers_locations,
    **friends_locations,
    **themes_locations,
    **badges_locations,
    **event_locations,
}
