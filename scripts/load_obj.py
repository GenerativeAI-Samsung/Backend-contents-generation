import bpy
import argparse
import sys

bpy.ops.object.select_all(action='SELECT')
#bpy.ops.object.override_object_delete(use=False, confirm=False)
bpy.ops.object.delete(use_global=False, confirm=False)
class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    This class is identical to its superclass, except for the parse_args
    method (see docstring). It resolves the ambiguity generated when calling
    Blender from the CLI with a python script, and both Blender and the script
    have arguments. E.g., the following call will make Blender crash because
    it will try to process the script's -a and -b flags:
    >>> blender --python my_script.py -a 1 -b 2

    To bypass this issue this class uses the fact that Blender will ignore all
    arguments given after a double-dash ('--'). The approach is that all
    arguments before '--' go to Blender, arguments after go to the script.
    The following calls work fine:
    >>> blender --python my_script.py -- -a 1 -b 2
    >>> blender --python my_script.py --
    """

    def _get_argv_after_doubledash(self):
        """
        Given the sys.argv as a list of strings, this method returns the
        sublist right after the '--' element (if present, otherwise returns
        an empty list).
        """
        try:
            idx = sys.argv.index("--")
            return sys.argv[idx+1:] # the list after '--'
        except ValueError as e: # '--' not in the list:
            return []

    # overrides superclass
    def parse_args(self):
        """
        This method is expected to behave identically as in the superclass,
        except that the sys.argv list will be pre-processed using
        _get_argv_after_doubledash before. See the docstring of the class for
        usage examples and details.
        """
        return super().parse_args(args=self._get_argv_after_doubledash())
        
parser = ArgumentParserForBlender()
parser.add_argument("-fbx_file", "--fbx_file_path", type=str, nargs='+', help="testing", default=[])
args = parser.parse_args()
lst_fbx_file_path = args.fbx_file_path

print("hello ", lst_fbx_file_path)

for fbx_file in lst_fbx_file_path:
    bpy.ops.import_scene.fbx( filepath = fbx_file, ignore_leaf_bones=True, automatic_bone_orientation=True, axis_forward='Y', axis_up='Z')
