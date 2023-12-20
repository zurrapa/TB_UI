import bpy
#HEADERS
wm = bpy.context.window_manager
def TB_TOPBAR_editor_menus(self, context):
    layout = self.layout
    if getattr(context.area, "show_menus", False):
        layout.menu("TOPBAR_MT_blender", text="", icon='BLENDER')
    else:
        layout.menu("TOPBAR_MT_blender", text="", icon='BLENDER')
    layout.menu("TOPBAR_MT_file",text="",icon='FILE')
    layout.menu("TOPBAR_MT_edit",text="",icon='EDITMODE_HLT')
    layout.menu("TOPBAR_MT_render",text="",icon='RESTRICT_RENDER_OFF')
    layout.menu("TOPBAR_MT_window",text="",icon='WINDOW')
    layout.menu("TOPBAR_MT_help",text="",icon='QUESTION')

lmda = lambda s,c:s.layout.separator()
bpy.types.TOPBAR_MT_editor_menus.draw = lmda
bpy.types.TOPBAR_MT_editor_menus.prepend(TB_TOPBAR_editor_menus)

def TB_VIEW3D_MT_editor_menus(self, context):
    layout = self.layout
    obj = context.active_object
    mode_string = context.mode
    edit_object = context.edit_object
    gp_edit = obj and obj.mode in {'EDIT_GPENCIL', 'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL', 'VERTEX_GPENCIL'}
    ts = context.scene.tool_settings
    #layout.prop(wm.tb_wm_bool,"header_icons",icon='IMAGE_RGB_ALPHA',text="")

    layout.menu("VIEW3D_MT_view",icon='HIDE_OFF', text="")
    # Select Menu
    if gp_edit:
        if mode_string not in {'PAINT_GPENCIL', 'WEIGHT_GPENCIL'}:
            if (
                    mode_string == 'SCULPT_GPENCIL' and
                    (ts.use_gpencil_select_mask_point or
                        ts.use_gpencil_select_mask_stroke or
                        ts.use_gpencil_select_mask_segment)
            ):
                layout.menu("VIEW3D_MT_select_gpencil",text="",icon='RESTRICT_SELECT_OFF')
            elif mode_string == 'EDIT_GPENCIL':
                layout.menu("VIEW3D_MT_select_gpencil",text="",icon='RESTRICT_SELECT_OFF')
            elif mode_string == 'VERTEX_GPENCIL':
                layout.menu("VIEW3D_MT_select_gpencil",text="",icon='RESTRICT_SELECT_OFF')
    elif mode_string in {'PAINT_WEIGHT', 'PAINT_VERTEX', 'PAINT_TEXTURE'}:
        mesh = obj.data
        if mesh.use_paint_mask:
            layout.menu("VIEW3D_MT_select_paint_mask",text="",icon='RESTRICT_SELECT_OFF')
        elif mesh.use_paint_mask_vertex and mode_string in {'PAINT_WEIGHT', 'PAINT_VERTEX'}:
            layout.menu("VIEW3D_MT_select_paint_mask_vertex",text="",icon='RESTRICT_SELECT_OFF')
    elif mode_string != 'SCULPT':
        layout.menu("VIEW3D_MT_select_%s" % mode_string.lower(),text="",icon='RESTRICT_SELECT_OFF')
    if gp_edit:
        pass
    elif mode_string == 'OBJECT':
        layout.menu("VIEW3D_MT_add", text="", icon='ADD')
    elif mode_string == 'EDIT_MESH':
        layout.menu("VIEW3D_MT_mesh_add", text="", icon='ADD')
        layout.template_node_operator_asset_root_items()
    elif mode_string == 'EDIT_CURVE':
        layout.menu("VIEW3D_MT_curve_add", text="", icon='ADD')
        layout.template_node_operator_asset_root_items()
    elif mode_string == 'EDIT_SURFACE':
        layout.menu("VIEW3D_MT_surface_add", text="", icon='ADD')
    elif mode_string == 'EDIT_METABALL':
        layout.menu("VIEW3D_MT_metaball_add", text="", icon='ADD')
    elif mode_string == 'EDIT_ARMATURE':
        layout.menu("TOPBAR_MT_edit_armature_add", text="", icon='ADD')
    if gp_edit:
        if obj and obj.mode == 'PAINT_GPENCIL':
            layout.menu("VIEW3D_MT_draw_gpencil",text="",icon='GREASEPENCIL')
        elif obj and obj.mode == 'EDIT_GPENCIL':
            layout.menu("VIEW3D_MT_edit_gpencil",text="",icon='OUTLINER_OB_GREASEPENCIL')
            layout.menu("VIEW3D_MT_select_edit_gpencil",text="",icon='RESTRICT_SELECT_OFF')
            layout.menu("VIEW3D_MT_edit_gpencil_stroke",text="",icon='OUTLINER_DATA_GREASEPENCIL')
            layout.menu("VIEW3D_MT_edit_gpencil_point",text="",icon='POINTCLOUD_DATA')
        elif obj and obj.mode == 'WEIGHT_GPENCIL':
            layout.menu("VIEW3D_MT_weight_gpencil",text="",icon='MOD_VERTEX_WEIGHT')
        if obj and obj.mode == 'VERTEX_GPENCIL':
            layout.menu("VIEW3D_MT_select_edit_gpencil",text="",icon='RESTRICT_SELECT_OFF')
            layout.menu("VIEW3D_MT_paint_gpencil",text="",icon='VPAINT_HLT')
    elif edit_object:
        layout.menu("VIEW3D_MT_edit_%s" % edit_object.type.lower(),text="",icon=bpy.context.active_object.type + '_DATA')
        if mode_string == 'EDIT_MESH':
            layout.menu("VIEW3D_MT_edit_mesh_vertices",text="",icon='VERTEXSEL')
            layout.menu("VIEW3D_MT_edit_mesh_edges",text="",icon='EDGESEL')
            layout.menu("VIEW3D_MT_edit_mesh_faces",text="",icon='FACESEL')
            layout.menu("VIEW3D_MT_uv_map",text="",icon='UV')
        elif mode_string in {'EDIT_CURVE', 'EDIT_SURFACE'}:
            layout.menu("VIEW3D_MT_edit_curve_ctrlpoints",text="",icon='CURVE_DATA')
            layout.menu("VIEW3D_MT_edit_curve_segments",text="",icon='CURVE_BEZCURVE')

    elif obj:
        if mode_string != 'PAINT_TEXTURE':
            layout.menu("VIEW3D_MT_%s" % mode_string.lower(),text="",icon='OBJECT_DATA')
        if mode_string == 'SCULPT':
            layout.menu("VIEW3D_MT_mask",text="",icon='MOD_MASK')
            layout.menu("VIEW3D_MT_face_sets",text="",icon='FACE_MAPS')

    else:
        layout.menu("VIEW3D_MT_object",text="",icon='OBJECT_DATA')
