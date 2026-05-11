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
#    "PC Room Floor":        LocData(LOC_ID_BASE + 1,  "Starter House"),
    "Dry Branch":            LocData(LOC_ID_BASE + 1,  "Starter House"),
    "Bottle of Alcohol":     LocData(LOC_ID_BASE + 2,  "Starter House"),
    "Basement Key":          LocData(LOC_ID_BASE + 3,  "Starter House"),
    "Lightbulb":             LocData(LOC_ID_BASE + 4,  "Starter House"),
}

# ── Barrens ───────────────────────────────────────────────────────────────────
barrens_locations = {
    "Metal Rod":            LocData(LOC_ID_BASE + 10, "Barrens"),
    "Broken Battery":       LocData(LOC_ID_BASE + 11, "Barrens"),
    "Screwdriver":          LocData(LOC_ID_BASE + 12, "Barrens"),
    "Camera":               LocData(LOC_ID_BASE + 13, "Barrens"),
    "Strange Journal":      LocData(LOC_ID_BASE + 14, "Barrens"),
    "Gas Mask":             LocData(LOC_ID_BASE + 15, "Barrens"),
    "Rubber Gloves":        LocData(LOC_ID_BASE + 16, "Barrens"),
    "Sponge":               LocData(LOC_ID_BASE + 17, "Barrens"),
    "Empty Syringe":        LocData(LOC_ID_BASE + 18, "Barrens"),
    "Amber":                LocData(LOC_ID_BASE + 19, "Barrens"),
}

# ── Glen ──────────────────────────────────────────────────────────────────────
glen_locations = {
    "Seed":                 LocData(LOC_ID_BASE + 30, "Glen"),
    "Wool":                 LocData(LOC_ID_BASE + 31, "Glen"),
    "Ink":                  LocData(LOC_ID_BASE + 32, "Glen"),
    "Novelty T-Shirt":      LocData(LOC_ID_BASE + 33, "Glen"),
    "Tube of Water":        LocData(LOC_ID_BASE + 34, "Glen"),
    "Feather":              LocData(LOC_ID_BASE + 35, "Glen"),
}

# ── Refuge ────────────────────────────────────────────────────────────────────
refuge_locations = {
    "Scissors":             LocData(LOC_ID_BASE + 50, "Refuge"),
    "Dirt":                 LocData(LOC_ID_BASE + 51, "Refuge"),
    "Magnets":              LocData(LOC_ID_BASE + 52, "Refuge"),
    "Taped Button":         LocData(LOC_ID_BASE + 53, "Refuge"),
    "Metal Can":            LocData(LOC_ID_BASE + 54, "Refuge"),
    "Weird Film":           LocData(LOC_ID_BASE + 55, "Refuge"),
    "Concave Lens":         LocData(LOC_ID_BASE + 56, "Refuge"),
    "Convex Lens":          LocData(LOC_ID_BASE + 57, "Refuge"),
    "Thin Lens":            LocData(LOC_ID_BASE + 58, "Refuge"),
    "Thick Lens":           LocData(LOC_ID_BASE + 59, "Refuge"),
    "Glitter Glue":         LocData(LOC_ID_BASE + 60, "Refuge"),
    "Kip's Library Card":   LocData(LOC_ID_BASE + 61, "Refuge"),
    "Photo of Niko (1)":    LocData(LOC_ID_BASE + 62, "Refuge"),
    "Photo of Niko (2)":    LocData(LOC_ID_BASE + 63, "Refuge"),
    "Photo of Niko (3)":    LocData(LOC_ID_BASE + 64, "Refuge"),
    "Photo of Niko (4)":    LocData(LOC_ID_BASE + 65, "Refuge"),
    "Photo of Niko (5)":    LocData(LOC_ID_BASE + 66, "Refuge"),
    "Photo of Niko (6)":    LocData(LOC_ID_BASE + 67, "Refuge"),
    "Photo of Niko (Blink)":LocData(LOC_ID_BASE + 68, "Refuge"),
    "Photo of Niko (7)":    LocData(LOC_ID_BASE + 69, "Refuge"),
    "Photo of Niko (8)":    LocData(LOC_ID_BASE + 70, "Refuge"),
    "Photo of Niko (9)":    LocData(LOC_ID_BASE + 71, "Refuge"),
    "Water Pill":           LocData(LOC_ID_BASE + 73, "Refuge"),
    "Die":                  LocData(LOC_ID_BASE + 74, "Refuge"),
}

solstice_locations = {
        "Memory Disk":             LocData(LOC_ID_BASE + 80, "Solstice"),
        "Memory Disk (Backup)":    LocData(LOC_ID_BASE + 81, "Solstice"),
        "Charged Battery (Green)": LocData(LOC_ID_BASE + 82, "Solstice"),
        "Music Box":               LocData(LOC_ID_BASE + 83, "Solstice"),
        }

