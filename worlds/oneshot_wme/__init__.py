import logging
from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict

from .Locations import get_location_names, get_total_locations
from .Items import create_item, create_itempool, item_table
from .Options import OneShotOptions
from .Regions import create_regions
from .Rules import set_rules


class OneShotWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up OneShot: World Machine Edition for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["YourName"]
    )]


class OneShotWorld(World):
    """
    OneShot: World Machine Edition is a puzzle adventure game in which you
    guide a child named Niko through a broken world to restore its sun.
    You only have One Shot to do it. The sun can only be destroyed once.
    """

    game = "OneShot World Machine Edition"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()
                       if data.ap_code is not None}
    location_name_to_id = get_location_names()
    options_dataclass = OneShotOptions
    options: OneShotOptions
    web = OneShotWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> Dict[str, object]:
        return {
            "options": {
                "Goal":                 self.options.GameGoal.value,
                "StartingZone":         self.options.StartingZone.value,
                "IncludeCrafts":        self.options.IncludeCrafts.value,
                "IncludeThemes":        self.options.IncludeThemes.value,
                "IncludeFriends":       self.options.IncludeFriends.value,
                "IncludeWallpapers":    self.options.IncludeWallpapers.value,
                "IncludeExternalFiles": self.options.IncludeExternalFiles.value,
                "IncludeBadges":        self.options.IncludeBadges.value,
                "TrapChance":             self.options.TrapChance.value,
                "SpookyPopupTrapWeight":  self.options.SpookyPopupTrapWeight.value,
                "CrashTrapWeight":        self.options.CrashTrapWeight.value,
            },
            "Seed":           self.multiworld.seed_name,
            "Slot":           self.multiworld.player_name[self.player],
            "TotalLocations": get_total_locations(self),
        }

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)
