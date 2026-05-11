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
    set_rule(world.multiworld.get_entrance("Starter House -> Refuge", player),
             lambda state: state.has("Lightbulb", player) and
                           state.has("Refuge Key", player))

    # Tower requires Tower Key + elevator items
    set_rule(world.multiworld.get_entrance("Refuge -> Tower", player),
             lambda state: state.has("Tower Key", player) and
                           state.has("Die", player) and
                           state.has("Amber", player) and
                           state.has("Feather", player) and
                           state.has("Lightbulb", player))

    # Solstice requires Solstice Protocol + Glowing Journal
    set_rule(world.multiworld.get_entrance("Starter House -> Solstice", player),
             lambda state: state.has("Solstice Protocol", player))

    # ── Goal condition ─────────────────────────────────────────────────────────
    world.multiworld.completion_condition[player] = \
        lambda state: state.has("Victory", player)
