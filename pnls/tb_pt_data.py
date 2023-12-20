import bpy
from bpy.types import Curve, SurfaceCurve, TextCurve
from bl_ui.properties_physics_common import (
    basic_force_field_settings_ui,
    basic_force_field_falloff_ui,
)

def use_branched_path(context):
    cscene = context.scene.cycles
    return (cscene.progressive == 'BRANCHED_PATH' and not use_optix(context))

def tbdatamain(context,box,layout):
    wm = context.window_manager
    tbb = wm.tb_wm_bool 
    ob = context.object
    mesh = ob.data
    obd = ob.data
    if bpy.context.object:
        me = context.object.data
        arm = context.object.data
        screen = context.screen
        if ob:
            if bpy.context.object.type == 'EMPTY':
                row = box.row(align= True)
            #elif bpy.context.object.type == 'MESH':
                #row.template_ID(space, "pin_id")
            else:  
                row = box.row(align= True)  
                row.template_ID(ob, "data")
      #OBJECTS
       #DATA
        if ob.type == 'EMPTY':
            row.prop(ob, "empty_display_type", text="")
            box.prop(ob, "empty_display_size", text="Size")
        if bpy.context.scene.render.engine == 'CYCLES' and (ob.type in ['MESH','CURVE','SURFACE','FONT','META','LIGHT']):
            cob = ob.cycles
            row.prop(cob, "is_shadow_catcher", text="", invert_checkbox=True, toggle=False,icon='INDIRECT_ONLY_OFF')
            row.prop(cob, "is_holdout", text="", toggle=False,icon='HOLDOUT_ON')
        row.prop(ob, "hide_viewport", text="", toggle=False, emboss=False, icon='HIDE_OFF')
        #row.label(text="",icon_value=bpy.context.scene.asd_icons['UP'].icon_id)                
        row.prop(ob, "hide_render", text="", toggle=False, emboss=False,icon='RESTRICT_RENDER_OFF')
        row.prop(ob, "hide_select", text="", toggle=False, emboss=False,icon='RESTRICT_SELECT_OFF')
       #EMPTY            
        if ob.type == 'EMPTY':
            if ob.empty_display_type == 'IMAGE':
                box.template_ID(ob, "data", open="image.open", unlink="object.unlink_data")
                box.template_image(ob, "data", ob.image_user, compact=True)
                row = box.row(align= True)  
                if ob.use_empty_image_alpha == True:
                    row.prop(ob, "use_empty_image_alpha",text="",icon='IMAGE_RGB_ALPHA')
                    row.prop(ob, "color", text="Opacity", index=3, slider=True)
                else:
                    row.prop(ob, "use_empty_image_alpha",icon='IMAGE_RGB_ALPHA')

                row = box.row(align=True)
                row.label(text="Offset")
                row.label(icon='EVENT_X')
                row.prop(ob, "empty_image_offset", text="X", index=0)
                row.label(icon='EVENT_Y')
                row.prop(ob, "empty_image_offset", text="Y", index=1)

                col = box.column()
                col.row().prop(ob, "empty_image_depth", text="Depth", expand=True)
                col.row().prop(ob, "empty_image_side", text="Side", expand=True)
                row = box.row(align=True)
                row.label(icon='HIDE_OFF')
                row.prop(ob, "show_empty_image_orthographic", text="Orthographic",icon='VIEW_ORTHO')
                row.prop(ob, "show_empty_image_perspective", text="Perspective",icon='VIEW_PERSPECTIVE')
                row.prop(ob, "show_empty_image_only_axis_aligned",text="Axis Allign",icon='EMPTY_AXIS')
            field = ob.field
            if not field or field.type == 'NONE':
                row = box.row(align=True)       
                row.operator("object.forcefield_toggle", text="Force Field", icon='FORCE_FORCE')
            else:
                row.operator("object.forcefield_toggle", text="", icon='X')
                if field.type != 'NONE':
                    row = box.row(align=True)
                    row.prop(field, "type",text="")
                    if field.type not in {'NONE', 'GUIDE', 'TEXTURE'}:
                        row = box.row(align=True)
                        row.prop_enum(field, "shape", "POINT",text="",icon='DECORATE')
                        if not field.type in {'GUIDE','VORTEX'}:
                            row.prop_enum(field, "shape", "LINE",text="",icon='IPO_LINEAR')
                        row.prop_enum(field, "shape", "PLANE",text="",icon='MESH_PLANE')
                if field.type == 'GUIDE':
                    row = box.row(align=True)
                    row.prop(field, "guide_minimum")
                    row.prop(field, "guide_free")
                    row.prop(field, "falloff_power")
                    row.prop(field, "use_guide_path_add",text="",icon='ADD')
                    row.prop(field, "use_guide_path_weight",text="",icon='MOD_VERTEX_WEIGHT')
                    row = box.row(align=True)
                    row.prop(field, "guide_clump_amount", text="Clumping Amount")
                    row.prop(field, "guide_clump_shape")
                    row.prop(field, "use_max_distance",text="",icon='TRIA_UP')
                    if field.use_max_distance == True:
                        row.prop(field, "distance_max")
                    row = box.row(align=True)
                    row.prop(field, "guide_kink_type",text="",icon='PARTICLE_TIP')
                    if field.guide_kink_type != 'NONE':
                        row.prop(field, "guide_kink_axis")
                        row = box.row(align=True)
                        row.prop(field, "guide_kink_frequency")
                        row.prop(field, "guide_kink_shape")
                        row.prop(field, "guide_kink_amplitude")
                elif field.type == 'TEXTURE':
                    row = box.row(align=True)
                    row.template_ID(field, "texture", new="texture.new")
                    row = box.row(align=True)
                    row.prop(field, "texture_mode")
                    row.prop(field, "strength")
                    row.prop(field, "apply_to_location", text="",icon='EMPTY_ARROWS')
                    row = box.row(align=True)
                    row.prop(field, "texture_nabla",icon='NODE_TEXTURE')
                    row.prop(field, "use_object_coords",text="",icon='CON_LOCLIKE')
                    row.prop(field, "use_2d_force",text="",icon='CON_LOCLIMIT')
                if field.type == 'FLUID_FLOW':
                    row = box.row(align=True)
                    row.prop(field, "strength")
                    row.prop(field, "flow")
                    row.prop(field, "apply_to_rotation", text="",icon='CON_LOCLIKE')
                    row.prop(field, "apply_to_location", text="",icon='CON_ROTLIKE')
                    row = box.row(align=True)
                    row.prop(field, "source_object",text="")
                    row.prop(field, "use_smoke_density",text="",icon='MOD_FLUID')
                else:
                    if field.type == 'DRAG':
                        row.prop(field, "linear_drag", text="Linear")
                    else:
                        row.prop(field, "strength")
                    if field.type == 'TURBULENCE':
                        row.prop(field, "size")
                        row.prop(field, "flow")
                    elif field.type == 'HARMONIC':
                        row.prop(field, "harmonic_damping", text="Damping")
                        row.prop(field, "rest_length")
                    elif field.type == 'VORTEX' and field.shape != 'POINT':
                        row.prop(field, "inflow")
                    elif field.type == 'DRAG':
                        row.prop(field, "quadratic_drag", text="Quadratic")
                    else:
                        row.prop(field, "flow")
                    row.prop(field, "apply_to_location", text="",icon='CON_LOCLIKE')
                    row.prop(field, "apply_to_rotation", text="", icon='CON_ROTLIKE')
                    row = box.row(align=True)
                    row.prop(field, "noise", text="Noise Amount")
                    row.prop(field, "seed", text="Seed")

                    if field.type == 'TURBULENCE':
                        row.prop(field, "use_global_coords", text="Global")

                    elif field.type == 'HARMONIC':
                        row.prop(field, "use_multiple_springs")
                    row = box.row(align=True)
                    row.prop(field, "wind_factor",icon='FORCE_WIND')            
                    if field.type == 'FORCE':
                        row.prop(field, "use_gravity_falloff", text="Gravitation")
                    row.prop(field, "use_absorption")
       #SPEAKER
        if ob.type == 'SPEAKER':
            speaker = context.object.data
            box = layout.box()
            row = box.row(align=True)
            row.template_ID(speaker, "sound", open="sound.open_mono")
            row.prop(speaker, "muted",text="",icon='OUTLINER_DATA_SPEAKER')
            row = box.row(align=True)
            row.label(icon='PLAY_SOUND')                
            row.prop(speaker, "volume", slider=True)
            row.prop(speaker, "pitch")
            row = box.row(align=True)
            row.label(icon='SPEAKER')
            row.prop(speaker, "volume_min", slider=True, text="Volume Min")
            row.prop(speaker, "volume_max", slider=True, text="Max")
            row = box.row(align=True)
            row.label(icon='DRIVER_DISTANCE')
            row.prop(speaker, "distance_reference", text="Ref Distance")
            row.prop(speaker, "distance_max", text="Max Distance")
            row = box.row(align=True)
            row.label(icon='FCURVE')
            row.prop(speaker, "attenuation")
            bow = box.box()
            row = bow.row(align=True)
            row.label(text="Cone",icon='CONE')
            row.prop(speaker, "cone_volume_outer", slider=True,text="Volume Outer Cone")
            row = bow.row(align=True)
            row.label(icon='BLANK1')
            row.label(icon='DRIVER_ROTATIONAL_DIFFERENCE')
            row.prop(speaker, "cone_angle_outer", text="Outer")
            row.prop(speaker, "cone_angle_inner", text="Inner")
       #CAMERA
        if ob.type == 'CAMERA':
            cam = context.object.data
            box = layout.box()
            row = box.row(align=True)
            row.prop_enum(cam, "type", "PERSP",icon='VIEW_PERSPECTIVE')
            row.prop_enum(cam, "type", "ORTHO",icon='VIEW_ORTHO')
            row.prop_enum(cam, "type", "PANO",icon='GRID')
            col = box.column()
            if cam.type == 'PERSP':
                row = box.row(align=True)
                if cam.lens_unit == 'MILLIMETERS':
                    row.prop(cam, "lens")
                elif cam.lens_unit == 'FOV':
                    row.prop(cam, "angle")
                row.prop(cam, "lens_unit",text="")
            elif cam.type == 'ORTHO':
                row = box.row(align=True)
                row.prop(cam, "ortho_scale")
            elif cam.type == 'PANO':
                engine = context.engine
                if engine == 'CYCLES':
                    ccam = cam.cycles
                    box.prop(ccam, "panorama_type",text="")
                    if ccam.panorama_type == 'FISHEYE_EQUIDISTANT':
                        box.prop(ccam, "fisheye_fov")
                    elif ccam.panorama_type == 'FISHEYE_EQUISOLID':
                        row = box.row()
                        row.prop(ccam, "fisheye_lens", text="Lens")
                        row.prop(ccam, "fisheye_fov")
                    elif ccam.panorama_type == 'EQUIRECTANGULAR':
                        split = box.split(align=True)
                        sub = split.column(align=True)                            
                        sub.label(text="Latitude")
                        sub.prop(ccam, "latitude_min", text="Min")
                        sub.prop(ccam, "latitude_max", text="Max")
                        sub = split.column(align=True)
                        sub.label(text="Longitude")                                                        
                        sub.prop(ccam, "longitude_min", text="Min")
                        sub.prop(ccam, "longitude_max", text="Max")
                elif engine in {'BLENDER_RENDER', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH'}:
                    if cam.lens_unit == 'MILLIMETERS':
                        col.prop(cam, "lens")
                    elif cam.lens_unit == 'FOV':
                        col.prop(cam, "angle")
                    col.prop(cam, "lens_unit")

            col = layout.column()
            col.separator()
            split = box.split(align=True)
            col = split.column(align=True)
            col.label(text="Shift")
            col.prop(cam, "shift_x", text="X")
            col.prop(cam, "shift_y", text="Y")
            col = split.column(align=True)
            col.label(text="Clip")
            col.prop(cam, "clip_start", text="Start")
            col.prop(cam, "clip_end", text="End")
            dof = cam.dof
            if bpy.context.object.data.dof.use_dof == False:
                box.prop(dof, "use_dof", text="Deph of Field",icon='VIEW_PERSPECTIVE')
            if bpy.context.object.data.dof.use_dof == True:
                row = box.row(align=True)
                row.prop(dof, "use_dof", text="",icon='VIEW_PERSPECTIVE')
                row.prop(dof, "focus_object", text="")
                row.label(icon='DRIVER_DISTANCE')
                row.prop(dof, "focus_distance", text="")
                split = box.split(align=True)
                col = split.column(align=True)      
                col.prop(dof, "aperture_fstop")
                col.prop(dof, "aperture_blades")
                col = split.column(align=True)                     
                col.prop(dof, "aperture_rotation")
                col.prop(dof, "aperture_ratio")
       #FONT           
        if ob.type == 'FONT':
            text = context.object.data
            box = layout.box()
            char = text.edit_format
            mode = context.mode
            if mode == 'EDIT_TEXT':
                row = box.row(align=True)
                row.prop(char, "use_bold", toggle=True)
                row.prop(char, "use_italic", toggle=True)
                row = box.row(align=True)
                row.prop(char, "use_underline", toggle=True)
                row.label(icon='CON_LOCLIMIT')
                row.prop(text, "underline_position", text="Underline Position")
                row.label(icon='MOD_THICKNESS')
                row.prop(text, "underline_height", text="Underline Thickness")
                row = box.row(align=True)
                row.prop(char, "use_small_caps", toggle=True)
                row.label(icon='SMALL_CAPS')
                row.prop(text, "small_caps_scale", text="Small Caps Scale")
            row = box.row(align=True)
            row.prop(text, "align_x", text="")
            row.prop(text, "align_y", text="")
            row = box.row(align=True)
            row.label(icon='FONT_DATA')
            row.prop(text, "space_character", text="Character Spacing")
            row.label(icon='SORTSIZE')
            row.prop(text, "space_word", text="Word Spacing")
            row.label(icon='COLLAPSEMENU')
            row.prop(text, "space_line", text="Line Spacing")
            row = box.row(align=True)
            row.label(icon='CON_LOCLIMIT')
            row.prop(text, "offset_x", text="X")
            row.prop(text, "offset_y", text="Y")
            row = box.row(align=True)
            row.label(icon='CON_SIZELIMIT')
            row.prop(text, "size", text="Size")
            row.label(icon='ITALIC')
            row.prop(text, "shear")
            row = box.row(align=True)
            row.prop(text, "family",icon='OBJECT_DATA',text="")
            row.prop(text, "follow_curve",text="",icon='CURVE_DATA')

            if bpy.context.object:
                box = layout.box()
                if not tbb.tb_obj_font_font:
                    row = box.row(align= True)     
                    row.prop(tbb, "tb_obj_font_font",text="Font_properties",icon='FILE_FONT')
                else:
                    char = text.edit_format
                    mode = context.mode
                    row = box.row(align= True)
                    row.prop(tbb, "tb_obj_font_font",text="",icon='FILE_FONT')
                    row.separator()
                    row.label(text="Regular",icon='FONT_DATA')
                    row.template_ID(text, "font", open="font.open", unlink="font.unlink")
                    row = box.split(factor=0.25)
                    row.label(text="Italic",icon='ITALIC')
                    row.template_ID(text, "font_italic", open="font.open", unlink="font.unlink")
                    row = box.split(factor=0.25)
                    row.label(text="Bold",icon='BOLD')
                    row.template_ID(text, "font_bold", open="font.open", unlink="font.unlink")
                    row = box.split(factor=0.25)
                    row.label(text="Bold & Italic",icon='FONTPREVIEW')
                    row.template_ID(text, "font_bold_italic", open="font.open", unlink="font.unlink")
                    box = layout.box()
                    row = box.row()
                    row.prop(text, "overflow", text="")
                    row.operator("font.textbox_add", icon='ADD')
                    for i, box in enumerate(text.text_boxes):
                        boxy = layout.box()
                        row = boxy.row()
                        row.label(icon='CON_SIZELIMIT')
                        row.prop(box, "width", text="X")
                        row.prop(box, "height", text="Y")
                        row.operator("font.textbox_remove", text="", icon='X', emboss=False).index = i
                        row = boxy.row()
                        row.label(icon='CON_LOCLIMIT')
                        row.prop(box, "x", text="X")
                        row.prop(box, "y", text="Y")
                        row.label(icon='BLANK1')                           
       #SHARED FONT,SURFACE, CURVE
        if ob.type == 'FONT' or ob.type == 'SURFACE' or ob.type == 'CURVE':
            if bpy.context.object:
                box = layout.box()
                row = box.row(align= True)     
                if not tbb.tb_obj_curve_prop:
                    row.prop(tbb, "tb_obj_curve_prop",text="Curve Settings",icon='OUTLINER_DATA_CURVE')
                else:
                    curve = context.object.data
                    is_surf = type(curve) is SurfaceCurve
                    is_curve = type(curve) is Curve
                    is_text = type(curve) is TextCurve
                    row.separator()
                    row.prop(tbb, "tb_obj_curve_prop",text="",icon='OUTLINER_DATA_CURVE')
                    #row = box.row(align=True)
                    if is_curve:
                        row.prop(curve, "dimensions", expand=True)
                    if is_curve or is_text:
                        row.active = (curve.dimensions == '2D' or (curve.bevel_object is None and curve.dimensions == '3D'))
                        row.prop(curve, "fill_mode",text="")
                        row.prop(curve, "use_fill_deform",icon='SELECT_SUBTRACT')
                    row = box.row(align=True)
                    if is_curve:
                        row = box.row(align=True)
                        row.prop(curve, "twist_mode",icon='FORCE_VORTEX',text="")
                        row.prop(curve, "twist_smooth", text="Smooth")
                        row = box.row(align=True)
                    if is_text:
                        row.prop(curve, "use_fast_edit", text="",icon='EDITMODE_HLT')
                        row = box.row(align=True)
                    row.prop(curve, "resolution_u", text="Preview U")
                    if is_surf:
                        row.prop(curve, "resolution_v", text="V")
                        row = box.row(align=True )
                    row.prop(curve, "render_resolution_u", text="Render U")
                    if is_surf:
                        row.prop(curve, "render_resolution_v", text="V")
                    row == box.row(align=True)
                    if is_curve:
                        row = box.row()
                        row.prop(curve, "use_radius",icon='CURVE_BEZCIRCLE')
                        row.prop(curve, "use_stretch",icon='CON_STRETCHTO')
                        row.prop(curve, "use_deform_bounds",icon='PIVOT_BOUNDBOX')
                    bow = box.box()
                    if is_curve or is_text:
                        row = bow.row(align=True)                           
                        row.label(icon='MESH_DATA')
                        row.label(icon='CON_SIZELIMIT')
                        row.prop(curve, "offset")
                        sub = row.row(align=True)
                        sub.active = (curve.bevel_object is None)
                        sub.label(icon='MOD_SOLIDIFY')
                        sub.prop(curve, "extrude")
                        row.prop(curve, "taper_object",text="")
                        if type(curve) is not TextCurve:
                            sub = row.row(align=True)
                            sub.active = curve.taper_object is not None
                            sub.prop(curve, "use_map_taper",icon='LIGHTPROBE_CUBEMAP',text="")
                    row = bow.row(align=True)
                    row.label(icon='BLANK1')
                    row.label(icon='MOD_BEVEL')
                    row.active = (curve.bevel_object is None)
                    row.prop(curve, "bevel_depth", text="Depth")
                    row.prop(curve, "bevel_resolution", text="Resolution")
                    row.prop(curve, "bevel_object", text="")
                    sub = row.row()
                    sub.active = curve.bevel_object is not None
                    sub.prop(curve, "use_fill_caps",text="",icon='FCURVE_SNAPSHOT')
                    if type(curve) is Curve:
                        col = box.column()
                        col.active = ((curve.bevel_depth > 0.0) or(curve.extrude > 0.0) or(curve.bevel_object is not None))
                        sub = col.column(align=True)
                        sub.prop(curve, "bevel_factor_start", text="Bevel Start")
                        sub.prop(curve, "bevel_factor_end", text="End")
                        sub = col.column(align=True)
                        sub.prop(curve, "bevel_factor_mapping_start", text="Bevel Mapping Start")
                        sub.prop(curve, "bevel_factor_mapping_end", text="End")
             
       #SURFACE                        
        if ob.type == 'SURFACE':
            curve = context.object.data
            act_spline = curve.splines.active
            is_surf = type(curve) is SurfaceCurve
            is_poly = (act_spline.type == 'POLY')
            row = box.row(align=True)
            row.label(icon='PIVOT_ACTIVE',text="Active Spline")
            row.prop(act_spline, "use_smooth",icon='MOD_SMOOTH')
            if is_poly:
                split = box.split(factor=0.8,align=True)
                col = split.column(align=True)
                # These settings are below but its easier to have
                # polys set aside since they use so few settings
                col.prop(act_spline, "use_cyclic_u")
                col.prop(act_spline, "use_smooth")
            else:
                split = box.split(align=True)
                col = split.column(align=True)
                col.label(text="Cyclic")
                col.prop(act_spline, "use_cyclic_u",icon='EVENT_U',text="")
                if is_surf:
                    col.prop(act_spline, "use_cyclic_v",icon='EVENT_V',text="")
                if act_spline.type == 'NURBS':
                    row = box.row()
                    if is_surf:
                        row.active = (not act_spline.use_cyclic_v)
                if act_spline.type == 'NURBS':
                    col = split.column(align=True)
                    col.label(text="Bezier")
                    # col.active = (not act_spline.use_cyclic_u)
                    col.prop(act_spline, "use_bezier_u",icon='EVENT_U',text="")

                    if is_surf:
                        sub = col.column(align=True)
                        sub.active = (not act_spline.use_cyclic_v)
                        sub.prop(act_spline, "use_bezier_v",icon='EVENT_V',text="")
                    col = split.column(align=True)
                    col.label(text="Endpoint")
                    col.prop(act_spline, "use_endpoint_u",icon='EVENT_U', text="")
                    if is_surf:
                        sub = col.column(align=True)
                        sub.active = (not act_spline.use_cyclic_v)
                        sub.prop(act_spline, "use_endpoint_v", text="",icon='EVENT_V')
                    col = split.column(align=True)
                    col.label(text="Order")
                    col.prop(act_spline, "order_u", text="U")
                    if is_surf:
                        col.prop(act_spline, "order_v", text="V")
                col = split.column(align=True)
                col.label(text="Resolution")
                col.prop(act_spline, "resolution_u", text="U")
                if is_surf:
                    col.prop(act_spline, "resolution_v", text="V")
                if act_spline.type == 'BEZIER':
                    col.separator()
                    sub = col.column()
                    sub.active = (curve.dimensions == '3D')
                    sub.prop(act_spline, "tilt_interpolation", text="Interpolation Tilt")
                    col.prop(act_spline, "radius_interpolation", text="Radius")
        if ob.type == 'LIGHT_PROBE':
            probe = context.object.data
            box.prop(probe, "type",text="")
            if probe.type == 'GRID':
                row = box.row(align=True)
                row.label(icon='DRIVER_DISTANCE') 
                row.prop(probe, "influence_distance", text="Distance")
                row.prop(probe, "falloff")
                row = box.row(align=True)
                row.prop(probe, "intensity")
                row = box.row(align=True)
                row.label(icon='MOD_MULTIRES')
                row.prop(probe, "grid_resolution_x", text="X")
                row.prop(probe, "grid_resolution_y", text="Y")
                row.prop(probe, "grid_resolution_z", text="Z")
            elif probe.type == 'PLANAR':
                row = box.row(align=True)
                row.label(icon='DRIVER_DISTANCE') 
                row.prop(probe, "influence_distance", text="Distance")
                row.prop(probe, "falloff")
            else:
                row = box.row(align=True)
                row.prop_enum(probe, "influence_type","ELIPSOID",icon='META_ELLIPSOID')
                row.prop_enum(probe, "influence_type","BOX",icon='META_CUBE')                    
                row = box.row(align=True)

                if probe.influence_type == 'ELIPSOID':
                    row.label(icon='DRIVER_DISTANCE') 
                    row.prop(probe, "influence_distance", text="Radius")
                else:
                    row.label(icon='DRIVER_DISTANCE') 
                    row.prop(probe, "influence_distance", text="Size")
                row.prop(probe, "falloff")
                row.prop(probe, "intensity")
            row = box.row(align=True)
            row.label(icon='CON_DISTLIMIT')
            if probe.type != 'PLANAR':
                row.prop(probe, "clip_start", text="Clipping Start")
            else:
                row.prop(probe, "clip_start", text="Clipping Offset")
            if probe.type != 'PLANAR':
                row.prop(probe, "clip_end", text="End")
                row = box.row(align=True)
                if bpy.context.object.data.use_custom_parallax == False:
                    row.prop(context.object.data,"use_custom_parallax",icon='MATSPHERE')
                if bpy.context.object.data.use_custom_parallax == True:
                    row.prop(context.object.data,"use_custom_parallax",text="",icon='MATSPHERE')
                    row.prop_enum(probe, "parallax_type","BOX",icon='META_CUBE')
                    row.prop_enum(probe, "parallax_type","ELIPSOID",icon='META_ELLIPSOID')
                    if probe.parallax_type == 'ELIPSOID':
                        row.prop(probe, "parallax_distance", text="Radius")
                    else:
                        row.prop(probe, "parallax_distance", text="Size")
            row = box.row(align=True)
            bow = box.box()
            row = bow.row(align=True)
            row.label(icon='HIDE_OFF')
            if probe.type == 'PLANAR':
                row.label(icon='EMPTY_SINGLE_ARROW') 
                row.prop(ob, "empty_display_size", text="Arrow Size")
                row.prop(probe, "show_data",text="",icon='IMAGE_PLANE') 
                row.prop(probe, "show_influence",icon='PIVOT_BOUNDBOX',text="") 
            if probe.type in {'GRID', 'CUBEMAP'}:
                row.prop(probe, "show_influence",icon='LIGHTPROBE_GRID')
                row.prop(probe, "show_clip",icon='EMPTY_AXIS')
                if bpy.context.object.data.use_custom_parallax == True:
                    row.prop(context.object.data,"show_parallax",icon='MATSPHERE')
            if probe.type == 'CUBEMAP':
                sub = col.column()
                sub.active = probe.use_custom_parallax
                sub.prop(probe, "show_parallax")       
                if ob.type == 'EMPTY':
                    row = box.row()
                    row.prop(ob, "empty_display_type", text="")
                    row.prop(ob, "empty_display_size", text="Size")
                    if bpy.context.object.empty_display_type == 'IMAGE':
                        box.template_ID(ob, "data", open="image.open", unlink="object.unlink_data")
       #LIGHT                
        if ob.type == 'LIGHT':
            light = context.object.data
            clamp = light.cycles
            row = box.row(align=True)
            row.prop_enum(light,"type","POINT",icon='LIGHT_POINT')
            row.prop_enum(light,"type","SUN",icon='LIGHT_SUN')
            row.prop_enum(light,"type","SPOT",icon='LIGHT_SPOT')
            row.prop_enum(light,"type","AREA",icon='LIGHT_AREA')
            if light.type == 'AREA':
                row = box.row(align=True)
                row.prop_enum(light, "shape", "SQUARE", text="Square",icon='MESH_PLANE')
                row.prop_enum(light, "shape", "RECTANGLE", text="Rectangle",icon='MESH_GRID')
                row.prop_enum(light, "shape", "DISK", text="Disk",icon='MESH_TORUS')
                row.prop_enum(light, "shape", "ELLIPSE", text="Ellipse",icon='META_ELLIPSOID')                                                            
            row = box.row(align=True)
            row.prop(light, "color",text="")
            row.prop(light, "energy")
            if light.type == 'SPOT':
                row = box.row(align=True)
                row.prop(light, "show_cone",text="",icon='CONE')                    
                row.prop(light, "spot_size", text="Radious")
                row.prop(light, "spot_blend", text="Blend", slider=True)
            row = box.row(align=True)
            if light.type in {'POINT', 'SPOT'}:
                row.prop(light, "shadow_soft_size", text="Radius")
            elif light.type == 'SUN':
                row.prop(light, "angle")
            elif light.type == 'AREA':
                if light.shape in {'SQUARE', 'DISK'}:
                    row.prop(light, "size")
                elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                    row.prop(light, "size", text="X")
                    row.prop(light, "size_y", text="Y")
            row = box.row(align = True)
            row.prop(context.object.data,"diffuse_factor")
            row.prop(context.object.data,"specular_factor")
            row.prop(context.object.data,"volume_factor")
            if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
                if light.type in {'AREA','SPOT','POINT'}:
                    row = box.row(align = True)
                    if not bpy.context.object.data.use_custom_distance:
                        row.prop(context.object.data,"use_custom_distance",text="Custom Distance",icon='DRIVER_DISTANCE')
                    else:
                        row.prop(context.object.data,"use_custom_distance",text="",icon='DRIVER_DISTANCE')
                        row.prop(context.object.data,"cutoff_distance")
            row = box.row(align = True)
            if bpy.context.object.data.use_shadow == False:
                row.prop(context.object.data,"use_shadow",text="Use Shadow",icon='MATSHADERBALL')
            else:
                bow = box.box()
                row = bow.row(align = True)
                row.prop(obd,"use_shadow",text="",icon='MATSHADERBALL')
                if not light.type == 'SUN':
                    row.prop(context.object.data,"shadow_buffer_clip_start",text="Clip Start")
                row.prop(context.object.data,"shadow_buffer_bias",text="Bias")
                row = bow.row(align = True)
                if bpy.context.object.data.use_contact_shadow == False:
                    row.prop(context.object.data,"use_contact_shadow",icon='SHAPEKEY_DATA')
                else:
                    row.prop(context.object.data,"use_contact_shadow",text="",icon='SHAPEKEY_DATA')
                    row.prop(context.object.data,"contact_shadow_distance")
                    row.prop(context.object.data,"contact_shadow_bias")
                    row.prop(context.object.data,"contact_shadow_thickness")
                if light.type == 'SUN':
                    bow = bow.box()
                    row = bow.row(align = True)
                    row.prop(obd,"shadow_cascade_count",text="Cascade")
                    row.prop(obd,"shadow_cascade_fade",text="Fade")
                    row.prop(obd,"shadow_cascade_max_distance",text="Max Distance")
                    row.prop(obd,"shadow_cascade_exponent",text="Distribution")

            if bpy.context.scene.render.engine == 'CYCLES':    
                if not (light.type == 'AREA' and clamp.is_portal):
                    row.prop(clamp, "max_bounces")
                    if use_branched_path(context):
                        row.active = use_sample_all_lights(context)
                        row.prop(clamp, "samples")
                row = box.row()
                row.prop(clamp, "cast_shadow",icon='SHADING_RENDERED')
                row.prop(clamp, "use_multiple_importance_sampling", text="Multiple Importance",icon='MOD_MULTIRES')
                if light.type == 'AREA':
                    row.prop(clamp, "is_portal", text="Portal",icon='HOLDOUT_ON')
                    row = box.row()
                    row.prop(context.object.data,"spread")
       #META
        if bpy.context.object.type == 'META':
            mball = context.object.data
            metaelem = mball.elements.active
            row = box.row(align=True)
            row.prop(mball, "resolution", text="Resolution Viewport")
            row.prop(mball, "render_resolution", text="Render")
            row = box.row(align=True)
            row.prop(mball, "threshold", text="Influence Threshold")
            row.separator()
            row.prop(mball, "update_method", text="",icon='RECOVER_LAST')
            row = box.row(align=True)
            if metaelem:
                row.label(icon='PIVOT_ACTIVE',text="Active Element")
                row.prop(metaelem, "use_negative", text="Boolean",icon='MOD_BOOLEAN')
                row.prop(metaelem, "hide", text="", invert_checkbox=True, emboss=True, icon='HIDE_OFF')
                row = box.row(align=True)
                row.prop_enum(metaelem, "type","PLANE")
                row.prop_enum(metaelem, "type","CUBE")
                row.prop_enum(metaelem, "type","BALL")
                row.prop_enum(metaelem, "type","CAPSULE")
                row.prop_enum(metaelem, "type","ELLIPSOID")
                row = box.row(align=True)
                row.prop(metaelem, "stiffness", text="Stiffness")
                row.prop(metaelem, "radius", text="Radius",icon='DRIVER_DISTANCE')

                if metaelem.type in {'CUBE', 'ELLIPSOID'}:
                    row = box.row(align=True)
                    row.prop(metaelem, "size_x", text="X")
                    row.prop(metaelem, "size_y", text="Y")
                    row.prop(metaelem, "size_z", text="Z")
                elif metaelem.type == 'CAPSULE':
                    row = box.row(align=True)
                    row.prop(metaelem, "size_x", text="Size X")
                elif metaelem.type == 'PLANE':
                    row = box.row(align=True)
                    row.prop(metaelem, "size_x", text="Size X")
                    row.prop(metaelem, "size_y", text="Y")
       #VOLUME
        if ob.type == 'VOLUME':
            volume = bpy.context.object.data
            box.template_list("VOLUME_UL_grids", "grids", volume, "grids", volume.grids, "active_index", rows=3)                
            display = volume.display
            row = box.row(align=True)                
            row.prop(volume, "filepath", text="")    
            if volume:                            
                row.prop(volume, "is_sequence",icon='FILE_MOVIE',text="")
                if volume.is_sequence:
                    row = box.row(align=True)  
                    row.label(icon='MOD_TIME')                                      
                    row.prop(volume, "frame_duration", text="Frames")
                    row.prop(volume, "sequence_mode", text="")                
                    row = box.row(align=True)                          
                    row.label(icon='BLANK1')
                    row.prop(volume, "frame_start", text="Start")
                    row.prop(volume, "frame_offset", text="Offset")
            row = box.row(align=True)
            row.label(icon='SCENE_DATA')
            row.prop(display, "wireframe_type",text="")
            if display.wireframe_type in {'BOXES','POINTS'}:
                row.separator()
                row.prop(display, "wireframe_detail", text="")
                row = box.row(align=True)                    
                row.label(icon='BLANK1')                    
                row.prop(display, "density")  
            scene = context.scene
            render = volume.render
            row = box.row(align=True)
            row.label(icon='SCENE')  
            row.prop(render, "space",text="")
            if scene.render.engine == 'CYCLES':
                row.prop(render, "step_size")
                row = box.row(align=True)                                    
                row.label(icon='BLANK1')                    
                row.prop(render, "clipping")                                                
       #LATTICE            
        if bpy.context.object.type == 'LATTICE':
            lat = context.object.data
            row = box.row(align=True)
            row.prop(lat, "use_outside",icon='SELECT_SUBTRACT')
            row.separator()
            row.prop_search(lat, "vertex_group", context.object, "vertex_groups",text="")
            row = box.row(align=False)
            row.label(text="U")
            row.prop(lat, "points_u", text="Resolution U")
            row.prop(lat, "interpolation_type_u", text="")
            row = box.row(align=False)
            row.label(text="V")
            row.prop(lat, "points_v", text="V")
            row.prop(lat, "interpolation_type_v", text="")
            row = box.row(align=False)
            row.label(text="W")                                
            row.prop(lat, "points_w", text="W")
            row.prop(lat, "interpolation_type_w", text="")

       #ARMATURE            
        if bpy.context.object.type == 'ARMATURE':
            bone = context.object.data.bones.active
            pchan = ob.pose.bones[bone.name]                
            row = box.row(align= True)
            arm = context.object.data
            row.prop_enum(arm, "pose_position","POSE",icon='ARMATURE_DATA')
            row.prop_enum(arm, "pose_position","REST",icon='OUTLINER_OB_ARMATURE')
            if tbb.tb_arm_view == False:
                row.prop(tbb, "tb_arm_view",text="",icon='BONE_DATA')
            if tbb.tb_arm_view == True:                
                row.prop(tbb, "tb_arm_view",text="",icon='HIDE_OFF')                    
                row = box.row(align= True)
                row.prop_enum(context.object.data,"display_type", "OCTAHEDRAL",icon='PMARKER_ACT')
                row.prop_enum(context.object.data,"display_type", "STICK",icon='IPO_LINEAR')
                row.prop_enum(context.object.data,"display_type", "WIRE",icon='MOD_SIMPLIFY')
                row.prop_enum(context.object.data,"display_type", "BBONE",icon='LIGHTPROBE_CUBEMAP')
                row.prop_enum(context.object.data,"display_type", "ENVELOPE",icon='MESH_CAPSULE')
                row = box.row(align= True)
                if pchan.custom_shape:
                    row.prop(bone, "show_wire",text="",icon='SHADING_WIRE')                
                row.prop(bone, "hide",text="",icon='HIDE_OFF',invert_checkbox=False)                
                row.prop(pchan, "custom_shape",text="")
                if pchan.custom_shape:
                    row.prop(pchan, "custom_shape_scale", text="Scale")
                    row.prop(pchan, "use_custom_shape_bone_size",icon='BONE_DATA',text="")
                    row = box.row(align= True)                        
                    row.label()
                    row.label(icon='BLANK1')
                    row.prop_search(pchan, "custom_shape_transform",ob.pose, "bones", text="")

           #DEFORM
            ob = context.object
            if ob.mode == 'POSE' or ob.mode == 'EDIT':
                box = layout.box()   
                row = box.row(align=True)                                 
                if bone.use_deform == False:
                    row.prop(bone,"use_deform",icon='MOD_SIMPLEDEFORM')
                if bone.use_deform == True:
                    row.prop(bone,"use_deform",icon='MOD_SIMPLEDEFORM',text="Deform")
                    if not tbb.tb_arm_def == False:
                        row.prop(tbb, "tb_arm_def",text="",icon='PROP_OFF')
                    else:      
                        row.prop(tbb, "tb_arm_def",text="",icon='PROP_OFF')                        
                        row.separator()                                        
                        row.prop(bone, "use_envelope_multiply",icon='GP_MULTIFRAME_EDITING', text="Envelope Multiply")
                        row = box.row(align=True)
                        row.prop(bone, "envelope_distance", text="Envelope Distance")
                        row.prop(bone, "envelope_weight", text="Envelope Weight")
                        row = box.row(align=True)
                        row.prop(bone, "head_radius", text="Radius Head")
                        row.prop(bone, "tail_radius", text="Tail")       
               #IK
                active = pchan.is_in_ik_chain                                
                if not tbb.tb_arm_ik:
                    if tbb.tb_arm_def:
                        box = layout.box()
                        row = box.row(align= True)                                                                             
                    elif tbb.tb_arm_def == False:
                        row.separator()
                    row.prop(tbb, "tb_arm_ik",text="Inverse Kinematic",icon='CON_KINEMATIC')
                else:
                    box = layout.box()
                    row = box.row(align= True)            
                    row.prop(tbb, "tb_arm_ik",text="",icon='CON_KINEMATIC')                 
                    row.separator()
                    row.prop(pchan, "ik_stretch", slider=True)
                    split = box.split(align=True)
                    col = split.column(align=True)
                    col.prop(pchan, "lock_ik_x", text="X")
                    if pchan.lock_ik_x == False:
                        col.prop(pchan, "ik_stiffness_x", text="Stiffness X", slider=True)
                        col.prop(pchan, "use_ik_limit_x", text="Limit X",icon='RESTRICT_INSTANCED_OFF')
                        if pchan.use_ik_limit_x == True:
                            col.prop(pchan, "ik_min_x", text="Min")
                            col.prop(pchan, "ik_max_x", text="Max")                        
                    col = split.column(align=True)
                    col.prop(pchan, "lock_ik_y", text="Y")
                    if pchan.lock_ik_y == False:         
                        col.prop(pchan, "ik_stiffness_y", text="Stiffness Y", slider=True)       
                        col.prop(pchan, "use_ik_limit_y", text="Limit Y",icon='RESTRICT_INSTANCED_OFF')
                        if pchan.use_ik_limit_y == True:
                            col.prop(pchan, "ik_min_y", text="Min")
                            col.prop(pchan, "ik_max_y", text="Max")                                                     
                    col = split.column(align=True)
                    col.prop(pchan, "lock_ik_z", text="Z")
                    if pchan.lock_ik_z == False:                    
                        col.prop(pchan, "ik_stiffness_z", text="Stiffness Z", slider=True)
                        col.prop(pchan, "use_ik_limit_z", text="Limit Z",icon='RESTRICT_INSTANCED_OFF')
                        if pchan.use_ik_limit_z == True:
                            col.prop(pchan, "ik_min_z", text="Min")
                            col.prop(pchan, "ik_max_z", text="Max")                     
                    col = layout.column(align=True)
                    col.separator()
                    if ob.pose.ik_solver == 'ITASC':
                        col = layout.column()
                        col.prop(pchan, "use_ik_rotation_control", text="Control Rotation")
                        col.active = active
                        col = layout.column()
                        col.prop(pchan, "ik_rotation_weight", text="IK Rotation Weight", slider=True)
                        col.active = active                             
       #MESH
        if ob.type == 'MESH':     
           #REMESH
            if not tbb.tb_over_mesh_re:
                row.separator()
                row.prop(tbb, "tb_over_mesh_re",text="Remesh",icon='MOD_REMESH')
            else:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_over_mesh_re",text="", icon='MOD_REMESH')                                
                mesh = context.object.data
                row.prop(mesh, "remesh_mode", text="Mode", expand=True)
                row = box.row(align=True)
                if mesh.remesh_mode == 'VOXEL':
                    row.label(icon='BLANK1')
                    row.prop(mesh, "remesh_voxel_size")
                    row.prop(mesh, "remesh_voxel_adaptivity")
                    row = box.row(align=True)         
                    row.label(icon='BLANK1')                                   
                    row.prop(mesh, "use_remesh_fix_poles",icon='VIEW_ORTHO')
                    row.separator()
                    #DEPRECATED
                    #row.prop(mesh, "use_remesh_smooth_normals",icon='MOD_SMOOTH')
                    row = box.row(align=True)      
                    row.label(icon='BLANK1')                                          
                    row.prop(mesh, "use_remesh_preserve_volume",text="Volume",icon='SNAP_VOLUME')
                    row.separator()                        
                    row.prop(mesh, "use_remesh_preserve_paint_mask",text="Paint Mask",icon='MOD_MASK')
                    row.separator()                        
                    row.prop(mesh, "use_remesh_preserve_sculpt_face_sets",text="Face Sets",icon='MOD_EXPLODE')
                    row = box.row(align=True)  
                    row.label(icon='BLANK1')                                              
                    row.operator("object.voxel_remesh", text="Voxel Remesh")
                else:
                    row.label(icon='BLANK1')                        
                    row.operator("object.quadriflow_remesh", text="QuadriFlow Remesh")                
       #ARMATURE            
        if ob.type == 'ARMATURE':
            box = layout.box()
            if not tbb.tb_arm_lay:
                row = box.row(align= False)            
                row.prop(tbb, "tb_arm_lay",text="Layers",icon='RENDERLAYERS')
            else:
                row = box.row(align= True)            
                row.prop(tbb, "tb_arm_lay",text="",icon='RENDERLAYERS')
                row.label(text="Layers:")
                box.prop(arm, "layers", text="")
                box.label(text="Protected Layers:",icon='LOCKED')
                box.prop(arm, "layers_protected", text="")
                if not tbb.tb_arm_bone_rel:                        
                    box = layout.box()
                row = box.row(align= False)            
            if not tbb.tb_arm_bone:
                row.prop(tbb, "tb_arm_bone",text="Vertex Group",icon='GROUP_BONE')
            else:
                if not tbb.tb_arm_lay:
                    box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_arm_bone",text="",icon='GROUP_BONE')                    
                pose = ob.pose
                group = pose.bone_groups.active
                row.label(text="Vertex Group")
                row.operator("pose.group_add", icon='ADD', text="")
                row.operator("pose.group_remove", icon='REMOVE', text="")
                row.separator()
                row.menu("DATA_MT_bone_group_context_menu", icon='DOWNARROW_HLT', text="")
                if group:
                    row.separator()
                    row.operator("pose.group_move", icon='TRIA_UP', text="").direction = 'UP'
                    row.operator("pose.group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                row = box.row()
                rows = 1
                if group:
                    rows = 2
                row.template_list("UI_UL_list","bone_groups",pose,"bone_groups",pose.bone_groups,"active_index",rows=rows)
                col = row.column(align=True)
                col.active = (ob.proxy is None)
                if group:
                    split = box.split()
                    split.active = (ob.proxy is None)
                    col = split.column()
                    col.prop(group, "color_set")
                    if group.color_set:
                        col = split.column()
                        sub = col.row(align=True)
                        sub.enabled = group.is_custom_color_set  # only custom colors are editable
                        sub.prop(group.colors, "normal", text="")
                        sub.prop(group.colors, "select", text="")
                        sub.prop(group.colors, "active", text="")
                row = box.row()
                row.active = (ob.proxy is None)
                sub = row.row(align=True)
                sub.operator("pose.group_assign", text="Assign",icon='CHECKMARK')
                sub.operator("pose.group_unassign", text="Remove",icon='X')
                sub = row.row(align=True)
                sub.operator("pose.group_select", text="Select")
                sub.operator("pose.group_deselect", text="Deselect",icon='RESTRICT_SELECT_OFF')
                box = layout.box()
           #Relations
            if not tbb.tb_arm_bone_rel:
                row = box.row(align= False)            
                row.prop(tbb, "tb_arm_bone_rel",text="Relations",icon='CONSTRAINT_BONE')
            else:
                if not tbb.tb_arm_bone:
                    box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_arm_bone_rel",text="",icon='CONSTRAINT_BONE') 
                ob = context.object
                bone = context.object.data.bones.active
                arm = context.object.data
                pchan = ob.pose.bones[bone.name]                                    

                row.prop_search(bone, "parent", arm, "edit_bones")
                row.prop(bone, "use_relative_parent",text="",icon='CON_CHILDOF')
                box.prop(bone, "layers", text="")
                col = box.column()
                row = box.row(align= True)            
                if ob and pchan:
                    row.prop_search(pchan, "bone_group", ob.pose, "bone_groups", text="")
                
                if bpy.context.object.mode == 'EDIT':
                    bone = context.object.data.edit_bones.active                       
                    row.prop(bone, "use_connect",icon='CON_CHILDOF')
                    row = box.row(align= True)                                    
                    row.prop(bone, "use_local_location",icon='CON_LOCLIMIT')
                    row.prop(bone, "use_inherit_rotation",icon='CON_ROTLIMIT')
                    row.prop(bone, "inherit_scale",icon='CON_SIZELIMIT',text="")                           
                if bpy.context.object.mode == 'POSE':
                    bone = context.object.data.bones.active                        
                    row.prop(bone, "use_connect",icon='CON_CHILDOF')
                    row = box.row(align= True)                                    
                    row.prop(bone, "use_local_location",icon='CON_LOCLIMIT')
                    row.prop(bone, "use_inherit_rotation",icon='CON_ROTLIMIT')
                    row.prop(bone, "inherit_scale",icon='CON_SIZELIMIT',text="")                           

            if tbb.tb_arm_bone_rel:
                box = layout.box()
           #Library
            if not tbb.tb_arm_lib:
                row.prop(tbb, "tb_arm_lib",text="Pose Library",icon='ASSET_MANAGER')
            else:
                row = box.row(align= True)            
                row.prop(tbb, "tb_arm_lib",text="",icon='ASSET_MANAGER')
                poselib = ob.pose_library
                row.label(text="Pose Library")
                if poselib:
                    row.operator("poselib.pose_add", icon='ADD', text="")
                    pose_marker_active = poselib.pose_markers.active
                    if pose_marker_active is not None:
                        row.operator("poselib.pose_remove", icon='REMOVE', text="")
                        row.separator()
                        row.operator(
                            "poselib.apply_pose",
                            icon='ZOOM_SELECTED',
                            text="",
                        ).pose_index = poselib.pose_markers.active_index
                    row.operator("poselib.action_sanitize", icon='HELP', text="")  # XXX: put in menu?
                    if pose_marker_active is not None:
                        row.separator()
                        row.operator("poselib.pose_move", icon='TRIA_UP', text="").direction = 'UP'
                        row.operator("poselib.pose_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                box.template_ID(ob, "pose_library", new="poselib.new", unlink="poselib.unlink")
                if poselib:
                    if poselib.fcurves and not poselib.pose_markers:
                        box.label(icon='ERROR', text="Error: Potentially corrupt library, run 'Sanitize' operator to fix")
                    row = box.row()
                    row.template_list("UI_UL_list", "pose_markers", poselib, "pose_markers",poselib.pose_markers, "active_index", rows=2)
                    col = row.column(align=True)
                    row.operator_context = 'EXEC_DEFAULT'  # exec not invoke, so that menu doesn't need showing
       #BOX WEIEGHT           
        if bpy.context.object.type == 'MESH':
            if tbb.tb_obj_vrtx == False or tbb.tb_obj_shap == False or tbb.tb_obj_uvmap == False:                
                box = layout.box()            
                row = box.row(align= False)                                           
        if bpy.context.object.type == 'LATTICE':
            if tbb.tb_obj_vrtx == False or tbb.tb_obj_shap == False:
                box = layout.box()
                row = box.row(align= False)                                
        if bpy.context.object.type == 'SURFACE':                                               
            if tbb.tb_obj_shap == False:
                box = layout.box()      
                row = box.row(align= False)                                
        if bpy.context.object.type == 'CURVE':                                               
            if tbb.tb_obj_shap == False:
                box = layout.box()                                        
                row = box.row(align= False)                                
        if ob.type == 'GPENCIL':
            if tbb.tb_obj_vrtx == False:
                box = layout.box()
                row = box.row(align= False)                                
        if bpy.context.object.type == 'MESH' or bpy.context.object.type == 'LATTICE' or ob.type == 'GPENCIL':
            if tbb.tb_obj_vrtx == False:
                row.prop(tbb, "tb_obj_vrtx",text="Vertex Group",icon='GROUP_VERTEX')
        if ob.type == 'MESH' or ob.type == 'LATTICE' or ob.type == 'SURFACE' or ob.type == 'CURVE':                
            if tbb.tb_obj_shap == False:
                row.prop(tbb, "tb_obj_shap",text="Shape Group",icon='SHAPEKEY_DATA')
        if bpy.context.object.type == 'MESH':
            if tbb.tb_obj_uvmap == False:
                row.prop(tbb, "tb_obj_uvmap",text="UV Maps",icon='GROUP_UVS')    
        if bpy.context.object.type == 'MESH':
            row = box.row(align= False)                                                    
            if tbb.tb_obj_attr == False:
                row.prop(tbb, "tb_obj_attr",text="Attributes",icon='GROUP_VCOL')           
            if tbb.tb_obj_col_attr == False:
                row.prop(tbb, "tb_obj_col_attr",text="Color Attributes",icon='GROUP_VCOL')           
       #VERTEX GROUP
        if bpy.context.object.type == 'MESH' or bpy.context.object.type == 'LATTICE' or ob.type == 'GPENCIL':        
            if tbb.tb_obj_vrtx:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_obj_vrtx",text="",icon='GROUP_VERTEX')
                group = ob.vertex_groups.active
                row.label(text="Vertex Group")
                row.operator("object.vertex_group_add", icon='ADD', text="")
                props = row.operator("object.vertex_group_remove", icon='REMOVE', text="")
                props.all_unlocked = props.all = False
                row.separator()
                row.menu("MESH_MT_vertex_group_context_menu", icon='DOWNARROW_HLT', text="")
                if group:
                    row.separator()
                    row.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
                    row.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                if (ob.vertex_groups and
                    (ob.mode == 'EDIT' or
                    (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex))
                ):            
                    row = box.row(align=True)
                    row.operator("object.vertex_group_sort",text="",icon='SORTALPHA').sort_type='NAME'
                    row.operator("object.vertex_group_sort",text="",icon='BONE_DATA').sort_type='BONE_HIERARCHY'
                    row.separator()
                    row.operator("v object.vertex_group_copy",text="",icon='COPYDOWN')
                    row.separator()
                    row.operator("object.vertex_group_lock",text="",icon='UNLOCKED').action='UNLOCK'
                    row.operator("object.vertex_group_lock",text="",icon='LOCKED').action='LOCK'
                    row.operator("object.vertex_group_lock",text="",icon='ARROW_LEFTRIGHT').action='INVERT'
                rows = 1
                if group:
                    rows = 2
                row = box.row()
                row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=rows)
                if (ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex))): 
                    row = box.row()
                    sub = row.row(align=True)
                    sub.operator("object.vertex_group_assign", text="Assign",icon='CHECKMARK')
                    sub.operator("object.vertex_group_remove_from", text="Delete",icon='X')

                    sub = row.row(align=True)
                    sub.operator("object.vertex_group_select", text="Select",icon='RESTRICT_SELECT_ON')
                    sub.operator("object.vertex_group_deselect", text="Deselect",icon='RESTRICT_SELECT_OFF')
                    box.prop(context.tool_settings, "vertex_group_weight", text="Weight")
       #SHAPE KEY
        if ob.type == 'MESH' or ob.type == 'LATTICE' or ob.type == 'SURFACE' or ob.type == 'CURVE':
            if tbb.tb_obj_shap:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_obj_shap",text="",icon='SHAPEKEY_DATA')
                key = ob.data.shape_keys
                kb = ob.active_shape_key
                enable_edit = ob.mode != 'EDIT'
                enable_edit_value = False
                row.label(text="Shape Group")
                if kb:
                    row.prop(key, "use_relative",icon='NORMALIZE_FCURVES',text="")
                    row.separator()            
                row.operator("object.shape_key_add", icon='ADD', text="").from_mix = False
                row.operator("object.shape_key_remove", icon='REMOVE', text="").all = False
                row.separator()
                row.menu("MESH_MT_shape_key_context_menu", icon='DOWNARROW_HLT', text="")
                if kb:
                    row.separator()
                    row.operator("object.shape_key_move", icon='TRIA_UP', text="").type = 'UP'
                    row.operator("object.shape_key_move", icon='TRIA_DOWN', text="").type = 'DOWN'

                if ob.show_only_shape_key is False:
                    if enable_edit or (ob.type == 'MESH' and ob.use_shape_key_edit_mode):
                        enable_edit_value = True
                row = box.row()
                rows = 1
                if kb:
                    rows = 2
                row.template_list("MESH_UL_shape_keys", "", key, "key_blocks", ob, "active_shape_key_index", rows=rows)
                if kb:
                    col = row.column(align=True)
                    col.enabled = enable_edit
                    col.prop(ob, "show_only_shape_key", text="")
                    col.prop(ob, "use_shape_key_edit_mode", text="")
                    if key.use_relative:
                        col.operator("object.shape_key_clear", icon='X', text="")
                    else:
                        col.operator("object.shape_key_retime", icon='RECOVER_LAST', text="")
                    layout.use_property_split = True
                    if key.use_relative:
                        if ob.active_shape_key_index != 0:
                            row = box.row()
                            row.active = enable_edit_value
                            row.prop(kb, "value")
                            row = box.row(align=True)
                            sub = col.column(align=True)
                            row.prop(kb, "slider_min", text="Range Min")
                            row.prop(kb, "slider_max", text="Max")
                            row = box.row()
                            row.prop_search(kb, "vertex_group", ob, "vertex_groups", text="")
                            row.prop_search(kb, "relative_key", key, "key_blocks", text="")
                    else:
                        row = box.row(align=True)
                        row.prop(kb, "interpolation",text="")
                        row.separator()
                        row.active = enable_edit_value
                        row.prop(key, "eval_time",text="")
                        row.label(icon='MOD_TIME')
        if bpy.context.object.type in ['MESH','POINTCLOUD']:
           #Attributes
            if tbb.tb_obj_attr:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_obj_attr",text="",icon='LINENUMBERS_ON')
                row.label(text="Vertex Colors")
                row.operator("geometry.attribute_add()", icon='ADD', text="")
                row.operator("geometry.attribute_remove()", icon='REMOVE', text="")
                row.menu("MESH_MT_attribute_context_menu", icon='DOWNARROW_HLT', text="")
                row = box.row()
                row.template_list("MESH_UL_attributes", "attributes", mesh, "attributes", mesh.vertex_colors, "active_index", rows=2)
        if bpy.context.object.type == 'MESH':   
           #MESH UV
            if tbb.tb_obj_uvmap:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_obj_uvmap",text="",icon='GROUP_UVS') 
                row.label(text="UV Maps")
                row.operator("mesh.uv_texture_add", icon='ADD', text="")
                row.operator("mesh.uv_texture_remove", icon='REMOVE', text="")
                row = box.row()
                row.template_list("MESH_UL_uvmaps", "uvmaps", me, "uv_layers", me.uv_layers, "active_index", rows=2)
           #Color Atributes
            if tbb.tb_obj_vrtx_col:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_obj_vrtx_col",text="",icon='GROUP_VCOL')
                row.label(text="Vertex Colors")
                row.operator("geometry.color_attribute_add()", icon='ADD', text="")
                row.operator("geometry.color_attribute_remove()", icon='REMOVE', text="")
                row.menu("MESH_MT_color_attribute_context_menu", icon='DOWNARROW_HLT', text="")
                row = box.row()
                row.template_list("MESH_UL_color_attributes", "color_attributes", mesh, "color_attributes", mesh.vertex_colors, "active_color_index", rows=2)
       
       
