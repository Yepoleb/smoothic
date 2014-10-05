#Smoothic for Minetest

Minetest port of the Smoothic texture pack for Minecraft.
Made by Leozy and ported by Yepoleb. 

[Original Post](http://www.planetminecraft.com/texture_pack/smoothic/)

##Usage

The actual texture pack is the `minetest` folder, to install it rename it to `Smoothic` 
and follow the instructions on http://wiki.minetest.net/Installing_Texture_Packs.

##License

Leozy gave me permission to release this under the Creative Commons Attribution-NonCommercial-ShareAlike License 
(http://creativecommons.org/licenses/by-nc-sa/4.0/). Please include the links to the original Minecraft post and 
this repository in the credits.

##Contents

* `original` - Copy of `/assets/minecraft/textures/` from the original resource pack
* `custom` - Modified textures which could not be copied from `original`
* `minetest` - Location of the generated texture pack
* `texturesmap.txt` - Most important file, it contains all Minetest texture filenames 
  and their location in `original` or `*custom*`, which means that there is a file with 
  the same name in the `custom` folder.
* `toscript.py` - Parses `texturesmap.txt` and writes a cp instruction 
  into `map.sh` for every line
* `map.sh` - Generates the minetest pack
* `magick.sh` - Collection of random imagemagick lines
