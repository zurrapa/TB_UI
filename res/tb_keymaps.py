import bpy

addon_keymaps = []
wm = bpy.context.window_manager
kc = wm.keyconfigs.addon
if kc:    
#3Dview
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new("context.tbnotespopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True)
    kmi.active = True
    addon_keymaps.append((km, kmi))
#Image_Editor
    km = kc.keymaps.new(name='Image', space_type='IMAGE_EDITOR')
    kmi = km.keymap_items.new("context.tbnotesipopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True)
    kmi.active = True
    addon_keymaps.append((km, kmi))
#Node_Editor
    km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
    kmi = km.keymap_items.new("context.tbnotesnpopup", 'D', 'PRESS', alt=True, ctrl=True, shift=True)
    kmi.active = True
    addon_keymaps.append((km, kmi))  

../__init__.addon_keymaps = addon_keymaps