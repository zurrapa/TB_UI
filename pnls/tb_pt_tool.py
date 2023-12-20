import bpy
def tbtoolorientation(context,box):
    wm = context.window_manager
    tbb = wm.tb_wm_bool
    scntt = context.tool_settings
    scentt = context.scene.tool_settings 
    ob = bpy.context.object
    orient_slot = context.scene.transform_orientation_slots[0]

    row = box.row(align=False)                
    row.prop_with_popover(orient_slot,"type",text="",panel="VIEW3D_PT_transform_orientations",)                             
    row.prop(scntt, "transform_pivot_point",text="")
    if tbb.tb_obj_snap == False:
        row.prop(tbb,"tb_obj_snap",text="",icon='SNAP_ON')  
    if tbb.tb_obj_prop == False:
        row.prop(tbb,"tb_obj_prop",text="",icon='PROP_ON')
   #SNAP                              
    if tbb.tb_obj_snap:  
        bow = box.box()
        row = bow.row(align = True)   
        row.prop(tbb,"tb_obj_snap",text="",icon='HIDE_OFF')   
        row.separator()       
        if not scntt.use_snap:
            row.prop(scntt, "use_snap",text="Use_Snap",icon='SNAP_OFF')
        else:           
            row.prop(scntt, "use_snap",text="",icon='SNAP_OFF')
            row.separator()
            row.prop(scntt, "snap_elements",text="")
            row.separator()    
            row.prop(scentt,"use_snap_translate",text="",icon='CON_LOCLIMIT')                                                                    
            row.prop(scentt,"use_snap_rotate",text="",icon='CON_ROTLIMIT')                                                                    
            row.prop(scentt,"use_snap_scale",text="",icon='CON_SIZELIMIT')                                                                                                                                                             
            row = bow.row(align=True)          
            if scentt.snap_elements == {'INCREMENT'}:
                row.prop(scentt, "use_snap_grid_absolute",icon='MESH_GRID')
            if scentt.snap_elements != {'INCREMENT'}:
                row.prop_enum(scentt, "snap_target","CLOSEST",icon='SNAP_GRID')                                               
                row.prop_enum(scentt, "snap_target","CENTER",icon='PIVOT_INDIVIDUAL')                                               
                row.prop_enum(scentt, "snap_target","MEDIAN",icon='PIVOT_MEDIAN')                                               
                row.prop_enum(scentt, "snap_target","ACTIVE",icon='PIVOT_ACTIVE')    
                row = bow.row(align=False)                                                                                                                                                               
                row.prop(scentt,"use_snap_backface_culling",icon='FACESEL')
                row.prop(scentt,"use_snap_align_rotation",icon='CON_ROTLIKE')                    
                if ob.mode == 'EDIT':
                    row.prop(scentt,"use_snap_self",icon='MOD_UVPROJECT')
            if scentt.snap_elements == {'FACE'}:
                row.prop(scentt,"use_snap_project",icon='NORMALS_FACE')                                    
            if scentt.snap_elements == {'VOLUME'}:                          
                row.prop(scentt,"use_snap_peel_object",icon='OBJECT_DATA')                                                        
   #PROPORTIONAL      
    if tbb.tb_obj_prop:
        bow = box.box()
        row = bow.row(align = True)   
        row.prop(tbb,"tb_obj_prop",text="",icon='HIDE_OFF')   
        row.separator()       
        if ob.mode in ['OBJECT','EDIT']:
            if ob.mode == 'OBJECT':
                row.prop(scentt,"use_proportional_edit_objects",text="Proportional Edit",icon='PROP_OFF')
                if scentt.use_proportional_edit_objects:
                    propon = True
                else:
                    propon = False
            if ob.mode == 'EDIT':
                if scentt.use_proportional_connected:
                    iconprop = 'PROP_CON'
                elif scentt.use_proportional_projected:
                    iconprop = 'PROP_PROJECTED'
                else:
                    iconprop = 'PROP_ON'
                if scentt.use_proportional_edit:
                    propon = True
                    row.prop(scentt,"use_proportional_edit",text="",icon=iconprop)           
                else:
                    propon = False
                    row.prop(scentt,"use_proportional_edit",text="Proportional Edit",icon='PROP_OFF')
            if propon:
                row.separator()                    
                row.prop_enum(scentt,"proportional_edit_falloff","SMOOTH",text="",icon='SMOOTHCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","SPHERE",text="",icon='SPHERECURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","ROOT",text="",icon='ROOTCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","INVERSE_SQUARE",text="",icon='SMOOTHCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","SHARP",text="",icon='SHARPCURVE')                                                                                                             
                row.prop_enum(scentt,"proportional_edit_falloff","LINEAR",text="",icon='LINCURVE')                                                                                                                                 
                row.prop_enum(scentt,"proportional_edit_falloff","CONSTANT",text="",icon='NOCURVE')      
                row.prop_enum(scentt,"proportional_edit_falloff","RANDOM",text="",icon='RNDCURVE')                                                                                                                                                                                                                                        
                if ob.mode == 'EDIT':
                    row = bow.row(align=True)   
                    row.prop(scentt,"use_proportional_connected",text="Conected",icon='PROP_CON')
                    subrow = row.row()
                    subrow.active = not scentt.use_proportional_connected                                 
                    subrow.prop(scentt,"use_proportional_projected",text="Projected from View",icon='PROP_PROJECTED')                                                                                       
   #OPTION     
    cw = wm.tb_wm_bool.tb_obj_option
    cwt = "tb_obj_option"
    bow = box.box()
    row = bow.row(align=True)                   
    if cw == False:
        row.prop(wm.tb_wm_bool, cwt,text="Options",icon='OPTIONS')
    if cw == True:   
        row.prop(wm.tb_wm_bool, cwt,text="",icon='HIDE_OFF')
        row.separator()
        if ob.mode == 'OBJECT':
            row.prop(context.scene.tool_settings, "use_transform_data_origin", text= "Origins",icon='OBJECT_ORIGIN')
            row.prop(context.scene.tool_settings, "use_transform_pivot_point_align", text= "Locations",icon='EMPTY_ARROWS')
            row.prop(context.scene.tool_settings, "use_transform_skip_children", text= "Parents",icon='CON_CHILDOF')                                                               

def tbtoolbase(context,box):
    wm = context.window_manager
    scntt = context.tool_settings
    scentt = context.scene.tool_settings   
    ob = bpy.context.object
    row = box.row(align=False)                
    orient_slot = context.scene.transform_orientation_slots[0]
    row.prop_with_popover(orient_slot,"type",text="",panel="VIEW3D_PT_transform_orientations",)                             
    row.prop(scntt, "transform_pivot_point",text="")
    bow = box.box()
    row = bow.row(align=True)                               
    if not scntt.use_snap:
        row.prop(scntt, "use_snap",text="Snap",icon='SNAP_OFF')
    else:           
        row.prop(scntt, "use_snap",text="",icon='SNAP_OFF')
        row.separator()
        row.prop(scntt, "snap_elements",text="")
        row.separator()    
        row.prop(scentt,"use_snap_translate",text="",icon='CON_LOCLIMIT')                                                                    
        row.prop(scentt,"use_snap_rotate",text="",icon='CON_ROTLIMIT')                                                                    
        row.prop(scentt,"use_snap_scale",text="",icon='CON_SIZELIMIT')                                                                                                                                                             
        row = bow.row(align=True)          
        if scentt.snap_elements == {'INCREMENT'}:
            row.prop(scentt, "use_snap_grid_absolute",icon='MESH_GRID')
        if scentt.snap_elements != {'INCREMENT'}:
            row.prop_enum(scentt, "snap_target","CLOSEST",icon='SNAP_GRID')                                               
            row.prop_enum(scentt, "snap_target","CENTER",icon='PIVOT_INDIVIDUAL')                                               
            row.prop_enum(scentt, "snap_target","MEDIAN",icon='PIVOT_MEDIAN')                                               
            row.prop_enum(scentt, "snap_target","ACTIVE",icon='PIVOT_ACTIVE')    
            row = bow.row(align=False)                                                                                                                                                               
            row.prop(scentt,"use_snap_backface_culling",icon='FACESEL')
            row.prop(scentt,"use_snap_align_rotation",icon='CON_ROTLIKE')                    
            if ob.mode == 'EDIT':
                row.prop(scentt,"use_snap_self",icon='MOD_UVPROJECT')
        if scentt.snap_elements == {'FACE'}:
            row.prop(scentt,"use_snap_project",icon='NORMALS_FACE')                                    
        if scentt.snap_elements == {'VOLUME'}:                          
            row.prop(scentt,"use_snap_peel_object",icon='OBJECT_DATA')                                                        
    #PROPORTIONAL                                
    bow = box.box()
    row = bow.row(align = True)

    if ob.mode in ['OBJECT','EDIT']:
        if ob.mode == 'OBJECT':
            row.prop(scentt,"use_proportional_edit_objects",text="Proportional Edit",icon='PROP_OFF')
            if scentt.use_proportional_edit_objects:
                propon = True
            else:
                propon = False
        if ob.mode == 'EDIT':
            if scentt.use_proportional_connected:
                iconprop = 'PROP_CON'
            elif scentt.use_proportional_projected:
                iconprop = 'PROP_PROJECTED'
            else:
                iconprop = 'PROP_ON'
            if scentt.use_proportional_edit:
                propon = True
                row.prop(scentt,"use_proportional_edit",text="",icon=iconprop)           
            else:
                propon = False
                row.prop(scentt,"use_proportional_edit",text="Proportional Edit",icon='PROP_OFF')
        if propon:
            row.separator()                    
            row.prop_enum(scentt,"proportional_edit_falloff","SMOOTH",text="",icon='SMOOTHCURVE')                             
            row.prop_enum(scentt,"proportional_edit_falloff","SPHERE",text="",icon='SPHERECURVE')                             
            row.prop_enum(scentt,"proportional_edit_falloff","ROOT",text="",icon='ROOTCURVE')                             
            row.prop_enum(scentt,"proportional_edit_falloff","INVERSE_SQUARE",text="",icon='SMOOTHCURVE')                             
            row.prop_enum(scentt,"proportional_edit_falloff","SHARP",text="",icon='SHARPCURVE')                                                                                                             
            row.prop_enum(scentt,"proportional_edit_falloff","LINEAR",text="",icon='LINCURVE')                                                                                                                                 
            row.prop_enum(scentt,"proportional_edit_falloff","CONSTANT",text="",icon='NOCURVE')      
            row.prop_enum(scentt,"proportional_edit_falloff","RANDOM",text="",icon='RNDCURVE')                                                                                                                                                                                                                                        
            if ob.mode == 'EDIT':
                row = bow.row(align=True)   
                row.prop(scentt,"use_proportional_connected",text="Conected",icon='PROP_CON')
                subrow = row.row()
                subrow.active = not scentt.use_proportional_connected                                 
                subrow.prop(scentt,"use_proportional_projected",text="Projected from View",icon='PROP_PROJECTED')                                                                                       
    if ob.mode == 'OBJECT':
        #OPTION     
        cw = wm.tb_wm_bool.tb_obj_option
        cwt = "tb_obj_option"
        bow = box.box()
        row = bow.row(align=False)                   
        if cw == False:
            row.prop(wm.tb_wm_bool, cwt,text="Options",icon='OPTIONS')
        if cw == True:   
            row.prop(wm.tb_wm_bool, cwt,text="",icon='OPTIONS')
            row.prop(context.scene.tool_settings, "use_transform_data_origin", text= "Origins",icon='OBJECT_ORIGIN')
            row.prop(context.scene.tool_settings, "use_transform_pivot_point_align", text= "Locations",icon='EMPTY_ARROWS')
            row.prop(context.scene.tool_settings, "use_transform_skip_children", text= "Parents",icon='CON_CHILDOF')                                                               

def tbmesheditclean(context,box):
    wm = context.window_manager
    tbb = wm.tb_wm_bool
    row = box.row(align=True)               
    if not tbb.tb_mesh_clean:
        row.prop(tbb,"tb_mesh_clean",text="Clean Mesh",icon_value=bpy.types.Scene.tb_pnl_icons["tbi_clean"].icon_id)
    else:
        box = box.box()
        row = box.row(align=True) 
        row.prop(tbb,"tb_mesh_clean",text="",icon='HIDE_OFF')
        row.label(text="Clean Mesh",icon_value=bpy.types.Scene.tb_pnl_icons["tbi_clean"].icon_id)
        row = box.row(align=True) 
        row.operator("mesh.delete_loose",icon='STICKY_UVS_DISABLE')
        row.separator()
        row.operator("mesh.decimate",text="Decimate",icon='MOD_DECIM')                
        row.operator("mesh.dissolve_degenerate",text="Dissolve",icon='MOD_TRIANGULATE')                                
        row = box.row(align=False)                
        row.operator("mesh.remove_doubles",text="Merge by Distance",icon='DRIVER_DISTANCE')                                                
        row.operator("mesh.fill_holes",text="Fill Holes",icon='CLIPUV_DEHLT')                                                                
        row.operator("mesh.face_make_planar",text="Planar",icon='LIGHTPROBE_PLANAR')                                                
        if bpy.context.tool_settings.mesh_select_mode[0]:
            row = box.row(align=True)                    
            row.label(icon='VERTEXSEL')         
            row.operator("mesh.vertices_smooth",icon='MOD_SMOOTH')           
            row.operator("mesh.vertices_smooth",icon='SHARPCURVE')    
        if bpy.context.tool_settings.mesh_select_mode[1]:
            row = box.row(align=True)     
            row.label(icon='EDGESEL')                                                       
            row.operator("mesh.extrude_edges_move",text="",icon='EMPTY_SINGLE_ARROW')                                               
            row.separator()
            row.operator("mesh.delete_loose",icon='STICKY_UVS_DISABLE')                    
        if bpy.context.tool_settings.mesh_select_mode[2]:              
            row = box.row(align=True)
            row.label(icon='FACESEL')                   
            row.operator("mesh.extrude_faces_move",text="",icon='EMPTY_SINGLE_ARROW')                                                                                                   
            row.separator()                           
            row.operator("mesh.poke",icon='X')                                      
            row.separator()                           
            row.operator("mesh.faces_shade_smooth",icon='MOD_SMOOTH')   
            row.operator("mesh.faces_shade_flat",icon='SHARPCURVE')                       
        if bpy.context.scene.tool_settings.use_mesh_automerge == False:
            row = box.row(align=True)
            row.prop(context.scene.tool_settings,"use_mesh_automerge")
        if bpy.context.scene.tool_settings.use_mesh_automerge == True:
            bow = box.box()
            row = bow.row(align=True)
            row.prop(context.scene.tool_settings,"use_mesh_automerge",text="")                                                
            row.prop(context.scene.tool_settings,"double_threshold",text="")                                                                                                
            row.prop(context.scene.tool_settings,"use_mesh_automerge_and_split",text="",icon='MOD_EDGESPLIT')                                                
        row = box.row(align=True)
        row.operator("mesh.select_non_manifold()",text="Non_manifold")
        row.separator()
        row.operator("mesh.select_face_by_sides(number=3)",text="3")
        row.operator("mesh.select_face_by_sides(number=5)",text="5")

def tbtooltexturetexture(context,box,split):
    ob = bpy.context.object
    settings = context.tool_settings.image_paint
    row = box.row(align=True)
    row.label(icon='TEXTURE',text="Slo ts")
    row.prop_enum(settings, "mode", "IMAGE",text="Image",icon='IMAGE')
    row.prop_enum(settings, "mode", "MATERIAL",text="Material",icon='MATERIAL')
    if settings.mode == 'MATERIAL':
        if len(ob.material_slots) > 1:
            box.template_list("MATERIAL_UL_matslots", "layers",
                                    ob, "material_slots",
                                    ob, "active_material_index", rows=2)
        mat = ob.active_material
        if mat and mat.texture_paint_images:
            row = box.row()
            row.template_list("TEXTURE_UL_texpaintslots", "",
                                mat, "texture_paint_images",
                                mat, "paint_active_slot", rows=2)
            if mat.texture_paint_slots:
                slot = mat.texture_paint_slots[mat.paint_active_slot]
            else:
                slot = None
            have_image = slot is not None
        else:
            row = box.row()
            boe = row.box()
            boe.label(text="No Textures")
            have_image = False
        sub = row.column(align=True)
        sub.operator_menu_enum("paint.add_texture_paint_slot", "type", icon='ADD', text="")
    elif settings.mode == 'IMAGE':
        mesh = ob.data
        uv_text = mesh.uv_layers.active.name if mesh.uv_layers.active else ""
        box.template_ID(settings, "canvas", new="image.new", open="image.open")
        have_image = settings.canvas is not None
        if have_image:
            row = box.row(align=True)
            row.prop(settings, "interpolation", text="")
            if settings.missing_uvs:
                row.operator("paint.add_simple_uvs", icon='ADD', text="Add UVs")                          
            else:
                row.menu("VIEW3D_MT_tools_projectpaint_uvlayer", text=uv_text, translate=False)
    if have_image:
        if settings.missing_uvs:
            box.label(text="UV Map Needed", icon='INFO')
            box.operator("paint.add_simple_uvs", icon='ADD', text="Add Simple UVs")
        if have_image:
            row.operator("image.save_all_modified", text="", icon='FILE_TICK')
def tbtooltexture(context,box,split):
    wm = bpy.context.window_manager
    ob = context.active_object
    mesh = ob.data
    paint = context.tool_settings.image_paint
    settings = context.tool_settings.image_paint
    brush = settings.brush
    bow = box.box()                
    row = bow.row(align=True)
    row.column().template_ID(settings, "brush", new="brush.add")
    colt = box.row() 
    splitt = colt.split() 
    boxt = splitt.column().box()
    if brush is None:
        boxt.prop(brush, "blend", text="") 
    if brush is not None:
        
        if brush is not None:
            row = boxt.row(align=True)
            if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_size == False:
                row.prop(context.scene.tool_settings.image_paint.brush,"size",slider=True)
            if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_size == True:
                row.prop(context.scene.tool_settings.unified_paint_settings,"size",slider=True)
            row.prop(context.scene.tool_settings.image_paint.brush,"use_pressure_size",text="")
            row.prop(context.scene.tool_settings.unified_paint_settings,"use_unified_size",icon='WORLD',text="")
            row = boxt.row(align=True)
            if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_strength == False:
                row.prop(context.scene.tool_settings.image_paint.brush,"strength")                    
            if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_strength == True:                    
                row.prop(context.scene.tool_settings.unified_paint_settings,"strength")
            row.prop(context.scene.tool_settings.image_paint.brush,"use_pressure_strength",text="")
            row.prop(context.scene.tool_settings.unified_paint_settings,"use_unified_strength",icon='WORLD',text="")                                   
            #Adaptative
            mode = ob.mode
            row = boxt.row(align=True)
            row.prop(brush, "use_alpha",text="Alpha",icon='IMAGE_RGB_ALPHA')
            row.prop(brush, "use_accumulate",text="Accumulate",icon='LIBRARY_DATA_OVERRIDE')
            row.prop(brush, "use_frontface", text="Front Faces Only",icon='VERTEXSEL')
            if brush.image_tool == 'SOFTEN':
                row.prop(brush, "blur_mode",text="")
                boxt.row().prop(brush, "direction", expand=True)
                boxt.prop(brush, "sharp_threshold")
                if mode == 'PAINT_2D':
                    boxt.prop(brush, "blur_kernel_radius")
            elif brush.image_tool == 'MASK':
                boxt.prop(brush, "weight", text="Mask Value", slider=True)   
        boxt = box.box()                       
        row.prop(brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
        if brush.use_custom_icon:
            box.prop(brush, "icon_filepath", text="")
        row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")
        boxt.prop(brush, "blend", text="")                    
        #COLOR       
        ups = context.scene.tool_settings.unified_paint_settings
        row = boxt.row(align=True)  
        row.prop_enum(brush, "color_type", "COLOR",icon='COLOR')
        row.prop_enum(brush, "color_type", "GRADIENT",icon='NODE_TEXTURE',text='Gradient')
        if brush.color_type == 'COLOR':
            row = boxt.row(align=True)
            row.prop(brush, "color",text="")
            row.prop(brush, "secondary_color",text="")
            row.separator()
            row.prop(brush, "strenght",text="")                
            row.operator("paint.brush_colors_flip", icon='FILE_REFRESH', text="", emboss=False)
            row.prop(ups, "use_unified_color", text="", icon='WORLD')               
        #Gradient
        elif brush.color_type == 'GRADIENT':
            boxt.prop(brush, "gradient_stroke_mode", text="")
            boxt.template_color_ramp(brush, "gradient", expand=True)
        #Palette
        cw = wm.tb_wm_bool.tb_brush_palette
        cwt = "tb_brush_palette"
        if cw == False:
            row.prop(wm.tb_wm_bool, cwt,text="",icon='RESTRICT_COLOR_OFF')
        if cw == True:   
            row.prop(wm.tb_wm_bool, cwt,text="",icon='COLOR')                                          
            boxt.template_ID(settings, "palette", new="palette.new")
            if settings.palette:
                boxt.template_palette(settings, "palette", color=True)
def tbtoolsculpt(context,box,split):
    wm = bpy.context.window_manager
    tool_settings = context.tool_settings
    dyno = context.sculpt_object.use_dynamic_topology_sculpting
    sculpt = tool_settings.sculpt
    brush = bpy.context.tool_settings.sculpt.brush
    ts = bpy.context.tool_settings.sculpt
    st = brush.sculpt_tool       
   #Dyntopo
    #box = box.box()
    if st == 'PAINT' or st == 'MASK' or st == 'TOPOLOGY' or st == 'CLOTH' or st == 'DRAW_FACE_SETS' or st == 'DRAW_SHARP' or st == 'LAYER ' or st == 'SMOOTH' or st == 'GRAB' or st == 'ELASTIC_DEFORM' or st == 'SNAKE_HOOK' or st == 'CLAY_THUMB' or st == 'POSE' or st == 'NUDGE' or st == 'ROTATE':
        row = box.row(align=True)                                                            
        row.label(icon='VIEW_ORTHO',text="Tool not compatible with dyntopo")                        
    else:
        if dyno == False:
            row = box.row(align=True)                                        
            row.operator("sculpt.dynamic_topology_toggle",icon='VIEW_ORTHO',text="Dyntopo")
        if dyno == True:
            row = box.row(align=True)                    
            row.operator("sculpt.dynamic_topology_toggle",icon='VIEW_ORTHO',text="")                
            if sculpt.detail_type_method in {'CONSTANT', 'MANUAL'}:
                row.prop(sculpt, "constant_detail_resolution")
                props = row.operator("sculpt.sample_detail_size", text="", icon='EYEDROPPER')
                props.mode = 'DYNTOPO'
            elif (sculpt.detail_type_method == 'BRUSH'):
                row.prop(sculpt, "detail_percent")
                row.prop(sculpt, "use_smooth_shading",text="",icon='MOD_SMOOTH')                               
            else:
                row.prop(sculpt, "detail_size")
                row.prop(sculpt, "use_smooth_shading",text="",icon='MOD_SMOOTH')   
            if sculpt.detail_type_method in {'CONSTANT', 'MANUAL'}:
                row.operator("sculpt.detail_flood_fill",icon='FILE_REFRESH',text="")
            row = box.row(align=True)                                                
            row.prop(sculpt, "detail_refine_method", text="")
            row.prop(sculpt, "detail_type_method", text="")
   #Sculpt_BRUSH        
    box = box.box()
    row = box.row(align=True)
    row.column().template_ID(ts, "brush", new="brush.add")
    ups = context.tool_settings.unified_paint_settings
    colt = box.row() 
    splitt = colt.split()
    boxt = splitt.column().box()                    
    if ts.brush is not None:
        if ts.brush.use_custom_icon:
            row.prop(ts.brush, "icon_filepath", text="")
            row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")                        
        row.prop(ts.brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")                                                                       
   #BURSH                                       
    if st == 'MASK':
        row = boxt.row(align=True)
        row.prop_enum(brush,"mask_tool","DRAW")                            
        row.prop_enum(brush,"mask_tool","SMOOTH") 
        if brush.mask_tool == 'DRAW':
            row = boxt.row(align=True)    
            row.prop_enum(brush,"direction","ADD",icon='ADD')                    
            row.prop_enum(brush,"direction","SUBTRACT",icon='REMOVE')                                                                                 
    if st == 'CLOTH':
        row = boxt.row(align=True)
        row.prop(brush,"cloth_deform_type",text="")  
        row.prop(brush,"cloth_force_falloff_type",text="")                                        
    if st == 'DRAW' or st == 'DRAW_SHARP' or st == 'CLAY' or st == 'CLAY_STRIPS' or st == 'LAYER' or st == 'BLOB' or st == 'CREASE': 
        row = boxt.row(align=True)    
        row.prop_enum(brush,"direction","ADD",icon='ADD')                    
        row.prop_enum(brush,"direction","SUBTRACT",icon='REMOVE')                                            
    if st == 'INFLATE':
        row = boxt.row(align=True)
        row.prop_enum(brush,"direction","INFLATE",icon='ADD')
        row.prop_enum(brush,"direction","DEFLATE",icon='REMOVE')                        
    if st == 'FLATTEN':
        row = boxt.row(align=True)
        row.prop_enum(brush,"direction","CONTRAST",icon='ADD')
        row.prop_enum(brush,"direction","FLATTEN",icon='REMOVE')
    if st == 'FILL':
        row = boxt.row(align=True)
        row.prop_enum(brush,"direction","FILL",icon='ADD')
        row.prop_enum(brush,"direction","DEEPEN",icon='REMOVE')                            
    if st == 'SCRAPE':
        row = boxt.row(align=True)
        row.prop_enum(brush,"direction","SCRAPE",icon='ADD')
        row.prop_enum(brush,"direction","PEAKS",icon='REMOVE') 
    if st == 'PINCH':
        row = boxt.row(align=True)
        row.prop_enum(brush,"direction","MAGNIFY",icon='ADD')
        row.prop_enum(brush,"direction","PINCH",icon='REMOVE')
    if st == 'SMOOTH':
        row = boxt.row(align=True)
        row.prop_enum(brush,"smooth_deform_type","SURFACE")
        row.prop_enum(brush,"smooth_deform_type","LAPLACIAN")                            
    if st == 'FILL' or st == 'SCRAPE':                                             
        row.prop(brush,"invert_to_scrape_fill",icon='ARROW_LEFTRIGHT',text="")
    if st == 'GRAB':
        row = boxt.row(align=True)                            
        row.prop(brush,"use_grab_active_vertex",icon='VERTEXSEL')
    if st == 'ELASTIC_DEFORM':
        row = boxt.row(align=True)                            
        row.prop(brush,"elastic_deform_type",icon='SCULPTMODE_HLT',text="")                                                                                     
    if st == 'MULTIPLANE_SCRAPE':
        row = boxt.row(align=True)
        row.prop(brush,"use_multiplane_scrape_dynamic",icon='UV_SYNC_SELECT')                                                            
        row.prop(brush,"show_multiplane_scrape_planes_preview",icon='BRUSH_DATA')                                                                                        
    if st == 'POSE':
        row = boxt.row(align=True)
        row.prop_enum(brush,"pose_deform_type","ROTATE_TWIST",icon='CON_ROTLIMIT')                            
        row.prop_enum(brush,"pose_deform_type","SCALE_TRANSLATE",icon='CON_SIZELIMIT')                            
        row.prop_enum(brush,"pose_deform_type","SQUASH_STRETCH",icon='CON_SAMEVOL')
        row = boxt.row(align=True)
        row.prop_enum(brush,"pose_origin_type","TOPOLOGY",icon='MESH_ICOSPHERE')                            
        row.prop_enum(brush,"pose_origin_type","FACE_SETS",icon='FACE_MAPS')                            
        row.prop_enum(brush,"pose_origin_type","FACE_SETB_FK",icon='CON_KINEMATIC')                            
    if st == 'PAINT':
        row = boxt.row(align=True)
        row.label(icon='COLOR')
        row.prop(brush,"color",text="")                                                                            
        row.prop(brush,"blend",text="")                        
    #Directions
    row = boxt.row(align=True)                                             
    if bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size == 'VIEW':
        if ups.use_unified_size == True:
            row.prop(ups,"size", slider=True)                             
        else:
            row.prop(brush,"size", slider=True) 
        row.prop(brush, "use_pressure_size", text="")                                          
        row.prop(ups,"use_unified_size", slider=True,text="",icon='BRUSHES_ALL')           
    if bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size == 'SCENE':                                                                 
        if ups.use_unified_size == True:
            row.prop(ups,"unprojected_radius", slider=True,text="Radius")                                                            
        else:                            
            row.prop(brush,"unprojected_radius", slider=True,text="Radius")      
        row.prop(brush, "use_pressure_size", text="")                                          
        row.prop(ups,"use_unified_size", slider=True,text="",icon='BRUSHES_ALL')        
    row.prop_enum(ups, "use_locked_size","VIEW",icon='HIDE_OFF',text="")
    row.prop_enum(ups, "use_locked_size","SCENE",icon='SCENE_DATA',text="")   
    row = boxt.row(align=True) 
    boxt = box.box()                                        
    if ups.use_unified_strength == True: 
        row.prop(ups,"strength", slider=True,text="Strenght")                                                                                                                              
    else:
        row.prop(brush,"strength", slider=True,text="Strenght")                                                                                                                                                          
    row.prop(brush,"use_pressure_strength",text="")    
    row.prop(ups,"use_unified_strength",icon='BRUSHES_ALL',text="")                                                                                                                           
    #Normal Rad
    row = boxt.row(align=True)
    row.label(icon='SNAP_NORMAL')
    row.prop(brush, "normal_radius_factor", slider=True)                       
    #Hardness
    row = boxt.row(align=True)                        
    row.label(icon='ALIASED')
    row.prop(brush, "hardness", slider=True)
    #Autosmooth
    if st != 'SMOOTH' and st != 'MASK':
        row = boxt.row(align=True)                        
        row.label(icon='ANTIALIASED')
        row.prop(brush, "auto_smooth_factor", slider=True)                                                                       
        row.prop(brush, "use_inverse_smooth_pressure",text="")
    if st == 'CLAY' or st == 'CLAY_STRIPS' or st == 'CLAY_THUMB' or st == 'FLATTEN' or st == 'SCRAPE' or st == 'FILL':
        row = boxt.row(align=True)       
        row.label(icon='NORMALS_FACE')                         
        row.prop(brush, "plane_offset", slider=True)
        row.prop(brush, "use_offset_pressure", text="")                            
        row = boxt.row(align=True)       
        if brush.use_plane_trim == False:
            row.prop(brush, "use_plane_trim",icon='HOLDOUT_ON')                                                                                                                                                                                                                                                                                                          
        else:
            row.prop(brush, "use_plane_trim", text="",icon='HOLDOUT_ON')                                                                                                                                                                                                                                                                                                                                      
            row.prop(brush, "plane_trim")
    if st == 'CLAY_STRIPS':
        row = boxt.row(align=True)     
        row.label(icon='SMOOTHCURVE')                                                                                                                                                                                                  
        row.prop(brush, "tip_roundness") 
    if st == 'BLOB' or st == 'CREASE' or st == 'SNAKE_HOOK':
        if st == 'BLOB' or st == 'SNAKE_HOOK':
            stt = "Magnify"
            sti = 'SPHERECURVE'
        if st == 'CREASE':
            stt = "Pinch"
            sti = 'SHARPCURVE'
        row = boxt.row(align=True)     
        row.label(icon=sti)                                                                                                                                                                                                  
        row.prop(brush, "crease_pinch_factor",text = stt)                                                                             
    if st == 'SNAKE_HOOK':
            row = boxt.row(align=True)
            row.label(icon='BRUSH_DATA')                                                                                                                                                                                                                                  
            row.prop(brush, "rake_factor")
    if st == 'SMOOTH':
        if brush.smooth_deform_type == 'SURFACE':
            row = boxt.row(align=True)
            row.label(icon='CON_SAMEVOL')                                                                                                                                                                                                                                  
            row.prop(brush, "surface_smooth_shape_preservation")
            row.prop(brush, "surface_smooth_iterations")                                                                
            row = boxt.row(align=True)
            row.label(icon='VERTEXSEL')                                                                                                                                                                                                                                       
            row.prop(brush, "surface_smooth_current_vertex")
            row = boxt.row(align=True)                                                                                         
    if st == 'LAYER':                 
        row = boxt.row(align=True)     
        row.label(icon='CON_SAMEVOL')                                                                                                                                                                                                  
        row.prop(brush, "height")    
        row = boxt.row(align=True)     
        row.prop(brush,"use_persistent",icon='NOCURVE')
        row.operator("sculpt.set_persistent_base",text="Set Base")      
    if st == 'FILL' or st == 'SCRAPE':                 
        row = boxt.row(align=True)     
        row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                                                                                                                                  
        row.prop(brush, "area_radius_factor")
    if st == 'MULTIPLANE_SCRAPE':                 
        row = boxt.row(align=True)     
        row.label(icon='NORMALS_FACE')                                                                                                                                                                                                  
        row.prop(brush, "multiplane_scrape_angle")
    if st == 'ELASTIC_DEFORM':                                                    
        row = boxt.row(align=True)     
        row.label(icon='NORMALS_FACE')                                                                                                                                                                                                  
        row.prop(brush, "normal_weight")
        row = boxt.row(align=True)     
        row.label(icon='FILE_VOLUME')                                                                                                                                                                                                  
        row.prop(brush, "elastic_deform_volume_preservation")
    if st == 'POSE':
        row = boxt.row(align=True)
        row.label(icon='OBJECT_ORIGIN')  
        row.prop(brush, "pose_offset")
        row.prop(brush,"use_pose_ik_anchored",text="",icon='CON_KINEMATIC')
        row = boxt.row(align=True)
        row.label(icon='MOD_SMOOTH')  
        row.prop(brush, "pose_smooth_iterations")
    if st == 'CLOTH':
        row = boxt.row(align=True)
        row.prop(brush,"cloth_sim_limit",text="Limit")                                                       
        row.prop(brush,"cloth_sim_falloff",text="Falloff")
        row = boxt.row(align=True)                            
        row.prop(brush,"cloth_mass",text="Mass")                                                       
        row.prop(brush,"cloth_damping",text="Damping") 
    if st == 'PAINT':   
        row = boxt.row(align=True)  
        row.label(icon='CON_FOLLOWPATH')                                                  
        row.prop(brush,"flow",slider=True)
        row.prop(brush,"density",slider=True)
        row = boxt.row(align=True)        
        row.label(icon='WPAINT_HLT')                                                                    
        row.prop(brush,"wet_mix",slider=True)
        row.prop(brush,"wet_persistence",slider=True)
        row = boxt.row(align=True)             
        row.label(icon='CON_SIZELIMIT')                                                                                       
        row.prop(brush,"tip_scale_x",slider=True)
        row.label(icon='SMOOTHCURVE')
        row.prop(brush,"tip_roundness",slider=True)
def tbtoolsculpttxtr(context,box,split):
    wm = bpy.context.window_manager
    tool_settings = context.tool_settings
    sculpt = tool_settings.sculpt

def tbtooltexturetextures(context,box,split): 
    wm = bpy.context.window_manager   
    ob = context.active_object
    mesh = ob.data
    paint = context.tool_settings.image_paint
    ipaint = context.tool_settings.image_paint    
    settings = context.tool_settings.image_paint
    pb = settings.brush
    ups = context.scene.tool_settings.unified_paint_settings
    mode = ob.mode
    settings = bpy.context.tool_settings.image_paint
    bow = box.box()                   
    row = bow.row(align=True)
    row.template_ID(pb, "texture", new="texture.new")
   #TEXTURE 
    if pb.texture:
        cw = wm.tb_wm_bool.tb_paint_txtr
        cwt = "tb_paint_txtr"
        if cw == False:
            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
        if cw == True:       
            row = bow.row(align=True)
            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
            row = bow.row(align=True)                        
            row.prop(pb.texture_slot,"map_mode",text="")
            if pb.texture_slot.map_mode in ['TILED','VIEW_PLANE','RANDOM']:                   
                row = bow.row(align=True)
                row.label(text="Angle",icon='CON_ROTLIMIT')
                row.prop(pb.texture_slot,"angle",text="")                   
            if pb.texture_slot.map_mode in ['VIEW_PLANE','RANDOM']:
                row.prop(pb.texture_slot,"use_rake",text="",icon='TRACKING')
                row.prop(pb.texture_slot,"use_random",text="",icon='MOD_NOISE')
            if pb.texture_slot.map_mode == 'STENCIL':                                       
                row.prop(brush,"texture_overlay_alpha")
                row.prop(brush,"use_primary_overlay_override",icon='BRUSH_DATA',text="")              
                row = bow.row(align=True)
                row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')                            
            split = bow.split(align=False)
            col = split.column(align=True)
            col.label(text="Offset",icon='CON_LOCLIMIT')                  
            col.prop(pb.texture_slot,"offset",text="")             
            col = split.column(align=True)
            col.label(text="Scale",icon='CON_SIZELIMIT')  
            col.prop(pb.texture_slot,"scale",text="")
   #MASK_TEXTURE
    bow = box.box()                                  
    row = bow.row(align=True)
    if bpy.context.scene.tool_settings.image_paint.use_stencil_layer == False:
        row.prop(ipaint, "use_stencil_layer", text="",icon='MOD_MASK')
    else:
        row.label(icon='MOD_MASK')
    row.template_ID(pb, "mask_texture", new="texture.new")
    if pb.mask_texture:
        cw = wm.tb_wm_bool.tb_paint_mask_txtr
        cwt = "tb_paint_mask_txtr"
        if cw == False:
            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
        if cw == True:       
            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                               
            row = bow.row(align=True)
            row.prop(pb.mask_texture_slot,"mask_map_mode",text="")
            if pb.mask_texture_slot.mask_map_mode == 'TILED' or pb.mask_texture_slot.mask_map_mode == 'VIEW_PLANE' or pb.mask_texture_slot.mask_map_mode == 'RANDOM':                   
                row = bow.row(align=True)
                row.label(text="Angle",icon='CON_ROTLIMIT')
                row.prop(pb.mask_texture_slot,"angle",text="")                   
            if pb.mask_texture_slot.mask_map_mode == 'VIEW_PLANE' or pb.mask_texture_slot.mask_map_mode == 'RANDOM':
                row.prop(brush.mask_texture_slot,"use_rake",text="",icon='TRACKING')
                row.prop(brush.mask_texture_slot,"use_random",text="",icon='MOD_NOISE')
            if pb.mask_texture_slot.mask_map_mode == 'STENCIL':
                row.prop(brush,"mask_overlay_alpha")
                row.prop(brush,"use_secondary_overlay_override",icon='BRUSH_DATA',text="")                                                                 
                row = bow.row(align=True)
                row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')                             
            row = bow.row(align=True)                             
            row.prop(pb,"use_pressure_masking",text="")                
            split = bow.split(align=False)
            col = split.column(align=True)
            col.label(text="Offset",icon='CON_LOCLIMIT')                  
            col.prop(pb.mask_texture_slot,"offset",text="")             
            col = split.column(align=True)
            col.label(text="Scale",icon='CON_SIZELIMIT')  
            col.prop(pb.mask_texture_slot,"scale",text="")                                 
    if bpy.context.scene.tool_settings.image_paint.use_stencil_layer == True:
        row = bow.row(align=True)
        row.prop(ipaint, "use_stencil_layer", text="",icon='MOD_MASK')
        row.prop(ipaint, "stencil_color", text="")
        row.prop(ipaint, "invert_stencil", text="", icon='IMAGE_ALPHA')
        bow.template_ID(ipaint, "stencil_image", new="image.new", open="image.open")
        stencil_text = mesh.uv_layer_stencil.name if mesh.uv_layer_stencil else ""
        bow.menu("VIEW3D_MT_tools_projectpaint_stencil", text=stencil_text, translate=False)     

def tbtoolbrush(context,box,split):
    ob = bpy.context.object
    tool_settings = context.tool_settings
    mesh = ob.data
    if ob.mode == 'TEXTURE_PAINT':
        brush = bpy.context.tool_settings.image_paint.brush
        capabilities = brush.image_paint_capabilities
        use_accumulate = capabilities.has_accumulate
        ipaint = tool_settings.image_paint   
    if ob.mode == 'WEIGHT_PAINT': 
        tool_settings = bpy.context.tool_settings
        brush = bpy.context.tool_settings.weight_paint.brush
        wpaint = context.tool_settings.weight_paint
        ups = context.tool_settings.unified_paint_settings
        if brush is None:
            row.column().template_ID_preview(tool_settings, "brush", new="brush.add", rows=3, cols=8, hide_buttons=False)
        if brush is not None:            
            boxt = box.box()
            row = boxt.row(align=True)  
            row.prop(brush,"blend",text="")
            row = boxt.row(align=True)  
            row.prop(ups,"weight")
            row.prop(ups,"use_unified_weight", text="",icon='BRUSHES_ALL')
            row = boxt.row(align=True)  
            row.prop(ups,"size")       
            row.prop(brush,"use_pressure_size", text="",icon='STYLUS_PRESSURE')
            row.prop(ups,"use_unified_size", text="",icon='BRUSHES_ALL')
            row = boxt.row(align=True)  
            row.prop(brush,"strength")       
            row.prop(brush,"use_pressure_strength", text="",icon='STYLUS_PRESSURE')
            row.prop(ups,"use_unified_strength", text="",icon='BRUSHES_ALL')         
    if ob.mode == 'VERTEX_PAINT': 
        wm = bpy.context.window_manager
        tool_settings_mode = tool_settings.vertex_paint
        brush = tool_settings_mode.brush
        ups = context.tool_settings.unified_paint_settings

        vpaint = context.tool_settings.vertex_paint 
        paint = context.tool_settings.image_paint
        
        boxt = box.box()
        row = boxt.row(align=True)  
        row.prop(brush,"blend",text="")

        if brush is None:
            row.column().template_ID_preview(tool_settings, "brush", new="brush.add", rows=3, cols=8, hide_buttons=False)
        if brush is not None:
            row.prop(brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
            if brush.use_custom_icon:
                box.prop(brush, "icon_filepath", text="")
            row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")
            boxt.prop(brush, "blend", text="")                    
            #COLOR       
            row = boxt.row(align=True)  
            row.prop(ups,"size")       
            row.prop(brush,"use_pressure_size", text="",icon='STYLUS_PRESSURE')
            row.prop(ups,"use_unified_size", text="",icon='BRUSHES_ALL')
            row = boxt.row(align=True)  
            row.prop(brush,"strength")       
            row.prop(brush,"use_pressure_strength", text="",icon='STYLUS_PRESSURE')
            row.prop(ups,"use_unified_strength", text="",icon='BRUSHES_ALL')    

            row = boxt.row(align=True)  
            row.prop(brush,"color",text="")
            row.prop(brush,"secondary_color",text="")
            row.operator("paint.brush_colors_flip",text="",emboss=False,icon='FILE_REFRESH')
            row.prop(ups,"use_unified_color",icon='BRUSHES_ALL',text="")
            row = boxt.row(align=True)
            boxt.template_ID(vpaint, "palette", new="palette.new")
            if tool_settings_mode.palette:
                boxt.template_palette(vpaint, "palette", color=True)  
            

    
    if ob.mode == 'SCULPT':
        tbtoolsculpt(context,box,split)
    if ob.mode == 'TEXTURE_PAINT':
        tbtooltexturetexture(context,box,split)
        layout = split.column(align=True)
        box = layout.box()
        tbtooltexture(context,box,split)


def tbtoolstroke(context,box,split):
    ob = bpy.context.object
    wm = bpy.context.window_manager
    tool_settings = context.tool_settings
    #split = col.split()
    #box = split.column().box()
    bow = box.box()                     
    if ob.mode == 'SCULPT':
        settings = tool_settings.sculpt     
        brush = bpy.context.tool_settings.sculpt.brush  
    if ob.mode == 'TEXTURE_PAINT':       
        settings = tool_settings.image_paint
        brush = bpy.context.tool_settings.image_paint.brush             
    if ob.mode == 'WEIGHT_PAINT':       
        settings = tool_settings.weight_paint
        brush = bpy.context.tool_settings.weight_paint.brush         
    if ob.mode == 'VERTEX_PAINT':      
        settings = tool_settings.vertex_paint 
        brush = bpy.context.tool_settings.vertex_paint.brush                                                                                            
    row = bow.row(align=True)         
    cw = wm.tb_wm_bool.tb_sculpt_stroke
    cwt = "tb_sculpt_stroke"
    if cw == False:
        row.prop(wm.tb_wm_bool, cwt,text="",icon='CON_TRACKTO')                    
        row.prop(brush, "stroke_method",text="")
    if cw == True:       
        row.prop(wm.tb_wm_bool, cwt,text="",icon='CON_TRACKTO')                                                                             
        row.prop(brush, "stroke_method",text="")
        tex_slot = brush.texture_slot
        mode = bpy.context.object.mode
        row.prop_enum(brush, "use_scene_spacing", "VIEW",text="",icon='HIDE_OFF')
        row.prop_enum(brush, "use_scene_spacing", "SCENE",text="",icon='SCENE_DATA')                    
        if brush.use_anchor:
            row = bow.row(align=True)
            row.prop(brush, "use_edge_to_edge", text="Edge To Edge",icon='SNAP_EDGE')
        if brush.use_airbrush:
            row = bow.row(align=True)                        
            row.prop(brush, "rate", text="Rate", slider=True)
        if brush.use_space:
            row = bow.row(align=True)
            row.prop(brush, "spacing", text="Spacing")
            row.prop(brush, "use_pressure_spacing", toggle=True, text="")
        if brush.use_line or brush.use_curve:
            row = bow.row(align=True)
            row.prop(brush, "spacing", text="Spacing")
        if mode in {'TEXTURE_PAINT', 'PAINT_2D', 'SCULPT'}:
            if brush.image_paint_capabilities.has_space_attenuation or brush.sculpt_capabilities.has_space_attenuation:
                row.prop(brush, "use_space_attenuation",icon='OPTIONS',text="")
        if brush.use_curve:
            row = bow.row(align=True)
            row.template_ID(brush, "paint_curve", new="paintcurve.new")
            row.operator("paintcurve.draw",icon='GREASEPENCIL')
        if brush.use_space:
            row = bow.row(align=True)
            row.prop(brush, "dash_ratio", text="Dash Ratio")
            row.prop(brush, "dash_samples", text="Dash Length")
        if (mode == 'SCULPT' and brush.sculpt_capabilities.has_jitter) or mode != 'SCULPT':
            row = bow.row(align=True)
            if brush.jitter_unit == 'BRUSH':
                row.prop(brush, "jitter", slider=True)
            else:
                row.prop(brush, "jitter_absolute")
            row.prop(brush, "use_pressure_jitter", toggle=True, text="")
            row.prop_enum(brush, "jitter_unit","VIEW",icon='HIDE_OFF',text="")
            row.prop_enum(brush, "jitter_unit","BRUSH",icon='BRUSH_DATA',text="")                        
        row = bow.row(align=True)
        row.prop(settings, "input_samples")
        if brush.brush_capabilities.has_smooth_stroke:
            if brush.use_smooth_stroke == False:
                row = bow.row(align=True)
                row.prop(brush,"use_smooth_stroke",icon='MOD_SMOOTH',text="Stabilize Stroke")
            else:                
                row = bow.row(align=True)
                row.prop(brush,"use_smooth_stroke",text="",icon='MOD_SMOOTH')
                row.separator()
                row.prop(brush, "smooth_stroke_radius", text="Radius", slider=True)
                row.prop(brush, "smooth_stroke_factor", text="Factor", slider=True)                
   #FCURVES
    bow = box.box()
    row = bow.row(align=True)                
    cw = wm.tb_wm_bool.tb_sculpt_falloff
    cwt = "tb_sculpt_falloff"
    if cw == False:
        row.prop(wm.tb_wm_bool, cwt,text="",icon='FCURVE')
        row.prop(brush, "curve_preset", text="")
    if cw == True:       
        row.prop(wm.tb_wm_bool, cwt,text="",icon='FCURVE')                                                                             
        row.prop(brush, "curve_preset", text="")
        if brush.curve_preset == 'CUSTOM':
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
            bow.template_curve_mapping(brush, "curve", brush=True)
        if ob.mode == 'SCULPT':
            if brush.sculpt_tool != 'POSE':
                row = box.row(align=True)
                row.use_property_split = True
                row.use_property_decorate = False
                brush = bpy.context.tool_settings.sculpt.brush
                row.prop(brush, "falloff_shape", expand=True)
        if ob.mode == 'TEXTURE_PAINT': 
            row = bow.row(align=True)
            ipaint = tool_settings.image_paint
            if   ipaint.use_normal_falloff == False:
                row.prop(ipaint, "use_normal_falloff", text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                     
            else:
                row.prop(ipaint, "use_normal_falloff", text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                     
                row.prop(ipaint, "normal_angle", text="Angle")                                                                                     
        if ob.mode == 'WEIGHT_PAINT' or ob.mode == 'VERTEX_PAINT':
            row = bow.row(align=True)
            if brush.use_frontface_falloff == False:             
                row.prop(brush, "use_frontface_falloff", text="Frontface_Falloff",icon='FACESEL')                                                                       
            else:
                row.prop(brush, "use_frontface_falloff", text="",icon='FACESEL')
                row.prop(brush, "falloff_angle")                                        
        #Advancew
    cw = wm.tb_wm_bool.tb_brush_advanced
    cwt = "tb_brush_advanced"
    bow = box.box()
    row = bow.row(align=False)                
    if cw == False:
        row.prop(wm.tb_wm_bool, cwt,text="Advanced",icon='BRUSH_DATA')
    if cw == True:   
        row.prop(wm.tb_wm_bool, cwt,text="",icon='BRUSH_DATA')  
        if ob.mode == 'SCULPT':
            capabilities = brush.sculpt_capabilities
            use_accumulate = capabilities.has_accumulate
            use_frontface = True
            cw = wm.tb_wm_bool.tb_brush_automask
            cwt = "tb_brush_automask"
            row.prop(wm.tb_wm_bool, cwt,text="Auto-Masking",icon='MOD_MASK')
            if cw == True:
                row = bow.row(align=False)                
                row.prop(wm.tb_wm_bool, cwt,text="",icon='MOD_MASK')      
                row.prop(brush, "use_automasking_topology", text="Topology",icon='VIEW_ORTHO')
                row.prop(brush, "use_automasking_face_sets", text="Face Sets",icon='MOD_EXPLODE')
                row = bow.row(align=True)
                row.label(icon='BLANK1')
                row.separator()
                row.prop(brush, "use_automasking_boundary_edges", text="Mesh Boundary",icon='PIVOT_BOUNDBOX')
                row.separator()
                if brush.use_automasking_boundary_face_sets:
                    row.prop(brush, "use_automasking_boundary_face_sets", text="",icon='MOD_MESHDEFORM')
                    row.prop(brush, "automasking_boundary_edges_propagation_steps")
                else:
                    row.prop(brush, "use_automasking_boundary_face_sets", text="Face Sets Boundary",icon='MOD_MESHDEFORM')
            #cavity
            bown = bow.box()
            row = bown.row()
            row.prop(brush, "use_automasking_cavity", text="Cavity",icon='IMPORT')
            row.prop(brush, "use_automasking_cavity_inverted", text="Inverted",icon='EXPORT')
            if brush.use_automasking_cavity or brush.use_automasking_cavity_inverted:
                row = bown.row(align=True)
                row.prop(brush, "automasking_cavity_factor")
                row.prop(brush, "automasking_cavity_blur_steps")
                row.prop(brush, "use_automasking_custom_cavity_curve",text="",icon='FCURVE')
                # if brush.use_automasking_custom_cavity_curve: (LACKS CURVE)
                row = bown.row()
                row.operator("sculpt.mask_from_cavity").settings_source = 'BRUSH'
            bown = bow.box()
            if not brush.use_automasking_view_normal or not brush.use_automasking_start_normal:
                row = bown.row()
            if not brush.use_automasking_view_normal:
                row.prop(brush, "use_automasking_view_normal",icon='NORMALS_FACE')
            if not brush.use_automasking_start_normal:
                row.prop(brush, "use_automasking_start_normal",icon='LIGHT_AREA')
            #view_normal    
            if brush.use_automasking_view_normal:
                bowns = bown.box()
                row = bowns.row()
                row.prop(brush, "use_automasking_view_normal",icon='NORMALS_FACE')
                row.prop(brush, "use_automasking_view_occlusion",text="",icon='MATSHADERBALL')
                if not brush.use_automasking_view_occlusion:
                    row = bowns.row(align=True)
                    row.prop(settings, "automasking_view_normal_limit")
                    row.prop(settings, "automasking_view_normal_falloff")
            #view_area
            if brush.use_automasking_start_normal:
                bowns = bown.box()
                row = bowns.row(align=True)
                row.prop(brush, "use_automasking_start_normal",icon='LIGHT_AREA')
                row = bowns.row(align=True)
                row.prop(settings, "automasking_start_normal_limit")
                row.prop(settings, "automasking_start_normal_falloff")                    



            if capabilities.has_sculpt_plane:
                box.prop(brush, "sculpt_plane",text="")
                row = bow.row(align=False)                
                row.label(text="Use Original")
                row.prop(brush, "use_original_normal", text="Normal",icon='NORMALS_FACE')
                row.prop(brush, "use_original_plane", text="Plane",icon='ORIENTATION_NORMAL')
        if ob.mode == 'TEXTURE_PAINT':
            capabilities = brush.image_paint_capabilities                        
            row.prop(brush, "use_alpha",icon='IMAGE_RGB_ALPHA')
            if brush.image_tool == 'SOFTEN':
                box.row().prop(brush, "direction", expand=True)
                box.prop(brush, "sharp_threshold")
                box.prop(brush, "blur_mode",text="")
            elif brush.image_tool == 'MASK':
                box.prop(brush, "weight", text="Mask Value", slider=True)
            if brush.use_accumulate:
                row.prop(brush, "use_accumulate",icon='ADD')                    
        if ob.mode == 'WEIGHT_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode =='SCULPT':
            if ob.mode == 'VERTEX_PAINT':
                row.prop(brush, "use_alpha",icon='IMAGE_RGB_ALPHA')                            
            if ob.mode == 'SCULPT':
                row = box.row(align=False)                                            
            if brush.weight_tool != 'SMEAR':
                use_accumulate = True
            else:
                use_accumulate = False                        
            use_frontface = True
            if use_accumulate:
                row.prop(brush, "use_accumulate",icon='ADD')
            if use_frontface:
                row.prop(brush, "use_frontface", text="Front Faces Only",icon='AXIS_FRONT')                                                                        


def tbtoolsettings(context,box,split):   
    wm = bpy.context.window_manager
    ob = bpy.context.object
    obd = ob.data
    tool_settings = context.tool_settings
    ipaint = tool_settings.image_paint         
   #SYMMETRY
    if ob.mode in {'EDIT','EDIT_GPENCIL','TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT'}:          
        if ob.type == 'MESH':
            cw = wm.tb_wm_bool.tb_brush_mirror
            cwt = "tb_brush_mirror"
            if cw == False:
                row = box.row(align=False)
                row.prop(wm.tb_wm_bool, cwt,text="Symmetry",icon='MOD_MIRROR')
            if cw == True:  
                bow = box.box()
                row = bow.row(align=True)
                row.prop(wm.tb_wm_bool, cwt,text="",icon='MOD_MIRROR')
                row.separator()     
                if ob.mode == 'EDIT':   
                    row.prop(obd,"use_mirror_x",text="X", toggle=True)                       
                    row.prop(obd,"use_mirror_y",text="Y", toggle=True)                       
                    row.prop(obd,"use_mirror_z",text="Z", toggle=True)  
                    if obd in ["use_mirror_x","use_mirror_y","use_mirror_z"]:
                        row.separator()
                        row.prop(context.object.data,"use_mirror_topology",text="", toggle=True,icon='MESH_ICOSPHERE')                       
                if ob.mode == 'TEXTURE_PAINT':
                    row.prop(ipaint, "use_symmetry_x", text="X", toggle=True)
                    row.prop(ipaint, "use_symmetry_y", text="Y", toggle=True)
                    row.prop(ipaint, "use_symmetry_z", text="Z", toggle=True)
                if ob.mode == 'VERTEX_PAINT':          
                    vpaint = tool_settings.vertex_paint              
                    row.prop(vpaint, "use_mesh_mirror_x", text="X", toggle=True)
                    row.prop(ob, "use_mesh_mirror_y", text="Y", toggle=True)
                    row.prop(ob, "use_mesh_mirror_z", text="Z", toggle=True)
                    row = bow.row(align=True)
                    row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                    row.separator()                                                
                    row.prop(vpaint, "radial_symmetry", text="")  
                if ob.mode == 'WEIGHT_PAINT':           
                    wpaint = tool_settings.weight_paint             
                    row.prop(ob, "use_mesh_mirror_x", text="X", toggle=True)
                    row.prop(ob, "use_mesh_mirror_y", text="Y", toggle=True)
                    row.prop(ob, "use_mesh_mirror_z", text="Z", toggle=True)
                    row = bow.row(align=True)
                    row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                    row.separator()                                                
                    row.prop(wpaint, "radial_symmetry", text="")                        
                if ob.mode == 'SCULPT':
                    sculpt = tool_settings.sculpt
                    row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
                    row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
                    row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)
                    row = bow.row(align=True)
                    row.label(icon='LOCKED')
                    row.separator()
                    row.prop(sculpt, "lock_x", text="X", toggle=True)
                    row.prop(sculpt, "lock_y", text="Y", toggle=True)
                    row.prop(sculpt, "lock_z", text="Z", toggle=True)
                    row = bow.row(align=True)
                    row.label(icon='VIEW_ORTHO')
                    row.separator()
                    row.prop(sculpt, "tile_x", text="X", toggle=True)
                    row.prop(sculpt, "tile_y", text="Y", toggle=True)
                    row.prop(sculpt, "tile_z", text="Z", toggle=True)
                    row = bow.row(align=True)
                    row.label(icon='TRANSFORM_ORIGINS')
                    row.separator()
                    row.prop(sculpt, "tile_offset", text="")
                    row = bow.row(align=True)
                    row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                    row.separator()                        
                    row.prop(sculpt, "radial_symmetry", text="")
                    row = bow.row(align=True)                        
                    row.operator("sculpt.symmetrize")
                    row.prop(sculpt, "use_symmetry_feather", text="",icon='MOD_SMOOTH')
                    splits = bow.split(align=True)                      
                    cols = splits.column(align=True)                                                
                    cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_X",text="  X  / - X")
                    cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_X",text="- X  /   X")
                    cols = splits.column(align=True)                                                
                    cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_Y",text="  Y  / - Y")
                    cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_Y",text="- Y  /   Y")
                    cols = splits.column(align=True)                                                
                    cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_Z",text="  Z  / - Z")                        
                    cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_Z",text="- Z  /   Z")    
    
                    #AUTOMERGE
                    if ob.mode == 'EDIT':
                        bow = box.box()
                        row = bow.row()
                        if bpy.context.scene.tool_settings.use_mesh_automerge == False:
                            row.prop(context.scene.tool_settings,"use_mesh_automerge")
                        if bpy.context.scene.tool_settings.use_mesh_automerge == True:
                            row.prop(context.scene.tool_settings,"use_mesh_automerge",text="")                                                
                            row.prop(context.scene.tool_settings,"double_threshold",text="")                                                                                                
                            row.prop(context.scene.tool_settings,"use_mesh_automerge_and_split",text="",icon='MOD_EDGESPLIT')                                                
       #OPTION        
        if ob.mode !='VERTEX_PAINT' and ob.mode != 'OBJECT':
            cw = wm.tb_wm_bool.tb_brush_option
            cwt = "tb_brush_option"               
            if cw == False:
                row = box.row(align=False) 
                row.prop(wm.tb_wm_bool, cwt,text="Options",icon='OPTIONS')
            if cw == True:   
                bow = box.box()
                row = bow.row(align=False)   
                row.prop(wm.tb_wm_bool, cwt,text="",icon='OPTIONS')

                if ob.mode =='EDIT':
                    mesh = ob.data
                    if tool_settings. use_transform_correct_face_attributes == True:
                        row.prop(tool_settings, "use_transform_correct_face_attributes",text="",icon='FACESEL')
                        row.prop(tool_settings, "use_transform_correct_keep_connected",text="Keep Conected",icon='EDGESEL') 
                    else:
                        row.prop(tool_settings, "use_transform_correct_face_attributes",icon='FACESEL') 
                    row.prop(tool_settings, "use_edge_path_live_unwrap",icon='GROUP_UVS')                        
                    if not tool_settings.use_mesh_automerge:
                        row = bow.row(align=True)
                        row.prop(tool_settings,"use_mesh_automerge")
                    if tool_settings.use_mesh_automerge:
                        bow = bow.box()
                        row = bow.row(align=True)
                        row.prop(tool_settings,"use_mesh_automerge",text="")                                                
                        row.prop(tool_settings,"double_threshold",text="")                                                                                                
                        row.prop(tool_settings,"use_mesh_automerge_and_split",text="",icon='MOD_EDGESPLIT')   

                if ob.mode == 'WEIGHT_PAINT':
                    row.prop(tool_settings, "use_auto_normalize", text="Auto Normalize",icon='NORMALS_FACE')
                    row.prop(tool_settings, "use_lock_relative", text="Lock-Relative",icon='LOCKED')
                    row.prop(tool_settings, "use_multipaint", text="Multi-Paint",icon='TPAINT_HLT')
                    row = bow.row(align=False)       
                    row.label(icon='BLANK1')                                                                                                                                                         
                    row.prop(wpaint, "use_group_restrict",icon='STICKY_UVS_VERT')
                    obj = context.weight_paint_object
                    if obj.type == 'MESH':
                        mesh = obj.data
                        row.prop(mesh, "use_mirror_x",icon='MOD_MIRROR')
                        if mesh.use_mirror_x:
                            row.prop(mesh, "use_mirror_topology")                        
                if ob.mode == 'TEXTURE_PAINT':
                    row.prop(ipaint, "use_backface_culling", text="Backface Culling",icon='FACESEL')                        
                    row = bow.row(align=False)       
                    row.label(icon='BLANK1')                                                                                 
                    row.prop(ipaint, "seam_bleed")
                    row.prop(ipaint, "dither", slider=True)
                    row = bow.row(align=False)       
                    row.label(icon='BLANK1')                                                                                 
                    row.prop(ipaint, "use_occlude")
                    row = bow.row(align=False)                                  
                    row.label(icon='SCENE_DATA')      
                    row.prop(ipaint, "screen_grab_size", text="Screen Grab Size")

                    row = bow.row(align=True)     
                    row.label(icon='BLANK1')                                                                             
                    row.operator("image.project_apply", text="Apply",icon='CHECKMARK')
                    row.operator("image.project_edit", text="Quick Edit")
                    row.separator()
                    row.operator("paint.project_image", text="Apply Camera Image",icon='CAMERA_DATA')
                if ob.mode == 'SCULPT':
                    sculpt = tool_settings.sculpt
                    row = bow.row(align=False)                
                    row.label(icon='HIDE_OFF')
                    row.prop(sculpt, "use_threaded", text="Threaded Sculpt",icon='SCULPTMODE_HLT')
                    row.prop(sculpt, "show_low_resolution",icon='MOD_MULTIRES')
                    row = bow.row(align=False)                                        
                    row.label(icon='BLANK1')                        
                    row.prop(sculpt, "use_sculpt_delay_updates",icon='SCENE_DATA')
                    row.prop(sculpt, "use_deform_only",icon='MOD_SIMPLEDEFORM')
                    row = bow.row(align=False)                
                    row.label(icon='MOD_MASK')
                    row.prop(sculpt, "use_automasking_topology", text="Topology",icon='VIEW_ORTHO')
                    row.prop(sculpt, "use_automasking_face_sets", text="Face Sets",icon='MOD_EXPLODE')
                    row = bow.row(align=False)                                        
                    row.label(icon='BLANK1')
                    row.prop(sculpt, "use_automasking_boundary_edges", text="Mesh Boundary",icon='PIVOT_BOUNDBOX')
                    row.prop(sculpt, "use_automasking_boundary_face_sets", text="Face Sets Boundary",icon='OBJECT_HIDDEN')                               
            #WEIGHTPAIINT
                if ob.mode == 'WEIGHT_PAINT':
                    tool_settings = context.tool_settings
                    box = box.box()                                
                    ts = bpy.context.tool_settings
                    brush = bpy.context.tool_settings.weight_paint.brush
                    wpaint = context.tool_settings.weight_paint
                    us = ts.unified_paint_settings             
                    if brush.weight_tool == 'DRAW':
                        box.prop(brush, "blend",text="")
                        row = box.row(align=True)
                        if us.use_unified_weight:
                            row.prop(us, "weight",slider=True)
                        else:                      
                            row.prop(brush, "weight",slider=True)
                        row.prop(us,"use_unified_weight",text="",icon='BRUSHES_ALL')                                    
                    row = box.row(align=True)
                    if us.use_unified_size:
                        row.prop(us, "size",slider=True)
                    else:                      
                        row.prop(brush, "size",slider=True)
                    row.prop(brush,"use_pressure_size",text="")
                    row.prop(us,"use_unified_size",text="",icon='BRUSHES_ALL')                
                    row = box.row(align=True)  
                    if us.use_unified_strength:
                        row.prop(us, "strength",slider=True)
                    else:                      
                        row.prop(brush, "strength",slider=True)                              
                    row.prop(brush,"use_pressure_strength",text="")     
                    row.prop(us,"use_unified_strength",text="",icon='BRUSHES_ALL')
            #VERTEX_PAINT
                if ob.mode == 'VERTEX_PAINT':
                    tool_settings = context.tool_settings
                    split = col.split()
                    box = split.column().box()                
                    wm = bpy.context.window_manager                
                    ts = bpy.context.tool_settings
                    brush = bpy.context.tool_settings.vertex_paint.brush
                    vpaint = context.tool_settings.vertex_paint
                    us = ts.unified_paint_settings       
                    bow = box.box()
                    row = bow.row(align=True)
                    row.column().template_ID(vpaint, "brush", new="brush.add")                
                    if wm.tb_vertex_brush == False:
                        row.prop(wm.tb_wm_bool, 'tb_vertex_brush', text="",toggle=True,icon='PROP_OFF')      
                    if wm.tb_vertex_brush == True:
                        if brush is not None:
                            row.prop(brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
                            if brush.use_custom_icon:
                                box.prop(brush, "icon_filepath", text="")
                            row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")
                        row.prop(wm.tb_wm_bool, 'tb_vertex_brush', text="",toggle=True,icon='PROP_ON')                              
                        row = bow.row(align=True)                    
                        row.prop(brush, "blend",text="")
                        row = bow.row(align=True)                                        
                        if us.use_unified_size == False:
                            row.prop(brush,"size",slider=True)                        
                        else:
                            row.prop(us,"size",slider=True)
                        row.prop(brush,"use_pressure_size",text="")
                        row.prop(us,"use_unified_size",text="",icon='BRUSHES_ALL')
                        row = bow.row(align=True)                                        
                        if us.use_unified_strength == False:
                            row.prop(brush,"strength",slider=True)                        
                        else:
                            row.prop(us,"strength",slider=True)
                        row.prop(brush,"use_pressure_strength",text="")
                        row.prop(us,"use_unified_strength",text="",icon='BRUSHES_ALL')                    
                        if brush.vertex_tool == 'DRAW':
                            row = bow.row(align=True)
                            row.prop(brush,"color",text="")                                      
                            row.prop(brush,"secondary_color",text="")
                            row.operator("paint.brush_colors_flip",text="",emboss=False,icon='FILE_REFRESH')
                            row.prop(us,"use_unified_color",icon='BRUSHES_ALL',text="")
                            row = bow.row(align=True)
                            bow.template_ID(vpaint, "palette", new="palette.new")
                            if settings.palette:
                                bow.template_palette(vpaint, "palette", color=True)                                                                                     
                    bow = box.box()
                    row = bow.row(align=True)
                    row.template_ID(brush, "texture", new="texture.new")
                    if brush.texture:
                        cw = wm.tb_wm_bool.tb_paint_txtr
                        cwt = "tb_paint_txtr"
                        if cw == False:
                            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                        if cw == True:       
                            row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
                            row = bow.row(align=True)
                            row.prop(brush.texture_slot,"map_mode",text="")
                            if brush.texture_slot.map_mode == 'TILED' or brush.texture_slot.map_mode == 'VIEW_PLANE' or brush.texture_slot.map_mode == 'RANDOM':                   
                                row = bow.row(align=True)
                                row.label(text="Angle",icon='CON_ROTLIMIT')
                                row.prop(brush.texture_slot,"angle",text="")                   
                            if brush.texture_slot.map_mode == 'VIEW_PLANE' or brush.texture_slot.map_mode == 'RANDOM':
                                row.prop(brush.texture_slot,"use_rake",text="",icon='TRACKING')
                                row.prop(brush.texture_slot,"use_random",text="",icon='MOD_NOISE')
                            if brush.texture_slot.map_mode == 'STENCIL':
                                row = bow.row(align=True)
                                row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                                row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')
                            split = bow.split(align=False)
                            col = split.column(align=True)
                            col.label(text="Offset",icon='CON_LOCLIMIT')                  
                            col.prop(brush.texture_slot,"offset",text="")             
                            col = split.column(align=True)
                            col.label(text="Scale",icon='CON_SIZELIMIT')  
                            col.prop(brush.texture_slot,"scale",text="")                                                      

def tbtooldatadrawn(self, context, box):
    wm = context.window_manager
    ob = context.object

    settings = context.tool_settings.image_paint
    ob = context.active_object
    layout = self.layout

    if bpy.context.object:    
        me = context.object.data
        arm = context.object.data
        if ob.mode in ['OBJECT','EDIT']:
            box = layout.box()
            scntt = context.tool_settings
            scentt = context.scene.tool_settings                
            row = box.row(align=False)                
            orient_slot = context.scene.transform_orientation_slots[0]
            row.prop_with_popover(orient_slot,"type",text="",panel="VIEW3D_PT_transform_orientations",)                             
            row.prop(scntt, "transform_pivot_point",text="")
            cw = wm.tb_wm_bool.tb_obj_snap
            cwt = "tb_obj_snap"
            cwtt = "Snap"
            cwi = 'SNAP_ON'
            if cw == False:
                row.prop(wm.tb_wm_bool,cwt,text="",icon=cwi)   
            cw = wm.tb_wm_bool.tb_obj_snap
            cwt = "tb_obj_snap"
            cwtt = "Snap"
            cwi = 'SNAP_ON'                    
            if cw == True:
                bor = box.box()                
                row = bor.row(align=True)                               
                row.prop(scntt, "use_snap",text="")
                row.prop(wm.tb_wm_bool,cwt,text="",icon='EXPORT')
                row.separator()
                row.label(text="")
                row.prop(scntt, "snap_elements",text="")
                row.separator()                    
                row = bor.row(align=True)          
                row.prop(scentt,"use_snap_translate",text="",icon='CON_LOCLIMIT')                                                                    
                row.prop(scentt,"use_snap_rotate",text="",icon='CON_ROTLIMIT')                                                                    
                row.prop(scentt,"use_snap_scale",text="",icon='CON_SIZELIMIT')                                                                                                                                                             
                row.separator() 
                if scentt.snap_elements == {'INCREMENT'}:
                    row.prop(scentt, "use_snap_grid_absolute",icon='MESH_GRID')
                if scentt.snap_elements != {'INCREMENT'}:
                    row.prop_enum(scentt, "snap_target","CLOSEST",icon='SNAP_GRID')                                               
                    row.prop_enum(scentt, "snap_target","CENTER",icon='PIVOT_INDIVIDUAL')                                               
                    row.prop_enum(scentt, "snap_target","MEDIAN",icon='PIVOT_MEDIAN')                                               
                    row.prop_enum(scentt, "snap_target","ACTIVE",icon='PIVOT_ACTIVE')    
                    row = bor.row(align=False)                                                                                                                                                               
                    row.prop(scentt,"use_snap_backface_culling",icon='FACESEL')
                    row.prop(scentt,"use_snap_align_rotation",icon='CON_ROTLIKE')                    
                    if ob.mode == 'EDIT':
                        row.prop(scentt,"use_snap_self",icon='MOD_UVPROJECT')
                if scentt.snap_elements == {'FACE'}:
                    row.prop(scentt,"use_snap_project",icon='NORMALS_FACE')                                    
                if scentt.snap_elements == {'VOLUME'}:                          
                    row.prop(scentt,"use_snap_peel_object",icon='OBJECT_DATA')                                                        
            if wm.tb_wm_bool.tb_obj_prop == False and wm.tb_wm_bool.tb_obj_snap == True:
                bow = box.box()    
                row = bow.row(align=True)   
           #PROPORTIONAL                                
            cw = wm.tb_wm_bool.tb_obj_prop
            cwt = "tb_obj_prop"
            cwtt = "Proportional Editing"
            cwi = 'PROP_ON'
            if cw == False:
                row.prop(wm.tb_wm_bool,cwt,text="",icon=cwi)   
            if cw == True: 
                bow = box.box()   
                row = bow.row(align=True)
                if ob.mode == 'OBJECT':
                    row.prop(scentt,"use_proportional_edit_objects",text="")
                if ob.mode == 'EDIT':
                    row.prop(scentt,"use_proportional_edit",text="")
                row.prop(wm.tb_wm_bool,cwt,text="",icon='EXPORT')   
                row.separator()                    
                row.prop_enum(scentt,"proportional_edit_falloff","SMOOTH",text="",icon='SMOOTHCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","SPHERE",text="",icon='SPHERECURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","ROOT",text="",icon='ROOTCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","INVERSE_SQUARE",text="",icon='SMOOTHCURVE')                             
                row.prop_enum(scentt,"proportional_edit_falloff","SHARP",text="",icon='SHARPCURVE')                                                                                                             
                row.prop_enum(scentt,"proportional_edit_falloff","LINEAR",text="",icon='LINCURVE')                                                                                                                                 
                row.prop_enum(scentt,"proportional_edit_falloff","CONSTANT",text="",icon='NOCURVE')      
                row.prop_enum(scentt,"proportional_edit_falloff","RANDOM",text="",icon='RNDCURVE')                                                                                                                                                                                                                                        
                if ob.mode == 'EDIT':
                    row.separator()  
                    row.prop(scentt,"use_proportional_connected",text="",icon='EDGESEL')                                      
                    row.prop(scentt,"use_proportional_projected",text="",icon='MOD_UVPROJECT')                                                                                       
           #OPTION     
        if ob.mode == 'OBJECT':
            cw = wm.tb_wm_bool.tb_obj_option
            cwt = "tb_obj_option"
            bow = box.box()
            row = bow.row(align=False)                   
            if cw == False:
                row.prop(wm.tb_wm_bool, cwt,text="Options",icon='OPTIONS')
            if cw == True:   
                row.prop(wm.tb_wm_bool, cwt,text="",icon='OPTIONS')
                if ob.mode == 'OBJECT':
                    row.prop(context.scene.tool_settings, "use_transform_data_origin", text= "Origins",icon='OBJECT_ORIGIN')
                    row.prop(context.scene.tool_settings, "use_transform_pivot_point_align", text= "Locations",icon='EMPTY_ARROWS')
                    row.prop(context.scene.tool_settings, "use_transform_skip_children", text= "Parents",icon='CON_CHILDOF')                                                               
                if ob.mode == 'EDIT':
                    tool_settings = context.tool_settings
                    ob = context.active_object
                    mesh = ob.data
                    if tool_settings. use_transform_correct_face_attributes == True:
                        row.prop(tool_settings, "use_transform_correct_face_attributes",text="",icon='FACESEL')
                        row.prop(tool_settings, "use_transform_correct_keep_connected",text="",icon='EDGESEL') 
                    else:
                        row.prop(tool_settings, "use_transform_correct_face_attributes",icon='FACESEL')
        if ob.type == 'MESH':
            if ob.mode == 'EDIT':
                box = layout.box()
                row = box.row(align=True)               
                row.operator("mesh.delete_loose",icon='STICKY_UVS_DISABLE')
                row.separator()
                row.operator("mesh.decimate",text="Decimate",icon='MOD_DECIM')                
                row.operator("mesh.dissolve_degenerate",text="Dissolve",icon='MOD_TRIANGULATE')                                
                row = box.row(align=False)                
                row.operator("mesh.remove_doubles",text="Merge by Distance",icon='DRIVER_DISTANCE')                                                
                row.operator("mesh.fill_holes",text="Fill Holes",icon='CLIPUV_DEHLT')                                                                
                row.operator("mesh.face_make_planar",text="Planar",icon='LIGHTPROBE_PLANAR')                                                
                if bpy.context.tool_settings.mesh_select_mode[0]:
                    row = box.row(align=True)                    
                    row.label(icon='VERTEXSEL')         
                    row.operator("mesh.vertices_smooth",icon='MOD_SMOOTH')           
                    row.operator("mesh.vertices_smooth",icon='SHARPCURVE')    
                if bpy.context.tool_settings.mesh_select_mode[1]:
                    row = box.row(align=True)     
                    row.label(icon='EDGESEL')                                                       
                    row.operator("mesh.extrude_edges_move",text="",icon='EMPTY_SINGLE_ARROW')                                               
                    row.separator()
                    row.operator("mesh.delete_loose",icon='STICKY_UVS_DISABLE')                    
                if bpy.context.tool_settings.mesh_select_mode[2]:              
                    row = box.row(align=True)
                    row.label(icon='FACESEL')                   
                    row.operator("mesh.extrude_faces_move",text="",icon='EMPTY_SINGLE_ARROW')                                                                                                   
                    row.separator()                           
                    row.operator("mesh.poke",icon='X')                                      
                    row.separator()                           
                    row.operator("mesh.faces_shade_smooth",icon='MOD_SMOOTH')   
                    row.operator("mesh.faces_shade_flat",icon='SHARPCURVE')                       
            #VARIABLES     
            if ob.mode == 'TEXTURE_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode == 'WEIGHT_PAINT' or ob.mode == 'SCULPT':
                tool_settings = context.tool_settings
                if ob.mode == 'TEXTURE_PAINT':
                    brush = bpy.context.tool_settings.image_paint.brush
                    capabilities = brush.image_paint_capabilities
                    use_accumulate = capabilities.has_accumulate
                    ipaint = tool_settings.image_paint   
                if ob.mode == 'WEIGHT_PAINT': 
                    tool_settings = bpy.context.tool_settings
                    brush = bpy.context.tool_settings.weight_paint.brush
                    wpaint = context.tool_settings.weight_paint
                if ob.mode == 'VERTEX_PAINT': 
                    tool_settings = bpy.context.tool_settings
                    brush = bpy.context.tool_settings.vertex_paint.brush
                    vpaint = context.tool_settings.vertex_paint                           
            if ob.mode == 'SCULPT':
                wm = bpy.context.window_manager
                tool_settings = context.tool_settings
                dyno = context.sculpt_object.use_dynamic_topology_sculpting
                sculpt = tool_settings.sculpt
                brush = bpy.context.tool_settings.sculpt.brush
                ts = bpy.context.tool_settings.sculpt
                st = brush.sculpt_tool                

                #Dyntopo
                box = layout.box()
                if st == 'PAINT' or st == 'MASK' or st == 'TOPOLOGY' or st == 'CLOTH' or st == 'DRAW_FACE_SETS' or st == 'DRAW_SHARP' or st == 'LAYER ' or st == 'SMOOTH' or st == 'GRAB' or st == 'ELASTIC_DEFORM' or st == 'SNAKE_HOOK' or st == 'CLAY_THUMB' or st == 'POSE' or st == 'NUDGE' or st == 'ROTATE':
                    row = box.row(align=True)                                                            
                    row.label(icon='VIEW_ORTHO',text="Tool not compatible with dyntopo")                        
                else:
                    if dyno == False:
                        row = box.row(align=True)                                        
                        row.operator("sculpt.dynamic_topology_toggle",icon='VIEW_ORTHO',text="Dyntopo")
                    if dyno == True:
                        row = box.row(align=True)                    
                        row.operator("sculpt.dynamic_topology_toggle",icon='VIEW_ORTHO',text="")                
                        if sculpt.detail_type_method in {'CONSTANT', 'MANUAL'}:
                            row.prop(sculpt, "constant_detail_resolution")
                            props = row.operator("sculpt.sample_detail_size", text="", icon='EYEDROPPER')
                            props.mode = 'DYNTOPO'
                        elif (sculpt.detail_type_method == 'BRUSH'):
                            row.prop(sculpt, "detail_percent")
                            row.prop(sculpt, "use_smooth_shading",text="",icon='MOD_SMOOTH')                               
                        else:
                            row.prop(sculpt, "detail_size")
                            row.prop(sculpt, "use_smooth_shading",text="",icon='MOD_SMOOTH')   
                        if sculpt.detail_type_method in {'CONSTANT', 'MANUAL'}:
                            row.operator("sculpt.detail_flood_fill",icon='FILE_REFRESH',text="")
                        row = box.row(align=True)                                                
                        row.prop(sculpt, "detail_refine_method", text="")
                        row.prop(sculpt, "detail_type_method", text="")
                    #BRUSH
                box = layout.box()
                row = box.row(align=True)
                row.column().template_ID(ts, "brush", new="brush.add")                   
                cw = wm.tb_wm_bool.tb_sculpt_brush
                cwt = "tb_sculpt_brush"
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                if cw == True:       
                    ups = context.tool_settings.unified_paint_settings
                    colt = box.row() 
                    splitt = colt.split()
                    boxt = splitt.column().box()                    
                    if ts.brush is not None:
                        if ts.brush.use_custom_icon:
                            row.prop(ts.brush, "icon_filepath", text="")
                            row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")                        
                        row.prop(ts.brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
                    #Direction                                         
                    if st == 'MASK':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"mask_tool","DRAW")                            
                        row.prop_enum(brush,"mask_tool","SMOOTH") 
                        if brush.mask_tool == 'DRAW':
                            row = boxt.row(align=True)    
                            row.prop_enum(brush,"direction","ADD",icon='ADD')                    
                            row.prop_enum(brush,"direction","SUBTRACT",icon='REMOVE')                                                                                 
                    if st == 'CLOTH':
                        row = boxt.row(align=True)
                        row.prop(brush,"cloth_deform_type",text="")  
                        row.prop(brush,"cloth_force_falloff_type",text="")                                        
                    if st == 'DRAW' or st == 'DRAW_SHARP' or st == 'CLAY' or st == 'CLAY_STRIPS' or st == 'LAYER' or st == 'BLOB' or st == 'CREASE': 
                        row = boxt.row(align=True)    
                        row.prop_enum(brush,"direction","ADD",icon='ADD')                    
                        row.prop_enum(brush,"direction","SUBTRACT",icon='REMOVE')                                            
                    if st == 'INFLATE':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"direction","INFLATE",icon='ADD')
                        row.prop_enum(brush,"direction","DEFLATE",icon='REMOVE')                        
                    if st == 'FLATTEN':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"direction","CONTRAST",icon='ADD')
                        row.prop_enum(brush,"direction","FLATTEN",icon='REMOVE')
                    if st == 'FILL':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"direction","FILL",icon='ADD')
                        row.prop_enum(brush,"direction","DEEPEN",icon='REMOVE')                            
                    if st == 'SCRAPE':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"direction","SCRAPE",icon='ADD')
                        row.prop_enum(brush,"direction","PEAKS",icon='REMOVE') 
                    if st == 'PINCH':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"direction","MAGNIFY",icon='ADD')
                        row.prop_enum(brush,"direction","PINCH",icon='REMOVE')
                    if st == 'SMOOTH':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"smooth_deform_type","SURFACE")
                        row.prop_enum(brush,"smooth_deform_type","LAPLACIAN")                            
                    if st == 'FILL' or st == 'SCRAPE':                                             
                        row.prop(brush,"invert_to_scrape_fill",icon='ARROW_LEFTRIGHT',text="")
                    if st == 'GRAB':
                        row = boxt.row(align=True)                            
                        row.prop(brush,"use_grab_active_vertex",icon='VERTEXSEL')
                    if st == 'ELASTIC_DEFORM':
                        row = boxt.row(align=True)                            
                        row.prop(brush,"elastic_deform_type",icon='SCULPTMODE_HLT',text="")                                                                                     
                    if st == 'MULTIPLANE_SCRAPE':
                        row = boxt.row(align=True)
                        row.prop(brush,"use_multiplane_scrape_dynamic",icon='UV_SYNC_SELECT')                                                            
                        row.prop(brush,"show_multiplane_scrape_planes_preview",icon='BRUSH_DATA')                                                                                        
                    if st == 'POSE':
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"pose_deform_type","ROTATE_TWIST",icon='CON_ROTLIMIT')                            
                        row.prop_enum(brush,"pose_deform_type","SCALE_TRANSLATE",icon='CON_SIZELIMIT')                            
                        row.prop_enum(brush,"pose_deform_type","SQUASH_STRETCH",icon='CON_SAMEVOL')
                        row = boxt.row(align=True)
                        row.prop_enum(brush,"pose_origin_type","TOPOLOGY",icon='MESH_ICOSPHERE')                            
                        row.prop_enum(brush,"pose_origin_type","FACE_SETS",icon='FACE_MAPS')                            
                        row.prop_enum(brush,"pose_origin_type","FACE_SETB_FK",icon='CON_KINEMATIC')                            
                    if st == 'PAINT':
                        row = boxt.row(align=True)
                        row.label(icon='COLOR')
                        row.prop(brush,"color",text="")                                                                            
                        row.prop(brush,"blend",text="")                        
                    #Directions
                    row = boxt.row(align=True)                                             
                    if bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size == 'VIEW':
                        if ups.use_unified_size == True:
                            row.prop(ups,"size", slider=True)                             
                        else:
                            row.prop(brush,"size", slider=True) 
                        row.prop(brush, "use_pressure_size", text="")                                          
                        row.prop(ups,"use_unified_size", slider=True,text="",icon='BRUSHES_ALL')           
                    if bpy.context.scene.tool_settings.unified_paint_settings.use_locked_size == 'SCENE':                                                                 
                        if ups.use_unified_size == True:
                            row.prop(ups,"unprojected_radius", slider=True,text="Radius")                                                            
                        else:                            
                            row.prop(brush,"unprojected_radius", slider=True,text="Radius")      
                        row.prop(brush, "use_pressure_size", text="")                                          
                        row.prop(ups,"use_unified_size", slider=True,text="",icon='BRUSHES_ALL')        
                    row.prop_enum(ups, "use_locked_size","VIEW",icon='HIDE_OFF',text="")
                    row.prop_enum(ups, "use_locked_size","SCENE",icon='SCENE_DATA',text="")   
                    row = boxt.row(align=True) 
                    boxt = splitt.column().box()                                        
                    if ups.use_unified_strength == True: 
                        row.prop(ups,"strength", slider=True,text="Strenght")                                                                                                                              
                    else:
                        row.prop(brush,"strength", slider=True,text="Strenght")                                                                                                                                                          
                    row.prop(brush,"use_pressure_strength",text="")    
                    row.prop(ups,"use_unified_strength",icon='BRUSHES_ALL',text="")                                                                                                                           
                    #Normal Rad
                    row = boxt.row(align=True)
                    row.label(icon='SNAP_NORMAL')
                    row.prop(brush, "normal_radius_factor", slider=True)                       
                    #Hardness
                    row = boxt.row(align=True)                        
                    row.label(icon='ALIASED')
                    row.prop(brush, "hardness", slider=True)
                    #Autosmooth
                    if st != 'SMOOTH' and st != 'MASK':
                        row = boxt.row(align=True)                        
                        row.label(icon='ANTIALIASED')
                        row.prop(brush, "auto_smooth_factor", slider=True)                                                                       
                        row.prop(brush, "use_inverse_smooth_pressure",text="")
                    if st == 'CLAY' or st == 'CLAY_STRIPS' or st == 'CLAY_THUMB' or st == 'FLATTEN' or st == 'SCRAPE' or st == 'FILL':
                        row = boxt.row(align=True)       
                        row.label(icon='NORMALS_FACE')                         
                        row.prop(brush, "plane_offset", slider=True)
                        row.prop(brush, "use_offset_pressure", text="")                            
                        row = boxt.row(align=True)       
                        if brush.use_plane_trim == False:
                            row.prop(brush, "use_plane_trim",icon='HOLDOUT_ON')                                                                                                                                                                                                                                                                                                          
                        else:
                            row.prop(brush, "use_plane_trim", text="",icon='HOLDOUT_ON')                                                                                                                                                                                                                                                                                                                                      
                            row.prop(brush, "plane_trim")
                    if st == 'CLAY_STRIPS':
                        row = boxt.row(align=True)     
                        row.label(icon='SMOOTHCURVE')                                                                                                                                                                                                  
                        row.prop(brush, "tip_roundness") 
                    if st == 'BLOB' or st == 'CREASE' or st == 'SNAKE_HOOK':
                        if st == 'BLOB' or st == 'SNAKE_HOOK':
                            stt = "Magnify"
                            sti = 'SPHERECURVE'
                        if st == 'CREASE':
                            stt = "Pinch"
                            sti = 'SHARPCURVE'
                        row = boxt.row(align=True)     
                        row.label(icon=sti)                                                                                                                                                                                                  
                        row.prop(brush, "crease_pinch_factor",text = stt)                                                                             
                    if st == 'SNAKE_HOOK':
                            row = boxt.row(align=True)
                            row.label(icon='BRUSH_DATA')                                                                                                                                                                                                                                  
                            row.prop(brush, "rake_factor")
                    if st == 'SMOOTH':
                        if brush.smooth_deform_type == 'SURFACE':
                            row = boxt.row(align=True)
                            row.label(icon='CON_SAMEVOL')                                                                                                                                                                                                                                  
                            row.prop(brush, "surface_smooth_shape_preservation")
                            row.prop(brush, "surface_smooth_iterations")                                                                
                            row = boxt.row(align=True)
                            row.label(icon='VERTEXSEL')                                                                                                                                                                                                                                       
                            row.prop(brush, "surface_smooth_current_vertex")
                            row = boxt.row(align=True)                                                                                         
                    if st == 'LAYER':                 
                        row = boxt.row(align=True)     
                        row.label(icon='CON_SAMEVOL')                                                                                                                                                                                                  
                        row.prop(brush, "height")    
                        row = boxt.row(align=True)     
                        row.prop(brush,"use_persistent",icon='NOCURVE')
                        row.operator("sculpt.set_persistent_base",text="Set Base")      
                    if st == 'FILL' or st == 'SCRAPE':                 
                        row = boxt.row(align=True)     
                        row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                                                                                                                                  
                        row.prop(brush, "area_radius_factor")
                    if st == 'MULTIPLANE_SCRAPE':                 
                        row = boxt.row(align=True)     
                        row.label(icon='NORMALS_FACE')                                                                                                                                                                                                  
                        row.prop(brush, "multiplane_scrape_angle")
                    if st == 'ELASTIC_DEFORM':                                                    
                        row = boxt.row(align=True)     
                        row.label(icon='NORMALS_FACE')                                                                                                                                                                                                  
                        row.prop(brush, "normal_weight")
                        row = boxt.row(align=True)     
                        row.label(icon='FILE_VOLUME')                                                                                                                                                                                                  
                        row.prop(brush, "elastic_deform_volume_preservation")
                    if st == 'POSE':
                        row = boxt.row(align=True)
                        row.label(icon='OBJECT_ORIGIN')  
                        row.prop(brush, "pose_offset")
                        row.prop(brush,"use_pose_ik_anchored",text="",icon='CON_KINEMATIC')
                        row = boxt.row(align=True)
                        row.label(icon='MOD_SMOOTH')  
                        row.prop(brush, "pose_smooth_iterations")
                    if st == 'CLOTH':
                        row = boxt.row(align=True)
                        row.prop(brush,"cloth_sim_limit",text="Limit")                                                       
                        row.prop(brush,"cloth_sim_falloff",text="Falloff")
                        row = boxt.row(align=True)                            
                        row.prop(brush,"cloth_mass",text="Mass")                                                       
                        row.prop(brush,"cloth_damping",text="Damping") 
                    if st == 'PAINT':   
                        row = boxt.row(align=True)  
                        row.label(icon='CON_FOLLOWPATH')                                                  
                        row.prop(brush,"flow",slider=True)
                        row.prop(brush,"density",slider=True)
                        row = boxt.row(align=True)        
                        row.label(icon='WPAINT_HLT')                                                                    
                        row.prop(brush,"wet_mix",slider=True)
                        row.prop(brush,"wet_persistence",slider=True)
                        row = boxt.row(align=True)             
                        row.label(icon='CON_SIZELIMIT')                                                                                       
                        row.prop(brush,"tip_scale_x",slider=True)
                        row.label(icon='SMOOTHCURVE')
                        row.prop(brush,"tip_roundness",slider=True)                                                                                                
                #TEXTURE
                box = layout.box()
                row = box.row(align=True)                        
                row.template_ID(brush, "texture", new="texture.new")                       
                cw = wm.tb_wm_bool.tb_sculpt_txtr
                cwt = "tb_sculpt_txtr"
                if bpy.context.tool_settings.sculpt.brush.texture:                    
                    if cw == False:
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                    if cw == True:       
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
                        row = box.row(align=True)
                        tex_slot = brush.texture_slot
                        if sculpt:
                            box.prop(tex_slot, "map_mode", text="")
                        else:
                            box.prop(tex_slot, "map_mode", text="Mapping")
                        if tex_slot.map_mode == 'STENCIL':
                            row = box.row(align=False)                                    
                            if brush.texture and brush.texture.type == 'IMAGE':
                                row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                            row.operator("brush.stencil_reset_transform")
                        if tex_slot.has_texture_angle:
                            col = layout.column()
                            row = box.row(align=True)                                
                            if tex_slot.has_texture_angle_source:
                                row.prop(tex_slot, "use_rake", text="Rake",icon='BRUSH_DATA')
                                row.separator()
                                if brush.brush_capabilities.has_random_texture_angle and tex_slot.has_random_texture_angle:
                                    if sculpt:
                                        if brush.sculpt_capabilities.has_random_texture_angle:
                                            if tex_slot.use_random:
                                                row.prop(tex_slot, "use_random", text="",icon='MOD_NOISE')
                                                row.prop(tex_slot, "random_angle", text="Random Angle")
                                            else:              
                                                row.prop(tex_slot, "use_random", text="Random",icon='MOD_NOISE')                                                                                          
                                    else:
                                        row.prop(tex_slot, "use_random", text="Random")
                                        if tex_slot.use_random:
                                            row.prop(tex_slot, "random_angle", text="Random Angle")
                            row = box.row(align=True)
                            row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                            row.prop(tex_slot, "angle", text="Angle")
                        split = box.split(align=False)
                        col = split.column(align=True)                            
                        col.prop(tex_slot, "offset")                      
                        col = split.column(align=True)                                                        
                        col.prop(tex_slot, "scale")
                        if sculpt:
                            box.prop(brush, "texture_sample_bias", slider=True, text="Sample Bias")

            if ob.mode == 'TEXTURE_PAINT':                              
                box = layout.box()                
                row = box.row(align=True)
                row.label(icon='TEXTURE',text="Slots")
                row.prop_enum(settings, "mode", "IMAGE",text="Image",icon='IMAGE')
                row.prop_enum(settings, "mode", "MATERIAL",text="Material",icon='MATERIAL')
                if settings.mode == 'MATERIAL':
                    if len(ob.material_slots) > 1:
                        box.template_list("MATERIAL_UL_matslots", "layers",
                                             ob, "material_slots",
                                             ob, "active_material_index", rows=2)
                    mat = ob.active_material
                    if mat and mat.texture_paint_images:
                        row = box.row()
                        row.template_list("TEXTURE_UL_texpaintslots", "",
                                          mat, "texture_paint_images",
                                          mat, "paint_active_slot", rows=2)
                        if mat.texture_paint_slots:
                            slot = mat.texture_paint_slots[mat.paint_active_slot]
                        else:
                            slot = None
                        have_image = slot is not None
                    else:
                        row = box.row()
                        boe = row.box()
                        boe.label(text="No Textures")
                        have_image = False
                    sub = row.column(align=True)
                    sub.operator_menu_enum("paint.add_texture_paint_slot", "type", icon='ADD', text="")
                elif settings.mode == 'IMAGE':
                    mesh = ob.data
                    uv_text = mesh.uv_layers.active.name if mesh.uv_layers.active else ""
                    box.template_ID(settings, "canvas", new="image.new", open="image.open")
                    have_image = settings.canvas is not None
                    if have_image:
                        row = box.row(align=True)
                        row.prop(settings, "interpolation", text="")
                        if settings.missing_uvs:
                            row.operator("paint.add_simple_uvs", icon='ADD', text="Add UVs")                          
                        else:
                            row.menu("VIEW3D_MT_tools_projectpaint_uvlayer", text=uv_text, translate=False)
                if have_image:
                    if settings.missing_uvs:
                        split = layout.split()
                        box.label(text="UV Map Needed", icon='INFO')
                        box.operator("paint.add_simple_uvs", icon='ADD', text="Add Simple UVs")
                    if have_image:
                        row.operator("image.save_all_modified", text="", icon='FILE_TICK')
        #ASSIGMENT
            if ob.mode == 'TEXTURE_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode == 'WEIGHT_PAINT' or ob.mode == 'SCULPT':        
                ipaint = tool_settings.image_paint         
            #TEXTURE BRUSH
            if ob.mode == 'TEXTURE_PAINT':

                mesh = ob.data
                ob = context.active_object
                paint = context.tool_settings.image_paint
                settings = context.tool_settings.image_paint
                brush = settings.brush
                bow = box.box()                
                row = bow.row(align=True)
                row.column().template_ID(settings, "brush", new="brush.add")

                if wm.tb_paint_brush == False:
                    row.prop(wm.tb_wm_bool, 'tb_paint_brush', text="",toggle=True,icon='PROP_OFF')      
                if wm.tb_paint_brush == True:
                    colt = bow.row() 
                    splitt = colt.split()
                    boxt = splitt.column().box()
                    if brush is not None:
                        row.prop(brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
                        if brush.use_custom_icon:
                            box.prop(brush, "icon_filepath", text="")
                        row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")
                        row.prop(wm.tb_wm_bool, 'tb_paint_brush', text="", toggle=True,icon='PROP_ON')
                        boxt.prop(brush, "blend", text="")                    
                    #COLOR       
                    ups = context.scene.tool_settings.unified_paint_settings
                    row = boxt.row(align=True)  
                    row.prop_enum(brush, "color_type", "COLOR",icon='COLOR')
                    row.prop_enum(brush, "color_type", "GRADIENT",icon='NODE_TEXTURE',text='Gradient')
                    if brush.color_type == 'COLOR':
                        row = boxt.row(align=True)
                        row.prop(brush, "color",text="")
                        row.prop(brush, "secondary_color",text="")
                        row.separator()
                        row.prop(brush, "strenght",text="")                
                        row.operator("paint.brush_colors_flip", icon='FILE_REFRESH', text="", emboss=False)
                        row.prop(ups, "use_unified_color", text="", icon='WORLD')               
                    #Gradient
                    elif brush.color_type == 'GRADIENT':
                        boxt.prop(brush, "gradient_stroke_mode", text="")
                        boxt.template_color_ramp(brush, "gradient", expand=True)
                    #Palette
                    cw = wm.tb_wm_bool.tb_brush_palette
                    cwt = "tb_brush_palette"
                    if cw == False:
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='RESTRICT_COLOR_OFF')
                    if cw == True:   
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='COLOR')                                          
                        boxt.template_ID(settings, "palette", new="palette.new")
                        if settings.palette:
                            boxt.template_palette(settings, "palette", color=True)
                    boxt = splitt.column().box()                        
                    if brush is not None:
                        row = boxt.row(align=True)
                        if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_size == False:
                            row.prop(context.scene.tool_settings.image_paint.brush,"size",slider=True)
                        if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_size == True:
                            row.prop(context.scene.tool_settings.unified_paint_settings,"size",slider=True)
                        row.prop(context.scene.tool_settings.image_paint.brush,"use_pressure_size",text="")
                        row.prop(context.scene.tool_settings.unified_paint_settings,"use_unified_size",icon='WORLD',text="")
                        row = boxt.row(align=True)
                        if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_strength == False:
                            row.prop(context.scene.tool_settings.image_paint.brush,"strength")                    
                        if bpy.context.scene.tool_settings.unified_paint_settings.use_unified_strength == True:                    
                            row.prop(context.scene.tool_settings.unified_paint_settings,"strength")
                        row.prop(context.scene.tool_settings.image_paint.brush,"use_pressure_strength",text="")
                        row.prop(context.scene.tool_settings.unified_paint_settings,"use_unified_strength",icon='WORLD',text="")                                   
                        #Adaptative
                        mode = ob.mode
                        row = boxt.row(align=True)
                        row.prop(brush, "use_alpha",text="Alpha",icon='IMAGE_RGB_ALPHA')
                        row.prop(brush, "use_accumulate",text="Accumulate",icon='LIBRARY_DATA_OVERRIDE')
                        row.prop(brush, "use_frontface", text="Front Faces Only",icon='VERTEXSEL')
                        if brush.image_tool == 'SOFTEN':
                            row.prop(brush, "blur_mode",text="")
                            boxt.row().prop(brush, "direction", expand=True)
                            boxt.prop(brush, "sharp_threshold")
                            if mode == 'PAINT_2D':
                                boxt.prop(brush, "blur_kernel_radius")
                        elif brush.image_tool == 'MASK':
                            boxt.prop(brush, "weight", text="Mask Value", slider=True)                
                #SYMMETRY
            if ob.mode == 'EDIT' or ob.mode == 'TEXTURE_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode == 'WEIGHT_PAINT' or ob.mode == 'SCULPT':        
                col = layout.row()
                split = col.split()
                box = split.column().box()
                bow = box.box()
                cw = wm.tb_wm_bool.tb_brush_mirror
                cwt = "tb_brush_mirror"
                row = bow.row(align=False)
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="Symmetry",icon='MOD_MIRROR')
                if cw == True:   
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='MOD_MIRROR')
                    row.separator()            
                    if ob.mode == 'EDIT':   
                        row.prop(context.object.data,"use_mirror_x",text="X", toggle=True)                       
                        row.prop(context.object.data,"use_mirror_y",text="Y", toggle=True)                       
                        row.prop(context.object.data,"use_mirror_z",text="Z", toggle=True)  
                        row.separator()
                        row.prop(context.object.data,"use_mirror_topology",text="", toggle=True,icon='MESH_ICOSPHERE')                                                                                            
                        
                    if ob.mode == 'TEXTURE_PAINT':
                        row.prop(ipaint, "use_mesh_mirror_x", text="X", toggle=True)
                        row.prop(ipaint, "use_mesh_mirror_y", text="Y", toggle=True)
                        row.prop(ipaint, "use_mesh_mirror_z", text="Z", toggle=True)
                    if ob.mode == 'VERTEX_PAINT':                        
                        row.prop(vpaint, "use_mesh_mirror_x", text="X", toggle=True)
                        row.prop(vpaint, "use_mesh_mirror_y", text="Y", toggle=True)
                        row.prop(vpaint, "use_mesh_mirror_z", text="Z", toggle=True)
                        row = bow.row(align=True)
                        row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                        row.separator()                                                
                        row.prop(vpaint, "radial_symmetry", text="")  
                    if ob.mode == 'WEIGHT_PAINT':                        
                        row.prop(wpaint, "use_mesh_mirror_x", text="X", toggle=True)
                        row.prop(wpaint, "use_mesh_mirror_y", text="Y", toggle=True)
                        row.prop(wpaint, "use_mesh_mirror_z", text="Z", toggle=True)
                        row = bow.row(align=True)
                        row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                        row.separator()                                                
                        row.prop(wpaint, "radial_symmetry", text="")                        
                    if ob.mode == 'SCULPT':
                        row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
                        row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
                        row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)
                        row = bow.row(align=True)
                        row.label(icon='LOCKED')
                        row.separator()
                        row.prop(sculpt, "lock_x", text="X", toggle=True)
                        row.prop(sculpt, "lock_y", text="Y", toggle=True)
                        row.prop(sculpt, "lock_z", text="Z", toggle=True)
                        row = bow.row(align=True)
                        row.label(icon='VIEW_ORTHO')
                        row.separator()
                        row.prop(sculpt, "tile_x", text="X", toggle=True)
                        row.prop(sculpt, "tile_y", text="Y", toggle=True)
                        row.prop(sculpt, "tile_z", text="Z", toggle=True)
                        row = bow.row(align=True)
                        row.label(icon='TRANSFORM_ORIGINS')
                        row.separator()
                        row.prop(sculpt, "tile_offset", text="")
                        row = bow.row(align=True)
                        row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
                        row.separator()                        
                        row.prop(sculpt, "radial_symmetry", text="")
                        row = bow.row(align=True)                        
                        row.operator("sculpt.symmetrize")
                        row.prop(sculpt, "use_symmetry_feather", text="",icon='MOD_SMOOTH')
                        splits = bow.split(align=True)                      
                        cols = splits.column(align=True)                                                
                        cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_X",text="  X  / - X")
                        cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_X",text="- X  /   X")
                        cols = splits.column(align=True)                                                
                        cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_Y",text="  Y  / - Y")
                        cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_Y",text="- Y  /   Y")
                        cols = splits.column(align=True)                                                
                        cols.prop_enum(sculpt, "symmetrize_direction","POSITIVE_Z",text="  Z  / - Z")                        
                        cols.prop_enum(sculpt, "symmetrize_direction","NEGATIVE_Z",text="- Z  /   Z")
                #AUTOMERGE
                if ob.mode == 'EDIT':
                    bow = box.box()
                    row = bow.row()
                    if bpy.context.scene.tool_settings.use_mesh_automerge == False:
                        row.prop(context.scene.tool_settings,"use_mesh_automerge")
                    if bpy.context.scene.tool_settings.use_mesh_automerge == True:
                        row.prop(context.scene.tool_settings,"use_mesh_automerge",text="")                                                
                        row.prop(context.scene.tool_settings,"double_threshold",text="")                                                                                                
                        row.prop(context.scene.tool_settings,"use_mesh_automerge_and_split",text="",icon='MOD_EDGESPLIT')                                                
            #OPTION        
            if ob.mode != 'EDIT' and ob.mode !='VERTEX_PAINT' and ob.mode != 'OBJECT':
                cw = wm.tb_wm_bool.tb_brush_option
                cwt = "tb_brush_option"
                bow = box.box()
                row = bow.row(align=False)                
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="Options",icon='OPTIONS')
                if cw == True:   
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='OPTIONS')                  
                    if ob.mode == 'WEIGHT_PAINT':
                        row.prop(tool_settings, "use_auto_normalize", text="Auto Normalize",icon='NORMALS_FACE')
                        row.prop(tool_settings, "use_lock_relative", text="Lock-Relative",icon='LOCKED')
                        row.prop(tool_settings, "use_multipaint", text="Multi-Paint",icon='TPAINT_HLT')
                        row = bow.row(align=False)       
                        row.label(icon='BLANK1')                                                                                                                                                         
                        row.prop(wpaint, "use_group_restrict",icon='STICKY_UVS_VERT')
                        obj = context.weight_paint_object
                        if obj.type == 'MESH':
                            mesh = obj.data
                            row.prop(mesh, "use_mirror_x",icon='MOD_MIRROR')
                            if mesh.use_mirror_x:
                                row.prop(mesh, "use_mirror_topology")                        
                    if ob.mode == 'TEXTURE_PAINT':
                        row.prop(ipaint, "use_backface_culling", text="Backface Culling",icon='FACESEL')                        
                        row = bow.row(align=False)       
                        row.label(icon='BLANK1')                                                                                 
                        row.prop(ipaint, "seam_bleed")
                        row.prop(ipaint, "dither", slider=True)
                        row = bow.row(align=False)       
                        row.label(icon='BLANK1')                                                                                 
                        row.prop(ipaint, "use_occlude")
                        row = bow.row(align=False)                                  
                        row.label(icon='SCENE_DATA')      
                        row.prop(ipaint, "screen_grab_size", text="Screen Grab Size")

                        row = bow.row(align=True)     
                        row.label(icon='BLANK1')                                                                             
                        row.operator("image.project_apply", text="Apply",icon='CHECKMARK')
                        row.operator("image.project_edit", text="Quick Edit")
                        row.separator()
                        row.operator("paint.project_image", text="Apply Camera Image",icon='CAMERA_DATA')
                    if ob.mode == 'SCULPT':
                        row = bow.row(align=False)                
                        row.label(icon='HIDE_OFF')
                        row.prop(sculpt, "use_threaded", text="Threaded Sculpt",icon='SCULPTMODE_HLT')
                        row.prop(sculpt, "show_low_resolution",icon='MOD_MULTIRES')
                        row = bow.row(align=False)                                        
                        row.label(icon='BLANK1')                        
                        row.prop(sculpt, "use_sculpt_delay_updates",icon='SCENE_DATA')
                        row.prop(sculpt, "use_deform_only",icon='MOD_SIMPLEDEFORM')
                        row = bow.row(align=False)                
                        row.label(icon='MOD_MASK')
                        row.prop(sculpt, "use_automasking_topology", text="Topology",icon='VIEW_ORTHO')
                        row.prop(sculpt, "use_automasking_face_sets", text="Face Sets",icon='MOD_EXPLODE')
                        row = bow.row(align=False)                                        
                        row.label(icon='BLANK1')
                        row.prop(sculpt, "use_automasking_boundary_edges", text="Mesh Boundary",icon='PIVOT_BOUNDBOX')
                        row.prop(sculpt, "use_automasking_boundary_face_sets", text="Face Sets Boundary",icon='OBJECT_HIDDEN')                               
        #WEIGHTPAIINT
            if ob.mode == 'WEIGHT_PAINT':
                tool_settings = context.tool_settings
                split = col.split()
                box = split.column().box()                                
                ts = bpy.context.tool_settings
                brush = bpy.context.tool_settings.weight_paint.brush
                wpaint = context.tool_settings.weight_paint
                us = ts.unified_paint_settings             
                if brush.weight_tool == 'DRAW':
                    box.prop(brush, "blend",text="")
                    row = box.row(align=True)
                    if us.use_unified_weight:
                        row.prop(us, "weight",slider=True)
                    else:                      
                        row.prop(brush, "weight",slider=True)
                    row.prop(us,"use_unified_weight",text="",icon='BRUSHES_ALL')                                    
                row = box.row(align=True)
                if us.use_unified_size:
                    row.prop(us, "size",slider=True)
                else:                      
                    row.prop(brush, "size",slider=True)
                row.prop(brush,"use_pressure_size",text="")
                row.prop(us,"use_unified_size",text="",icon='BRUSHES_ALL')                
                row = box.row(align=True)  
                if us.use_unified_strength:
                    row.prop(us, "strength",slider=True)
                else:                      
                    row.prop(brush, "strength",slider=True)                              
                row.prop(brush,"use_pressure_strength",text="")     
                row.prop(us,"use_unified_strength",text="",icon='BRUSHES_ALL')
        #VERTEX_PAINT
            if ob.mode == 'VERTEX_PAINT':
                tool_settings = context.tool_settings
                split = col.split()
                box = split.column().box()                
                wm = bpy.context.window_manager                
                ts = bpy.context.tool_settings
                brush = bpy.context.tool_settings.vertex_paint.brush
                vpaint = context.tool_settings.vertex_paint
                us = ts.unified_paint_settings       

                bow = box.box()
                row = bow.row(align=True)
                row.column().template_ID(vpaint, "brush", new="brush.add")                
                if wm.tb_vertex_brush == False:
                    row.prop(wm.tb_wm_bool, 'tb_vertex_brush', text="",toggle=True,icon='PROP_OFF')      
                if wm.tb_vertex_brush == True:
                    if brush is not None:
                        row.prop(brush, "use_custom_icon", toggle=True, icon='FILE_IMAGE', text="")
                        if brush.use_custom_icon:
                            box.prop(brush, "icon_filepath", text="")
                        row.menu("VIEW3D_MT_brush_context_menu", icon='DOWNARROW_HLT', text="")
                    row.prop(wm.tb_wm_bool, 'tb_vertex_brush', text="",toggle=True,icon='PROP_ON')                              
                    row = bow.row(align=True)                    
                    row.prop(brush, "blend",text="")
                    row = bow.row(align=True)                                        
                    if us.use_unified_size == False:
                        row.prop(brush,"size",slider=True)                        
                    else:
                        row.prop(us,"size",slider=True)
                    row.prop(brush,"use_pressure_size",text="")
                    row.prop(us,"use_unified_size",text="",icon='BRUSHES_ALL')
                    row = bow.row(align=True)                                        
                    if us.use_unified_strength == False:
                        row.prop(brush,"strength",slider=True)                        
                    else:
                        row.prop(us,"strength",slider=True)
                    row.prop(brush,"use_pressure_strength",text="")
                    row.prop(us,"use_unified_strength",text="",icon='BRUSHES_ALL')                    
                    if brush.vertex_tool == 'DRAW':
                        row = bow.row(align=True)
                        row.prop(brush,"color",text="")                                      
                        row.prop(brush,"secondary_color",text="")
                        row.operator("paint.brush_colors_flip",text="",emboss=False,icon='FILE_REFRESH')
                        row.prop(us,"use_unified_color",icon='BRUSHES_ALL',text="")
                        row = bow.row(align=True)
                        bow.template_ID(vpaint, "palette", new="palette.new")
                        if settings.palette:
                            bow.template_palette(vpaint, "palette", color=True)                                                                                     
                               
                bow = box.box()
                row = bow.row(align=True)
                row.template_ID(brush, "texture", new="texture.new")
                if brush.texture:
                    cw = wm.tb_wm_bool.tb_paint_txtr
                    cwt = "tb_paint_txtr"
                    if cw == False:
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                    if cw == True:       
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
                        row = bow.row(align=True)
                        row.prop(brush.texture_slot,"map_mode",text="")
                        if brush.texture_slot.map_mode == 'TILED' or brush.texture_slot.map_mode == 'VIEW_PLANE' or brush.texture_slot.map_mode == 'RANDOM':                   
                            row = bow.row(align=True)
                            row.label(text="Angle",icon='CON_ROTLIMIT')
                            row.prop(brush.texture_slot,"angle",text="")                   
                        if brush.texture_slot.map_mode == 'VIEW_PLANE' or brush.texture_slot.map_mode == 'RANDOM':
                            row.prop(brush.texture_slot,"use_rake",text="",icon='TRACKING')
                            row.prop(brush.texture_slot,"use_random",text="",icon='MOD_NOISE')
                        if brush.texture_slot.map_mode == 'STENCIL':
                            row = bow.row(align=True)
                            row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                            row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')
                        split = bow.split(align=False)
                        col = split.column(align=True)
                        col.label(text="Offset",icon='CON_LOCLIMIT')                  
                        col.prop(brush.texture_slot,"offset",text="")             
                        col = split.column(align=True)
                        col.label(text="Scale",icon='CON_SIZELIMIT')  
                        col.prop(brush.texture_slot,"scale",text="")
                                                    
            #TEXTURE BRUSH
            if ob.mode == 'TEXTURE_PAINT':
                split = col.split()
                box = split.column().box()                 
                mesh = ob.data
                ob = context.active_object
                paint = context.tool_settings.image_paint
                settings = context.tool_settings.image_paint
                pb = settings.brush
                ups = context.scene.tool_settings.unified_paint_settings
                mode = ob.mode
                settings = bpy.context.tool_settings.image_paint
                split = col.split()
                bow = box.box()                   
                row = bow.row(align=True)
                row.template_ID(pb, "texture", new="texture.new")
                if pb.texture:
                    cw = wm.tb_wm_bool.tb_paint_txtr
                    cwt = "tb_paint_txtr"
                    if cw == False:
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                    if cw == True:       
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                                             
                        row = bow.row(align=True)                        
                        row.prop(pb.texture_slot,"map_mode",text="")
                        if pb.texture_slot.map_mode == 'TILED' or pb.texture_slot.map_mode == 'VIEW_PLANE' or pb.texture_slot.map_mode == 'RANDOM':                   
                            row = bow.row(align=True)
                            row.label(text="Angle",icon='CON_ROTLIMIT')
                            row.prop(pb.texture_slot,"angle",text="")                   
                        if pb.texture_slot.map_mode == 'VIEW_PLANE' or pb.texture_slot.map_mode == 'RANDOM':
                            row.prop(pb.texture_slot,"use_rake",text="",icon='TRACKING')
                            row.prop(pb.texture_slot,"use_random",text="",icon='MOD_NOISE')
                        if pb.texture_slot.map_mode == 'STENCIL':                                       
                            row.prop(brush,"texture_overlay_alpha")
                            row.prop(brush,"use_primary_overlay_override",icon='BRUSH_DATA',text="")              
                            row = bow.row(align=True)
                            row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                            row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')                            
                        split = bow.split(align=False)
                        col = split.column(align=True)
                        col.label(text="Offset",icon='CON_LOCLIMIT')                  
                        col.prop(pb.texture_slot,"offset",text="")             
                        col = split.column(align=True)
                        col.label(text="Scale",icon='CON_SIZELIMIT')  
                        col.prop(pb.texture_slot,"scale",text="")
                #MASK_TEXTURE
                bow = box.box()                                  
                row = bow.row(align=True)
                if bpy.context.scene.tool_settings.image_paint.use_stencil_layer == False:
                    row.prop(ipaint, "use_stencil_layer", text="",icon='MOD_MASK')
                else:
                    row.label(icon='MOD_MASK')
                row.template_ID(pb, "mask_texture", new="texture.new")
                if pb.mask_texture:
                    cw = wm.tb_wm_bool.tb_paint_mask_txtr
                    cwt = "tb_paint_mask_txtr"
                    if cw == False:
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_OFF')
                    if cw == True:       
                        row.prop(wm.tb_wm_bool, cwt,text="",icon='PROP_ON')                                                               
                        row = bow.row(align=True)
                        row.prop(pb.mask_texture_slot,"mask_map_mode",text="")
                        if pb.mask_texture_slot.mask_map_mode == 'TILED' or pb.mask_texture_slot.mask_map_mode == 'VIEW_PLANE' or pb.mask_texture_slot.mask_map_mode == 'RANDOM':                   
                            row = bow.row(align=True)
                            row.label(text="Angle",icon='CON_ROTLIMIT')
                            row.prop(pb.mask_texture_slot,"angle",text="")                   
                        if pb.mask_texture_slot.mask_map_mode == 'VIEW_PLANE' or pb.mask_texture_slot.mask_map_mode == 'RANDOM':
                            row.prop(brush.mask_texture_slot,"use_rake",text="",icon='TRACKING')
                            row.prop(brush.mask_texture_slot,"use_random",text="",icon='MOD_NOISE')
                        if pb.mask_texture_slot.mask_map_mode == 'STENCIL':
                            row.prop(brush,"mask_overlay_alpha")
                            row.prop(brush,"use_secondary_overlay_override",icon='BRUSH_DATA',text="")                                                                 
                            row = bow.row(align=True)
                            row.operator("brush.stencil_fit_image_aspect",icon='FULLSCREEN_ENTER')
                            row.operator("brush.stencil_reset_transform",icon='ORIENTATION_LOCAL')                             
                        row = bow.row(align=True)                             
                        row.prop(pb,"use_pressure_masking",text="")                
                        split = bow.split(align=False)
                        col = split.column(align=True)
                        col.label(text="Offset",icon='CON_LOCLIMIT')                  
                        col.prop(pb.mask_texture_slot,"offset",text="")             
                        col = split.column(align=True)
                        col.label(text="Scale",icon='CON_SIZELIMIT')  
                        col.prop(pb.mask_texture_slot,"scale",text="")                                 
                if bpy.context.scene.tool_settings.image_paint.use_stencil_layer == True:
                    row = bow.row(align=True)
                    row.prop(ipaint, "use_stencil_layer", text="",icon='MOD_MASK')
                    row.prop(ipaint, "stencil_color", text="")
                    row.prop(ipaint, "invert_stencil", text="", icon='IMAGE_ALPHA')
                    bow.template_ID(ipaint, "stencil_image", new="image.new", open="image.open")
                    stencil_text = mesh.uv_layer_stencil.name if mesh.uv_layer_stencil else ""
                    bow.menu("VIEW3D_MT_tools_projectpaint_stencil", text=stencil_text, translate=False)        
        #STROKE
            if ob.mode == 'SCULPT' or ob.mode == 'TEXTURE_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode == 'WEIGHT_PAINT':
                if ob.mode != 'SCULPT':
                    bow = box.box()      
                if ob.mode == 'SCULPT':
                    split = col.split()
                    box = split.column().box()
                    bow = box.box()                     
                    brush = bpy.context.tool_settings.sculpt.brush                                                                                           
                row = bow.row(align=True)         
                cw = wm.tb_wm_bool.tb_sculpt_stroke
                cwt = "tb_sculpt_stroke"
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='CON_TRACKTO')                    
                    row.prop(brush, "stroke_method",text="")
                if cw == True:       
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='CON_TRACKTO')                                                                             
                    row.prop(brush, "stroke_method",text="")
                    tex_slot = brush.texture_slot
                    mode = bpy.context.object.mode
                    row.prop_enum(brush, "use_scene_spacing", "VIEW",text="",icon='HIDE_OFF')
                    row.prop_enum(brush, "use_scene_spacing", "SCENE",text="",icon='SCENE_DATA')                    
                    if brush.use_anchor:
                        row = bow.row(align=True)
                        row.prop(brush, "use_edge_to_edge", text="Edge To Edge",icon='SNAP_EDGE')
                    if brush.use_airbrush:
                        row = bow.row(align=True)                        
                        row.prop(brush, "rate", text="Rate", slider=True)
                    if brush.use_space:
                        row = bow.row(align=True)
                        row.prop(brush, "spacing", text="Spacing")
                        row.prop(brush, "use_pressure_spacing", toggle=True, text="")
                    if brush.use_line or brush.use_curve:
                        row = bow.row(align=True)
                        row.prop(brush, "spacing", text="Spacing")
                    if mode in {'TEXTURE_PAINT', 'PAINT_2D', 'SCULPT'}:
                        if brush.image_paint_capabilities.has_space_attenuation or brush.sculpt_capabilities.has_space_attenuation:
                            row.prop(brush, "use_space_attenuation",icon='OPTIONS',text="")
                    if brush.use_curve:
                        row = bow.row(align=True)
                        row.template_ID(brush, "paint_curve", new="paintcurve.new")
                        row.operator("paintcurve.draw",icon='GREASEPENCIL')
                    if brush.use_space:
                        row = bow.row(align=True)
                        row.prop(brush, "dash_ratio", text="Dash Ratio")
                        row.prop(brush, "dash_samples", text="Dash Length")
                    if (mode == 'SCULPT' and brush.sculpt_capabilities.has_jitter) or mode != 'SCULPT':
                        row = bow.row(align=True)
                        if brush.jitter_unit == 'BRUSH':
                            row.prop(brush, "jitter", slider=True)
                        else:
                            row.prop(brush, "jitter_absolute")
                        row.prop(brush, "use_pressure_jitter", toggle=True, text="")
                        row.prop_enum(brush, "jitter_unit","VIEW",icon='HIDE_OFF',text="")
                        row.prop_enum(brush, "jitter_unit","BRUSH",icon='BRUSH_DATA',text="")                        
                    row = bow.row(align=True)
                    row.prop(settings, "input_samples")
                    if brush.brush_capabilities.has_smooth_stroke:
                        if brush.use_smooth_stroke == False:
                            row = bow.row(align=True)
                            row.prop(brush,"use_smooth_stroke",icon='MOD_SMOOTH',text="Stabilize Stroke")
                        else:                
                            row = bow.row(align=True)
                            row.prop(brush,"use_smooth_stroke",text="",icon='MOD_SMOOTH')
                            row.separator()
                            row.prop(brush, "smooth_stroke_radius", text="Radius", slider=True)
                            row.prop(brush, "smooth_stroke_factor", text="Factor", slider=True)                
            #FCURVES
                bow = box.box()
                row = bow.row(align=True)                
                cw = wm.tb_wm_bool.tb_sculpt_falloff
                cwt = "tb_sculpt_falloff"
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='FCURVE')
                    row.prop(brush, "curve_preset", text="")
                if cw == True:       
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='FCURVE')                                                                             
                    row.prop(brush, "curve_preset", text="")
                    if brush.curve_preset == 'CUSTOM':
                        row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
                        row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
                        row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
                        row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
                        row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
                        row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
                        bow.template_curve_mapping(brush, "curve", brush=True)
                    if ob.mode == 'SCULPT':
                        if brush.sculpt_tool != 'POSE':
                            row = box.row(align=True)
                            row.use_property_split = True
                            row.use_property_decorate = False
                            row.prop(brush, "falloff_shape", expand=True)
                    if ob.mode == 'TEXTURE_PAINT': 
                        row = bow.row(align=True)
                        if ipaint.use_normal_falloff == False:
                            row.prop(ipaint, "use_normal_falloff", text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                     
                        else:
                            row.prop(ipaint, "use_normal_falloff", text="Angle",icon='DRIVER_ROTATIONAL_DIFFERENCE')                                                                                     
                            row.prop(ipaint, "normal_angle", text="Angle")                                                                                     
                    if ob.mode == 'WEIGHT_PAINT' or ob.mode == 'VERTEX_PAINT':
                        row = bow.row(align=True)
                        if brush.use_frontface_falloff == False:             
                            row.prop(brush, "use_frontface_falloff", text="Frontface_Falloff",icon='FACESEL')                                                                       
                        else:
                            row.prop(brush, "use_frontface_falloff", text="",icon='FACESEL')
                            row.prop(brush, "falloff_angle")                                        
                    #Advance
                cw = wm.tb_wm_bool.tb_brush_advanced
                cwt = "tb_brush_advanced"
                bow = box.box()
                row = bow.row(align=False)                
                if cw == False:
                    row.prop(wm.tb_wm_bool, cwt,text="Advanced",icon='BRUSH_DATA')
                if cw == True:   
                    row.prop(wm.tb_wm_bool, cwt,text="",icon='BRUSH_DATA')  
                    if ob.mode == 'SCULPT':
                        capabilities = brush.sculpt_capabilities
                        use_accumulate = capabilities.has_accumulate
                        use_frontface = True
                        cw = wm.tb_wm_bool.tb_brush_automask
                        cwt = "tb_brush_automask"
                        if cw == False:
                            row.prop(wm.tb_wm_bool, cwt,text="Auto-Masking",icon='MOD_MASK')
                        if cw == True:
                            row = bow.row(align=False)                
                            row.prop(wm.tb_wm_bool, cwt,text="",icon='MOD_MASK')      
                            row.prop(brush, "use_automasking_topology", text="Topology",icon='VIEW_ORTHO')
                            row.prop(brush, "use_automasking_face_sets", text="Face Sets",icon='MOD_EXPLODE')
                            row = bow.row()
                            row.label(icon='BLANK1')
                            row.prop(brush, "use_automasking_boundary_edges", text="Mesh Boundary",icon='PIVOT_BOUNDBOX')
                            row.prop(brush, "use_automasking_boundary_face_sets", text="Face Sets Boundary",icon='MOD_MESHDEFORM')
                            row = bow.row()   
                            row.label(icon='BLANK1')                                                     
                            row.prop(brush, "automasking_boundary_edges_propagation_steps")
                        if capabilities.has_sculpt_plane:
                            bow.prop(brush, "sculpt_plane",text="")
                            row = bow.row(align=False)                
                            row.label(text="Use Original")
                            row.prop(brush, "use_original_normal", text="Normal",icon='NORMALS_FACE')
                            row.prop(brush, "use_original_plane", text="Plane",icon='ORIENTATION_NORMAL')
                    if ob.mode == 'TEXTURE_PAINT':
                        capabilities = brush.image_paint_capabilities                        
                        row.prop(brush, "use_alpha",icon='IMAGE_RGB_ALPHA')
                        if brush.image_tool == 'SOFTEN':
                            box.row().prop(brush, "direction", expand=True)
                            box.prop(brush, "sharp_threshold")
                            box.prop(brush, "blur_mode",text="")
                        elif brush.image_tool == 'MASK':
                            box.prop(brush, "weight", text="Mask Value", slider=True)
                        if use_accumulate:
                            row.prop(brush, "use_accumulate",icon='ADD')                    
                    if ob.mode == 'WEIGHT_PAINT' or ob.mode == 'VERTEX_PAINT' or ob.mode =='SCULPT':
                        if ob.mode == 'VERTEX_PAINT':
                            row.prop(brush, "use_alpha",icon='IMAGE_RGB_ALPHA')                            
                        if ob.mode == 'SCULPT':
                            row = box.row(align=False)                                            
                        if brush.weight_tool != 'SMEAR':
                            use_accumulate = True
                        else:
                            use_accumulate = False                        
                        use_frontface = True
                        if use_accumulate:
                            row.prop(brush, "use_accumulate",icon='ADD')
                        if use_frontface:
                            row.prop(brush, "use_frontface", text="Front Faces Only",icon='AXIS_FRONT')                                                                        



def tbtooldatadraw(self, context):
    wm = context.window_manager
    ob = bpy.context.object
    layout = self.layout
    if ob.mode in ['EDIT','EDIT_GPENCIL','OBJECT']:
        box = layout.box()
        tbtoolorientation(context,box)
    if ob.type == 'MESH' and ob.mode == 'EDIT':
        tbmesheditclean(context,box) 
    if ob.mode in ['TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT']:      
        box = layout.box()
        tbtoolbrush(context,box,box)
    if ob.mode in ['SCULPT','TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT']:
        box = layout.box()
        tbtoolstroke(context,box,box)    
    if ob.mode == 'TEXTURE_PAINT':   
        box = layout.box()
        tbtooltexturetextures(context,box,box)          
    if ob.mode in ['TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT','EDIT']:   
        box = layout.box()
        tbtoolsettings(context,box,box)        

def tbooldatadrawpop(self,context):
    wm = context.window_manager
    ob = bpy.context.object
    layout = self.layout
    split = layout.split(align=True)
    if ob.mode in ['EDIT','EDIT_GPENCIL','OBJECT']:
        layout = split.column(align=True)
        box = layout.box()
        tbtoolorientation(context,box)
    if ob.type == 'MESH':
        if bpy.context.object.mode == 'EDIT':
            #layout = split.column(align=True)
            #box = layout.box()
            tbmesheditclean(context,box) 
    if ob.mode in ['TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT']:      
        layout = split.column(align=True)
        box = layout.box()
        tbtoolbrush(context,box,split)
    if ob.mode in ['SCULPT','TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT']:
        layout = split.column(align=True)
        box = layout.box()
        tbtoolstroke(context,box,split)    
    if ob.mode == 'TEXTURE_PAINT':    
        layout = split.column(align=True)
        box = layout.box()
        tbtooltexturetextures(context,box,split)          
    if ob.mode in ['TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT','EDIT']:   
        layout = split.column(align=True)
        box = layout.box()
        tbtoolsettings(context,box,split)      



class TB_Data_Tool_UI_3D(bpy.types.Panel):
    bl_label = "Tool Data"
    bl_idname = "TBPNL_PT_tool_data"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    @classmethod
    def poll(cls, context):
        return context.object is not None and (bpy.context.mode in ['TEXTURE_PAINT','VERTEX_PAINT','WEIGHT_PAINT','SCULPT','EDIT','EDIT_MESH','EDIT_GPENCIL','OBJECT'])
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='SCULPTMODE_HLT')        
    def draw(self, context):
        tbtooldatadraw(self, context)
class TB_Data_Tool_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_label = "Tool Data PoP"
    bl_idname = "context.tbtoolpopup"
    @classmethod
    def poll(cls, context):
        return context.object is not None
    def invoke(self, context, event):
        if bpy.context.object.mode == 'OBJECT':
            widthsize = 300
        elif bpy.context.object.mode in ['EDIT','VERTEX_PAINT','WEIGHT_PAINT']:
            widthsize = 700  
        elif bpy.context.object.mode in ['TEXTURE_PAINT']:
            widthsize = 1200
        elif bpy.context.object.mode == 'SCULPT':
            widthsize = 700                        
        else:
            widthsize = 500
        return context.window_manager.invoke_props_dialog(self, width = widthsize)         
    def draw (self, context):
        tbooldatadrawpop(self,context)
    def execute(self, context):
        return {'FINISHED'}