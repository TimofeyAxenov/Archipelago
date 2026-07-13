from ssl import OP_LEGACY_SERVER_CONNECT
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import OneShotWorld


def set_rules(world: "OneShotWorld"):
    player = world.player
    starting_zone = world.options.StartingZone.value
    goal = world.options.GameGoal.value

    # ── Region access from Starter House ──────────────────────────────────────
    # Barrens requires Lightbulb + Barrens Key
    set_rule(world.multiworld.get_entrance("Starter House -> Barrens", player),
             lambda state: state.has("Lightbulb", player) and
                           state.has("Barrens Key", player))

    # Glen requires Lightbulb + Glen Key
    set_rule(world.multiworld.get_entrance("Starter House -> Glen", player),
             lambda state: state.has("Lightbulb", player) and
                           state.has("Glen Key", player))

    # Refuge requires Lightbulb + Refuge Key
    set_rule(world.multiworld.get_entrance("Starter House -> Refuge Upper", player),
             lambda state: state.has("Lightbulb", player) and
                           state.has("Refuge Key", player))

    set_rule(world.multiworld.get_entrance("Refuge Upper -> Refuge Lower", player),
             lambda state: state.has_all(["Weird Film", "Taped Button"], player))

    # Tower requires Tower Key + elevator items
    set_rule(world.multiworld.get_entrance("Refuge Lower -> Tower", player),
             lambda state: state.has("Die", player) and
                           state.has("Amber", player) and
                           state.has("Feather", player) and
                           state.has("Lightbulb", player))

    # Solstice requires Solstice Protocol + Glowing Journal
#    set_rule(world.multiworld.get_entrance("Starter House -> Solstice", player),
#             lambda state: state.has("Solstice Protocol", player))

    # Starter House Region
    set_rule(world.multiworld.get_location("Empty Bottle", player),
             lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))

    set_rule(world.multiworld.get_location("Lightbulb", player),
             lambda state: state.has("Basement Key", player))
             
    set_rule(world.multiworld.get_location("Wet Branch", player),
             lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))

    set_rule(world.multiworld.get_location("Torch", player),
             lambda state: state.has("Wet Branch", player))

    set_rule(world.multiworld.get_location("Basement Key", player),
             lambda state: state.has("Torch", player))
    
    # Barrens Region
    set_rule(world.multiworld.get_location("Crowbar", player),
             lambda state: state.has("Metal Rod", player))

    set_rule(world.multiworld.get_location("Broken Battery", player),
             lambda state: state.has("Crowbar", player))

    set_rule(world.multiworld.get_location("Lens", player),
             lambda state: state.has_all(["Camera", "Screwdriver"], player))

    set_rule(world.multiworld.get_location("Empty Battery", player),
             lambda state: state.has_all(["Broken Battery", "Lens"], player))

    set_rule(world.multiworld.get_location("Charged Battery", player),
             lambda state: state.has_all(["Empty Battery", "Lightbulb"], player))

    set_rule(world.multiworld.get_location("Badge: Shock", player),
             lambda state: state.has("Charged Battery", player))

    set_rule(world.multiworld.get_location("DOCUMENT oneshot", player),
             lambda state: state.has("Charged Battery", player))
    
    set_rule(world.multiworld.get_location("Strange Journal", player),
             lambda state: state.has_all("DOCUMENT oneshot", player))
             
    set_rule(world.multiworld.get_location("Gas Mask", player),
             lambda state: state.has("DOCUMENT oneshot", player))
             
    set_rule(world.multiworld.get_location("Rubber Gloves", player),
             lambda state: state.has_all("Gas Mask", player))
    
    set_rule(world.multiworld.get_location("Empty Syringe", player),
             lambda state: state.has_all("Gas Mask", player))
    
    set_rule(world.multiworld.get_location("Bottle of Smoke", player),
             lambda state: state.has_all(["Gas Mask", "Empty Bottle"], player))

    set_rule(world.multiworld.get_location("Filled Bottle", player),
             lambda state: state.has_all(["Empty Bottle", "Filled Syringe"], player))

    set_rule(world.multiworld.get_location("Filled Syringe", player),
             lambda state: state.has_all(["Empty Syringe", "Gas Mask"], player))
   
    set_rule(world.multiworld.get_location("Theme: Teal", player),
             lambda state: state.has("Gas Mask", player))

    set_rule(world.multiworld.get_location("Bottle of Acid", player),
             lambda state: state.has_all(["Bottle of Smoke", "Filled Syringe"], player))
    
    set_rule(world.multiworld.get_location("Sponge", player),
             lambda state: state.has_all(["Gas Mask", "Crowbar"], player))
    
    set_rule(world.multiworld.get_location("Wallpaper: Factory", player),
             lambda state: state.has_all(["Gas Mask", "Crowbar"], player))
    
    set_rule(world.multiworld.get_location("Wet Sponge", player),
             lambda state: state.has_all(["Sponge", "Bottle of Acid"], player))

    set_rule(world.multiworld.get_location("Amber", player),
             lambda state: state.has_all(["Charged Battery", "Wet Sponge", "Rubber Gloves"], player))
             
    set_rule(world.multiworld.get_location("Profile: Silver", player),
             lambda state: state.has_all(["Charged Battery", "Wet Sponge", "Rubber Gloves"], player))

    # Glen Region
    set_rule(world.multiworld.get_location("Seed", player),
             lambda state: state.has_all(["Feather", "Wool"], player))

    set_rule(world.multiworld.get_location("Ink", player),
             lambda state: state.has("Wool", player))

    set_rule(world.multiworld.get_location("Profile: Magpie", player),
             lambda state: state.has("Wool", player))

    set_rule(world.multiworld.get_location("Novelty T-Shirt", player),
             lambda state: state.has("Wool", player))

    set_rule(world.multiworld.get_location("Profile: Maize", player),
             lambda state: state.has("Seed", player))

    set_rule(world.multiworld.get_location("Feather Pen", player),
             lambda state: state.has_all(["Feather", "Bottle of Dye"], player))

    set_rule(world.multiworld.get_location("Wallpaper: Calamus and Alula", player),
             lambda state: state.has("Feather Pen", player))

    set_rule(world.multiworld.get_location("Badge: Extreme Bartering", player),
             lambda state: state.has("Novelty T-Shirt", player))

    # Refuge Upper Locations
    set_rule(world.multiworld.get_location("Dirt", player),
             lambda state: state.has("Seed", player))

    set_rule(world.multiworld.get_location("Profile: Mason", player),
             lambda state: state.has("Seed", player))

