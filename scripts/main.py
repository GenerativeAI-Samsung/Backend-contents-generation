import bpy
import sys

scripts_dir = "/home/ducb/Local-Git-Repos/Backend-contents-generation/scripts"
sys.path.append(scripts_dir)

from toon_shader import ToonShader
from load_obj import ArgumentParserForBlender
from automatic_renderer import automatic_renderer

# Import FBX into the virtual studio
parser = ArgumentParserForBlender()
parser.add_argument("-fbx_file", "--fbx_file_path", type=str, nargs='+', help="testing", default=[])
args = parser.parse_args()
lst_fbx_file_path = args.fbx_file_path

for fbx_file in lst_fbx_file_path:
    bpy.ops.import_scene.fbx( filepath = fbx_file, \
                            use_custom_normals=False, use_image_search=False, \
                            bake_space_transform=True, use_prepost_rot=False, \
                            use_manual_orientation=True, axis_forward='Y', axis_up='Z', \
                            ignore_leaf_bones=True, automatic_bone_orientation=True)

dog_mesh = bpy.data.objects['dog mesh']

toon_shader = ToonShader(dog_mesh)
toon_shader.config_material_toon_shader()
toon_shader.config_material_outline()
toon_shader.apply_shader()

# automatic_renderer()
