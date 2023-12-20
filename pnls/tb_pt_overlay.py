import bpy
from bpy.app.translations import pgettext_iface as iface_
#HEADER
def overlayheader (context,layout):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    sover = context.space_data.overlay    
    mode = bpy.context.mode
    tool_settings = context.tool_settings
  #CURSOR
    if mode in {'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'PAINT_TEXTURE', 'PAINT_WEIGHT', 'PAINT_VERTEX', 'SCULPT'}:
        if mode == 'SCULPT':
            settings = tool_settings.sculpt     
            brush = bpy.context.tool_settings.sculpt.brush  
        if mode == 'PAINT_VERTEX':       
            settings = tool_settings.vertex_paint
            brush = bpy.context.tool_settings.vertex_paint.brush   
        if mode == 'PAINT_TEXTURE':       
            settings = tool_settings.image_paint
            brush = bpy.context.tool_settings.image_paint.brush             
        if mode == 'PAINT_WEIGHT':       
            settings = tool_settings.weight_paint
            brush = bpy.context.tool_settings.weight_paint.brush         
        if mode == 'PAINT_GPENCIL':      
            settings = tool_settings.gpencil_paint
            brush = bpy.context.tool_settings.gpencil_paint.brush
        if mode == 'SCULPT_GPENCIL':      
            settings = tool_settings.gpencil_sculpt_paint
            brush = bpy.context.tool_settings.gpencil_sculpt_paint.brush

        box = layout.box()
        tex_slot = brush.texture_slot
        tex_slot_mask = brush.mask_texture_slot
        row = box.row(align=True)
        if not settings.show_brush:
            row.prop(settings, "show_brush", text="Display Cursor",icon='CURSOR')
        else:
            row.prop(settings, "show_brush", text="",icon='CURSOR')
            row.prop(brush, "cursor_color_add", text="")
            if mode == 'SCULPT' and brush.sculpt_capabilities.has_secondary_color:
                row.prop(brush, "cursor_color_subtract", text="")
            row = box.row(align=True)
            row.prop(brush, "cursor_overlay_alpha", text="Falloff Opacity")
            row.prop(brush, "use_cursor_overlay_override", toggle=True, text="", icon='BRUSH_DATA')
            row.prop(brush, "use_cursor_overlay", text="", toggle=True,
                icon='HIDE_OFF' if brush.use_cursor_overlay else 'HIDE_ON',)

            if mode in {'PAINT_2D', 'PAINT_TEXTURE', 'PAINT_VERTEX', 'SCULPT'}:
                row = box.row(align=True)
                row.prop(brush, "texture_overlay_alpha", text="Texture Opacity")
                row.prop(brush, "use_primary_overlay_override", toggle=True, text="", icon='BRUSH_DATA')
                if tex_slot.map_mode != 'STENCIL':
                    row.prop(brush, "use_primary_overlay", text="", toggle=True,
                        icon='HIDE_OFF' if brush.use_primary_overlay else 'HIDE_ON',)

            if mode in {'PAINT_TEXTURE', 'PAINT_2D'}:
                row = box.row(align=True)
                row.prop(brush, "mask_overlay_alpha", text="Mask Texture Opacity")
                row.prop(brush, "use_secondary_overlay_override", toggle=True, text="", icon='BRUSH_DATA')
                if tex_slot_mask.map_mode != 'STENCIL':
                    row.prop(brush, "use_secondary_overlay", text="", toggle=True,
                        icon='HIDE_OFF' if brush.use_secondary_overlay else 'HIDE_ON',)  
  #Vertex_Paint
    if bpy.context.mode == 'PAINT_VERTEX':
        box = layout.box()
        row = box.row(align= True)  
        row.label(text="Vertex_Paint",icon='VPAINT_HLT')
        row = box.row(align= True)
        row.prop(sover, "vertex_paint_mode_opacity")
  #Texture_Paint
    if bpy.context.mode == 'PAINT_TEXTURE':
        box = layout.box()
        row = box.row(align= True)  
        row.label(text="Texture_Paint",icon='TPAINT_HLT')
        row = box.row(align= True)
        row.prop(sover, "texture_paint_mode_opacity")
  #Weight_Paint
    if bpy.context.mode == 'PAINT_WEIGHT':
        box = layout.box()
        row = box.row(align= True)  
        row.label(text="Weight_Paint",icon='WPAINT_HLT')
        row.prop(sover, "show_wpaint_contours",icon='FORCE_TURBULENCE')
        row = box.row(align= True)
        split = box.split(factor=0.8, align=True)
        col = split.column(align=True)
        col.prop(sover, "weight_paint_mode_opacity", text= "Opacity")
        col = split.column(align=True)
        col.prop(context.tool_settings, "vertex_group_user", text= "")
  #POSE_MODE
    if bpy.context.mode == 'POSE':
        box = layout.box()
        if sover.show_xray_bone == True:
            split = box.split(factor=0.08, align=True)
            col = split.column(align=True)
            col.prop(sover, "show_xray_bone", text= "",icon='ARMATURE_DATA')
            col = split.column(align=True)
            col.prop(sover, "xray_alpha_bone")
        elif sover.show_xray_bone == False:
            row = box.row(align= True)
            row.prop(sover, "show_xray_bone", text= "Fade Geometry",icon='ARMATURE_DATA')
  #Curve
    if bpy.context.mode == 'EDIT_CURVE':
        box = layout.box()
        row = box.row(align= True)  
        row.label(text="Curve Edit Mode", icon='MOD_CURVE')
        row = box.row(align= True)
        row.prop_enum(sover,"display_handle","NONE",icon="X")
        row.prop_enum(sover,"display_handle","SELECTED",icon="RESTRICT_SELECT_OFF")
        row.prop_enum(sover,"display_handle","ALL",icon="CURVE_PATH")                        
        row = box.row(align= True)
        row.prop(sover, "show_curve_handles", text= "Handlers",icon='OUTLINER_DATA_CURVE')
        row.prop(sover, "show_curve_normals", text= "Normals",icon='CURVE_PATH')
        if sover.show_curve_normals == True:
            row.prop(sover, "normals_length", text= "Lenght")
  #SCULPT
    if bpy.context.mode == 'SCULPT':
        box = layout.box()
        ss = bpy.context.tool_settings.sculpt
       #mask
        if sover.show_sculpt_mask == True:
            split = box.split(factor=0.08, align=True)
            col = split.column(align=True)
            col.prop(sover, "show_sculpt_mask", text= "",icon='MOD_MASK')
            col = split.column(align=True)
            col.prop(sover, "sculpt_mode_mask_opacity")
        else:
            row = box.row(align= True)
            row.prop(sover, "show_sculpt_mask", text= "Sculpt Mask Opacity",icon='MOD_MASK')      
       #face_sets     
        if sover.show_sculpt_face_sets == True:
            split = box.split(factor=0.08, align=True)
            col = split.column(align=True)
            col.prop(sover, "show_sculpt_face_sets", text= "",icon='FACE_MAPS')
            col = split.column(align=True)
            col.prop(sover, "sculpt_mode_face_sets_opacity")
        else:
            row = box.row(align= True)
            row.prop(sover, "show_sculpt_face_sets", text= "Face Maps Opacity",icon='FACE_MAPS')         
   #MESH
    if bpy.context.mode == 'EDIT_MESH':
        if not tbb.tb_over_mesh_edit:
            box = layout.box()
            row = box.row(align= False)            
            row.prop(tbb, "tb_over_mesh_edit",text="Mesh Edit Mode",icon='OUTLINER_DATA_MESH')
        else:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, "tb_over_mesh_edit",text="",icon='OUTLINER_DATA_MESH')
            row.label(text="Mesh Edit Mode")
        #EDITMODE COLORS
            if bpy.context.tool_settings.mesh_select_mode[0] or bpy.context.tool_settings.mesh_select_mode[1] or bpy.context.tool_settings.mesh_select_mode[2] or sover.show_edges == True or sover.showfaces == True:        
                #VERTICES
                if bpy.context.tool_settings.mesh_select_mode[0]:
                    row = box.row(align= True)
                    row.label(icon='VERTEXSEL')
                    row.prop(context.preferences.themes['Default'].view_3d, "vertex", text= "")
                    row.prop(context.preferences.themes['Default'].view_3d, "vertex_select", text= "")
                    row.prop(context.preferences.themes['Default'].view_3d, "vertex_size", text= "")                    
                #EDGES
                if bpy.context.tool_settings.mesh_select_mode[1]:
                    row = box.row(align= True)
                    row.label(icon='EDGESEL')
                    row.prop(context.preferences.themes['Default'].view_3d, "wire_edit", text= "")
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_select", text= "")
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_width", text= "")
                #FACES
                row = box.row(align= True) 
                if not sover.show_faces:
                    row.prop(sover, "show_faces", text= "Faces",icon='FACESEL')
                    row.prop(context.preferences.themes['Default'].view_3d, "face", text= "")
                else:
                    row.prop(sover, "show_faces", text= "",icon='FACESEL')
                    row.prop(context.preferences.themes['Default'].view_3d, "face", text= "")
                    row.prop(context.preferences.themes['Default'].view_3d, "face_select", text= "")
                #FACECENTER
                if bpy.context.tool_settings.mesh_select_mode[2]:
                    row = box.row(align= True) 
                    row.prop(sover, "show_face_center", text= "Face Center",icon='SNAP_FACE_CENTER')
                    if sover.show_face_center:
                        row.prop(context.preferences.themes['Default'].view_3d, "face_dot", text= "")
                        row.prop(context.preferences.themes['Default'].view_3d, "facedot_size", text= "")   
              
       #Edge_type
        if not tbb.tb_over_mesh_edge:
            if tbb.tb_over_mesh_edit:
                box = layout.box()
                row = box.row(align= False)            
            row.prop(tbb, "tb_over_mesh_edge",text="Edge type",icon='EDGESEL')
        else:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, "tb_over_mesh_edge",text="",icon='EDGESEL')
            row.label(text="Edge type")             
            row = box.row(align= True)  
            row.prop(sover, "show_edge_seams", text= "Seams")
            row.prop(sover, "show_edge_crease", text= "Crease")
            row.prop(sover, "show_edge_sharp", text= "Sharp")
            row.prop(sover, "show_edge_bevel_weight", text= "Bevel")
            if sover.show_edge_seams == True or sover.show_edge_crease == True or sover.show_edge_sharp == True or sover.show_edge_bevel_weight == True:
                row = box.row(align= False)
                if sover.show_edge_seams == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_seam", text= "")
                else:
                    row.label(text= "      ")
                if sover.show_edge_crease == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_crease", text= "")
                else:
                    row.label(text= "      ")
                if sover.show_edge_sharp == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_sharp", text= "")
                else:
                    row.label(text= "      ")
                if sover.show_edge_bevel_weight == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "edge_bevel", text= "")
                else:
                    row.label(text= "      ")
       #Normals
        if not tbb.tb_over_mesh_normal:
            box = layout.box()
            row = box.row(align= False)            
            row.prop(tbb, "tb_over_mesh_normal",text="Display Normals",icon='ORIENTATION_NORMAL')
        else:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, "tb_over_mesh_normal",text="",icon='ORIENTATION_NORMAL')
            row.label(text="Display Normals")                      
            row = box.row(align= True)  
            row.prop(sover, "show_vertex_normals", text= "Vertex",icon='NORMALS_VERTEX')
            if sover.show_vertex_normals == True:
                row.prop(context.preferences.themes['Default'].view_3d, "vertex_normal", text= "")
            if sover.show_vertex_normals == True or sover.show_split_normals == True:
                row.separator()
            row.prop(sover, "show_split_normals", text= "Split",icon='NORMALS_VERTEX_FACE')
            if sover.show_split_normals == True:
                row.prop(context.preferences.themes['Default'].view_3d, "split_normal", text= "")
            if sover.show_split_normals == True or sover.show_face_normals == True:
                row.separator()
            row.prop(sover, "show_face_normals", text= "Face",icon='NORMALS_FACE')
            if sover.show_face_normals == True:
                row.prop(context.preferences.themes['Default'].view_3d, "normal", text= "")
            if sover.show_vertex_normals == True or sover.show_split_normals == True or sover.show_face_normals == True:
                row = box.row(align= True)
                if sover.use_normals_constant_screen_size == True:
                    row.prop(sover,"normals_constant_screen_size", text= "Lenghts")
                else:
                    row.prop(sover, "normals_length", text= "Lenghts")
                row.prop(sover,"use_normals_constant_screen_size",icon='DRIVER_DISTANCE',text="")
       #Excemption text
        if not tbb.tb_over_mesh_index:
            if tbb.tb_over_mesh_normal == True:
                box = layout.box()
                row = box.row(align= False)            
            row.prop(tbb, "tb_over_mesh_index",text="Index Number",icon='LINENUMBERS_ON')
        else:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, "tb_over_mesh_index",text="",icon='LINENUMBERS_ON')
            row.label(text="Index Number")  
            if sover.show_text == True:
              #Indices
                row = box.row(align= True)  
                row.prop(sover, "show_extra_indices", text= "Indices",icon='LINENUMBERS_ON')
                if sover.show_extra_indices == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "extra_face_angle", text= "")
               #Measure
                row = box.row(align= True)
                if sover.show_extra_edge_length == True or sover.show_extra_face_area == True:
                    row.label(text="",icon='DRIVER_DISTANCE')
                else:
                    row.label(text="Measure",icon='DRIVER_DISTANCE')
                row.prop(sover, "show_extra_edge_length", text= "",icon='EDGESEL')
                if sover.show_extra_edge_length == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "extra_edge_len", text= "")
                row.prop(sover, "show_extra_face_area", text= "",icon='FACESEL')
                if sover.show_extra_face_area == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "extra_face_area", text= "")
                row.separator()
                if sover.show_extra_edge_angle == True or sover.show_extra_face_area == True:
                    row.label(text="",icon='DRIVER_ROTATIONAL_DIFFERENCE')
                else:
                    row.label(text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')
                row.prop(sover, "show_extra_edge_angle", text= "",icon='MOD_EDGESPLIT')
                if sover.show_extra_edge_angle == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "extra_edge_angle", text= "")
                row.prop(sover, "show_extra_face_angle", text= "",icon='UV_FACESEL')
                if sover.show_extra_face_angle == True:
                    row.prop(context.preferences.themes['Default'].view_3d, "extra_face_angle", text= "")
            else:
                row = box.row(align= True)
                row.prop(sover, "show_text", text= "",icon='FILE_TEXT')
                row.label(text="Need to Visualize Text to Access")
                row = box.row(align= True)
                row.label(text="Indices",icon='LINENUMBERS_ON')
                row.label(text="Measure",icon='DRIVER_DISTANCE')
                row.label(text="Angles",icon='DRIVER_ROTATIONAL_DIFFERENCE')

   #Grease Pencil
    if bpy.context.object:    
        if bpy.context.active_object.type == 'GPENCIL':
            box = layout.box()
            row = box.row(align= True)  
            row.label(text="Grease Pencil Overlays",icon='OUTLINER_OB_GREASEPENCIL')
            row = box.row(align= True) 
            row.prop(sover, "use_gpencil_onion_skin", icon='ONIONSKIN_ON')
            row = box.row(align= True)
            if sover.use_gpencil_grid == True:
                split = box.split(factor=0.08, align=True)
                col = split.column(align=True)
                col.prop(sover, "use_gpencil_grid",icon='MESH_GRID')
                col = split.column(align=True)
                col.prop(sover, "gpencil_grid_opacity", text="" ,slider= True)
            elif sover.use_gpencil_grid == False:
                row.prop(sover, "use_gpencil_grid", icon='MESH_GRID')
            if sover.use_gpencil_fade_layers == True:
                split = box.split(factor=0.08, align=True)
                col = split.column(align=True)
                col.prop(sover, "use_gpencil_fade_layers",text="", icon='RENDERLAYERS')
                col = split.column(align=True)
                col.prop(sover, "gpencil_fade_layer",slider= True)
            elif sover.use_gpencil_fade_layers == False:
                row.prop(sover, "use_gpencil_fade_layers",icon='RENDERLAYERS')
            if sover.use_gpencil_fade_objects == True:
                split = box.split(factor=0.08, align=True)
                col = split.column(align=True)
                col.prop(sover, "use_gpencil_fade_objects", text= "",icon='IMAGE_BACKGROUND')
                col = split.column(align=True)
                col.prop(sover, "gpencil_fade_objects",text="Fade Object",slider= True)
            elif sover.use_gpencil_fade_objects == False:
                row.prop(sover, "use_gpencil_fade_objects", text= "Fade Object",icon='IMAGE_BACKGROUND')
        if bpy.context.mode == 'SCULPT_GPENCIL' or bpy.context.mode == 'WEIGHT_GPENCIL' or bpy.context.mode == 'EDIT_GPENCIL':
            row = box.row(align= True)  
            row.prop(sover, "use_gpencil_edit_lines", icon='OUTLINER_DATA_GREASEPENCIL')
            row.prop(sover, "use_gpencil_multiedit_line_only", icon='GP_MULTIFRAME_EDITING')
            row = box.row(align= True)  
            row.prop(sover, "vertex_opacity", text="Vertex Opacity" ,slider= True)
