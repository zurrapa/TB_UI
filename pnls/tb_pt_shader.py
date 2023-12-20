import bpy 

def tbshadingdraw(self,context):    
    wm = context.window_manager
    tbb = wm.tb_wm_bool
    ob = context.object

    layout = self.layout
    box = layout.box()
    row = box.row(align=True)
    row.prop_enum(context.scene.render, "engine", "BLENDER_WORKBENCH", icon='SHADING_SOLID')
    row.prop_enum(context.scene.render, "engine", "BLENDER_EEVEE", icon='SHADING_TEXTURE')
    row.prop_enum(context.scene.render, "engine", "CYCLES", icon='SHADING_RENDERED')
    if bpy.context.scene.render.engine == 'CYCLES':
        cscene = context.scene.cycles
        row = box.row(align=True)
        row.prop(cscene, "feature_set",text="")
        row.prop(cscene, "device",text="")
        if cscene.device == 'CPU':
            row.prop(cscene, "shading_system",text="",icon='NODE_MATERIAL')       
    row = box.row(align=True)
    row.prop_enum(context.space_data.shading, "type", "WIREFRAME", icon='SHADING_WIRE')
    row.prop_enum(context.space_data.shading, "type", "SOLID", icon='SHADING_SOLID')
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES':
        row.prop_enum(context.space_data.shading, "type", "MATERIAL", icon='SHADING_TEXTURE')
    row.prop_enum(context.space_data.shading, "type", "RENDERED", icon='SHADING_RENDERED')        
    if bpy.context.space_data.shading.type == 'SOLID':
        split = box.split(align=True)
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "light", "FLAT", text="", icon='SHADING_SOLID')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "light", "STUDIO", text="", icon='MESH_UVSPHERE')  
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "light", "MATCAP", text="", icon='SHADING_RENDERED')
        if bpy.context.space_data.shading.light == 'STUDIO':
            split = box.split(factor=0.8,align=True)
            col = split.column(align= True)
            col.prop(context.space_data.shading, "studio_light", text="")
            col = split.column(align= True)
            col.prop(context.space_data.shading, "use_world_space_lighting",text="",icon='WORLD')
            col = split.column(align= True)
            col.operator("preferences.studiolight_show",text="",icon='PRESET')
            if bpy.context.space_data.shading.use_world_space_lighting == True:
                row = box.row(align= True)
                row.prop(context.space_data.shading, "studiolight_rotate_z",text="")
        if bpy.context.space_data.shading.light == 'MATCAP':
            split = box.split(factor=0.8,align=True)
            col = split.column(align= True)
            col.prop(context.space_data.shading, "studio_light", text="")
            col = split.column(align= True)
            col.operator("view3d.toggle_matcap_flip",text="",icon='ARROW_LEFTRIGHT')
            col = split.column(align= True)
            col.operator("preferences.studiolight_show",text="",icon='OPTIONS')
        split = box.split(align=True)
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "TEXTURE", text="", icon='TEXTURE')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "OBJECT", text="", icon='OBJECT_DATAMODE')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "MATERIAL", text="", icon='MATERIAL')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "VERTEX", text="", icon='GROUP_VERTEX')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "SINGLE", text="", icon='SHADING_SOLID')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "color_type", "RANDOM", text="", icon='GROUP_VCOL')
        if bpy.context.space_data.shading.color_type == 'SINGLE':
            row = box.row(align= True)
            row.prop(context.space_data.shading, "single_color",text="")
    if bpy.context.space_data.shading.type == 'WIREFRAME':
        split = box.split(align=True)
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "wireframe_color_type", "OBJECT", text="", icon='OBJECT_DATAMODE')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "wireframe_color_type", "THEME", text="", icon='SHADING_SOLID')
        col = split.column(align= True)
        col.prop_enum(context.space_data.shading, "wireframe_color_type", "RANDOM", text="", icon='GROUP_VCOL')
        if bpy.context.space_data.shading.color_type == 'SINGLE':
            row = box.row(align= True)
            row.prop(context.space_data.shading, "single_color",text="")
    if bpy.context.space_data.shading.type == 'SOLID' or bpy.context.space_data.shading.type == 'WIREFRAME':
        row = box.row(align= True)    
        row.prop_enum(context.space_data.shading, "background_type" , "VIEWPORT", icon='RESTRICT_VIEW_ON')
        row.prop_enum(context.space_data.shading, "background_type" , "THEME", icon='IMAGE_BACKGROUND')
        row.prop_enum(context.space_data.shading, "background_type" , "WORLD", icon='WORLD')
        if bpy.context.space_data.shading.background_type == 'VIEWPORT':
           row = box.row(align= True)
           row.prop(context.space_data.shading, "background_color",text="")
        if bpy.context.space_data.shading.background_type == 'THEME':
            row = box.row(align= True)
            row.prop(context.preferences.themes['Default'].view_3d.space.gradients, "high_gradient", text= "")
            if bpy.context.preferences.themes['Default'].view_3d.space.gradients.background_type != "SINGLE_COLOR":
                row.prop(context.preferences.themes['Default'].view_3d.space.gradients, "gradient", text= "")
            row.prop_enum(context.preferences.themes['Default'].view_3d.space.gradients, "background_type", "SINGLE_COLOR",text= "",icon='X')
            row.prop_enum(context.preferences.themes['Default'].view_3d.space.gradients, "background_type", "RADIAL",text= "",icon='RADIOBUT_OFF')
            row.prop_enum(context.preferences.themes['Default'].view_3d.space.gradients, "background_type", "LINEAR",text= "",icon='IPO_LINEAR')                    
        if bpy.context.space_data.shading.background_type == 'WORLD':
            row = box.row(align= True)       
            row.template_ID(context.scene, "world", new="world.new")                         
            row = box.row(align= True)                       
            row.prop(context.scene.world,"color",text="")
            
   #SCENE WORLD           
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        if bpy.context.space_data.shading.type == 'RENDERED' or bpy.context.space_data.shading.type == 'MATERIAL':
            row = box.row(align=True)
            if bpy.context.space_data.shading.type == 'MATERIAL':
                row.prop(context.space_data.shading, "use_scene_lights", icon='LIGHT_DATA')
                row.prop(context.space_data.shading, "use_scene_world", icon='LIGHT_SUN')
                if bpy.context.space_data.shading.use_scene_world == False :
                    split = box.split(factor=0.9,align=True)
                    col = split.column(align= True)
                    col.prop(context.space_data.shading, "studio_light", text="")
                    col = split.column(align= True)
                    col.operator("preferences.studiolight_show",text="",icon='OPTIONS')
                    row = box.row(align=True)
                    row.label(icon='CON_ROTLIMIT')
                    row.prop(context.space_data.shading, "studiolight_rotate_z",text="Rotate")
                    row = box.row(align=True)
                    row.label(icon='LIGHT_HEMI')
                    row.prop(context.space_data.shading, "studiolight_intensity",text="Intensity")
                    row = box.row(align=True)
                    row.label(icon='IMAGE_RGB_ALPHA')
                    row.prop(context.space_data.shading, "studiolight_background_alpha",text="Opacity")
                if bpy.context.space_data.shading.use_scene_world == True:
                    box.template_ID(context.scene, "world", new="world.new")
                    box.prop(context.scene.world,"color",text="")
            if bpy.context.space_data.shading.type == 'RENDERED':
                row.prop(context.space_data.shading, "use_scene_lights_render", icon='LIGHT_DATA')
                row.prop(context.space_data.shading, "use_scene_world_render", icon='LIGHT_SUN')
                if bpy.context.space_data.shading.use_scene_world_render == False:
                    split = box.split(factor=0.9,align=True)
                    col = split.column(align= True)
                    col.prop(context.space_data.shading, "studio_light", text="")
                    col = split.column(align= True)
                    col.operator("preferences.studiolight_show",text="",icon='OPTIONS')
                    row = box.row(align=True)
                    row.label(icon='CON_ROTLIMIT')
                    row.prop(context.space_data.shading, "studiolight_rotate_z",text="Rotate")
                    row = box.row(align=True)
                    row.label(icon='LIGHT_HEMI')
                    row.prop(context.space_data.shading, "studiolight_intensity",text="Intensity")
                    row = box.row(align=True)
                    row.label(icon='IMAGE_RGB_ALPHA')
                    row.prop(context.space_data.shading, "studiolight_background_alpha",text="Opacity")
                if bpy.context.space_data.shading.use_scene_world_render == True:
                    box.template_ID(context.scene, "world", new="world.new")
                    box.prop(context.scene.world,"color",text="")                        
    if bpy.context.scene.render.engine == 'CYCLES':
        if bpy.context.space_data.shading.type == 'MATERIAL':
            row = box.row(align=True)
            row.prop(context.space_data.shading, "use_scene_lights", icon='LIGHT_DATA')
            row.prop(context.space_data.shading, "use_scene_world", icon='LIGHT_SUN')
            if bpy.context.space_data.shading.use_scene_world == False:
                split = box.split(factor=0.9,align=True)
                col = split.column(align= True)
                col.prop(context.space_data.shading, "studio_light", text="")
                col = split.column(align= True)
                col.operator("preferences.studiolight_show",text="",icon='OPTIONS')
                row = box.row(align=True)
                row.label(icon='CON_ROTLIMIT')
                row.prop(context.space_data.shading, "studiolight_rotate_z",text="Rotate")
                row = box.row(align=True)
                row.label(icon='LIGHT_HEMI')
                row.prop(context.space_data.shading, "studiolight_intensity",text="Intensity")
                row = box.row(align=True)
                row.label(icon='IMAGE_RGB_ALPHA')
                row.prop(context.space_data.shading, "studiolight_background_alpha",text="Opacity")
            if bpy.context.space_data.shading.use_scene_world == True:
                box.template_ID(context.scene, "world", new="world.new")
                box.prop(context.scene.world,"color",text="")                    
    if bpy.context.scene.render.engine == 'CYCLES':
        if bpy.context.space_data.shading.type == 'RENDERED':
            row = box.row(align=True)
            row.prop(context.space_data.shading, "use_scene_lights_render", icon='LIGHT_DATA')
            row.prop(context.space_data.shading, "use_scene_world_render", icon='LIGHT_SUN')
            if bpy.context.space_data.shading.use_scene_world_render == False:
                split = box.split(factor=0.9,align=True)
                col = split.column(align= True)
                col.prop(context.space_data.shading, "studio_light", text="")
                col = split.column(align= True)
                col.operator("preferences.studiolight_show",text="",icon='OPTIONS')
                row = box.row(align=True)
                row.label(icon='CON_ROTLIMIT')
                row.prop(context.space_data.shading, "studiolight_rotate_z",text="Rotate")
                row = box.row(align=True)
                row.label(icon='LIGHT_HEMI')
                row.prop(context.space_data.shading, "studiolight_intensity",text="Intensity")
                row = box.row(align=True)
                row.label(icon='IMAGE_RGB_ALPHA')
                row.prop(context.space_data.shading, "studiolight_background_alpha",text="Opacity")
            if bpy.context.space_data.shading.use_scene_world_render == True:
                box.template_ID(context.scene, "world", new="world.new")
                box.prop(context.scene.world,"color",text="")    
   #COMPOSIOR
    if bpy.context.space_data.shading.type == 'RENDERED' or bpy.context.space_data.shading.type == 'MATERIAL':
        row = box.row(align= False)      
        row.label(text="",icon='NODE_COMPOSITING') 
        row.label(text="Compositor")
        if bpy.context.space_data.shading.use_compositor == 'CAMERA':
            compositor_icon='CAMERA_DATA'
        elif bpy.context.space_data.shading.use_compositor == 'ALWAYS':
            compositor_icon='CHECKMARK'
        elif bpy.context.space_data.shading.use_compositor == 'DISABLED':
            compositor_icon='X'
        row.label(text="",icon=compositor_icon)
        row.prop(bpy.context.space_data.shading,"use_compositor",text="")
   #PASSES

    if bpy.context.scene.render.engine == 'CYCLES' or bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        if bpy.context.space_data.shading.type == 'RENDERED' or bpy.context.space_data.shading.type == 'MATERIAL':
            if not tbb.tb_ren_pass:
                row = box.row(align= False)            
                row.prop(tbb, "tb_ren_pass",text="Passes",icon='NODE_COMPOSITING')
            else:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, "tb_ren_pass",text="",icon='NODE_COMPOSITING')
                row.label(text="Passes")    
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        if bpy.context.space_data.shading.type == 'RENDERED' or bpy.context.space_data.shading.type == 'MATERIAL':
            if tbb.tb_ren_pass:    
                row = box.row(align=True)
                row.prop_enum(context.space_data.shading, "render_pass", "COMBINED", icon='CAMERA_DATA')
                row.prop_enum(context.space_data.shading, "render_pass", "EMISSION", icon='LIGHT_HEMI')
 
                if bpy.context.scene.eevee.use_gtao == True:                   
                    row.prop_enum(context.space_data.shading, "render_pass", "AO", icon='CLIPUV_DEHLT')
                row.prop_enum(context.space_data.shading, "render_pass", "ENVIRONMENT", icon='SCENE_DATA')
                row = box.row(align=True)
                row.prop_enum(context.space_data.shading, "render_pass", "SHADOW", icon='MATSHADERBALL')               
                if bpy.context.scene.eevee.use_bloom == True:
                    row.prop_enum(context.space_data.shading, "render_pass", "BLOOM", text= "Bloom",icon='LIGHT_SUN')
                row.prop_enum(context.space_data.shading, "render_pass", "NORMAL", text="Normal", icon='NORMALS_FACE')
                row = box.row(align=True)
                split = box.split(align=True)                        
                col = split.column(align=True)
                col.label(text="Diffuse",icon='MATERIAL_DATA')
                col.prop_enum(context.space_data.shading, "render_pass", "DIFFUSE_LIGHT", icon='LIGHT', text="Light")
                col.prop_enum(context.space_data.shading, "render_pass", "DIFFUSE_COLOR", icon='COLOR',text="Color")                
                col = split.column(align=True)
                col.label(text="Specular",icon='NODE_MATERIAL')     
                col.prop_enum(context.space_data.shading, "render_pass", "SPECULAR_LIGHT", icon='LIGHT', text="Light")
                col.prop_enum(context.space_data.shading, "render_pass", "SPECULAR_COLOR", icon='COLOR',text="Color") 
                col = split.column(align=True)
                col.label(text="Volume",icon='VOLUME_DATA')               
                col.prop_enum(context.space_data.shading, "render_pass", "VOLUME_LIGHT", icon='LIGHT', text="Light")                                                                                                      
    if bpy.context.scene.render.engine == 'CYCLES':
        if bpy.context.space_data.shading.type == 'RENDERED' or bpy.context.space_data.shading.type == 'MATERIAL':
            if tbb.tb_ren_pass:
                row = box.row(align=True)
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "COMBINED", icon='CAMERA_DATA')
            #COMBINED 
                if bpy.context.space_data.shading.type == 'RENDERED' and bpy.context.space_data.shading.cycles.render_pass == 'COMBINED':
                    tworld = context.scene.world
                    if tbb.tb_over_world:
                        row.prop(tbb, "tb_over_world",text="",icon='CON_CAMERASOLVER')
                        box1 = box.box()
                        row = box1.row(align= True)
                        row.prop(tworld.cycles_visibility, "camera" ,icon='CAMERA_DATA')
                        row.separator()
                        row.prop(tworld.cycles_visibility, "scatter" ,icon='FILE_VOLUME')                                                
                        row = box1.row(align= True)            
                        row.prop(tworld.cycles_visibility, "diffuse" ,icon='MATERIAL')
                        row.prop(tworld.cycles_visibility, "glossy" ,icon='NODE_MATERIAL')                                    
                        row.prop(tworld.cycles_visibility, "transmission" ,icon='SHADING_RENDERED')   
                        row = box.row(align= True)            
                    else:
                        row.prop(tbb, "tb_over_world",text="",icon='CON_CAMERASOLVER')
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "EMISSION", icon='LIGHT_HEMI')
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "BACKGROUND", icon='IMAGE_BACKGROUND')
                row = box.row(align=True)    
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "AO", icon='CLIPUV_DEHLT')
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "NORMAL", text="Normal", icon='NORMALS_FACE')
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "UV", text="UV", icon='UV_DATA')
                row.prop_enum(context.space_data.shading.cycles, "render_pass", "MIST", text="Mist", icon='MAT_SPHERE_SKY')
                split = box.split(align=True)
                col = split.column(align=True)
                col.label(text="Diffuse",icon='MATERIAL_DATA')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "DIFFUSE_DIRECT", text= "Direct",icon='INDIRECT_ONLY_OFF')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "DIFFUSE_INDIRECT", text="Indirect", icon='LIBRARY_DATA_OVERRIDE')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "DIFFUSE_COLOR", text="Color",icon='COLOR')
                col = split.column(align=True)
                col.label(text="Glossy",icon='NODE_MATERIAL')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "GLOSSY_DIRECT", text="Direct",icon='INDIRECT_ONLY_OFF')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "GLOSSY_INDIRECT",text="Indirect", icon='LIBRARY_DATA_OVERRIDE')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "GLOSSY_COLOR",text="Color", icon='COLOR')
                col = split.column(align=True)
                col.label(text="Transmission",icon='SHADING_RENDERED')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "TRANSMISSION_DIRECT", text="Direct",icon='INDIRECT_ONLY_OFF')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "TRANSMISSION_INDIRECT",text="Indirect", icon='LIBRARY_DATA_OVERRIDE')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "TRANSMISSION_COLOR",text="Color", icon='COLOR')
                #row = box.row(align=True)
                #split = box.split(align=True)
                col = split.column(align=True)
                col.label(text="Volume",icon='VOLUME_DATA')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "VOLUME_DIRECT", text="Direct",icon='INDIRECT_ONLY_OFF')
                col.prop_enum(context.space_data.shading.cycles, "render_pass", "VOLUME_INDIRECT",text="Indirect", icon='LIBRARY_DATA_OVERRIDE')
    if bpy.context.space_data.shading.type == 'SOLID' or bpy.context.space_data.shading.type == 'WIREFRAME':
        if not tbb.tb_ren_opt:
            row = box.row(align= False)            
            row.prop(tbb, "tb_ren_opt",text="Options",icon='OPTIONS')
        else:
            if bpy.context.scene.render.engine == 'BLENDER_WORKBENCH':
                shade = context.scene.display.shading
            else:
                shade = context.space_data.shading
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, "tb_ren_opt",text="",icon='OPTIONS')
            row.label(text="Options")        
            if shade.show_xray == True:
                split = box.split(factor=0.08, align=True)
                col = split.column(align=True)       
                col.prop(shade, "show_xray",text="",icon='XRAY')
                col = split.column(align=True)
                col.prop(shade, "xray_alpha_wireframe")
            else:
                row = box.row(align= True)
                row.prop(shade, "show_xray", icon='XRAY')
            if shade.show_object_outline == True:
                split = box.split(factor=0.08, align=True)
                col = split.column(align=True)       
                col.prop(shade, "show_object_outline", text="", icon='SEQ_CHROMA_SCOPE')  
                col = split.column(align=True)
                col.prop(shade, "object_outline_color",text="")
            else:
                row = box.row(align= True)
                row.prop(shade, "show_object_outline", icon='SEQ_CHROMA_SCOPE')
            if bpy.context.space_data.shading.type == 'SOLID':
                row = box.row(align= True)
                if shade.show_shadows == False:
                    row.prop(shade, "show_shadows", icon='MATSHADERBALL')
                else:
                    row.prop(shade, "show_shadows",text="", icon='MATSHADERBALL')
                    row.prop(shade, "shadow_intensity", icon='MATSHADERBALL')
                    row.popover(panel="VIEW3D_PT_shading_options_shadow",icon='PREFERENCES',text="")

                #shade.show_cavity = False
                row = box.row(align= True)
                row.prop(shade, "show_backface_culling", icon='MOD_EXPLODE')
                row.prop(shade, "use_dof", icon='CAMERA_DATA')
                if shade.show_cavity == True:
                    split = box.split(factor=0.1, align=True)
                    col = split.column(align=True)       
                    col.prop(shade, "show_cavity", icon='MOD_SOLIDIFY', text="")
                    col = split.column(align=True)
                    col.prop_enum(shade, "cavity_type", "SCREEN",text="Screen",icon='RESTRICT_VIEW_ON')
                    col = split.column(align=True)
                    col.prop_enum(shade, "cavity_type", "WORLD",text="World",icon='WORLD')
                    col = split.column(align=True)
                    col.prop_enum(shade, "cavity_type", "BOTH",text="Both")
                    if shade.cavity_type == 'SCREEN' or shade.cavity_type == 'BOTH':
                        row = box.row(align=True)
                        row.label(text="Screen Space",icon='RESTRICT_VIEW_ON')
                        row = box.row(align=True)
                        row.prop(shade, "curvature_ridge_factor")
                        row.prop(shade, "curvature_valley_factor")
                    if shade.cavity_type == 'WORLD' or shade.cavity_type == 'BOTH':
                        row = box.row(align=True)
                        row.label(text="World Space",icon='WORLD')
                        row = box.row(align=True)
                        row.prop(shade, "cavity_ridge_factor")
                        row.prop(shade, "cavity_valley_factor")
                        row = box.row(align=True)
                if shade.show_cavity == False:
                    row = box.row(align=True)
                    row.prop(shade, "show_cavity", icon='MOD_SOLIDIFY')    
class TB_Shading_UI_3D(bpy.types.Panel):
    bl_label = "Shader Panel (Engine)"
    bl_idname = "TBPNL_PT_shader"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='SCENE')     
    def draw(self, context):    
        tbshadingdraw(self,context)       
class TB_Shading_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tbshadingpopup"
    bl_label = "Shading Popup"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    def draw(self, context):
        tbshadingdraw(self,context)
    def execute(self, context):
        return {'FINISHED'}