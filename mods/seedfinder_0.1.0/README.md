# Seed finding for Factorio

The goal of this mod is to find seeds with specific properties (huge resources) for speedrunning Factorio.

## How to install

Copy the directory "seedfinder_x.x.x" into your mods directory where "x.x.x" is the version as specified in info.json.

## How to use

Modify the settings.lua / seed_list.lua

## How it works

Basically the mod creates new surfaces with incremental mapseeds and teleports the player into it.
It initiates to chart the area around the player.
Hoever, the chunks are not generated instantly, so we wait until a "sentry chunk" is generated.
The mod then checks the resource & tree count and if it was deemed to have potential.
For good maps a screenshot is made (if not headless), and an entry is added to a csv file.
 
## Note from the author

The implementation is completely prototypic. I am currently not firm with lua, so please bear with me - I wanted to share it anyway. The documentation is very rough.
