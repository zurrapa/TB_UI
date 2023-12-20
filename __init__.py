# "Kreepyrights (GNU GPL) <2022> <tbtbpy, Taiseibutsu>" Developed for Blender 3.2
# This program is free software: you can redistribute it and/or modify it, WITHOUT ANY WARRANTY that wont wake up on the backrooms. --- Kreepyrights is just a joke, this is license under GNU General Public License (GPL, or “free software”), but just with a strange name to reference, or maybe not...

bl_info = {
    "name": "TBF", "author": "tbtbpy, Taiseibutsu",
    "version": (0, 1), "blender": (2, 80, 0), "location": "General UI Changes",
    "description": "Custom flavor for Blender",
    "warning": "This addon may breack and overwrite parts from your userpref, save your pref before starting", "wiki_url": "", "category": "TB"}

import bpy, bmesh, addon_utils, os, rna_keymap_ui
from bpy.types import AddonPreferences, Operator, Header, Menu, Panel, Curve, SurfaceCurve, TextCurve
from .res import tb_panel_bool, tb_keep_ui
from .pnls import tb_pt_notes,tb_pt_unwrap,tb_pt_tool,tb_pt_bake,tb_pt_data,tb_pt_frame,tb_pt_overlay,tb_pie,tb_pt_render,tb_pt_transform, tb_pt_shader
from .ui import tb_workspaces
#from .ui import tb_add_browser

class TB_UI_Workspaces(bpy.types.PropertyGroup):
    tb_workspace_01: bpy.props.StringProperty(default="LT")

class TB_PreferencesPanels(AddonPreferences):
    bl_idname = __name__
    def draw(self, context):
        wm = bpy.context.window_manager
        layout = self.layout
        layout.label(text="Make sure you are using 2.82 or Shading Panel won't work properly", icon="ERROR")
        box=layout.box()
        box.label(text="tb_set = 3D Cursor, Origins, Trnasforms")
        box.label(text="tb_scn = Render, Output, Bake, Frame, Layer/Compositing : Settings")
        box.label(text="tb_ovr = Overlays, Viewport Shading,  UI Colors")
        layout.label(text="Hotkey:")
        box.prop(self, "category", text="")
        row = layout.row()
        if wm.tb_wm_bool.keymap_bool:
            temp_bool_text = ""
        else:
            temp_bool_text = "Show Extra Keymaps"            
        row.prop(wm.tb_wm_bool,"keymap_bool",icon='PROP_ON',text=temp_bool_text)
        if wm.tb_wm_bool.keymap_bool:
            col = layout.column()
            kc = bpy.context.window_manager.keyconfigs.addon
            for km, kmi in addon_keymaps:
                km = km.active()
                col.context_pointer_set("keymap", km)
                rna_keymap_ui.draw_kmi([], kc, km, kmi, col, 0)

addon_keymaps = []
classes = (
   #NOTES 
    tb_pt_notes.TB_Notes_PoP_3D,
    tb_pt_notes.TB_Notes_PoP_NDS,
    tb_pt_notes.TB_Notes_PoP_IMG,
   #TRANSFORM 
    tb_pt_transform.TB_OT_prop_dim,
    tb_pt_transform.TB_Transform_UI_3D,    
    tb_pt_transform.TB_Transform_PoP_3D,    
   #Data 
    tb_pt_data.TB_Data_UI_3D,
    tb_pt_data.TB_Data_PoP_3D, 
   #TOOL 
    tb_pt_tool.TB_Data_Tool_UI_3D,
    tb_pt_tool.TB_Data_Tool_PoP_3D,   
   #BAKE
    tb_pt_bake.TB_Bake_UI_3D,
   #Time
    tb_pt_frame.TB_Frame_UI_3D,
    tb_pt_frame.TB_Frame_PoP_3D,   
   #OVERLAY
    tb_pt_overlay.TB_Overlay_UI_3D,
    tb_pt_overlay.TB_Overlay_PoP_3D,
    tb_pt_overlay.TB_Overlay_UI_IMG,
    tb_pt_overlay.TB_Overlay_PoP_IMG,
    tb_pt_overlay.TB_Overlay_NDS,
    tb_pt_overlay.TB_Overlay_NDS_PoP,   
   #RENDER
    tb_pt_render.TB_PT_Render_UI_3D,
    tb_pt_render.TB_PT_Render_PoP_3D,
    #RENDER
    tb_pt_render.TB_PT_Render_UI_3D_RENDER,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_RESOLUTION,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_OUTPUT,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_SAMPLES,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_LIGHT,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_FILM,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_PREF,
    #POSTPROCESS
    tb_pt_render.TB_PT_Render_UI_3D_POST_PROCESS,
    tb_pt_render.TB_PT_Render_UI_3D_COLOR,
    tb_pt_render.TB_PT_Render_UI_3D_SHADOW,
    tb_pt_render.TB_PT_Render_UI_3D_POST_SUBSURFACESCATTER,
    tb_pt_render.TB_PT_Render_UI_3D_POST_DEPTHFIELD,
    tb_pt_render.TB_PT_Render_UI_3D_POST_MOTIONBLUR,
    tb_pt_render.TB_PT_Render_UI_3D_POST_AMBIENT_OCCLUSION,
    tb_pt_render.TB_PT_Render_UI_3D_POST_BLOOM,
    tb_pt_render.TB_PT_Render_UI_3D_POST_SCREENSPACEREFLECTIONS,
    tb_pt_render.TB_PT_Render_UI_3D_VOLUME,
    tb_pt_render.TB_PT_Render_UI_3D_SCENE_LEVEL,
    tb_pt_render.TB_PT_Render_UI_3D_RENDER_SIMPLY,
    tb_pt_render.TB_PT_Render_UI_3D_LEVEL_HAIR,
    tb_pt_render.TB_PT_Render_UI_3D_GREASE_PENCIL,
    tb_pt_render.TB_PT_Render_UI_3D_FREESTYLE,   
    tb_workspaces.TB_WORKSPACE_LT,
    tb_workspaces.TB_WORKSPACE_UV,
    tb_workspaces.TB_WORKSPACE_NG,
    tb_workspaces.TB_WORKSPACE_NS,
    tb_workspaces.TB_WORKSPACE_NGS,
    tb_workspaces.TB_WORKSPACE_CM,
    tb_workspaces.TB_WORKSPACE_SCR,
   #SHADER
    tb_pt_shader.TB_Shading_PoP_3D,
    tb_pt_shader.TB_Shading_UI_3D,
   #UNWRAP
    tb_pt_unwrap.TB_UV_UI_3D,        
    tb_pt_unwrap.TB_UV_PoP_3D,        
    tb_pt_unwrap.TB_UV_UI_IMG,            
    tb_pt_unwrap.TB_UV_PoP_IMG,  
   #Pie
    tb_pie.TB_PIE_ORIGIN, 
    tb_pie.TB_PIE_ORIENTATION, 
    tb_pie.TB_PIE_PIVOT, 
    tb_pie.TB_PIE_MERGE, 
   #  
    TB_PreferencesPanels,
)
preview_collections = {}
def tb_register_icons():
    import bpy.utils.previews
    icons = ["tbi_clean","tbi_refresh","tbi_0"]
    bpy.types.Scene.tb_pnl_icons = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname( __file__ ), "ico")
    for icon in icons:
        bpy.types.Scene.tb_pnl_icons.load(icon, os.path.join(icons_dir, icon + ".png" ), 'IMAGE')

