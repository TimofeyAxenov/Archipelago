import logging
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

from worlds.oneshot_wme.Options import IncludeCrafts

if TYPE_CHECKING:
    from . import OneShotWorld

logger = logging.getLogger("OneShot")


def _set_rule_if_exists(multiworld, player: int, loc_name: str, rule_fn):
    try:
        set_rule(multiworld.get_location(loc_name, player), rule_fn)
    except KeyError:
        logger.debug(f"Skipping rule for non-existent location: {loc_name}")


def set_rules(world: "OneShotWorld"):
    player = world.player
    mw = world.multiworld
    loc = lambda name, fn: _set_rule_if_exists(mw, player, name, fn)
    ent = lambda name, fn: set_rule(mw.get_entrance(name, player), fn)

    incl_crafts = bool(world.options.IncludeCrafts)
    incl_files  = bool(world.options.IncludeExternalFiles)

    # ── Region access from Starter House ──────────────────────────────────────
    ent("Starter House -> Barrens",
        lambda state: state.has("Lightbulb", player) and
                      state.has("Barrens Key", player))

    ent("Starter House -> Glen",
        lambda state: state.has("Lightbulb", player) and
                      state.has("Glen Key", player))

    ent("Starter House -> Refuge Upper",
        lambda state: state.has("Lightbulb", player) and
                      state.has("Refuge Key", player))

    # Refuge Lower requires Weird Film + Taped Button (craft).
    if incl_files:
        ent("Refuge Upper -> Refuge Lower",
            lambda state: state.has_all(["Weird Film", "Taped Button"], player))

    ent("Refuge Lower -> Tower",
        lambda state: state.has("Die", player) and
                      state.has("Amber", player) and
                      state.has("Feather", player) and
                      state.has("Lightbulb", player))

    # ── Starter House ─────────────────────────────────────────────────────────
    loc("Lightbulb", lambda state: state.has("Basement Key", player))

    if incl_files:
        loc("Basement Key", lambda state: state.has("Torch", player))
        loc("Empty Bottle", lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))
        loc("Wet Branch", lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))
        loc("Torch", lambda state: state.has("Wet Branch", player))

    # ── Barrens ───────────────────────────────────────────────────────────────
    loc("Broken Battery", lambda state: state.has("Crowbar", player)
                          if incl_crafts else True)

    loc("Badge: Shock", lambda state: state.has("Charged Battery", player)
                         if incl_crafts else True)

    loc("DOCUMENT oneshot", lambda state: state.has("Charged Battery", player)
                             if incl_crafts else True)

    loc("Strange Journal", lambda state: state.has("Outpost PC File", player)
                            if incl_files else True)

    loc("Gas Mask", lambda state: state.has("Outpost PC File", player)
                     if incl_files else True)

    loc("Rubber Gloves", lambda state: state.has("Gas Mask", player))
    loc("Empty Syringe", lambda state: state.has("Gas Mask", player))
    loc("Theme: Teal", lambda state: state.has("Gas Mask", player))

    loc("Sponge", lambda state: state.has_all(["Gas Mask", "Crowbar"], player)
                  if incl_crafts else state.has("Gas Mask", player))

    loc("Wallpaper: Factory", lambda state: state.has_all(["Gas Mask", "Crowbar"], player)
                               if incl_crafts else state.has("Gas Mask", player))

    loc("Amber", lambda state: state.has_all(["Charged Battery", "Wet Sponge", "Rubber Gloves"], player)
                  if incl_crafts else state.has("Rubber Gloves", player))

    loc("Profile: Silver", lambda state: state.has_all(["Charged Battery", "Wet Sponge", "Rubber Gloves"], player)
                            if incl_crafts else state.has("Rubber Gloves", player))

    if incl_crafts:
        loc("Crowbar", lambda state: state.has("Metal Rod", player))
        loc("Lens", lambda state: state.has_all(["Camera", "Screwdriver"], player))
        loc("Empty Battery", lambda state: state.has_all(["Broken Battery", "Lens"], player))
        loc("Charged Battery", lambda state: state.has_all(["Empty Battery", "Lightbulb"], player))
        loc("Bottle of Smoke", lambda state: state.has_all(["Gas Mask", "Empty Bottle"], player))
        loc("Filled Bottle", lambda state: state.has_all(["Empty Bottle", "Filled Syringe"], player))
        loc("Filled Syringe", lambda state: state.has_all(["Empty Syringe", "Gas Mask"], player))
        loc("Bottle of Acid", lambda state: state.has_all(["Bottle of Smoke", "Filled Syringe"], player))
        loc("Wet Sponge", lambda state: state.has_all(["Sponge", "Bottle of Acid"], player))

    # ── Glen ──────────────────────────────────────────────────────────────────
    loc("Seed", lambda state: state.has_all(["Feather", "Wool"], player))
    loc("Ink", lambda state: state.has("Wool", player))
    loc("Profile: Magpie", lambda state: state.has("Wool", player))
    loc("Novelty T-Shirt", lambda state: state.has("Wool", player))
    loc("Profile: Maize", lambda state: state.has("Seed", player))
    loc("Badge: Extreme Bartering", lambda state: state.has("Novelty T-Shirt", player))

    loc("Wallpaper: Calamus and Alula", lambda state: state.has("Feather Pen", player)
                                          if incl_crafts else True)

    if incl_crafts:
        loc("Feather Pen", lambda state: state.has_all(["Feather", "Bottle of Dye"], player))

    # ── Refuge Upper ──────────────────────────────────────────────────────────
    loc("Dirt", lambda state: state.has("Seed", player))
    loc("Profile: Mason", lambda state: state.has("Seed", player))

    if incl_crafts:
        loc("Button (?)", lambda state: state.has_all(["Scissors", "Metal Can"], player))
        loc("Magnetized Button", lambda state: state.has_all(["Button (?)", "Magnets"], player))
        loc("Taped Button", lambda state: state.has("Magnetized (?) Button", player))

    # ── Refuge Lower ──────────────────────────────────────────────────────────
    loc("Badge: Secret", lambda state: state.has("Novelty T-Shirt", player))
    loc("Wallpaper: Secret RAM Club", lambda state: state.has("Novelty T-Shirt", player))
    loc("Profile: Shepherd", lambda state: state.has("Novelty T-Shirt", player))
    loc("Profile: Kip", lambda state: state.has("Amber", player))

    tags = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)",
            "(Blink)", "(8)", "(9)"]
    for tag in tags:
        loc(f"Photo of Niko {tag}",
            lambda state, t=tag: state.has_all(
                ["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    loc("Wallpaper: Maize", lambda state: state.has_all(["Dirt", "Seed", "Medicated Water"], player)
                             if incl_crafts else state.has_all(["Dirt", "Seed"], player))

    loc("Badge: Bookworm", lambda state: state.has("Niko's Library Card", player)
                            if incl_crafts else True)

    loc("Die", lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player)
               if incl_crafts else state.has("Strange Journal", player))

    loc("Profile: George", lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player)
                            if incl_crafts else state.has("Strange Journal", player))

    loc("Wallpaper: Cafe", lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player)
                            if incl_crafts else state.has("Strange Journal", player))

    loc("Badge: Pancakes", lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player)
                            if incl_crafts else state.has("Strange Journal", player))

    loc("Badge: Rebirth", lambda state: state.has_all(["Seed", "Dirt", "Medicated Water"], player)
                           if incl_crafts else state.has_all(["Seed", "Dirt"], player))

    if incl_crafts:
        loc("Medicated Water", lambda state: state.has_all(["Tube of Water", "Water Pill"], player))
        loc("Niko's Library Card", lambda state: state.has_all(["Photo of Niko", "Kip's Library Card", "Glitter Glue"], player))

    # ── Tower ─────────────────────────────────────────────────────────────────
    loc("Theme: Rainbow", lambda state: state.has("Clover App", player)
                           if incl_files else True)
    loc("Wallpaper: Tower", lambda state: state.has("Clover App", player)
                             if incl_files else True)

    # ── Endgame badges ──────────────────────────────────────────────────────
    loc("Badge: Color Coordinator",
        lambda state: state.has_all(["Theme: Blue", "Theme: Teal",
                                     "Theme: Green", "Theme: Yellow",
                                     "Theme: Red", "Theme: Pink",
                                     "Theme: White", "Theme: Orange",
                                     "Theme: Rainbow"], player))

    # ── Goal condition ─────────────────────────────────────────────────────────
    mw.completion_condition[player] = lambda state: state.has("Victory", player)
