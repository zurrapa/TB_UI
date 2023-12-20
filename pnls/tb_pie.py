import bpy
from bpy.types import Menu
class TB_PIE_ORIGIN(Menu):
    bl_label = "Origin Pie"
    bl_idname= "TB_MT_Pie_Origin"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("object.origin_set",text="Geo To Origin", icon='PIVOT_BOUNDBOX'). type= 'GEOMETRY_ORIGIN'  
        pie.operator("object.origin_set",text="Origin(Mass)", icon='MOD_MESHDEFORM'). type='ORIGIN_CENTER_OF_MASS'
        pie.operator("object.origin_set",text="Origin To Cursor", icon='ORIENTATION_CURSOR'). type='ORIGIN_CURSOR'
        pie.operator("object.transform_apply",text="To Scene Origin", icon='EMPTY_AXIS')
        pie.operator("object.origin_set",text="Origin To Geo", icon='OUTLINER_DATA_MESH'). type='ORIGIN_GEOMETRY'
        pie.operator("object.origin_set",text="Origin(Volume)", icon='OUTLINER_DATA_META'). type='ORIGIN_CENTER_OF_VOLUME'

class TB_PIE_ORIENTATION(Menu):
    bl_label = "Orientation Pie"
    bl_idname= "TB_MT_Pie_Orientation"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'VIEW',text="VIew", icon='ORIENTATION_VIEW')
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'LOCAL',text="Local", icon='ORIENTATION_LOCAL')
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'CURSOR',text="Cursor", icon='ORIENTATION_CURSOR')
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'GLOBAL',text="Global", icon='ORIENTATION_GLOBAL')
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'NORMAL',text="Normal", icon='ORIENTATION_NORMAL')
        pie.prop_enum(context.scene.transform_orientation_slots[0],"type",'GIMBAL',text="Gimbal", icon='ORIENTATION_GIMBAL')
class TB_PIE_PIVOT(Menu):
    bl_label = "Pivot Pie"
    bl_idname= "TB_MT_Pie_Pivot"

    def draw(self, context):
        mode_string = context.mode        
        layout = self.layout
        pie = layout.menu_pie()
        pie.prop_enum(context.scene.tool_settings,"transform_pivot_point",'INDIVIDUAL_ORIGINS',text="Individual", icon='PIVOT_INDIVIDUAL')
        pie.prop_enum(context.scene.tool_settings,"transform_pivot_point",'MEDIAN_POINT',text="Median", icon='PIVOT_MEDIAN')
        pie.prop_enum(context.scene.tool_settings,"transform_pivot_point",'CURSOR',text="Cursor", icon='PIVOT_CURSOR')
        pie.prop_enum(context.scene.tool_settings,"transform_pivot_point",'BOUNDING_BOX_CENTER',text="Bounding", icon='PIVOT_BOUNDBOX')
        pie.prop_enum(context.scene.tool_settings,"transform_pivot_point",'ACTIVE_ELEMENT',text="Active", icon='PIVOT_ACTIVE')

class TB_PIE_MERGE(Menu):
    bl_label = "PivotMerge Pie"
    bl_idname= "TB_MT_Merge_Pivot"
    def draw(self, context):        
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("mesh.merge",text="Cursor", icon='PIVOT_CURSOR').type='CURSOR'
        pie.operator("mesh.merge",text="Center", icon='PIVOT_MEDIAN').type='CENTER'
        pie.operator("mesh.merge",text="Collapse", icon='PIVOT_MEDIAN').type='COLLAPSE'
        if bpy.context.tool_settings.mesh_select_mode[1] or bpy.context.tool_settings.mesh_select_mode[2]:        
            pie.label(text="")
            pie.label(text="")    
        else:
            pie.operator("mesh.merge",text="First", icon='PIVOT_ACTIVE').type='FIRST'
            pie.operator("mesh.merge",text="Last", icon='PIVOT_ACTIVE').type='LAST'
        if bpy.context.tool_settings.mesh_select_mode[0]:             
            pie.operator("mesh.remove_doubles",text="Remove Doubles", icon='DRIVER_DISTANCE')        
        else:
            pie.label(text="")                      