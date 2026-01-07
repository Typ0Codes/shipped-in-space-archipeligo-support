from dataclasses import dataclass

from Options import PerGameCommonOptions, Range

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  ShippedInSpace doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.



# A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
class NumberOfLevels(Range):
    """
    currently useless
    """

    display_name = "NumberOfLevels"

    range_start = 10
    range_end = 40

    # Range options must define an explicit default value.
    default = 40



@dataclass
class ShippedInSpaceOptions(PerGameCommonOptions):
    numberoflevels: NumberOfLevels
    


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.


# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
