from BaseClasses import CollectionState
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .__init__ import OneShotWorld


def set_rules(world: OneShotWorld) -> None:
    player = world.player
    options = world.options
    
    def can_move_to_barrens(state: CollectionState) -> bool:
        if not state.has("Lightbulb", player):
            return False

        if state.has("Barrens Key", player):
            return True

    world.get_entrance("Starter House -> Barrens", player).access_rule = can_move_to_barrens

    def can_move_to_glen(state: CollectionState) -> bool:
        if not state.has("Lightbulb", player):
            return False

        if state.has("Glen Key", player):
            return True

    world.get_entrance("Starter House -> Glen", player).access_rule = can_move_to_glen

    def can_move_to_refuge(state: CollectionState) -> bool:
        if not state.has("Lightbulb", player):
            return False

        if state.has("Refuge Key", player):
            return True

    world.get_entrance("Starter House -> Refuge Upper", player).access_rule = can_move_to_refuge

    def can_use_elevator(state: CollectionState) -> bool:
        if not state.has("Weird Film", player):
            return False

        has_button = state.has("Taped Button", player)

        if not has_button:
            if options.IncludeCrafts:
                return False
            else:
                return(
                    state.has("Magnets", player) and
                    state.has("Scissors", player) and
                    state.has("Metal Can", player)
                )
        else:
            return True

    world.get_entrance("Refuge Upper -> Refuge Lower", player).access_rule = can_use_elevator

    def can_enter_tower(state: CollectionState) -> bool:
        return (
            state.has("Amber", player)
            state.has("Die", player)
            state.has("Feather", player)
        )

    world.get_entrance("Refuge Lower -> Tower", player).access_rule = can_enter_tower

    # Item logic in Starter House
    ## Obtaining
    world.set_rule(world.get_location("Basement Key"), Has("Torch"))
    world.set_rule(world.get_location("Lightbulb"), Has("Basement Key"))

    ## Crafting
    world.set_rule(world.get_location("Wet Branch"), HasAll("Dry Branch", "Bottle of Alcohol"))
    world.set_rule(world.get_location("Empty Bottle"), HasAll("Dry Branch", "Bottle of Alcohol"))
    world.set_rule(world.get_location("Torch"), Has("Wet Branch"))


    # Barrens
    ## Obtaining
    world.set_rule(world.get_location("Gas Mask"), Has("Outpost PC File"))
    world.set_rule(world.get_location("Strange Journal"), Has("Outpost PC File"))
    world.set_rule(world.get_location("Rubber Gloves"), Has("Gas Mask"))
    world.set_rule(world.get_location("Empty Syringe"), Has("Gas Mask"))
    world.set_rule(world.get_location("Broken Battery"), Has("Crowbar"))
    world.set_rule(world.get_location("Sponge"), HasAll("Gas Mask", "Crowbar"))
    world.set_rule(world.get_location("Rubber Gloves"), Has("Gas Mask"))
    world.set_rule(world.get_location("Amber"), Has("Wet Sponge"))

    ## Crafting
    world.set_rule(world.get_location("Crowbar"), Has("Metal Rod"))
    world.set_rule(world.get_location("Lens"), HasAll("Screwdriver", "Camera"))
    world.set_rule(world.get_location("Empty Battery"), HasAll("Lens", "Broken Battery"))
    world.set_rule(world.get_location("Charged Battery"), HasAll("Empty Battery", "Lightbulb"))
    world.set_rule(world.get_location("Bottle of Smoke"), HasAll("Empty Bottle", "Gas Mask"))
    world.set_rule(world.get_location("Filled Syringe"), HasAll("Empty Syringe", "Gas Mask"))
    world.set_rule(world.get_location("Bottle of Acid"), HasAll("Filled Syringe", "Bottle of Smoke"))
    world.set_rule(world.get_location("Wet Sponge"), HasAll("Bottle of Acid", "Sponge", "Rubber Gloves"))

    ## Files
    world.set_rule(world.get_location("Outpost PC File"), Has("Charged Battery"))

    ## Themes
    world.set_rule(world.get_location("Theme: Cyan"), Has("Gas Mask"))

    ## Wallpapers
    world.set_rule(world.get_location("Wallpaper: Factory"), Has("Gas Mask"))

    ## Friends
    world.set_rule(world.get_location("Profile: Silver"), Has("Wet Sponge"))

    ## Badges
    world.set_rule(world.get_location("Badge: Shock"), Has("Charged Battery"))


    # Glen
    ## Obtaining
    world.set_rule(world.get_location("Bottle of Dye"), Has("Wool"))
    world.set_rule(world.get_location("Novelty T-Shirt"), Has("Wool"))
    world.set_rule(world.get_location(""))

