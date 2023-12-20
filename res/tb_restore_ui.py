import bpy
from . import tb_keep_ui
from ..ui import tb_replace_icons
#UNAPEND
bpy.types.VIEW3D_HT_header.remove(tb_replace_icons.TB_VIEW3D_UI_HEADER)
bpy.types.SEQUENCER_HT_header.remove(tb_replace_icons.TB_SEQUENCER_HT_header)
bpy.types.DATA_PT_vertex_groups.remove(tb_replace_icons.TB_DATA_PT_vertex_groups)
bpy.types.FILEBROWSER_PT_directory_path.remove(tb_replace_icons.TB_BROWSER_UI_HEADER)
#REDRAW
bpy.types.TOPBAR_MT_editor_menus.draw = tb_keep_ui.keep_TOPBAR_MT_editor_menus
bpy.types.VIEW3D_MT_editor_menus.draw = tb_keep_ui.keep_VIEW3D_MT_editor_menus
bpy.types.TEXT_MT_editor_menus.draw = tb_keep_ui.keep_TEXT_MT_editor_menus
bpy.types.NODE_MT_editor_menus.draw = tb_keep_ui.keep_NODE_MT_editor_menus
bpy.types.CONSOLE_MT_editor_menus.draw = tb_keep_ui.keep_CONSOLE_MT_editor_menus
bpy.types.INFO_MT_editor_menus.draw = tb_keep_ui.keep_INFO_MT_editor_menus
bpy.types.DOPESHEET_MT_editor_menus.draw = tb_keep_ui.keep_DOPESHEET_MT_editor_menus
bpy.types.IMAGE_MT_editor_menus.draw = tb_keep_ui.keep_IMAGE_MT_editor_menus

