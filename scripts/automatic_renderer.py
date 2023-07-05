import bpy

def automatic_renderer():
    scene = bpy.context.scene
    scene.render.image_settings.file_format='FFMPEG'
    # Somehow this only works if absolute path is provided?
    scene.render.filepath='/content/output'
    bpy.ops.render.render(write_still=1, animation=True)
