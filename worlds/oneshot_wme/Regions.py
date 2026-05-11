from BaseClasses import Region
from .Types import OneShotLocation
from .Locations import location_table, is_valid_location, event_locations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import OneShotWorld


def create_regions(world: "OneShotWorld"):
    menu          = create_region(world, "Menu")
    starter_house = create_region_and_connect(world, "Starter House", "Menu -> Starter House",          menu)
    barrens       = create_region_and_connect(world, "Barrens",       "Starter House -> Barrens",       starter_house)
    glen          = create_region_and_connect(world, "Glen",           "Starter House -> Glen",          starter_house)
    refuge        = create_region_and_connect(world, "Refuge",         "Starter House -> Refuge",        starter_house)

    tower         = create_region_and_connect(world, "Tower",          "Refuge -> Tower",                refuge)
    endgame       = create_region_and_connect(world, "Endgame",        "Tower -> Endgame",               tower)
    solstice = create_region_and_connect(world, "Solstice", "Starter House -> Solstice", starter_house)


def create_region(world: "OneShotWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)
    goal = world.options.GameGoal.value
    goal_location = ["Leave", "Victory?", "Solstice"][goal]

    for key, data in location_table.items():
        if data.region == name:
            if key in event_locations:
                if key != goal_location:
                    continue
            elif not is_valid_location(world, key):
                continue
            location = OneShotLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    world.multiworld.regions.append(reg)
    return reg


def create_region_and_connect(world: "OneShotWorld", name: str,
                               entrance_name: str, connected_region: Region) -> Region:
    reg = create_region(world, name)
    connected_region.connect(reg, entrance_name)
    return reg
