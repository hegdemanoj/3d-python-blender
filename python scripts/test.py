import bpy

#bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(0, 0, -10))
bpy.ops.transform.resize(value=(-30.0001, -30.0001, -30.0001), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.rigidbody.objects_add(type='PASSIVE')



for z in range(20):
    for y in range(10):
        for x in range(10):
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x,y,z))
            bpy.ops.rigidbody.objects_add(type='ACTIVE')

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(65, -65, 30), rotation=(1.02626, 2.27337e-07, 0.816814))    
bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end=50)
bpy.context.scene.frame_end = 50



    
    

