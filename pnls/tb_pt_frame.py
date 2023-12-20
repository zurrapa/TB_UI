import bpy

def tbframedraw(self, context):
    scene = context.scene
    rd = scene.render
    screen = context.screen
    tool_settings = context.tool_settings
    layout = self.layout
    box = layout.box()
    split = box.split(align=True)
    col = split.column(align=True)
    col.prop(tool_settings, "use_keyframe_insert_auto", text="", toggle=True)
    col.separator()
    col = split.column(align=True)
    col = split.column(align=True)
    col.operator("screen.frame_jump", text="", icon='REW').end = False
    col = split.column(align=True)
    col.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False
    if not screen.is_animation_playing:
        if scene.sync_mode == 'AUDIO_SYNC' and context.preferences.system.audio_device == 'JACK':
            col = split.column(align=True)
            col.operator("screen.animation_play", text="", icon='PLAY')
        else:
            col = split.column(align=True)
            col.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
            col = split.column(align=True)
            col.operator("screen.animation_play", text="", icon='PLAY')
    else:
        col = split.column(align=True)
        col.operator("screen.animation_play", text="", icon='PAUSE')
    col = split.column(align=True)
    col.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
    col = split.column(align=True)
    col.operator("screen.frame_jump", text="", icon='FF').end = True
    box.prop(scene, "frame_current", text="")
    row = box.row(align=True)
    row.prop(scene, "use_preview_range", text="", toggle=True)
    row.prop(scene, "frame_start", text="Frame Start")
    row.prop(scene, "frame_end", text="End")
    row.prop(scene, "frame_step", text="Step")
    row = box.row(align=True)
    row.prop(rd, "fps")
    row.prop(rd, "fps_base", text="Base")
    row = box.row(align=True) 
    row.prop(rd, "frame_map_old", text="Old")
    row.prop(rd, "frame_map_new", text="New")
class TB_Frame_UI_3D(bpy.types.Panel):
    bl_label = "Frame"
    bl_idname = "TBPNL_PT_Set_Frame_UI"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    bl_options = {'DEFAULT_CLOSED'}
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='MOD_TIME')       
    def draw(self, context):
        tbframedraw(self, context)     
class TB_Frame_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_label = "Frame"
    bl_idname = "context.tbframepopup"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tbframedraw(self,context)
    def execute(self, context):
        return {'FINISHED'}    
