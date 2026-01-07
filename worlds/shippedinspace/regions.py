from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ShippedInSpaceWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: ShippedInSpaceWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ShippedInSpaceWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    space = Region("Space", world.player, world.multiworld)
    lvl40 = Region("Level 40", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [space,lvl40]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: ShippedInSpaceWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    space = world.get_region("Space")

    lvl40 = world.get_region("Level 40")

    space.connect(lvl40, "space to Lvl40")


    