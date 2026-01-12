from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ShippedInSpaceWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "somewhere in space 1": 1,
    "somewhere in space 2": 2,
    "somewhere in space 3": 3,
    "somewhere in space 4": 4,
    "somewhere in space 5": 5,
    "somewhere in space 6": 6,
    "somewhere in space 7": 7,
    "somewhere in space 8": 8,
    "somewhere in space 9": 9,
    "somewhere in space 10": 10,
    "somewhere in space 11": 11,
    "somewhere in space 12": 12,
    "somewhere in space 13": 13,
    "somewhere in space 14": 14,
    "somewhere in space 15": 15,
    "somewhere in space 16": 16,
    "somewhere in space 17": 17,
    "somewhere in space 18": 18,
    "somewhere in space 19": 19,
    "somewhere in space 20": 20,
    "somewhere in space 21": 21,
    "somewhere in space 22": 22,
    "somewhere in space 23": 23,
    "somewhere in space 24": 24,
    "somewhere in space 25": 25,
    "somewhere in space 26": 26,
    "somewhere in space 27": 27,
    "somewhere in space 28": 28,
    "somewhere in space 29": 29,
    "somewhere in space 30": 30,
    "somewhere in space 31": 31,
    "somewhere in space 32": 32,
    "somewhere in space 33": 33,
    "somewhere in space 34": 34,
    "somewhere in space 35": 35,
    "somewhere in space 36": 36,
    "somewhere in space 37": 37,
    "somewhere in space 38": 38,
    "somewhere in space 39": 39,
    "somewhere in space 40": 40
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class ShippedInSpaceLocation(Location):
    game = "ShippedInSpace"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ShippedInSpaceWorld) -> None:
    create_regular_locations(world)
    


def create_regular_locations(world: ShippedInSpaceWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    space = world.get_region("Space")
    lvl40 = world.get_region("Level 40")

    space10 = world.get_region("Space 10-20")

    space20 = world.get_region("Space 20-30")

    space30 = world.get_region("Space 30-40")
    
    
    

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    space_locations = get_location_names_with_ids(
        ["somewhere in space 1","somewhere in space 2","somewhere in space 3","somewhere in space 4","somewhere in space 5","somewhere in space 6","somewhere in space 7","somewhere in space 8","somewhere in space 9","somewhere in space 10"]
    )

    space10_locations = get_location_names_with_ids(
        ["somewhere in space 11","somewhere in space 12","somewhere in space 13","somewhere in space 14","somewhere in space 15","somewhere in space 16","somewhere in space 17","somewhere in space 18","somewhere in space 19","somewhere in space 20"]
    )

    space20_locations = get_location_names_with_ids(
        ["somewhere in space 21","somewhere in space 22","somewhere in space 23","somewhere in space 24","somewhere in space 25","somewhere in space 26","somewhere in space 27","somewhere in space 28","somewhere in space 29","somewhere in space 30"]
    )

    space30_locations = get_location_names_with_ids(
        ["somewhere in space 31","somewhere in space 32","somewhere in space 33","somewhere in space 34","somewhere in space 35","somewhere in space 36","somewhere in space 37","somewhere in space 38","somewhere in space 39","somewhere in space 40"]
    )

    

    space.add_locations(space_locations, ShippedInSpaceLocation)

    

    space10.add_locations(space10_locations, ShippedInSpaceLocation)

    space20.add_locations(space20_locations, ShippedInSpaceLocation)

    space30.add_locations(space30_locations, ShippedInSpaceLocation)    
    

def create_events(world: ShippedInSpaceWorld) -> None:
    lvl40 = world.get_region("Level 40")

    lvl40.add_event(
        "Victory",
        "Victory",
        location_type=ShippedInSpaceLocation,
        item_type=items.ShippedInSpaceItem,
    )


