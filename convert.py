#feel free to create a issue about anything not working cuz i made this in like 5 minutes lol
import os

print("converting shader frag...")

replacements = {'void mainImage( out vec4 fragColor, in vec2 fragCoord )':'void main()', 'void mainImage(out vec4 fragColor, in vec2 fragCoord)':'void main()' 'texture':'flixel_texture2D','iChannel0':'bitmap',
                'fragCoord / iResolution.xy':'openfl_TextureCoordv', 'fragCoord.xy / iResolution.xy':'openfl_TextureCoordv', 'fragCoord.xy/iResolution.xy':'openfl_TextureCoordv', 
                'fragCoord/iResolution.xy':'openfl_TextureCoordv', 'fragCoord/iResolution':'openfl_TextureCoordv.xy', 'fragColor':'gl_FragColor'
               }



with open(os.getcwd() + "/shadertoy.frag") as infile, open(os.getcwd() + "/flixel.frag", 'w') as outfile:
    outfile.write("#pragma header\nuniform float iTime;\nuniform sampler2D iChannel1;\nuniform sampler2D iChannel2;\nuniform sampler2D iChannel3;\n") # write new content at the beginning
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)
print("done converting shader frag!")
