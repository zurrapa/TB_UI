import bpy
def ts3dcrsrot(context):
    bpy.context.scene.cursor.rotation_euler[1] = 0
    bpy.context.scene.cursor.rotation_euler[2] = 0
    bpy.context.scene.cursor.rotation_euler[0] = 0  
def ts3dcrslocx(context):
    bpy.context.scene.cursor.location[0] = 0  
def ts3dcrslocy(context):
    bpy.context.scene.cursor.location[1] = 0  
def ts3dcrslocz(context):
    bpy.context.scene.cursor.location[2] = 0  
def ts3dcrsrotx(context):
    bpy.context.scene.cursor.rotation_euler[0] = 0   
def ts3dcrsroty(context):
    bpy.context.scene.cursor.rotation_euler[1] = 0   
def ts3dcrsrotz(context):
    bpy.context.scene.cursor.rotation_euler[2] = 0
def tsobjlocx(context):
    bpy.context.object.location[0] = 0   
def tsobjlocy(context):
    bpy.context.object.location[1] = 0 
def tsobjlocz(context):
    bpy.context.object.location[2] = 0
def tsobjrotx(context):
    bpy.context.object.rotation_euler[0] = 0
def tsobjroty(context):
    bpy.context.object.rotation_euler[1] = 0
def tsobjrotz(context):
    bpy.context.object.rotation_euler[2] = 0
def proportional_dimension():
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    if tbb.tb_set_dim_proportional_axis == "X":
        active_axis = 0
    elif tbb.tb_set_dim_proportional_axis == "Y":        
        active_axis = 1
    else:
        active_axis = 2
    act_ob = bpy.context.active_object
    act_ob_dim = act_ob.dimensions
    return ((1.0/act_ob_dim[active_axis])*tbb.tb_set_dim_proportional_factor)

