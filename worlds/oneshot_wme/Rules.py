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
    set_rule(world.multiworld.get_entrance("Starter House -> Solstice", player),
             lambda state: state.has("Solstice Protocol", player))

    set_rule(world.multiworld.get_location("Wet Branch Craft", player),
             lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))

    set_rule(world.multiworld.get_location("Torch Craft", player),
             lambda state: state.has("Wet Branch", player))

    set_rule(world.multiworld.get_location("Empty Bottle Craft", player),
             lambda state: state.has_all(["Dry Branch", "Bottle of Alcohol"], player))

    set_rule(world.multiworld.get_location("Crowbar", player),
             lambda state: state.has("Metal Rod", player))

    set_rule(world.multiworld.get_location("Filled Bottle", player),
             lambda state: state.has_all(["Empty Bottle", "Filled Syringe"], player))

    set_rule(world.multiworld.get_location("Filled Syringe", player),
             lambda state: state.has("Empty Syringe", player))

    set_rule(world.multiworld.get_location("Bottle of Acid", player),
             lambda state: state.has_all(["Bottle of Smoke", "Filled Syringe"], player))

    set_rule(world.multiworld.get_location("Wet Sponge", player),
             lambda state: state.has_all(["Sponge", "Bottle of Acid"], player))

    set_rule(world.multiworld.get_location("Lens", player),
             lambda state: state.has_all(["Camera", "Screwdriver"], player))

    set_rule(world.multiworld.get_location("Empty Battery", player),
             lambda state: state.has_all(["Broken Battery", "Lens"], player))

    set_rule(world.multiworld.get_location("Charged Battery", player),
             lambda state: state.has_all(["Empty Battery", "Lightbulb"], player))

    set_rule(world.multiworld.get_location("Feather Pen", player),
             lambda state: state.has_all(["Feather", "Bottle of Dye"], player))

    set_rule(world.multiworld.get_location("Magnetized Button", player),
             lambda state: state.has_all(["Button (?)", "Magnets"], player))

    set_rule(world.multiworld.get_location("Button (?)", player),
             lambda state: state.has_all(["Scissors", "Metal Can"], player))

    set_rule(world.multiworld.get_location("Taped Button", player),
             lambda state: state.has("Magnetized (?) Button"), player)

    # ── Goal condition ─────────────────────────────────────────────────────────
    world.multiworld.completion_condition[player] = \
        lambda state: state.has("Victory", player)
