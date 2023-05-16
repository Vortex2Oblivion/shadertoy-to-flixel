#pragma header
//https://www.shadertoy.com/view/lsKSDz

void main( out vec4 gl_FragColor, in vec2 fragCoord )
{
	vec2 uv = openfl_TextureCoordv;
	
    vec2 d = abs((uv - 0.5) * 2.0);
    d = pow(d, vec2(2.0, 2.0));
        
    vec4 r = flixel_texture2D(bitmap, uv - d * 0.015);
    vec4 g = flixel_texture2D(bitmap, uv);
    vec4 b = flixel_texture2D(bitmap, uv);
    
    gl_FragColor = vec4(r.r, g.g, b.b, 1.0);
}