def key(dfbool,km,kmi):
    kmi.active = dfbool
    addon_keymaps.append((km, kmi)) 
def keypie(dfbool,km,keypie,namepie):
    kmi = km.keymap_items.new("wm.call_menu_pie", keypie, 'PRESS')
    kmi.properties.name = namepie
    kmi.active = dfbool
    addon_keymaps.append((km, kmi)) 

def register():
 #CLASS
    for cls in classes:
        bpy.utils.register_class(cls)
    from .ui import tb_replace_icons
 #KEYMAP
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    tb_register_icons()
    
    bpy.utils.register_class(TB_UI_Workspaces)
    bpy.types.WindowManager.tb_workspaces = bpy.props.PointerProperty(type=TB_UI_Workspaces)
    
    if kc:    
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        key(True,km,km.keymap_items.new("context.tbframepopup", 'Y', 'PRESS', alt=True, ctrl=True, shift=True))   
        km = kc.keymaps.new(name='Screen', space_type='EMPTY')
        key(True,km,km.keymap_items.new("context.tb_workspace_lt", 'BACK_SLASH', 'CLICK_DRAG',direction = 'SOUTH', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_ng", 'BACK_SLASH', 'CLICK_DRAG',direction = 'NORTH_EAST', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_ns", 'BACK_SLASH', 'CLICK_DRAG',direction = 'SOUTH_EAST', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_ngs", 'BACK_SLASH', 'CLICK_DRAG',direction = 'EAST', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_cm", 'BACK_SLASH', 'CLICK_DRAG',direction = 'NORTH', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_uv", 'BACK_SLASH', 'CLICK_DRAG',direction = 'SOUTH_WEST', alt=True))
        key(True,km,km.keymap_items.new("context.tb_workspace_scr", 'BACK_SLASH', 'CLICK_DRAG',direction = 'NORTH_WEST', alt=True))
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        key(True,km,km.keymap_items.new("context.tbnotespopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tstransform_popup", 'C', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbuvpopup3d", 'U', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbtoolpopup", 'T', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbdatapopup", 'W', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tboverlaypopup", 'Q', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbrenderpopup", 'R', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbshadingpopup", 'Z', 'PRESS', alt=True, ctrl=True, shift=True))

        #PIE
        keypie(True,km,'MINUS',"TB_MT_Pie_Origin")
        keypie(True,km,'COMMA',"TB_MT_Pie_Orientation")
        keypie(True,km,'PERIOD',"TB_MT_Pie_Pivot")
        keypie(True,km,'M',"TB_MT_Merge_Pivot")

        km = kc.keymaps.new(name='Image', space_type='IMAGE_EDITOR')
        key(True,km,km.keymap_items.new("context.tbnotesipopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tbuvimgpop", 'U', 'PRESS', alt=True, ctrl=True))   
        key(True,km,km.keymap_items.new("context.tboverlayimgpopup", 'Q', 'PRESS', alt=True, ctrl=True, shift=True))   
        km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        key(True,km,km.keymap_items.new("context.tbnotesnpopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True))
        key(True,km,km.keymap_items.new("context.tboverlayndspopup", 'Q', 'PRESS', alt=True, ctrl=True, shift=True))
        #km = kc.keymaps.new(name='File Browser', space_type='FILE_BROWSER')
        #key(True,km,km.keymap_items.new("p.filesizedecrease", 'WHEELOUTMOUSE', 'PRESS', alt=True))
        #key(True,km,km.keymap_items.new("tbcontext.filesizedecrease", 'WHEELINMOUSE', 'PRESS', alt=True))   

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    from .res import tb_restore_ui
 #KEYMAP
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()    

    bpy.utils.previews.remove(bpy.types.Scene.tb_pnl_icons)   
if __name__ == "__main__":
    register()

#from addns import tb_data_renamer, tb_view_to_individual_selection