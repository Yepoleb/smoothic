convert original/gui/icons.png -crop 9x9+16+18 minetest/bubble.png
#convert original/blocks/destroy_stage_*.png -append minetest/crack_anylength.png
#convert original/gui/container/furnace.png -crop 16x16+56+35 minetest/default_furnace_fire_bg.png
convert original/gui/container/furnace.png -crop 16x16+176+0 minetest/default_furnace_fire_fg.png
convert original/blocks/grass_side.png original/blocks/grass_side_overlay.png -compose CopyOpacity -composite minetest/default_grass_side.png
convert original/blocks/grass_side_snowed.png original/blocks/grass_side_overlay.png -compose CopyOpacity -composite minetest/default_snow_side.png
convert original/gui/widgets.png -crop 24x24+0+22 minetest/gui_hotbar_selected.png
convert original/gui/icons.png -crop 9x9+52+0 minetest/heart.png
convert original/particle/particles.png -crop 9x9+56+0 minetest/tnt_smoke.png