#SHADING
def tboverlayshading(context,box,row):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    sover = context.space_data.overlay
    if bpy.context.space_data.shading.type == 'MATERIAL':
        row.prop(sover, "show_look_dev", text= "",icon='MATERIAL')
    row = box.row(align= True)      
    row.prop(sover, "show_face_orientation", text= "Normals",icon='MOD_NORMALEDIT')        
 #SHADEREDITMESH      
    if bpy.context.mode != 'OBJECT':
    #MESH_ACTIVE_TRANSPARENCY
        row = box.row(align= True)
        if sover.show_fade_inactive:
            row.prop(sover, "show_fade_inactive", text= "",icon='MOD_MASK')
            row.prop(sover, "fade_inactive_alpha", text= "Inactive Transparency")
        else:
            row.prop(sover, "show_fade_inactive", text= "Show Fade Inactive",icon='MOD_MASK')
    #ANALICE_MESH
        if sover.show_statvis:
            row = box.row(align= True)
            row.prop(sover, "show_statvis", text= "Mesh_Analitics",icon='LIGHT_AREA')
            row.prop(context.scene.tool_settings.statvis, "type", text= "",icon='LIGHT_AREA')
            split = box.split(align=True)
            col = split.column(align=True)
            col.prop_enum(context.scene.tool_settings.statvis, "type", "OVERHANG", text="", icon='CON_FLOOR')
            col = split.column(align=True)
            col.prop_enum(context.scene.tool_settings.statvis, "type", "THICKNESS", text="", icon='MOD_THICKNESS')
            col = split.column(align=True)
            col.prop_enum(context.scene.tool_settings.statvis, "type", "INTERSECT", text="", icon='SELECT_INTERSECT')
            col = split.column(align=True)
            col.prop_enum(context.scene.tool_settings.statvis, "type", "DISTORT", text="", icon='MOD_NOISE')
            col = split.column(align=True)
            col.prop_enum(context.scene.tool_settings.statvis, "type", "SHARP", text="", icon='SHARPCURVE')
        #Overhang
            if context.scene.tool_settings.statvis.type == 'OVERHANG':
                row = box.row(align= True)
                row.prop(context.scene.tool_settings.statvis, "overhang_min", text= "Min")
                row.prop(context.scene.tool_settings.statvis, "overhang_max", text="Max")
                row.prop(context.scene.tool_settings.statvis,"overhang_axis", text="")
        #Thickness
            if context.scene.tool_settings.statvis.type == 'THICKNESS':
                row = box.row(align= True)
                row.prop(context.scene.tool_settings.statvis, "thickness_min", text= "Min")
                row.prop(context.scene.tool_settings.statvis, "thickness_max", text= "Max")
                row = box.row(align= True)
                row.prop(context.scene.tool_settings.statvis, "thickness_samples", text="Samples")  
        #Distord
            if context.scene.tool_settings.statvis.type == 'DISTORT':
                row = box.row(align= True)
                row.prop(context.scene.tool_settings.statvis, "distort_min", text= "Min")
                row.prop(context.scene.tool_settings.statvis, "distort_max", text="Max")
        #Sharpwireframe_color
            if context.scene.tool_settings.statvis.type == 'SHARP':
                row = box.row(align= True)
                row.prop(context.scene.tool_settings.statvis, "sharp_min", text= "Min")
                row.prop(context.scene.tool_settings.statvis, "sharp_max", text="Max")
        elif sover.show_statvis == False:
            row = box.row(align= True)
            row.prop(sover, "show_statvis", text= "Mesh Analitics",icon='LIGHT_AREA')
        if sover.show_statvis == True:
            row = box.row(align= True)
    #WEIGHT     
        if sover.show_weight == True:
            split = box.split(factor=0.5, align=True)
            col = split.column(align=True)
            col.prop(sover, "show_weight", text= "Weight",icon='MOD_VERTEX_WEIGHT')
            col = split.column(align=True)
            col.prop(context.scene.tool_settings, "vertex_group_user",text="")
        elif sover.show_weight == False:
            row = box.row(align= True)
            row.prop(sover, "show_weight", text= "Weight",icon='MOD_VERTEX_WEIGHT')   
 
 #WIREFRAME
    if sover.show_wireframes == True:
        split = box.split(factor=0.08, align=True)
        col = split.column(align=True)       
        col.prop(sover, "show_wireframes", text= "",icon='MOD_WIREFRAME')
        col = split.column(align=True)
        col.prop(sover,"wireframe_threshold")
        col = split.column(align=True)
        col.prop(sover,"wireframe_opacity")
        col = split.column(align=True)
        col.prop(context.preferences.themes['Default'].view_3d, "wire", text= "")
    elif sover.show_wireframes == False:
        row = box.row(align= True)
        row.prop(sover, "show_wireframes", text= "Wireframes",icon='MOD_WIREFRAME')
    if bpy.context.active_object.mode == 'EDIT_MESH':
        if sover.show_wireframes == True:
            col = split.column(factor=0.02,align=True)
            col.prop(sover, "show_occlude_wire", text= "",icon='MESH_CUBE')
        else:
            row.prop(sover, "show_occlude_wire", text= "Hidden Wre",icon='MESH_CUBE')
    if bpy.context.mode == 'PAINT_VERTEX' or bpy.context.mode == 'PAINT_WEIGHT':
        row.prop(sover, "show_paint_wire", text= "Paint Wire",icon='MOD_WIREFRAME')