# ── Crafts ────────────────────────────────────────────────────────────────────
crafts_locations = {
    "Wet Branch Craft":      LocData(LOC_ID_BASE + 100, "Starter House"),
    "Torch Craft":           LocData(LOC_ID_BASE + 101, "Starter House"),
    "Empty Bottle Craft":    LocData(LOC_ID_BASE + 102, "Starter House"),
    "Crowbar":               LocData(LOC_ID_BASE + 103, "Barrens"),
    "Filled Bottle":         LocData(LOC_ID_BASE + 104, "Barrens"),
    "Filled Syringe":        LocData(LOC_ID_BASE + 105, "Barrens"),
    "Bottle of Acid":        LocData(LOC_ID_BASE + 106, "Barrens"),
    "Wet Sponge":            LocData(LOC_ID_BASE + 107, "Barrens"),
    "Lens":                  LocData(LOC_ID_BASE + 108, "Barrens"),
    "Empty Battery":         LocData(LOC_ID_BASE + 109, "Barrens"),
    "Charged Battery":       LocData(LOC_ID_BASE + 110, "Barrens"),
    "Feather Pen":           LocData(LOC_ID_BASE + 111, "Glen"),
    "Magnetized Button":     LocData(LOC_ID_BASE + 112, "Refuge"),
    "Taped Button":          LocData(LOC_ID_BASE + 113, "Refuge"),
    "Niko Library Card":     LocData(LOC_ID_BASE + 114, "Refuge"),
    "Sticky Photo Craft":    LocData(LOC_ID_BASE + 115, "Refuge"),
    "Medicated Water Craft": LocData(LOC_ID_BASE + 116, "Refuge"),
    "Sticky Photo":          LocData(LOC_ID_BASE + 117, "Refuge"),
    "Niko's Library Card":   LocData(LOC_ID_BASE + 118, "Refuge")
}

# ── External TWM files ────────────────────────────────────────────────────────
files_locations = {
    "DOCUMENT oneshot":      LocData(LOC_ID_BASE + 200, "Barrens"),
    "Clover App":            LocData(LOC_ID_BASE + 201, "Tower"),
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
    "Profile: Rowbot":            LocData(LOC_ID_BASE + 402, "Glen"), 
    "Profile: Magpie":            LocData(LOC_ID_BASE + 403, "Glen"),
    "Profile: Alula":             LocData(LOC_ID_BASE + 404, "Glen"),
    "Profile: Calamus":           LocData(LOC_ID_BASE + 405, "Glen"),
    "Profile: Maize":             LocData(LOC_ID_BASE + 406, "Glen"),
    "Profile: Mason":             LocData(LOC_ID_BASE + 407, "Refuge"),
    "Profile: Watcher":           LocData(LOC_ID_BASE + 408, "Refuge"),
    "Profile: Kelvin":            LocData(LOC_ID_BASE + 409, "Refuge"),
    "Profile: Shepherd":          LocData(LOC_ID_BASE + 410, "Refuge"),
    "Profile: Kip":               LocData(LOC_ID_BASE + 411, "Refuge"),
    "Profile: George":            LocData(LOC_ID_BASE + 412, "Refuge"),
    "Profile: Prototype":         LocData(LOC_ID_BASE + 413, "Solstice"),
    "Profile: Cedric":            LocData(LOC_ID_BASE + 414, "Solstice"),
    "Profile: Rue":               LocData(LOC_ID_BASE + 415, "Solstice"),
    "Profile: The World Machine": LocData(LOC_ID_BASE + 416, "Solstice"),
    "Profile: The Author":        LocData(LOC_ID_BASE + 417, "Solstice"),
    "Profile: Niko":              LocData(LOC_ID_BASE + 418, "Solstice"),
}

# ── Desktop themes ────────────────────────────────────────────────────────────
themes_locations = {
    "Theme: Blue":    LocData(LOC_ID_BASE + 500, "Barrens"),
    "Theme: Cyan":    LocData(LOC_ID_BASE + 501, "Barrens"),
    "Theme: Yellow":  LocData(LOC_ID_BASE + 502, "Glen"),
    "Theme: Green":   LocData(LOC_ID_BASE + 503, "Glen"),
    "Theme: Red":     LocData(LOC_ID_BASE + 504, "Refuge"),
    "Theme: Pink":    LocData(LOC_ID_BASE + 505, "Refuge"),
    "Theme: Orange":  LocData(LOC_ID_BASE + 506, "Refuge"),
    "Theme: White":   LocData(LOC_ID_BASE + 507, "Refuge"),
    "Theme: Rainbow": LocData(LOC_ID_BASE + 508, "Tower"),
}

# ── Badges ────────────────────────────────────────────────────────────────────
badges_locations = {
    "Badge: Chaotic Evil":      LocData(LOC_ID_BASE + 600, "Barrens"),
    "Badge: Shock":             LocData(LOC_ID_BASE + 601, "Barrens"),
    "Badge: Extreme Bartering": LocData(LOC_ID_BASE + 602, "Glen"),
    "Badge: Ram Whisperer":     LocData(LOC_ID_BASE + 603, "Glen"),
    "Badge: We Ride at Dawn":   LocData(LOC_ID_BASE + 604, "Refuge"),
    "Badge: Secret":            LocData(LOC_ID_BASE + 605, "Refuge"),
    "Badge: Bookworm":          LocData(LOC_ID_BASE + 606, "Refuge"),
    "Badge: Pancakes":          LocData(LOC_ID_BASE + 607, "Refuge"),
    "Badge: Rebirth":           LocData(LOC_ID_BASE + 608, "Endgame"),
    "Badge: OneShot":           LocData(LOC_ID_BASE + 609, "Endgame"),
    "Badge: Color Coordinator": LocData(LOC_ID_BASE + 610, "Endgame"),
    "Badge: Return":            LocData(LOC_ID_BASE + 611, "Solstice"),
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
    **solstice_locations,
    **refuge_locations,
    **crafts_locations,
    **files_locations,
    **wallpapers_locations,
    **friends_locations,
    **themes_locations,
    **badges_locations,
    **event_locations,
}
