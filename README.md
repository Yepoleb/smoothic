#Smoothic for Minetest

Minetest port of the Smoothic texture pack for Minecraft.
Made by Leozy and ported by Yepoleb. 

[Original Post](http://www.planetminecraft.com/texture_pack/smoothic/)

##Usage

The actual texture pack is the `minetest` folder, to install it rename it to 
`Smoothic` and follow the instructions on 
http://wiki.minetest.net/Installing_Texture_Packs.

##Font

The font is currently a beta feature and can be found in the `font` folder.

###Install
* Copy the xml and png files to your `.minetest/fonts/` folder
* Set the `freetype` config value to `false`
* Set the `font_path` to the full path of your font files without the size and 
  extension, e.g. `/home/user/.minetest/fonts/smoothic` (relative links don't 
  seem to work)
* Set the `font_size` to 8, 16, 24 or 32 pixel, the recommended value is 16

###Build
The font is generated using the `convfont.py` script, which currently only 
supports the old (pre Minecraft 1.7) font structure (Codepage 437), because 
the original Smoothic files are not completely updated to the new format. To 
use it with your own files, copy `assets/textures/font/ascii.png` to 
`./<name>_img_<size>`, where `<name>` is the name of your font and `<size>` 
the size in pixel. Adjust the script variables (they all have comments above 
them) and run it. After the xml files are generated, add the missing image 
sizes and test it.

##License

Leozy gave me permission to release this under the Creative Commons 
Attribution-NonCommercial-ShareAlike License 
(http://creativecommons.org/licenses/by-nc-sa/4.0/). 
Please include the links to the original Minecraft post and this repository in 
the credits.

##Contents

* `original` - Copy of `/assets/minecraft/textures/` from the original resource 
  pack
* `custom` - Modified textures which could not be copied from `original`
* `minetest` - Location of the generated texture pack
* `texturesmap.txt` - Most important file, it contains all Minetest texture 
  filenames and their location in `original` or `*custom*`, which means that 
  there is a file with the same name in the `custom` folder.
* `toscript.py` - Parses `texturesmap.txt` and writes a cp instruction to 
  `map.sh` for every line
* `map.sh` - Generates the minetest pack
* `magick.sh` - Collection of random imagemagick lines