def tbdatasecond(context,box,layout):
    wm = context.window_manager
    tbb = wm.tb_wm_bool      
    ob = context.active_object
    if bpy.context.active_object:
        me = context.object.data
        arm = context.object.data
        screen = context.screen
        if not tbb.tb_ob_view:
            row = box.row(align= False)            
            row.prop(tbb, 'tb_ob_view', text="Viewport Display", toggle=True,icon='HIDE_OFF')
        else:
            row = box.row(align=True)
            row.prop(tbb, 'tb_ob_view', text="", toggle=True,icon='HIDE_OFF')                 
            row.separator()   
            if bpy.context.space_data.overlay.show_text == True:
                if ob.type == 'ARMATURE':
                    row.label(icon='FILE_TEXT')
                    row.prop(context.object, "show_name",text="",icon='ARMATURE_DATA')
                    row.prop(context.object.data,"show_names",text="",icon='BONE_DATA')
                else:
                    row.prop(context.object, "show_name",text="Name",icon='FILE_TEXT')         
                row.separator()
                if ob.type == 'CAMERA':
                    cam = context.object.data                           
                    view = context.space_data
                    if view.region_3d.view_perspective == 'CAMERA': 
                        row.prop(cam, "show_name", text="",icon='CAMERA_DATA')
            row.prop(context.object, "show_in_front",text="In front",icon='SELECT_SUBTRACT')
            if bpy.context.object.type == 'MESH' or bpy.context.object.type == 'CURVE' or bpy.context.object.type == 'SURFACE' or bpy.context.object.type == 'META' or bpy.context.object.type == 'FONT': 
                if bpy.context.space_data.shading.type == 'SOLID' or bpy.context.space_data.shading.type == 'MATERIAL' or bpy.context.space_data.shading.type == 'RENDERED':    
                    if bpy.context.object.show_wire == False:
                        row.prop(context.object, "show_wire",text="Wire",icon='SHADING_WIRE')
                    if bpy.context.object.show_wire == True:
                        split = box.split(factor=0.1,align=True)
                        col = split.column(align=True)
                        col.prop(context.object, "show_wire",text="",icon='SHADING_WIRE')
                    if bpy.context.object.type == 'MESH' and bpy.context.object.show_wire == True:   
                        col = split.column(align=True)
                        col.prop(context.space_data.overlay, "wireframe_threshold")
                        col = split.column(align=True)
                        col.prop(context.object, "show_all_edges",text="All_Edges",icon='MOD_EDGESPLIT')
            tstype = bpy.context.active_object.type
            if tstype in {'MESH','CURVE','SURFACE','META','FONT','VOLUME'}:
                if bpy.context.space_data.shading.show_shadows == True:
                    row.prop(context.object.display, "show_shadows",text="Shadow",icon='SHADING_RENDERED')
            if ob.type == 'ARMATURE':  
                row.label(icon='EMPTY_AXIS')                
                row.prop(context.object, "show_axis",text="",icon='ARMATURE_DATA')
                row.prop(context.object.data, "show_axes",text="",icon='BONE_DATA')              
            else:              
                row.prop(context.object, "show_axis",text="Axis",icon='EMPTY_AXIS')                    
            if tstype in {'MESH','CURVE','SURFACE','META','FONT'}:
                if bpy.context.object.show_texture_space == False:
                    row.prop(context.object, "show_texture_space",text="Texture Space",icon='FORCE_TEXTURE')
                if bpy.context.object.show_texture_space == True:
                    row = box.row(align=True)
                    if bpy.context.object.type == 'META':
                        row.prop(context.object, "show_texture_space",text="Texture Space",icon='FORCE_TEXTURE')                            
                    else:
                        row.prop(context.object, "show_texture_space",text="",icon='FORCE_TEXTURE')
                    row.prop(me, "use_auto_texspace",text="",icon='FILE_REFRESH')
                    row.prop(me, "texture_mesh",text="")
                    if bpy.context.object.type == 'SURFACE' or bpy.context.object.type == 'FONT':
                        row.operator("curve.match_texture_space")
                    if bpy.context.object.data.use_auto_texspace == False:
                        split = box.split(factor=0.1,align=True)
                        col = split.column(align=True)
                        col.label(icon='BLANK1')
                        col = split.column(align=True)
                        col.prop(me, "texspace_location", text="")
                        col = split.column(align=True)
                        col.prop(me, "texspace_size", text="")
                
            if bpy.context.object.type == 'ARMATURE':
                row = box.row(align=True)
                row.prop(context.object.data,"show_group_colors",text="Color Bones",icon='GROUP_VCOL')
                row.prop(me,"show_bone_custom_shapes",text="Shapes",icon='MOD_REMESH')
                if bpy.context.object.data.show_axes == False:
                    row.prop(context.object.data,"show_axes",text="",icon='EMPTY_AXIS')
                else:
                    row = box.row(align=True)
                    row.prop(context.object.data,"show_axes",text="",icon='EMPTY_AXIS')
                    row.prop(context.object.data,"axes_position")
            #BOUNDS
            if tstype in {'MESH','ARMATURE','GPENCIL','FONT','META','CURVE','SURFACE','VOLUME'}:                
                row = box.row(align= True)
                row.prop_enum(ob, "display_type","BOUNDS",text="Bound",icon='PIVOT_BOUNDBOX')
                if bpy.context.object.display_type == 'BOUNDS':
                    if bpy.context.object.show_bounds == False:
                        row.prop(ob, "show_bounds", text="",icon='PROP_OFF')
                    if bpy.context.object.show_bounds == True:
                        row.prop(ob, "show_bounds", text="",icon='PROP_ON')
                        row.prop_enum(context.object, "display_bounds_type", "BOX", text="",icon='MESH_CUBE')
                        row.prop_enum(context.object, "display_bounds_type", "SPHERE", text="",icon='MESH_UVSPHERE')
                        row.prop_enum(context.object, "display_bounds_type", "CAPSULE", text="",icon='MESH_CAPSULE')
                        row.prop_enum(context.object, "display_bounds_type", "CYLINDER", text="",icon='MESH_CYLINDER')
                        row.prop_enum(context.object, "display_bounds_type", "CONE", text="",icon='MESH_CONE')
                        row = box.row(align=True)
                row.prop_enum(ob, "display_type","WIRE",text="Wire",icon='SHADING_WIRE')
                row.prop_enum(ob, "display_type","SOLID",text="Solid",icon='SHADING_SOLID')
                row.prop_enum(ob, "display_type","TEXTURED",text="Texture",icon='TEXTURE')
                if bpy.context.object.display_type == 'SOLID' or bpy.context.object.display_type == 'TEXTURED':
                    row.separator()
                    row.prop_enum(context.space_data.shading, "color_type", "OBJECT", text="", icon='OBJECT_DATAMODE')
                    row.prop_enum(context.space_data.shading, "color_type", "MATERIAL", text="", icon='MATERIAL')                           
                    if bpy.context.space_data.shading.color_type == 'OBJECT':
                        row = box.row(align= True)  
                        row.prop(ob, "color",text="")
                    if bpy.context.space_data.shading.color_type == 'MATERIAL':
                        if context.object.active_material:
                            mat = context.object.active_material
                            row = box.row(align= True)  
                            row.prop(mat, "diffuse_color", text="")
                            row.label(icon='BLANK1')
                            row = box.row(align= True)                              
                            row.prop(mat, "metallic")
                            row.prop(mat, "roughness")
                            row.label(icon='BLANK1')           
            #GEOMETRY DATA
                if tstype in {'MESH'}:

                    me = context.object.data
                    row = box.row(align= True)
                    row.operator("mesh.customdata_mask_clear", icon='X')
                    row.operator("mesh.customdata_skin_clear", icon='X')
                    if me.has_custom_normals:
                        row.operator("mesh.customdata_custom_splitnormals_clear", icon='X')
                    else:
                        row.operator("mesh.customdata_custom_splitnormals_add", icon='ADD')                   
            #CAMERA
            if ob.type == 'CAMERA':
                cam = context.object.data
                view = context.space_data
                row = box.row(align=True)
                row.label(icon='BLANK1')
                row.prop(cam, "show_limits", text="Limits",icon='EMPTY_AXIS')
                row.prop(cam, "show_mist", text="Mist",icon='VIEW_PERSPECTIVE')
                if view.region_3d.view_perspective == 'CAMERA':                
                    row.prop(cam, "show_sensor", text="Sensor",icon='SELECT_SET')
                row = box.row(align=True)
                row.label(icon='CAMERA_DATA')
                row.prop(cam, "display_size", text="Size")
                if view.region_3d.view_perspective == 'CAMERA' and bpy.context.object == bpy.context.scene.camera:
                    if bpy.context.object.data.show_passepartout == False:
                        row = box.row(align=True)                
                        row.prop(context.object.data,"show_passepartout",icon='HOLDOUT_ON')
                    if bpy.context.object.data.show_passepartout == True:
                        row = box.row(align=True)
                        row.prop(context.object.data,"show_passepartout",text="",icon='HOLDOUT_ON')                
                        row.prop(context.object.data,"passepartout_alpha")
                    row = box.row(align=True)                
                    if tbb.tb_kmr_guides == False:
                        row.prop(tbb, 'tb_kmr_guides', text="Composition Guides", toggle=True,icon='OBJECT_HIDDEN')                                        
                    if tbb.tb_kmr_guides == True:
                        row = box.row(align=True)
                        row.prop(tbb, 'tb_kmr_guides', text="", toggle=True,icon='OBJECT_HIDDEN')                                                            
                        row.label(text="Composition Guides")
                        split = box.split(align=True)
                        col = split.column(align=True)
                        col.prop(cam, "show_composition_center",text="Center",icon='ADD')
                        col.prop(cam, "show_composition_thirds",text="Thirds",icon='BLANK1')
                        col.prop(cam, "show_composition_golden_tria_a",icon='BLANK1')
                        col.prop(cam, "show_composition_harmony_tri_a",icon='BLANK1')
                        col = split.column(align=True)
                        col.prop(cam, "show_composition_center_diagonal",text="Diagonal",icon='X')
                        col.prop(cam, "show_composition_golden",icon='BLANK1')
                        col.prop(cam, "show_composition_golden_tria_b",icon='BLANK1')
                        col.prop(cam, "show_composition_harmony_tri_b",icon='BLANK1')
                    if bpy.context.object.data.show_background_images == False:
                        box.prop(cam, "show_background_images", text="Background Image",icon='IMAGE_PLANE')
                    if bpy.context.object.data.show_background_images == True:
                        box = layout.box()
                        row = box.row(align=True)
                        row.prop(cam, "show_background_images", text="",icon='IMAGE_PLANE')
                        use_multiview = context.scene.render.use_multiview
                        row.operator("view3d.background_image_add", text="Add Image",icon='ADD')
                        for i, bg in enumerate(cam.background_images):
                            layout.active = cam.show_background_images
                            box = layout.box()
                            row = box.row(align=True)
                            row.prop(bg, "show_expanded", text="", emboss=False)
                            if bg.source == 'IMAGE' and bg.image:
                                row.prop(bg.image, "name", text="", emboss=False)
                            elif bg.source == 'MOVIE_CLIP' and bg.clip:
                                row.prop(bg.clip, "name", text="", emboss=False)
                            elif bg.source and bg.use_camera_clip:
                                row.label(text="Active Clip")
                            else:
                                row.label(text="Not Set")
                            row.prop(bg,"show_background_image",text="",emboss=False,icon='RESTRICT_VIEW_OFF' if bg.show_background_image else 'RESTRICT_VIEW_ON',)
                            row.operator("view3d.background_image_remove", text="", emboss=False, icon='X').index = i
                            if bg.show_expanded:
                                row = box.row()
                                row.prop(bg, "source", expand=True)
                                has_bg = False
                                if bg.source == 'IMAGE':
                                    row = box.row()
                                    row.template_ID(bg, "image", open="image.open")
                                    if bg.image is not None:
                                        box.template_image(bg, "image", bg.image_user, compact=True)
                                        has_bg = True
                                        if use_multiview:
                                            box.prop(bg.image, "use_multiview")
                                            column = box.column()
                                            column.active = bg.image.use_multiview
                                            column.label(text="Views Format:")
                                            column.row().prop(bg.image, "views_format", expand=True)
                                            sub = column.box()
                                            sub.active = bg.image.views_format == 'STEREO_3D'
                                            sub.template_image_stereo_3d(bg.image.stereo_3d_format)
                                elif bg.source == 'MOVIE_CLIP':
                                    row = box.row(align=True)
                                    row.prop(bg, "use_camera_clip", text="",icon='CON_CAMERASOLVER')
                                    sub = row.row(align=True)
                                    sub.active = not bg.use_camera_clip
                                    sub.template_ID(bg, "clip", open="clip.open")
                                    column = box.column()
                                    column.active = not bg.use_camera_clip
                                    if bg.clip:
                                        column.template_movieclip(bg, "clip", compact=True)
                                    if bg.use_camera_clip or bg.clip:
                                        has_bg = True
                                    column = box.column()
                                    column.active = has_bg
                                    column.prop(bg.clip_user, "use_render_undistorted",icon="RENDER_STILL")
                                    column.prop(bg.clip_user, "proxy_render_size",text="")
                                if has_bg:
                                    col = box.column()
                                    col.prop(bg, "alpha", slider=True)
                                    col.row().prop(bg, "display_depth", expand=True)
                                    col.row().prop(bg, "frame_method", expand=True)
                                    row = box.row()
                                    row.prop(bg, "offset")
                                    col = box.column()
                                    col.prop(bg, "rotation")
                                    col.prop(bg, "scale")
                                    row = box.row(align=True)
                                    row.prop(bg, "use_flip_x",icon='BLANK1')
                                    row.prop(bg, "use_flip_y",expand = False, event = True)     
    #Relations  
    if tbb.tb_ob_view == True:
        if tbb.tb_obj_rel == False:
            box = layout.box()
            row = box.row(align= True)            
    if not tbb.tb_obj_rel:
        row.prop(tbb, "tb_obj_rel",text="Relations",icon='TRACKING')
    else:
    #  if ob.type != 'ARMATURE':
        box = layout.box()
        row = box.row(align= True)            
        row.prop(tbb, "tb_obj_rel",text="",icon='TRACKING')  
        row.label(text="Relations")
        row = box.row(align=True)
        parent = context.object.parent
        row.prop(ob, "parent",text="")
        if parent:
            if bpy.context.object.parent_type == 'OBJECT':
                iconparentype = 'OBJECT_DATA'
            if bpy.context.object.parent_type == 'VERTEX':
                iconparentype = 'LAYER_USED'
            if bpy.context.object.parent_type == 'VERTEX_3':
                iconparentype = 'STICKY_UVS_DISABLE'
            row.prop(context.object,"parent_type",text="",icon=iconparentype)
            row.prop(ob, "use_camera_lock_parent",text="",icon='CAMERA_DATA')
            if context.object.parent_type == 'BONE' and parent.type == 'ARMATURE':
                row.prop_search(ob, "parent_bone", parent.data, "bones",text="")
            if parent.type == 'ARMATURE':
                row.prop_enum(ob, "parent_type","BONE",text="",icon='BONE_DATA')
                row.prop_enum(ob, "parent_type","ARMATURE",text="",icon='ARMATURE_DATA')
                row.prop_enum(ob, "parent_type","OBJECT",text="",icon='OBJECT_DATA')
            row = box.row(align=True)
            row.prop(ob, "track_axis", text="",icon='EMPTY_ARROWS')
            row.prop(ob, "up_axis", text="",icon='SORT_DESC')
            row.prop(ob, "pass_index", text="Index")
        if bpy.context.object in {'MESH'}:
            box = layout.box()