#Motion_Tracking
def tboverlaymotiontracking(context,row,box):
    row.label(text="Motion Track")
    row = box.row(align= True)
    row.prop(context.space_data, "show_camera_path", text= "Camera Path",icon='CON_CAMERASOLVER')
    row.prop(context.space_data, "show_bundle_names", text= "Marker name",icon='MARKER')
    row = box.row(align= True)
    row.prop(context.space_data, "tracks_display_type",text="")
    row.prop(context.space_data, "tracks_display_size")    
#Grid
def tboverlaygrid(context,box):
    sover = context.space_data.overlay   
    row = box.row(align= True)
    row.prop(sover, "show_axis_x", text= "",icon='EVENT_X')
    row.prop(sover, "show_axis_y", text= "",icon='EVENT_Y')
    row.prop(sover, "show_axis_z", text= "",icon='EVENT_Z')
    row.separator()
    row.prop(sover, "show_floor", text= "Floor",icon='VIEW_PERSPECTIVE')
    row.prop(sover, "show_ortho_grid", text= "Grid",icon='VIEW_ORTHO')
    if sover.show_floor == True or sover.show_ortho_grid == True:
        row.prop(context.preferences.themes['Default'].view_3d, "grid", text= "")
        split = box.split(align=True)
        col = split.column(align=True)
        col.prop(sover, "grid_scale")
        if context.scene.unit_settings.system == 'NONE':
            col = split.column(align= True)
            col.prop(sover, "grid_subdivisions")
        row = box.row(align= True)
        row.prop(context.scene.unit_settings, "system",text="")
        row.prop(context.scene.unit_settings, "use_separate", text="", icon='LINENUMBERS_ON')
        row.prop(context.scene.unit_settings, "scale_length")      