class TB_OT_prop_dim(bpy.types.Operator):
    bl_idname = "tb_ops.propdim"
    bl_label = "Set proportional dimension"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        dimension_op = proportional_dimension()
        bpy.ops.transform.resize(value=(dimension_op, dimension_op, dimension_op), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        return {'FINISHED'}


class Tcursor3dlocx(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_loc_x"
    bl_label = "Set Location 3D Cursor X"

    def execute(self, context):
        ts3dcrslocx(context)
        return {'FINISHED'}
class Tcursor3dlocy(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_loc_y"
    bl_label = "Set Location 3D Cursor Y"

    def execute(self, context):
        ts3dcrslocy(context)
        return {'FINISHED'}
class Tcursor3dlocz(bpy.types.Operator):

    bl_idname = "myops.t_cursor3d_loc_z"
    bl_label = "Set Location 3D Cursor Z"

    def execute(self, context):
        ts3dcrslocz(context)
        return {'FINISHED'}
class Tcursor3drotx(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_rot_x"
    bl_label = "Set Rotation 3D Cursor X"

    def execute(self, context):
        ts3dcrsrotx(context)
        return {'FINISHED'}
class Tcursor3droty(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_rot_y"
    bl_label = "Set Rotation 3D Cursor Y"

    def execute(self, context):
        ts3dcrsroty(context)
        return {'FINISHED'}
class Tcursor3drotz(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_rot_z"
    bl_label = "Set Rotation 3D Cursor Z"

    def execute(self, context):
        ts3dcrsrotz(context)
        return {'FINISHED'}
class Tcursor3drot0(bpy.types.Operator):
    bl_idname = "myops.t_cursor3d_rot_0"
    bl_label = "Set Rotation 3D Cursor 0"


    def execute(self, context):
        ts3dcrsrot(context)
        return {'FINISHED'}
class Tobjectlocx(bpy.types.Operator):
    bl_idname = "myops.t_object_loc_x"
    bl_label = "Set Location to X"

    def execute(self, context):
        tsobjlocx(context)
        return {'FINISHED'}
class Tobjectlocy(bpy.types.Operator):
    bl_idname = "myops.t_object_loc_y"
    bl_label = "Set Location to Y"

    def execute(self, context):
        tsobjlocy(context)
        return {'FINISHED'}
class Tobjectlocz(bpy.types.Operator):
    bl_idname = "myops.t_object_loc_z"
    bl_label = "Set Location to Z"

    def execute(self, context):
        tsobjlocz(context)
        return {'FINISHED'}

class Tobjectrotx(bpy.types.Operator):
    bl_idname = "myops.t_object_rot_x"
    bl_label = "Set Rotation to X"

    def execute(self, context):
        tsobjrotx(context)
        return {'FINISHED'}
class Tobjectroty(bpy.types.Operator):
    bl_idname = "myops.t_object_rot_y"
    bl_label = "Set Rotation to Y"

    def execute(self, context):
        tsobjroty(context)
        return {'FINISHED'}
class Tobjectrotz(bpy.types.Operator):
    bl_idname = "myops.t_object_rot_z"
    bl_label = "Set Rotation to Z"

    def execute(self, context):
        tsobjrotz(context)
        return {'FINISHED'}

def tsposdraw(self, context):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    layout = self.layout
    screen = context.screen
   #CURSOR3D
    cw = tbb.tb_set_3dc
    cwt = "tb_set_3dc"
    cwtt = "Cursor 3D"
    cwi = 'PIVOT_CURSOR'
    box = layout.box()
    if cw == False:
        box.prop(tbb, cwt,text=cwtt,icon=cwi)
    if cw == True:
        row = box.row(align= True)            
        row.prop(tbb, cwt,text="",icon=cwi)
        row.prop(context.space_data.overlay, "show_cursor", text= "Show Cursor 3D",icon='CURSOR')
        row.operator("view3d.view_center_cursor", text= "",icon='CAMERA_DATA')            
        split = box.split(factor=0.9, align=True)
        col = split.column(align=True)
        col.prop(context.scene.cursor, "location",text= "")
        row = col.row(align=True)
        row.operator("view3d.snap_cursor_to_center",text= " Origin ",icon='EMPTY_AXIS')
        col = split.column(align=True)        
        col.operator("myops.t_cursor3d_loc_x",text= "",icon='CON_LOCLIMIT')
        col.operator("myops.t_cursor3d_loc_y",text= "",icon='CON_LOCLIMIT')
        col.operator("myops.t_cursor3d_loc_z",text= "",icon='CON_LOCLIMIT')
        col.operator("view3d.snap_cursor_to_grid",text= "",icon='GRID')
        #Rotation
        split = box.split(factor=0.9, align=True)
        col = split.column(align=True)
        col.prop(context.scene.cursor, "rotation_euler",text= "")
        row = col.row(align=True)
        row.operator("myops.t_cursor3d_rot_0",text= " Reset Rotation ",icon='CON_ROTLIMIT')
        col = split.column(align=True)
        col.operator("myops.t_cursor3d_rot_x",text= "",icon='CON_ROTLIMIT')
        col.operator("myops.t_cursor3d_rot_y",text= "",icon='CON_ROTLIMIT')
        col.operator("myops.t_cursor3d_rot_z",text= "",icon='CON_ROTLIMIT')
        col.prop(context.scene.cursor, "rotation_mode", text="",icon='PRESET')
        row = box.row(align= True)
        row.operator("view3d.snap_cursor_to_active",text= "Cursor to Active",icon='PIVOT_ACTIVE')
        row.operator("view3d.snap_cursor_to_selected",text= "Cursor to Selection",icon='PIVOT_MEDIAN')
        row = box.row(align= True)
        row.operator("object.origin_set",text="Origin To Cursor", icon='ORIENTATION_CURSOR'). type='ORIGIN_CURSOR'
        row.operator("view3d.snap_selected_to_cursor",text="Geo to Cursor", icon='PIVOT_CURSOR')
    #ORIGINS
    cw = tbb.tb_set_ori
    cwt = "tb_set_ori"
    cwtt = "Origin"
    cwi = 'TRANSFORM_ORIGINS'
    box = layout.box()
    if cw == False:
        box.prop(tbb, cwt,text=cwtt,icon=cwi)
    if cw == True:
        row = box.row(align= True)            
        row.prop(tbb, cwt,text="",icon=cwi)
        row.label(text="Origin")
        split = box.split(factor=0.5, align=True)
        col = split.column(align=True)
        col.operator("object.origin_set",text="Geo To Origin", icon='PIVOT_BOUNDBOX'). type='GEOMETRY_ORIGIN'
        col.operator("object.origin_set",text="Origin(Mass)", icon='MOD_MESHDEFORM'). type='ORIGIN_CENTER_OF_MASS'
        col.operator("object.origin_set",text="Origin(Volume)", icon='OUTLINER_DATA_META'). type='ORIGIN_CENTER_OF_VOLUME'
        col = split.column(align=True)
        col.operator("object.origin_set",text="To Cursor", icon='PIVOT_CURSOR'). type='ORIGIN_CURSOR'
        col.operator("object.origin_set",text="Origin To Geo", icon='OUTLINER_DATA_MESH'). type='ORIGIN_GEOMETRY'
        col.operator("object.transform_apply",text="To Scene Origin", icon='EMPTY_AXIS')
    #LOCATION        
    if bpy.context.object:
        box = layout.box()
        ob = context.object
        if tbb.tb_set_loc == False:
            box.prop(tbb, "tb_set_loc",text="Transform Panel",icon='ORIENTATION_LOCAL')
        if tbb.tb_set_loc == True:
            row = box.row(align= True)            
            row.prop(tbb, "tb_set_loc",text="",icon='ORIENTATION_LOCAL')
            if bpy.context.object.type:
                if bpy.context.object.type == 'EMPTY':
                    row.prop(ob, "empty_display_type", text="")
                    row.prop(ob, "empty_display_size", text="Size")
                    if bpy.context.object.empty_display_type == 'IMAGE':
                        box.template_ID(ob, "data", open="image.open", unlink="object.unlink_data")
                if ob:
                    if not bpy.context.object.type == 'EMPTY':
                        row.template_ID(ob, "data")
                elif mesh:
                    row.template_ID(space, "pin_id")
                if ob.type == 'CAMERA':
                    view = context.space_data                    
                    if view.region_3d.view_perspective != 'CAMERA':
                        row.prop(view, "use_render_border",icon='OBJECT_HIDDEN',text="")
                    else:
                        row.prop(view, "lock_camera",icon='CON_CAMERASOLVER',text="")                 
                #Start
                row = box.row(align= True)   
                row.operator("view3d.snap_selected_to_active",text="Geo to Active", icon='PIVOT_ACTIVE')
                row.operator("view3d.snap_selected_to_cursor",text="Geo to Cursor", icon='ORIENTATION_CURSOR')
                split = box.split( align=True)
                col = split.column(align=True)
                col.prop(context.scene.tool_settings, "use_transform_data_origin", text= "Origins",icon='OBJECT_ORIGIN')
                col = split.column(align=True)
                col.prop(context.scene.tool_settings, "use_transform_pivot_point_align", text= "Locations",icon='EMPTY_ARROWS')
                col = split.column(align=True)
                col.prop(context.scene.tool_settings, "use_transform_skip_children", text= "Parents",icon='CON_CHILDOF')
                split = box.split(factor=0.8, align=True)
                col = split.column(align=True)
                col.prop(context.object, "location",text= "")
                col.operator("object.location_clear",text= " Clear Location ",icon='EMPTY_AXIS')         
                col = split.column(align=True)
                col.operator("myops.t_object_loc_x",text= "",icon='CON_LOCLIMIT')
                col.operator("myops.t_object_loc_y",text= "",icon='CON_LOCLIMIT')
                col.operator("myops.t_object_loc_z",text= "",icon='CON_LOCLIMIT')
                col.operator("view3d.snap_selected_to_grid",text="", icon='GRID')
                col = split.column(align=True)
                col.prop(context.object, "lock_location",text="")
                #Rotation
                split = box.split(factor=0.8, align=True)
                col = split.column(align=True)
                if ob.rotation_mode == 'QUATERNION':
                    col.column(align=True).prop(ob, "rotation_quaternion", text="")
                elif ob.rotation_mode == 'AXIS_ANGLE':
                    col.column(align=True).prop(ob, "rotation_axis_angle", text="")
                else:
                    col.column(align=True).prop(ob, "rotation_euler", text="")
                col.operator("object.rotation_clear",text= "    Clear Rotation    ",icon='CON_ROTLIMIT')
                col = split.column(align=True)
                col.operator("myops.t_object_rot_x",text= "",icon='CON_ROTLIMIT')
                col.operator("myops.t_object_rot_y",text= "",icon='CON_ROTLIMIT')
                col.operator("myops.t_object_rot_z",text= "",icon='CON_ROTLIMIT')
                col.prop(context.object, "rotation_mode",text="",icon='PRESET')
                col = split.column(align=True)
                col.prop(context.object, "lock_rotation",text="")
                #Scale
                split = box.split(factor=0.8, align=True)
                col = split.column(align=True)
                col.prop(context.object, "scale",text= "")
                col.operator("object.rotation_clear",text= "    Clear Scale    ",icon='CON_SIZELIMIT')
                col = split.column(align=True)
                col.operator("myops.t_object_rot_x",text= "",icon='CON_SIZELIMIT')
                col.operator("myops.t_object_rot_y",text= "",icon='CON_SIZELIMIT')
                col.operator("myops.t_object_rot_z",text= "",icon='CON_SIZELIMIT')
                col = split.column(align=True)
                col.prop(context.object, "lock_scale",text="")
                split = box.split(align=True)
                split = box.split(factor=0.5, align=True)
                col = split.column(align=True)
                props = col.operator("object.transform_apply",text= "Apply Location",icon='CON_LOCLIKE')
                props.location=True
                props.rotation=False
                props.scale=False
                props = col.operator("object.transform_apply",text= "Apply Rotation",icon='CON_ROTLIKE')
                props.location=False
                props.rotation=True
                props.scale=False
                props = col.operator("object.transform_apply",text= "Apply Scale",icon='CON_SIZELIKE')
                props.location=False
                props.rotation=False
                props.scale=True
                props = col.operator("object.transform_apply",text= "Apply All",icon='ORIENTATION_LOCAL')
                props.location=True
                props.rotation=True
                props.scale=True
                col = split.column(align=True)
                col.operator("object.transforms_to_deltas",text= "Delta Transform",icon='CON_LOCLIMIT').mode= 'LOC'
                col.operator("object.transforms_to_deltas",text= "Delta Rotation",icon='CON_ROTLIKE').mode= 'ROT'
                col.operator("object.transforms_to_deltas",text= "Delta Size",icon='CON_SIZELIMIT').mode= 'SCALE'
                col.operator("object.transforms_to_deltas",text= "All Delta",icon='EMPTY_ARROWS').mode= 'ALL'
                row = box.row(align= True)
                row.operator("object.visual_transform_apply",text= "Transform Apply",icon='VIS_SEL_11')
                row.operator("object.convert",text= "Convert to Mesh",icon='OUTLINER_DATA_MESH').target='MESH'
                row.operator("object.duplicates_make_real",text= "Duplicates",icon='DUPLICATE')        
        cw = tbb.tb_set_dim
        cwt = "tb_set_dim"
        cwtt = "Dimensions"
        cwi = 'ORIENTATION_GLOBAL'
        box = layout.box()
        if cw == False:
            box.prop(tbb, cwt,text=cwtt,icon=cwi)
        if cw == True:
            row = box.row(align= True)            
            row.prop(tbb, cwt,text="",icon=cwi)
            row.label(text="Dimensions")
            if tbb.tb_set_dim_proportional:
                row.prop(tbb,"tb_set_dim_proportional",text="",icon='PROP_ON')
                row.prop(tbb,"tb_set_dim_proportional_factor",text="")
                row.operator("tb_ops.propdim",text="",icon='CHECKMARK')       
            else:
                row.prop(tbb,"tb_set_dim_proportional",text="Proportional",icon='PROP_ON')
            row = box.row(align= True)         
            row.prop(context.active_object,"dimensions",index=0,text="X")
            row.prop(context.active_object,"dimensions",index=1,text="Y")
            row.prop(context.active_object,"dimensions",index=2,text="Z")
            if tbb.tb_set_dim_proportional:    
                row = box.row(align= True)                 
                row.prop_enum(tbb,"tb_set_dim_proportional_axis","X",text="X")
                row.prop_enum(tbb,"tb_set_dim_proportional_axis","Y",text="Y")
                row.prop_enum(tbb,"tb_set_dim_proportional_axis","Z",text="Z")        
    else:
        box = layout.box()
        row = box.row(align= True)            
        row.label(icon='ORIENTATION_LOCAL')
        row.label(icon='BLANK1')            
        row.label(text="No Object Select",icon='OBJECT_DATA')
class TB_Transform_UI_3D(bpy.types.Panel):
    bl_label = "Transform Panel"
    bl_idname = "OBJECT_PT_TB_SET_UI"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    @classmethod
    def poll(cls, context):
        return context.object is not None
    def draw_header(self, context):
        self.layout.label(icon='ORIENTATION_LOCAL')

    def draw(self, context):
        tsposdraw(self, context)
class TB_Transform_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tstransform_popup"
    bl_label = "Transform Popup"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        tsposdraw(self, context)
    def execute(self, context):
        return {'FINISHED'}
