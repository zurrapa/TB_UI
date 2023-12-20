import bpy
from bpy.app.translations import pgettext_iface as iface_

def tb_notes_draw(self,context):
    sd = bpy.context.space_data
    layout = self.layout
    box = layout.box()
    if context.area.type == 'VIEW_3D':
        row = box.row()
        sd_o = sd.overlay
        row.prop(sd_o, "show_annotation", text= "Toggle Annotation",icon='GREASEPENCIL')
    else:
        row = box.row()
        row.prop(sd,"show_annotation", text= "Toggle Annotation",icon='GREASEPENCIL')

    gpd_owner = context.annotation_data_owner
    gpd = context.annotation_data                
    bor = box.box()
    if context.area.type == 'VIEW_3D':
        row = bor.row(align=True)
        row.prop_enum(context.scene.tool_settings,"annotation_stroke_placement_view3d",'VIEW',text="")        
        row.prop_enum(context.scene.tool_settings,"annotation_stroke_placement_view3d",'SURFACE',text="")        
        row.prop_enum(context.scene.tool_settings,"annotation_stroke_placement_view3d",'CURSOR',text="")        
        row.separator()                 
        row.prop(context.scene.tool_settings,"use_gpencil_stroke_endpoints",icon='GP_ONLY_SELECTED')
    bor.template_ID(gpd_owner, "grease_pencil", new="gpencil.annotation_add", unlink="gpencil.data_unlink")                       
    if gpd is not None:
        if gpd:
            row = bor.row()
            col = row.column()
            if len(gpd.layers) >= 2:
                layer_rows = 5
            else:
                layer_rows = 1
            col.template_list("GPENCIL_UL_annotation_layer", "", gpd, "layers", gpd.layers, "active_index",
                            rows=layer_rows, sort_reverse=True, sort_lock=True)
            col = row.column()
            sub = col.column(align=True)
            sub.operator("gpencil.layer_annotation_add", icon='ADD', text="")
            sub.operator("gpencil.layer_annotation_remove", icon='REMOVE', text="")
            gpl = context.active_annotation_layer
            if gpl == True:
                if len(gpd.layers) > 1:
                    col.separator()
                    sub = col.column(align=True)
                    sub.operator("gpencil.layer_annotation_move", icon='TRIA_UP', text="").type = 'UP'
                    sub.operator("gpencil.layer_annotation_move", icon='TRIA_DOWN', text="").type = 'DOWN'
            tool_settings = context.tool_settings
            row = bor.row(align=True)                
            if gpd and gpl:
                row.prop(gpl, "annotation_opacity", text="Opacity", slider=True)
                row = bor.row(align=True)   
                row.prop(gpl, "thickness")
            else:
                row.prop(tool_settings, "annotation_thickness", text="Thickness")
            if context.area.type == 'VIEW_3D':
                if len(gpd.layers) >= 1:  
                    row.separator()
                    row.prop(gpl, "use_annotation_onion_skinning", text="",icon='ONIONSKIN_ON')  
                    if gpl.use_annotation_onion_skinning == True:               
                        row = bor.row(align=True)
                        row.prop(gpl, "annotation_onion_before_color", text="")
                        row.prop(gpl, "annotation_onion_after_color", text="")
                        row = bor.row(align=True)                
                        row.prop(gpl, "annotation_onion_before_range", text="Before")
                        row.prop(gpl, "annotation_onion_after_range", text="After")      
            if gpl:
                row = bor.row(align=True)
                row.active = not gpl.lock
                if gpl.active_frame:
                    lock_status = iface_("Locked") if gpl.lock_frame else iface_("Unlocked")
                    lock_label = iface_("Frame: %d (%s)") % (gpl.active_frame.frame_number, lock_status)
                else:
                    lock_label = iface_("Lock Frame")
                row.prop(gpl, "lock_frame", text=lock_label, icon='UNLOCKED')
                row.operator("gpencil.annotation_active_frame_delete", text="", icon='X')        

class TB_Notes_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbnotespopup"
    bl_label = "Annotation PoP Viewport 3D"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tb_notes_draw(self, context)
    def execute(self, context):
        return {'FINISHED'}   
class TB_Notes_PoP_IMG(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbnotesipopup"
    bl_label = "Annotation PoP Image Editor"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tb_notes_draw(self, context)
    def execute(self, context):
        return {'FINISHED'} 
class TB_Notes_PoP_NDS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbnotesnpopup"
    bl_label = "Annotation PoP Node Editor"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tb_notes_draw(self, context)
    def execute(self, context):
        return {'FINISHED'}