#    set_rule(world.multiworld.get_location("Empty Tube", player),
#             lambda state: state.has_all(["Seed", "Dirt"], player))

    set_rule(world.multiworld.get_location("Magnetized Button", player),
             lambda state: state.has_all(["Button (?)", "Magnets"], player))

    set_rule(world.multiworld.get_location("Button (?)", player),
             lambda state: state.has_all(["Scissors", "Metal Can"], player))

    set_rule(world.multiworld.get_location("Taped Button", player),
             lambda state: state.has("Magnetized (?) Button", player))

    # Refuge Lower Locations
    set_rule(world.multiworld.get_location("Badge: Secret", player),
             lambda state: state.has("Novelty T-Shirt", player))

    set_rule(world.multiworld.get_location("Wallpaper: Secret RAM Club", player),
             lambda state: state.has("Novelty T-Shirt", player))

    set_rule(world.multiworld.get_location("Profile: Shepherd", player),
             lambda state: state.has("Novelty T-Shirt", player))

    set_rule(world.multiworld.get_location("Profile: Kip", player),
             lambda state: state.has("Amber", player))

    set_rule(world.multiworld.get_location("Photo of Niko (1)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (2)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (3)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (4)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (5)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (6)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (Blink)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (8)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))

    set_rule(world.multiworld.get_location("Photo of Niko (9)", player),
             lambda state: state.has_all(["Concave Lens", "Convex Lens", "Thick Lens", "Thin Lens"], player))
    
    set_rule(world.multiworld.get_location("Medicated Water", player),
             lambda state: state.has_all(["Tube of Water", "Water Pill"], player))

    set_rule(world.multiworld.get_location("Wallpaper: Maize", player),
             lambda state: state.has_all(["Dirt", "Seed", "Medicated Water"], player))

#    set_rule(world.multiworld.get_location("Sticky Photo", player),
#             lambda state: state.has_all(["Photo of Niko", "Glitter Glue"], player))
    
    set_rule(world.multiworld.get_location("Niko's Library Card", player),
             lambda state: state.has_all(["Photo of Niko", "Kip's Library Card", "Glitter Glue"], player))

    set_rule(world.multiworld.get_location("Badge: Bookworm", player),
             lambda state: state.has("Niko's Library Card", player))

    set_rule(world.multiworld.get_location("Die", player),
             lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player))

    set_rule(world.multiworld.get_location("Profile: George", player),
             lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player))

    set_rule(world.multiworld.get_location("Wallpaper: Cafe", player),
             lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player))

    set_rule(world.multiworld.get_location("Badge: Pancakes", player),
             lambda state: state.has_all(["Niko's Library Card", "Strange Journal"], player))

    # The Tower
    set_rule(world.multiworld.get_location("Theme: Rainbow", player),
             lambda state: state.has("Clover App", player))

    set_rule(world.multiworld.get_location("Wallpaper: Tower", player),
             lambda state: state.has("Clover App", player))

    # Additional Badges
    set_rule(world.multiworld.get_location("Badge: Color Coordinator", player),
             lambda state: state.has_all(["Theme: Blue", "Theme: Teal", "Theme: Green", "Theme: Yellow", "Theme: Red", "Theme: Pink", "Theme: White", "Theme: Orange", "Theme: Rainbow"], player))

    set_rule(world.multiworld.get_location("Badge: Rebirth", player),
             lambda state: state.has_all(["Seed", "Dirt", "Medicated Water"], player))
#             lambda state: state.has_all(["Lightbulb", "Amber", "Seed", "Feather", "Wool", "Feather Pen", "Taped Button", "Weird Film", "Dirt", "Medicated Water", "Die", "Clover App"], player))

#    set_rule(world.multiworld.get_location("Badge: OneShot", player),
#             lambda state: state.has_all(["Lightbulb", "Amber", "Seed", "Feather", "Wool", "Feather Pen", "Taped Button", "Weird Film", "Dirt", "Medicated Water", "Die", "Clover App"], player))


    # ── Goal condition ─────────────────────────────────────────────────────────
    world.multiworld.completion_condition[player] = \
        lambda state: state.has("Victory", player)
