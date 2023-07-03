import bpy

# Create new material
material_toon_shader = bpy.data.materials.new(name="Toon Shader")
material_outline = bpy.data.materials.new(name="Outline")
material_toon_shader.use_nodes = True
material_outline.use_nodes = True

# Toon Shader
# Remove default nodes
default_principled_BSDF = material_toon_shader.node_tree.nodes['Principled BSDF']
material_toon_shader.node_tree.nodes.remove(default_principled_BSDF)
default_material_output = material_toon_shader.node_tree.nodes['Material Output']
material_toon_shader.node_tree.nodes.remove(default_material_output)

# Add Nodes
node_texture_coord = material_toon_shader.node_tree.nodes.new(type='ShaderNodeTexCoord')
node_mapping = material_toon_shader.node_tree.nodes.new(type='ShaderNodeMapping')
node_principled_BSDF = material_toon_shader.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
node_normal_map = material_toon_shader.node_tree.nodes.new(type='ShaderNodeNormalMap')
node_shader_to_RGB = material_toon_shader.node_tree.nodes.new(type='ShaderNodeShaderToRGB')
node_color_ramp = material_toon_shader.node_tree.nodes.new(type='ShaderNodeValToRGB')
node_color_mix = material_toon_shader.node_tree.nodes.new(type='ShaderNodeMix')
node_material_output = material_toon_shader.node_tree.nodes.new(type='ShaderNodeOutputMaterial')


# Establish connections between nodes
material_toon_shader.node_tree.links.new(node_texture_coord.outputs['Generated'], node_mapping.inputs['Vector'])
material_toon_shader.node_tree.links.new(node_mapping.outputs['Vector'], node_principled_BSDF.inputs['Base Color'])
material_toon_shader.node_tree.links.new(node_normal_map.outputs['Normal'], node_principled_BSDF.inputs['Normal'])
material_toon_shader.node_tree.links.new(node_principled_BSDF.outputs['BSDF'], node_shader_to_RGB.inputs['Shader'])
material_toon_shader.node_tree.links.new(node_shader_to_RGB.outputs['Color'], node_color_ramp.inputs['Fac'])
material_toon_shader.node_tree.links.new(node_color_ramp.outputs['Color'], node_color_mix.inputs['Factor'])
node_color_mix.data_type = 'RGBA'
# node_color_mix.outputs[0] is equivalent to float mix node Result
# node_color_mix.outputs[1] is equivalent to vector mix node Result
# node_color_mix.outputs[2] is equivalent to color mix node Result
material_toon_shader.node_tree.links.new(node_color_mix.outputs[2], node_material_output.inputs['Surface'])

# Nodes configuration
# Principled BSDF config
node_principled_BSDF.inputs['Subsurface Color'].default_value = (0.8, 0.5, 0.35, 1)

# Color ramp config
node_color_ramp.color_ramp.interpolation = 'CONSTANT'
# Adding new color stop at location
node_color_ramp.color_ramp.elements.new(0.120)
#Setting color for the stop that we recently created
node_color_ramp.color_ramp.elements[1].color = (0.5, 0.261, 0.257, 1.0)
#Assignng position and color to already present stops
node_color_ramp.color_ramp.elements[0].color = (0.055, 0.022, 0.022, 1.0)
node_color_ramp.color_ramp.elements[2].position = (0.55)
node_color_ramp.color_ramp.elements[2].color = (1.0, 0.723, 0.374, 1)

# Color mix config
node_color_mix.inputs[6].default_value = (0.263, 0.038, 0.028, 1.0)
node_color_mix.inputs[7].default_value = (0.761, 0.45, 0.203, 1.0)


# Outline
node_principled_BSDF_outline = material_outline.node_tree.nodes['Principled BSDF']
node_principled_BSDF_outline.inputs['Base Color'].default_value = (0, 0, 0, 1)
material_outline.use_backface_culling = True


# Create cube object
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
                                 location=(0, 0, 0), scale=(1, 1, 1))
cube = bpy.data.objects['Cube']

# Assign the material to desired object
cube.data.materials.append(material_toon_shader)
cube.data.materials.append(material_outline)

# Create object outline
# Create modifier
mod_solidify = cube.modifiers.new("Solidify", 'SOLIDIFY')
mod_solidify.thickness = -0.05
mod_solidify.use_flip_normals = True
mod_solidify.material_offset = 1

