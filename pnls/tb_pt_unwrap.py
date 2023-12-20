import bpy

def tb_def_pt_unwarp_3d(self,context):
    wm = context.window_manager
    layout = self.layout
    screen = context.screen
    box = layout.box()
    if bpy.context.object:            
        if bpy.context.object.type == 'MESH':
            if bpy.context.mode == 'EDIT_MESH':
                row = box.row(align=True)
                row.label(icon='UV')
                row.prop(context.scene.tool_settings,"use_edge_path_live_unwrap",icon='PROP_OFF',text="")
                row.operator("uv.unwrap",text="",icon='FILE_REFRESH')
                row.operator("uv.unwrap")
                row.operator("uv.export_layout",icon='EXPORT',text="")
                row.prop(wm.tb_wm_bool, "tb_uv_seam",text="",icon='COLORSET_01_VEC')                
                cw = wm.tb_wm_bool.tb_uv_seam
                if cw == True:
                    row = box.row(align= True)        
                    row.operator("mesh.mark_seam",icon='COLORSET_01_VEC')
                    row.operator("mesh.mark_seam",text="Clear Seam").clear=True      
                #NOUN
                if wm.tb_wm_bool.tb_uv_island == False or wm.tb_wm_bool.tb_uv_proj == False:         
                    row = box.row()
                if wm.tb_wm_bool.tb_uv_proj == False:
                    row.prop(wm.tb_wm_bool, "tb_uv_proj",text="Project",icon='MOD_UVPROJECT')
                #BOX                
                cw = wm.tb_wm_bool.tb_uv_proj
                cwt = "tb_uv_proj"
                cwtt = "Project"
                cwi = 'MOD_UVPROJECT'
                if cw == True:
                    box = layout.box()
                    row = box.row(align= True)        
                    row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
                    row.separator()                        
                    row.operator("uv.smart_project",icon='UV_DATA')
                    row.operator("uv.lightmap_pack",icon='STICKY_UVS_LOC')
                    row.operator("uv.follow_active_quads",icon='MOD_UVPROJECT')                                
                    row = box.row(align=True)
                    row.label(icon='BLANK1')
                    row.separator()
                    row.operator("uv.cube_project",text="Cube",icon='MESH_CUBE')                
                    row.operator("uv.cylinder_project",text="Cylinder",icon='MESH_CYLINDER')                
                    row.operator("uv.sphere_project",text="Sphere",icon='MESH_UVSPHERE')
