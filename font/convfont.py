#! /usr/bin/python3

import PIL.Image
import lxml.etree as ETree

# Size of the characters in pixel (probably block texture size / 2)
charsize = 8
# Length of the whitespace character (0x20) in pixel
spacesize = 4
# Each scale value gets multiplied with the charsize to get the actual font size
# A scale of 2 means the font will be 8px * 2 = 16px big 
# 16px seems to be the size for "Normal" gui scale in Minecraft
scales = (1, 2, 3, 4)
# Name of the font and image files
fontname = "smoothic"

print("Loading characters")

mcfont = PIL.Image.open(fontname + "_img_{}.png".format(charsize))
with open("cp437.txt", "r") as mapping:
    characters = mapping.read().replace("\n", "")
unicodes = []
for c in characters:
    unicodes.append(c)

locations = []

for i in range(256):
    y = i // 16 * charsize
    x = i % 16 * charsize
    sprite = mcfont.crop((x, y, x+charsize, y+charsize))
    # Get the image size without transparent parts
    bbox = sprite.getbbox()
    # Skip empty images
    if bbox is None:
        continue

    p1 = (x+bbox[0], y)
    # Check if we can add one more pixel without going over the limit
    if bbox[2] < charsize:
        # Add one pixel of spacing
        p2 = (x+bbox[2]+1, y+8)
    else:
        p2 = (x+bbox[2], y+8)
    
    locations.append((unicodes[i], p1+p2))


for scale in scales:
    fontsize = charsize * scale
    fontimage = fontname + "_img_{}.png".format(fontsize)
    fontfile = fontname + "_{}.xml".format(fontsize)
    
    print("Building font file for {}px".format(fontsize))
    
    font = ETree.Element("font", {"type": "bitmap"})
    font.append(ETree.Element("Texture", {
            "index": "0", 
            "filename": fontimage, 
            "hasAlpha": "true"}))
    for char, locs in locations:
        r = ", ".join(str(z*scale) for z in locs)
        entry = ETree.Element("c", {
                "c": char,
                "r": r})
        font.append(entry)

    # Append the whitespace character
    font.append(ETree.Element("c", {
            "c": " ",
            "r": ", ".join(str(z*scale) for z in (0, 16, 3, 24))}))
    doc = ETree.ElementTree(font)
    doc.write(fontfile, encoding="utf-16", xml_declaration=True, pretty_print=True)