bpy.types.VIEW3D_MT_editor_menus.draw = lmda
bpy.types.VIEW3D_MT_editor_menus.prepend(TB_VIEW3D_MT_editor_menus)


def TB_TEXT_MT_editor_menus(self,context):
    layout = self.layout
    st = context.space_data
    text = st.text
    layout.menu("TEXT_MT_view",text="",icon='HIDE_OFF')
    layout.menu("TEXT_MT_text",text="",icon='FILE_TEXT')
    if text:
        layout.menu("TEXT_MT_edit",text="",icon='EDITMODE_HLT')
        layout.menu("TEXT_MT_select",text="",icon='RESTRICT_SELECT_OFF')
        layout.menu("TEXT_MT_format",text="",icon='CON_TRANSFORM_CACHE')
    layout.menu("TEXT_MT_templates",text="",icon='TEXT')
bpy.types.TEXT_MT_editor_menus.draw = lmda
bpy.types.TEXT_MT_editor_menus.prepend(TB_TEXT_MT_editor_menus)

def TB_NODE_MT_editor_menus(self,context):
    layout = self.layout
    layout.menu("NODE_MT_view",text="",icon='HIDE_OFF')
    layout.menu("NODE_MT_select",text="",icon='RESTRICT_SELECT_OFF')
    layout.menu("NODE_MT_add",text="",icon='ADD')
    layout.menu("NODE_MT_node",text="",icon='NODETREE')
