#this conversion script does not remove paramaters from the main/mainImage function
#you will need to remove those yourself


#you will also need to insert #pragma header at the top of the file
#feel free to create a issue about anything not working cuz i made this in like 5 minutes lol
import os

replacements = {'mainImage':'main', 'texture':'flixel_texture2D', 'iChannel0':'bitmap', 'iChannel1':'sampler2D', 'iChannel2':'sampler2D', 'iChannel3':'sampler2D', 'fragCoord / iResolution.xy':'openfl_TextureCoordv', 'fragCoord.xy / iResolution.xy':'openfl_TextureCoordv','fragColor':'gl_FragColor'}

with open(os.getcwd() + "/shadertoy.frag") as infile, open(os.getcwd() + "/flixel.frag", 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)