#GENERAL_OVERLAYS
def overlaysgeneral(context,box):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    sover = context.space_data.overlay     
    #TEXT
    row = box.row(align= True)       
    if sover.show_text == True:
        row.prop(sover, "show_text", text= "",icon='FILE_TEXT')
        row.prop(sover, "show_stats", text= "",icon='LINENUMBERS_ON')                
        row.prop(context.preferences.themes['Default'].view_3d.space, "text_hi", text= "")
        row.separator()
    else:
        row.prop(sover, "show_text", text= "Text",icon='FILE_TEXT')
    #CURSOR
    row.separator() 
    row.prop(sover, "show_cursor", text= "",icon='PIVOT_CURSOR')
    row.separator()
    #EXTRAS
    if sover.show_extras == False:
        row.prop(sover, "show_extras", text= "Extras",icon='LIGHT_POINT')
    if sover.show_extras == True:
        row.separator()
        if tbb.tb_over_ex_col == False:
            row.prop(sover, "show_extras", text= "",icon='LIGHT_POINT') 
            row.prop(tbb, "tb_over_ex_col", text="",icon='COLOR')
        if tbb.tb_over_ex_col == True:
            row = box.row(align= True)
            row.prop(sover, "show_extras", text= "",icon='LIGHT_POINT') 
            row.prop(tbb, "tb_over_ex_col", text="",icon='COLOR')
            row.label(icon='CAMERA_DATA')
            row.prop(context.preferences.themes['Default'].view_3d, "camera", text= "")
            row.prop(sover, "show_light_colors", text= "",icon='LIGHT_POINT')
            row.prop(context.preferences.themes['Default'].view_3d, "light", text= "")
            row.label(icon='EMPTY_DATA')
            row.prop(context.preferences.themes['Default'].view_3d, "empty", text= "")
            row.label(icon='OUTLINER_DATA_SPEAKER')
            row.prop(context.preferences.themes['Default'].view_3d, "speaker", text= "")            
    #OUTLINE
    row = box.row(align= True)
    if sover.show_outline_selected == False:
        row.prop(sover, "show_outline_selected", text= "Outline",icon='MOD_SOLIDIFY')
    elif sover.show_outline_selected == True:
        row.prop(sover, "show_outline_selected", text= "",icon='MOD_SOLIDIFY')
        row.prop(context.preferences.themes['Default'].view_3d, "outline_width", text= "")
    #row = box.row(align= True)
    row.label(icon='OBJECT_DATA')
    row.prop(context.preferences.themes['Default'].view_3d, "object_active", text= "")
    row.label(icon='OBJECT_HIDDEN')
    row.prop(context.preferences.themes['Default'].view_3d, "object_selected", text= "")
    row = box.row(align= True)
    #ORIGINS
    row.prop(sover, "show_object_origins", text= "Origins",icon='DOT')
    if sover.show_object_origins == True:
        row.prop(sover, "show_object_origins_all", text= "All Origins",icon='LAYER_USED')
        row.prop(context.preferences.themes['Default'].view_3d, "object_origin_size", text= "")
    row = box.row(align= True)
    #BONES
    row.prop(sover, "show_bones", text= "Bone",icon='BONE_DATA')
    #SHOW_MOTION
    row.separator()
    row.prop(sover, "show_motion_paths", text= "Mothion Paths",icon='TRACKING')
    row.prop(sover, "show_relationship_lines", text= "Relation_Lines",icon='CON_TRACKTO')
    #MESH_RETOPOLOGY
    row = box.row(align= True)
    if not sover.show_retopology:
        row.prop(sover, "show_retopology",icon='MESH_ICOSPHERE')
    else:
        row.prop(sover, "show_retopology",text="",icon='MESH_ICOSPHERE')
        row.prop(sover, "retopology_offset")
        row.prop(context.preferences.themes['Default'].view_3d,"face_retopology",text="")