bpy.types.NODE_MT_editor_menus.draw = lmda
bpy.types.NODE_MT_editor_menus.prepend(TB_NODE_MT_editor_menus)

def TB_CONSOLE_MT_editor_menus(self,context):
    layout = self.layout
    layout.menu("CONSOLE_MT_view",text="",icon='HIDE_OFF')
    layout.menu("CONSOLE_MT_console",text="",icon='CONSOLE')
bpy.types.CONSOLE_MT_editor_menus.draw = lmda
bpy.types.CONSOLE_MT_editor_menus.prepend(TB_CONSOLE_MT_editor_menus)

def TB_INFO_MT_editor_menus(self,context):
    layout = self.layout
    layout.menu("INFO_MT_view",text="",icon='HIDE_OFF')
    layout.menu("INFO_MT_info",text="",icon='INFO')
bpy.types.CONSOLE_MT_editor_menus.draw = lmda
bpy.types.CONSOLE_MT_editor_menus.prepend(TB_CONSOLE_MT_editor_menus)

def TB_DOPESHEET_MT_editor_menus(self,context):    
    layout = self.layout
    st = context.space_data
    layout.menu("DOPESHEET_MT_view",text="",icon='HIDE_OFF')
    layout.menu("DOPESHEET_MT_select",text="",icon='RESTRICT_SELECT_OFF')
    if st.show_markers:
        layout.menu("DOPESHEET_MT_marker",text="",icon='MARKER')
    if st.mode == 'DOPESHEET' or (st.mode == 'ACTION' and st.action is not None):
        layout.menu("DOPESHEET_MT_channel",text="",icon='GROUP')
    elif st.mode == 'GPENCIL':
        layout.menu("DOPESHEET_MT_gpencil_channel",text="",icon='GROUP')
    if st.mode != 'GPENCIL':
        layout.menu("DOPESHEET_MT_key",text="",icon='KEYINGSET')
    else:
        layout.menu("DOPESHEET_MT_gpencil_key",icon='KEYINGSET')
bpy.types.DOPESHEET_MT_editor_menus.draw = lmda
bpy.types.DOPESHEET_MT_editor_menus.prepend(TB_DOPESHEET_MT_editor_menus)

def TB_IMAGE_MT_editor_menus(self, context):
    layout = self.layout
    sima = context.space_data
    ima = sima.image
    show_uvedit = sima.show_uvedit
    show_maskedit = sima.show_maskedit
    layout.menu("IMAGE_MT_view",text="",icon='HIDE_OFF')
    if show_uvedit:
        layout.menu("IMAGE_MT_select",text="",icon='RESTRICT_SELECT_OFF')
    if show_maskedit:
        layout.menu("MASK_MT_select",text="",icon='RESTRICT_SELECT_OFF')
    if ima and ima.is_dirty:
        layout.menu("IMAGE_MT_image",text="",icon='IMAGE_DATA')
    else:
        layout.menu("IMAGE_MT_image",text="",icon='IMAGE_DATA')
    if show_uvedit:
        layout.menu("IMAGE_MT_uvs",text="",icon='UV')
    if show_maskedit:
        layout.menu("MASK_MT_add",text="",icon='ADD')
        layout.menu("MASK_MT_mask",text="",icon='MOD_MASK')
bpy.types.IMAGE_MT_editor_menus.draw = lmda
bpy.types.IMAGE_MT_editor_menus.prepend(TB_IMAGE_MT_editor_menus)

def TB_SEQUENCER_HT_header(self, context):
    layout = self.layout
    row = layout.row(align=True)
    row.separator()
    if bpy.context.scene.render.sequencer_gl_preview in {'SOLID','WIREFRAME'}:
        row.prop(bpy.context.scene.render,"use_sequencer_override_scene_strip",text="",icon='LIBRARY_DATA_OVERRIDE')
    row.prop_enum(context.scene.render,"sequencer_gl_preview","WIREFRAME",text="")
    row.prop_enum(context.scene.render,"sequencer_gl_preview","SOLID",text="")
    row.prop_enum(context.scene.render,"sequencer_gl_preview","MATERIAL",text="")
    row.prop_enum(context.scene.render,"sequencer_gl_preview","RENDERED",text="")
