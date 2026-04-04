from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range


def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in oneshot_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))
    return option_group_list


class StartingZone(Choice):
    """
    Determines which zone Niko starts in.
    Barrens: Default start.
    Glen: Skip the Barrens entirely.
    Refuge: Skip both Barrens and Glen.
    """
    display_name = "Starting Zone"
    option_barrens = 1
    option_glen = 2
    option_refuge = 3
    default = 1


class GameGoal(Choice):
    """
    Determines your game goal.
    Leave: Leave Niko sleeping after reaching the Tower.
    Normal: Reach the top of the Tower and make the final choice.
    Solstice: Complete a Solstice run.
    """
    display_name = "Goal Ending"
    option_leave = 0
    option_normal = 1
    option_solstice = 2
    default = 1


class IncludeCrafts(Toggle):
    """Whether or not to include crafted items as checks."""
    display_name = "Include Craftable Items"


class IncludeThemes(Toggle):
    """Whether or not to include desktop themes as checks."""
    display_name = "Include Themes"


class IncludeFriends(Toggle):
    """Whether or not to include friend profiles as checks."""
    display_name = "Include Friends"


class IncludeWallpapers(Toggle):
    """Whether or not to include collectible wallpapers as checks."""
    display_name = "Include Wallpapers"


class IncludeExternalFiles(Toggle):
    """Whether or not to include external TWM files as checks."""
    display_name = "Include External Files"


class IncludeBadges(Toggle):
    """Whether or not to include Steam achievement badges as checks."""
    display_name = "Include Badges"


class TrapChance(Range):
    """Chance for any filler item to become a trap. Set to 0 to disable."""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0


class SpookyPopupTrapWeight(Range):
    """Weight of Spooky Popup traps. Gives you a scary popup from TWM."""
    display_name = "Spooky Popup Trap Weight"
    range_start = 0
    range_end = 100
    default = 50


class CrashTrapWeight(Range):
    """Weight of Crash traps. Forcibly closes OneShot.exe."""
    display_name = "Crash Trap Weight"
    range_start = 0
    range_end = 100
    default = 25


@dataclass
class OneShotOptions(PerGameCommonOptions):
    StartingZone:           StartingZone
    GameGoal:               GameGoal
    IncludeCrafts:          IncludeCrafts
    IncludeFriends:         IncludeFriends
    IncludeWallpapers:      IncludeWallpapers
    IncludeThemes:          IncludeThemes
    IncludeExternalFiles:   IncludeExternalFiles
    IncludeBadges:          IncludeBadges
    TrapChance:             TrapChance
    SpookyPopupTrapWeight:  SpookyPopupTrapWeight
    CrashTrapWeight:        CrashTrapWeight


oneshot_option_groups: Dict[str, List[Any]] = {
    "General Options": [StartingZone, GameGoal],
    "Item Options": [
        IncludeCrafts, IncludeThemes, IncludeFriends,
        IncludeWallpapers, IncludeExternalFiles, IncludeBadges,
    ],
    "Trap Options": [TrapChance, SpookyPopupTrapWeight, CrashTrapWeight],
}