def tb_def_pt_unwarp_img(self,context):
    wm = context.window_manager
    layout = self.layout
    box = layout.box()
    row = box.row(align=True)
    row.label(icon='UV')
    row.prop(context.scene.tool_settings,"use_edge_path_live_unwrap",icon='PROP_OFF',text="")
    row.operator("uv.unwrap",text="",icon='FILE_REFRESH')
    row.operator("uv.unwrap")
    row.prop(context.space_data.uv_editor,"lock_bounds",text="",icon='PIVOT_BOUNDBOX')
    row.operator("uv.export_layout",icon='EXPORT',text="")
    row.prop(wm.tb_wm_bool, "tb_uv_seam",text="",icon='COLORSET_01_VEC')                
    cw = wm.tb_wm_bool.tb_uv_seam
    if cw == True:
        row = box.row(align= True)        
        row.operator("mesh.mark_seam",icon='COLORSET_01_VEC')
        row.operator("mesh.mark_seam",text="Clear Seam").clear=True                
        row.operator("uv.seams_from_islands",text="Island")            
   #ORDER
    if wm.tb_wm_bool.tb_uv_island == False or wm.tb_wm_bool.tb_uv_proj == False:         
        row = box.row()
    if wm.tb_wm_bool.tb_uv_proj == False:
        row.prop(wm.tb_wm_bool, "tb_uv_proj",text="Project",icon='MOD_UVPROJECT')
    if wm.tb_wm_bool.tb_uv_island == False:
        row.prop(wm.tb_wm_bool, "tb_uv_island",text="Island",icon='UV_ISLANDSEL')
    if wm.tb_wm_bool.tb_uv_weld == False or wm.tb_wm_bool.tb_uv_snap == False:
        row = box.row()
    if wm.tb_wm_bool.tb_uv_weld == False:
        row.prop(wm.tb_wm_bool, "tb_uv_weld",text="Weld",icon='AUTOMERGE_OFF')
    if wm.tb_wm_bool.tb_uv_snap == False:
        row.prop(wm.tb_wm_bool, "tb_uv_snap",text="Snap",icon='SNAP_OFF')
   #PROJ
    cw = wm.tb_wm_bool.tb_uv_proj
    cwt = "tb_uv_proj"
    cwtt = "Project"
    cwi = 'MOD_UVPROJECT'
    if cw == True:
        box = layout.box()
        row = box.row(align= True)        
        row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
        row.separator()                        
        row.operator("uv.smart_project",icon='UV_DATA')
        row.operator("uv.lightmap_pack",icon='STICKY_UVS_LOC')
        row.operator("uv.follow_active_quads",icon='MOD_UVPROJECT')                                
        row = box.row(align=True)
        row.label(icon='BLANK1')
        row.separator()
        row.operator("uv.cube_project",text="Cube",icon='MESH_CUBE')                
        row.operator("uv.cylinder_project",text="Cylinder",icon='MESH_CYLINDER')                
        row.operator("uv.sphere_project",text="Sphere",icon='MESH_UVSPHERE')                                                
    cw = wm.tb_wm_bool.tb_uv_island
    cwt = "tb_uv_island"
    cwtt = "Island"
    cwi = 'UV_ISLANDSEL'
    if cw == True:
        box = layout.box()
        row = box.row(align= True)            
        row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
        row.separator()
        row.operator("uv.average_islands_scale",icon='CON_SIZELIMIT',text="")                 
        row.operator("uv.pack_islands",icon='UV_ISLANDSEL')
        row.operator("uv.minimize_stretch",icon='MOD_LATTICE')                   
    cw = wm.tb_wm_bool.tb_uv_weld
    cwt = "tb_uv_weld"
    cwtt = "Weld"
    cwi = 'AUTOMERGE_OFF'
    if cw == True:
        box = layout.box()
        row = box.row(align= True)            
        row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
        row.label(text=cwtt)
        row.operator("uv.weld")
        row.operator("uv.remove_doubles",icon='STICKY_UVS_LOC')                    
        row = box.row(align=True)
        row.label(icon='BLANK1')
        row.operator("uv.align",text="Align").axis='ALIGN_AUTO'
        row.operator("uv.align",text="",icon='EVENT_X').axis='ALIGN_X'                    
        row.operator("uv.align",text="",icon='EVENT_Y').axis='ALIGN_Y'
        row.separator()
        row.operator("uv.align",text="Straight").axis='ALIGN_S'                                                            
        row.operator("uv.align",text="",icon='EVENT_X').axis='ALIGN_U'
        row.operator("uv.align",text="",icon='EVENT_Y').axis='ALIGN_U'                    
   #SNAP
    cw = wm.tb_wm_bool.tb_uv_snap
    cwt = "tb_uv_snap"
    cwtt = "Snap"
    cwi = 'SNAP_OFF'
    if cw == True:
        box = layout.box()
        row = box.row(align= True)            
        row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
        row.label(text=cwtt)
        cw = wm.tb_wm_bool.tb_uv_snap_pix
        cwt = "tb_uv_snap_pix"
        cwtt = "To Pixel"
        cwi = 'ALIASED'
        if wm.tb_wm_bool.tb_uv_snap_sel == False:
            row.prop(wm.tb_wm_bool, "tb_uv_snap_sel",text="Selection",icon='RESTRICT_SELECT_OFF')   
        if wm.tb_wm_bool.tb_uv_snap_sel == False and cw == False:
            row.separator()
        if cw == False:
            row.prop(wm.tb_wm_bool, cwt,text=cwtt,icon=cwi)
        if wm.tb_wm_bool.tb_uv_snap_sel == True:
            row = box.row(align= True)
            row.prop(wm.tb_wm_bool, "tb_uv_snap_sel",text="",icon='RESTRICT_SELECT_ON')
            row.separator()           
            row.operator("uv.snap_selected",text="Pixels",icon='ALIASED').target='PIXELS'
            row.operator("uv.snap_selected",text="Adjacent Unselected",icon='STICKY_UVS_DISABLE').target='ADJACENT_UNSELECTED'  
            row = box.row(align= True)  
            row.label(icon='BLANK1')
            row.separator()                                            
            row.operator("uv.snap_selected",text="Cursor",icon='PIVOT_CURSOR').target='CURSOR'
            row.operator("uv.snap_selected",text="Cursor Offset",icon='ORIENTATION_CURSOR').target='CURSOR_OFFSET'
        if cw == True:
            row = box.row(align= True)            
            row.prop(wm.tb_wm_bool, cwt,text="",icon=cwi)
            row.prop_enum(context.space_data.uv_editor,"pixel_snap_mode","DISABLED",icon='X')
            row.prop_enum(context.space_data.uv_editor,"pixel_snap_mode","CORNER",icon='UV_VERTEXSEL')                    
            row.prop_enum(context.space_data.uv_editor,"pixel_snap_mode","CENTER",icon='PIVOT_BOUNDBOX')                                        
        cw = wm.tb_wm_bool.tb_uv_snap_sel
        cwt = "tb_uv_snap_sel"
        cwtt = "Selection"
        cwi = 'RESTRICT_SELECT_OFF'
class TB_UV_UI_3D(bpy.types.Panel):
    bl_label = "Unwrap Panel Viewport 3D"
    bl_idname = "TBPNL_PT_set_uv"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    bl_options = {'DEFAULT_CLOSED'}
    @classmethod
    def poll(cls, context):
        return context.object is not None and bpy.context.object.type == 'MESH' and bpy.context.mode == 'EDIT_MESH'
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='UV')    
    def draw(self, context):    
        tb_def_pt_unwarp_3d(self,context)
class TB_UV_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbuvpopup3d"
    bl_label = "Unwrap PoP Viewport 3D"
    @classmethod
    def poll(cls, context):
        return context.object is not None and bpy.context.object.type == 'MESH' and bpy.context.mode == 'EDIT_MESH'
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tb_def_pt_unwarp_3d(self,context)
    def execute(self, context):
        return {'FINISHED'}
#IMG
class TB_UV_UI_IMG(bpy.types.Panel):
    bl_label = "Unwrap Panel"
    bl_idname = "TBPNL_PT_set_uv_img"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "OUT"
    bl_label = "Unwrap Panel Image Editor"
    @classmethod
    def poll(cls, context):
        return context.object is not None and bpy.context.object.type == 'MESH' and bpy.context.mode == 'EDIT_MESH' and bpy.context.area.ui_type == 'UV'
    def draw(self, context):
        tb_def_pt_unwarp_img(self,context)
class TB_UV_PoP_IMG(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbuvimgpop"
    bl_label = "Unwrap PoP Image Editor"
    @classmethod
    def poll(cls, context):
        return context.object is not None and bpy.context.object.type == 'MESH' and bpy.context.mode == 'EDIT_MESH' and bpy.context.area.ui_type == 'UV'
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tb_def_pt_unwarp_img(self,context)               
    def execute(self, context):
        return {'FINISHED'}
