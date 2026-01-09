from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import ShippedInSpaceWorld

def set_all_entrance_rules(world: ShippedInSpaceWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    space_to_space10 = world.get_entrance("space to space10")
    space10_to_space20 = world.get_entrance("space10 to space20")
    space20_to_space30 = world.get_entrance("space20 to space30")

    # An access rule is a function. We can define this function like any other function.
    # This function must accept exactly one parameter: A "CollectionState".
    # A CollectionState describes the current progress of the players in the multiworld, i.e. what items they have,
    # which regions they've reached, etc.
    # In an access rule, we can ask whether the player has a collected a certain item.
    # We can do this via the state.has(...) function.
    # This function takes an item name, a player number, and an optional count parameter (more on that below)
    # Since a rule only takes a CollectionState parameter, but we also need the player number in the state.has call,
    # our function needs to be locally defined so that it has access to the player number from the outer scope.


    # Now we can set our "can_pass_level10" rule to our entrance which requires passing level 10 to clear the path.
    # One way to set rules is via the set_rule() function, which works on both Entrances and Locations.
    set_rule(space_to_space10, lambda state: state.has("level10Key", world.player))

    # Because the function has to be defined locally, most worlds prefer the lambda syntax.
    set_rule(space10_to_space20, lambda state: state.has("level20Key", world.player))

    # Conditions can depend on event items.
    set_rule(space20_to_space30, lambda state: state.has("level30Key", world.player))

def set_all_rules(world: ShippedInSpaceWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.
    set_all_entrance_rules(world)

    set_completion_condition(world)


def set_completion_condition(world: ShippedInSpaceWorld) -> None:


    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Winstate", world.player)
