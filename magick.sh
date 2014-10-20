# Some imagemagick to make porting easier. Run it and move the textures to 'custom'

convert original/gui/icons.png -crop 9x9+16+18 bubble.png
convert original/blocks/destroy_stage_*.png -append crack_anylength.png
convert original/gui/container/furnace.png -crop 16x16+56+35 default_furnace_fire_bg.png
convert original/gui/container/furnace.png -crop 16x16+176+0 default_furnace_fire_fg.png
convert original/blocks/grass_side.png original/blocks/grass_side_overlay.png -compose CopyOpacity -composite default_grass_side.png
convert original/blocks/grass_side_snowed.png original/blocks/grass_side_overlay.png -compose CopyOpacity -composite default_snow_side.png
convert original/gui/widgets.png -crop 24x24+0+22 gui_hotbar_selected.png
convert original/gui/icons.png -crop 9x9+52+0 heart.png
convert original/particle/particles.png -crop 9x9+56+0 tnt_smoke.png
convert original/blocks/door_wood_upper.png -flop door_wood_a.png
convert original/blocks/door_wood_lower.png -flop door_wood_b.png
convert original/blocks/door_iron_upper.png -flop door_steel_a.png
convert original/blocks/door_iron_lower.png -flop door_steel_b.png