bpy.types.SEQUENCER_HT_header.append(TB_SEQUENCER_HT_header)

def TB_VIEW3D_UI_HEADER(self, context):
    layout = self.layout
    row = layout.row(align=True)
    prefs = context.preferences
    inputs = prefs.inputs    
    if inputs.view_rotate_method == 'TURNTABLE':
        row.prop(inputs, "view_rotate_method", text="",icon='CON_ROTLIMIT', icon_only= True)
    else:
        row.prop(inputs, "view_rotate_method", text="",icon='ORIENTATION_GIMBAL', icon_only= True)
    row.separator()
    #row.operator("view3d.fly",text="",icon='CON_FOLLOWTRACK')     
    #row.operator("view3d.walk",text="",icon='MOD_DYNAMICPAINT')
    #row = layout.row(align=True)
    box = layout.box()
    rob = box.row(align=True)
    rob.prop_enum(context.scene.render, "engine", "BLENDER_WORKBENCH",text="", icon='SHADING_SOLID')
    rob.prop_enum(context.scene.render, "engine", "BLENDER_EEVEE",text="", icon='SHADING_TEXTURE')
    rob.prop_enum(context.scene.render, "engine", "CYCLES",text="", icon='SHADING_RENDERED')
bpy.types.VIEW3D_HT_header.append(TB_VIEW3D_UI_HEADER)

def TB_DATA_PT_vertex_groups(self, context):
    layout = self.layout
    layout.label(icon='GROUP_VERTEX')
bpy.types.DATA_PT_vertex_groups.draw_header = TB_DATA_PT_vertex_groups

def TB_BROWSER_UI_HEADER(self, context):
    wm = context.window_manager
    tbb = wm.tb_wm_bool
    space = context.space_data
    params = space.params

    layout = self.layout
    row = layout.row(align=True)
    flow = row.grid_flow(row_major=True, columns=0, even_columns=False, even_rows=False, align=False)

    if params.display_type != 'THUMBNAIL':
        subrow = flow.row()   
        subsubrow = subrow.row(align=True)    
        subsubrow.prop(context.space_data.params,"show_details_datetime",icon='SORTTIME',text="")        
        subsubrow.prop(context.space_data.params,"show_details_size",icon='SORTSIZE',text="")    
    row.separator()
    row.prop_enum(context.space_data.params, "sort_method", "FILE_SORT_ALPHA")
    row.prop_enum(context.space_data.params, "sort_method", "FILE_SORT_EXTENSION")
    row.prop_enum(context.space_data.params, "sort_method", "FILE_SORT_TIME")
    row.prop_enum(context.space_data.params, "sort_method", "FILE_SORT_SIZE")  
    row.prop(context.space_data.params,"use_sort_invert",icon='LOOP_BACK',text="")
    row.separator()
    if tbb.tb_fe_recursion:
        row.prop(tbb, "tb_fe_recursion",text="",icon_value=bpy.types.Scene.tb_pnl_icons['tbi_refresh'].icon_id)
        row.prop_enum(context.space_data.params,"recursion_level", "NONE", text="0")
        row.prop_enum(context.space_data.params,"recursion_level", "ALL_1",text="1")
        row.prop_enum(context.space_data.params,"recursion_level", "ALL_2",text="2")
        row.prop_enum(context.space_data.params,"recursion_level", "ALL_3",text="3")
    else:
        row.prop(tbb, "tb_fe_recursion",text="",icon_value=bpy.types.Scene.tb_pnl_icons['tbi_refresh'].icon_id)     
bpy.types.FILEBROWSER_PT_directory_path.append(TB_BROWSER_UI_HEADER)


#bpy.types.DATA_PT_vertex_groups.append(TB_DATA_PT_vertex_groups)