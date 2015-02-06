#! /usr/bin/env python

inp = open("texturesmap.txt", "r")
out = open("map.sh", "w")
for line in inp:
    if line.startswith("#"):
        continue
    s = line.split()
    if len(s) == 2:
        if s[1] == "*custom*":
            out.write("cp custom/{} minetest/{}\n".format(s[0], s[0]))
        else:
            out.write("cp original/{} minetest/{}\n".format(s[1], s[0]))
    elif len(s) > 0:
        out.write("#Missing: {}\n".format(s[0]))

inp.close()
out.close()