def overlaysgeonodes(context,box):
    sover = context.space_data.overlay  
    row = box.row(align= True)
    if sover.show_viewer_attribute:
        row.prop(sover, "show_viewer_attribute", text= "",icon='HIDE_OFF')
        row.prop(sover, "viewer_attribute_opacity")
        
    else:
        row.prop(sover, "show_viewer_attribute", text= "Show_viewer",icon='HIDE_OFF')


 #___________________________________

#___________________________________________
def tboverlaydraw(self, context):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    layout = self.layout
  #HEADER
    overlayheader(context, layout)
    if tbb.tb_over == False or tbb.tb_over_sha == False or tbb.tb_over_grid == False or context.space_data.show_reconstruction == False:  
        box = layout.box()   
        bow = box.box()
    if not tbb.tb_over:
        row = bow.row(align= False)            
        row.prop(tbb, "tb_over",text="General Overlays",icon='OVERLAY')
    if tbb.tb_over == True and tbb.tb_over_sha == False:
        box = layout.box()
        row = box.row()          
    if not tbb.tb_over_sha:
        row.prop(tbb, "tb_over_sha",text="Shading",icon='MATSHADERBALL')            
    if context.space_data.show_reconstruction == False:
        row = bow.row(align= False)
        row.prop(context.space_data, "show_reconstruction", text= "Motion Track",icon='CON_FOLLOWTRACK')
    if tbb.tb_over_grid == False and context.space_data.show_reconstruction == True:
        row = bow.row()
    if not tbb.tb_over_grid:
        row.prop(tbb, "tb_over_grid",text="Grid",icon='GRID') 
  #General_body     
    if tbb.tb_over:  
        box = layout.box()
        row = box.row(align= True)            
        row.prop(tbb, "tb_over",text="",icon='OVERLAY')
        row.label(text="General Overlays")           
        overlaysgeneral(context,box)
        box = layout.box()
        row = box.row(align= True)            
        row.prop(icon='GEOMETRY_NODES')
        row.label(text="Geometry Nodes")           
        overlaysgeonodes(context,box)
        
  #Overlay_shading
    if tbb.tb_over_sha:
        box = layout.box()
        row = box.row(align= True)            
        row.prop(tbb, "tb_over_sha",text="",icon='MATSHADERBALL')
        row.label(text="Shading")   
        tboverlayshading(context,box,row)
  #Grid 
    if tbb.tb_over_grid:
        box = layout.box()
        row = box.row(align= True)            
        row.prop(tbb, "tb_over_grid",text="",icon='GRID')
        row.label(text="Grid")   
        tboverlaygrid(context, box)     
  #Motion_Tracking
    if context.space_data.show_reconstruction == True:
        box = layout.box()  
        row = box.row(align= True)          
        row.prop(context.space_data, "show_reconstruction", text= "",icon='CON_FOLLOWTRACK') 
        tboverlaymotiontracking(context,row,box) 