def tbdatamaterial(context,box,layout):
   #MATERIAL 
    wm = context.window_manager
    tbb = wm.tb_wm_bool      
    ob = context.object   
    if bpy.context.object:
        if not tbb.tb_obj_mat:
            row = box.row(align= True)     
            row.prop(tbb, "tb_obj_mat",text="Material",icon='MATERIAL')                                   
        else:
            row = box.row(align= True)     
            row.prop(tbb, "tb_obj_mat",text="",icon='MATERIAL')  
            mat = context.object.active_material
            ob = context.object
            num = context.object.active_material_index       
            row.template_ID(context.object, "active_material", new="material.new")
            if context.object.material_slots:
                slot = context.object.material_slots[num]
                space = context.space_data
                if not tbb.tb_obj_mat_set:                   
                    row.prop(tbb, "tb_obj_mat_set",text="",icon='OPTIONS')            
                row.separator()      
                row.prop_enum(slot, "link", "DATA",text="",icon='MOD_DATA_TRANSFER')        
                row.prop_enum(slot, "link", "OBJECT",text="",icon='OBJECT_DATA')
                if ob:
                    is_sortable = len(ob.material_slots) > 1
                    rows = 1
                    if (is_sortable):
                        rows = 2
                    row = box.row(align=True)                
                    row.label(text="")
                    row.operator("object.material_slot_add", icon='ADD', text="")
                    row.operator("object.material_slot_remove", icon='REMOVE', text="")
                    row.separator()
                    row.menu("MATERIAL_MT_context_menu", icon='DOWNARROW_HLT', text="")
                    if is_sortable:
                        row.separator()      
                        row.operator("object.material_slot_move", icon='TRIA_UP', text="").direction = 'UP'
                        row.operator("object.material_slot_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                    row = box.row(align=True)                
                    row.template_list("MATERIAL_UL_matslots", "", ob, "material_slots", ob, "active_material_index", rows=rows)
                    if ob.mode == 'EDIT':
                        row = layout.row(align=True)
                        row.operator("object.material_slot_assign", text="Assign")
                        row.operator("object.material_slot_select", text="Select")
                        row.operator("object.material_slot_deselect", text="Deselect")
                if tbb.tb_obj_mat_set:
                    row = box.row(align= True)            
                    row.prop(tbb, "tb_obj_mat_set",text="",icon='MATERIAL')
                    row.label(text="Settings")
                    row.label(text="Backface")                    
                    row.prop(mat, "use_backface_culling",text="",icon='MOD_EXPLODE')
                    if mat.blend_method not in {'OPAQUE', 'CLIP', 'HASHED'}:
                        row.prop(mat, "show_transparent_back",text="",icon='HIDE_OFF')
                    row = box.row(align= True)                               
                    row.prop(mat, "blend_method",text="")
                    row.prop(mat, "shadow_method",text="")
                    row = box.row(align=True)                    
                    if mat.blend_method == 'CLIP' or mat.shadow_method == 'CLIP':
                        row.prop(mat, "alpha_threshold")
                    row = box.row(align=True)                    
                    row.prop(mat, "use_screen_refraction",icon='OUTLINER_DATA_LIGHTPROBE')
                    row.prop(mat, "refraction_depth")
                    row = box.row(align=True)                    
                    row.prop(mat, "use_sss_translucency",icon='SHADING_RENDERED')
                    row = box.row(align=True)                    
                    row.prop(mat, "pass_index")                                       

def tbdatadraw(self, context):  
    ob = context.object
    if bpy.context.object:
        me = context.object.data
        arm = context.object.data
        screen = context.screen
        layout = self.layout
        box = layout.box()
        if ob:
            if bpy.context.object.type == 'EMPTY':
                row = box.row(align= True)
            else:  
                row = box.row(align= True)  
                row.template_ID(ob, "data")
        tbdatamain(context,box,layout)
        box = layout.box()  
        tbdatasecond(context,box,layout)
        if ob.type in {'MESH','SURFACE','META','FONT','GPENCIL','VOLUME'}:  
                box = layout.box()    
                tbdatamaterial(context,box,layout)          
def tbdatadrawpop(self, context):
    ob = context.object
    layout = self.layout
    split = layout.split(align=True)
    layout = split.column(align=True)
    box = layout.box()
    if ob:
        if bpy.context.object.type == 'EMPTY':
            row = box.row(align= True)
        else:  
            row = box.row(align= True)  
            row.template_ID(ob, "data")
    tbdatamain(context,box,layout)
    layout = split.column(align=True)
    box = layout.box()    
    tbdatasecond(context,box,layout)
    if ob.type in {'MESH','SURFACE','META','FONT','GPENCIL','VOLUME'}:  
        layout = split.column(align=True)
        box = layout.box()    
        tbdatamaterial(context,box,layout)          

class TB_Data_UI_3D(bpy.types.Panel):
    bl_label = "Object Data"
    bl_idname = "TBPNL_PT_Data"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    @classmethod
    def poll(cls, context):
        return context.object is not None    
    def draw_header(self, context):
        self.layout.label(icon='OBJECT_DATA')
    def draw(self, context):
        tbdatadraw(self, context)            
class TB_Data_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_label = "Data PoP"
    bl_idname = "context.tbdatapopup"
    @classmethod
    def poll(cls, context):
        return context.object is not None
    def invoke(self, context, event):
        if bpy.context.object.type in {'MESH','SURFACE'}:
            widthsize = 800   
        elif bpy.context.object.type == 'CURVE':
            widthsize = 650   
        else:
            widthsize = 500     
        return context.window_manager.invoke_props_dialog(self,width = widthsize)
    def draw(self, context):
        tbdatadrawpop(self, context)    
    def execute(self, context):
        return {'FINISHED'}

