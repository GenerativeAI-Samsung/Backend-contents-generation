import bpy
import sys

scripts_dir = "/home/ducb/Local-Git-Repos/Backend-contents-generation/scripts"
sys.path.append(scripts_dir)

from toon_shader import ToonShader

bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', 
                                location=(0, 0, 0), scale=(1, 1, 1))

cube = bpy.data.objects['Cube']

toon_shader = ToonShader(cube)
toon_shader.config_material_toon_shader()
toon_shader.config_material_outline()
toon_shader.apply_shader()