def tboverlaydrawpop(self, context):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    layout = self.layout
    split = layout.split(align=True)
  #Header
    if bpy.context.mode in ['PAINT_VERTEX','PAINT_TEXTURE','PAINT_WEIGHT','POSE','EDIT_CURVE','EDIT_MESH','SCULPT']:
        layout = split.column(align=True)
        overlayheader (context, layout)
  #2                      
   #GENERERAL_BODY           
    layout = split.column(align=True)
    box = layout.box()
    box.label(text="Overlays",icon='OVERLAY')        
    overlaysgeneral(context,box)
    box = layout.box()
    box.label(text="Geometry Nodes",icon='GEOMETRY_NODES')
    overlaysgeonodes(context,box)
  #3 
   #OVERLAY_SHADING
    layout = split.column(align=True)   
    box = layout.box()
    row = box.row()
    row.label(text="Shading",icon='MATSHADERBALL')           
    tboverlayshading(context,box,row)
  #4  
    layout = split.column(align=True)   
    box = layout.box()
   #GRID
    box.label(text="Grid",icon='GRID')    
    tboverlaygrid(context, box)     
   #MOTION_TRACK
    box = layout.box()
    row = box.row(align= False)
    if context.space_data.show_reconstruction == False:
        row.prop(context.space_data, "show_reconstruction", text= "Motion Track",icon='CON_FOLLOWTRACK') 
    else:
        row.prop(context.space_data, "show_reconstruction", text= "",icon='CON_FOLLOWTRACK')   
        row.label(text="Morion Tracking")      
        tboverlaymotiontracking(context,row,box)

class TB_Overlay_UI_3D(bpy.types.Panel):
    bl_label = "Overlays"
    bl_idname = "TBPNL_PT_Set_Overlays"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='OVERLAY')        
    def draw(self, context):
        tboverlaydraw(self, context)       
class TB_Overlay_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tboverlaypopup"
    bl_label = "Overlays"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 1000)
    def draw(self, context):
        tboverlaydrawpop(self, context)
    def execute(self, context):
        return {'FINISHED'}

def tboverlayimgdraw(self, context):
    layout = self.layout
    wm = context.window_manager
    ob = context.object
    box = layout.box()
    row = box.row(align= True)  
    sover = context.space_data.overlay 
    sima = context.space_data
    uvedit = sima.uv_editor
    themeuv = context.preferences.themes['Default'].image_editor
    if bpy.context.active_object.type == 'MESH':
        if uvedit.show_stretch:
            row.prop(uvedit, "show_stretch", text="",icon='FACE_MAPS')
            row.separator()
            row.prop_enum(uvedit, "display_stretch_type","ANGLE", text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')
            row.prop_enum(uvedit, "display_stretch_type","AREA", text="Area",icon='LIGHT_AREA')
        else:
            row.prop(uvedit, "show_stretch", text="Streth",icon='FACE_MAPS')
        row.separator()
        row.prop(uvedit,"show_metadata",text="",icon='LINENUMBERS_ON')  
        row = box.row(align= True)       
        row.prop(uvedit, "uv_opacity")
        row.prop_enum(uvedit, "edge_display_type","OUTLINE",text="",icon='CUBE')
        row.prop_enum(uvedit, "edge_display_type","DASH",text="",icon='MOD_WIREFRAME')
        row.prop_enum(uvedit, "edge_display_type","WHITE",text="",icon='COLORSET_13_VEC')
        row.prop_enum(uvedit, "edge_display_type","BLACK",text="",icon='COLORSET_10_VEC')
        #VERTEX,EDGE,FACE
        row = box.row(align= True)  
        row.label(icon='VERTEXSEL')
        row.prop(themeuv, "vertex_size", text= "Size")
        row.prop(themeuv, "vertex", text= "")
        row.prop(themeuv, "vertex_select", text= "")
        row.separator()
        row.prop(uvedit,"show_modified_edges",text="Edges",icon='EDGESEL')     
        row.prop(themeuv,"edge_select",text="")
        row.separator()
        if uvedit.show_stretch == False:
            if uvedit.show_faces:
                row.prop(uvedit,"show_faces",text="",icon='FACESEL')
                row.prop(themeuv,"face",text="")
                row.prop(themeuv,"face_select",text="")
                row.prop(themeuv, "facedot_size", text= "Dot_Size")
            else:
                row.prop(uvedit,"show_faces",text="Show Faces",icon='FACESEL')
        row = box.row(align= True)          
        if sover.show_grid_background:
            row.prop(sover, "show_grid_background", text="",icon='MESH_GRID')
            row.separator()
            row.prop_enum(uvedit, "grid_shape_source","DYNAMIC",text="Dynamic")
            row.prop_enum(uvedit, "grid_shape_source","PIXEL",text="Pixel")
            row.prop_enum(uvedit, "grid_shape_source","FIXED",text="Fixed")
            if uvedit.gridshape_source == "FIXED":
                row.prop(uvedit, "custom_grid_subdivisions", text="Subdivisions")
        else:        
            row.prop(sover, "show_grid_background", text="Show Grid",icon='MESH_GRID')
        row = box.row(align= True)  
    else:
        row.prop(uvedit,"show_metadata",icon='LINENUMBERS_ON')  
    row.label(text="Tiles")
    row.prop(uvedit, "tile_grid_shape", text="")
class TB_Overlay_UI_IMG(bpy.types.Panel):
    bl_label = "Overlays Panel"
    bl_idname = "TBPNL_PT_Overlays_IMG"
    bl_space_type = 'IMAGE_EDITOR' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    def draw(self, context):
        tboverlayimgdraw(self, context)
class TB_Overlay_PoP_IMG(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tboverlayimgpopup"
    bl_label = "Overlays"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 700)
    def draw(self, context):
        tboverlayimgdraw(self, context)
    def execute(self, context):
        return {'FINISHED'}

def tboverlaynodesdraw(self, context):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    cntxdata = context.space_data
    overcntx = cntxdata.overlay

    layout = self.layout
    split = layout.split(align=True)
    box = split.box()
    row = box.row(align=True)
    if not overcntx.show_overlays:
        row.prop(overcntx, "show_overlays",icon='OVERLAY')
    else:
        row.prop(overcntx, "show_overlays",text="",icon='OVERLAY')
        row.separator()
        row.prop(overcntx, "show_wire_color",text="Color",icon='GRAPH')
        row.prop(overcntx, "show_context_path",text="Path",icon='FILE_TEXT')
        row.separator()
        row.prop(cntxdata, "show_annotation",text="",icon='GREASEPENCIL')
        if bpy.context.area.ui_type in {'ShaderNodeTree','CompositorNodeTree'}:
            split = layout.split(align=True)
            box = split.box()
            row = box.row(align=True)
            row.prop(overcntx, "show_previews",icon='IMAGE_DATA')
            if bpy.context.area.ui_type == 'ShaderNodeTree':
                if overcntx.show_previews == True:
                    row.separator()
                    row.prop_enum(overcntx,"preview_shape", "FLAT",text="Flat",icon='MATPLANE')            
                    row.prop_enum(overcntx,"preview_shape", "3D",text="3D",icon='MATSPHERE')                  
        if bpy.context.area.ui_type == 'GeometryNodeTree':
            split = layout.split(align=True)
            box = split.box()
            row = box.row(align=True)
            row.prop(overcntx, "show_timing",icon='TIME')
            row.separator()
            row.prop(overcntx, "show_named_attributes",text="Show_named",icon='PROPERTIES')
            
class TB_Overlay_NDS(bpy.types.Panel):
    bl_label = "Overlays Panel"
    bl_idname = "TBPNL_PT_Overlays_NDS"
    bl_space_type = 'NODE_EDITOR' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    def draw(self, context):
        tboverlaynodesdraw(self, context)
class TB_Overlay_NDS_PoP(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tboverlayndspopup"
    bl_label = "Overlays"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 700)
    def draw(self, context):
        tboverlaynodesdraw(self, context)
    def execute(self, context):
        return {'FINISHED'}
        