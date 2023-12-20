import bpy

def tbbakedraw(self,context):

    context = bpy.context
    scene = context.scene
    rd = scene.render
    teevee = scene.eevee
    layout = self.layout
    box = layout.box()  
    if bpy.context.scene.render.engine == 'CYCLES':
        cbk = scene.render.bake
        cscene = scene.cycles
        row = box.row(align=True)
        if rd.use_bake_multires:
            row.operator("object.bake_image")
            row.prop(rd, "use_bake_multires",text="",icon='MOD_MULTIRES')
            box.prop(rd, "bake_type",text="")
        else:
            row.operator("object.bake")
            row.prop(rd, "use_bake_multires",text="",icon='MOD_MULTIRES')
            row = box.row(align=True)
            row.prop(cscene, "bake_type",text="")
            if cscene.bake_type == 'NORMAL':
                row.prop(cbk, "normal_space", text="")
                row = box.row(align=True)
                row.prop(cbk, "normal_r", text="",icon='EVENT_R')
                row.prop(cbk, "normal_g", text="",icon='EVENT_G')
                row.prop(cbk, "normal_b",text="", icon='EVENT_B')
            elif cscene.bake_type == 'COMBINED':
                row = box.row(align=True)
                row.prop(cbk, "use_pass_direct", toggle=True,icon='EMPTY_SINGLE_ARROW')
                row.prop(cbk, "use_pass_indirect", toggle=True,icon='INDIRECT_ONLY_OFF')
                if cbk.use_pass_direct == True or cbk.use_pass_indirect == True:
                    split = box.split(align=True)
                    col = split.column(align=True)
                    col.prop(cbk, "use_pass_diffuse",icon='MATERIAL_DATA')
                    col.prop(cbk, "use_pass_transmission",icon='SHADING_TEXTURE')
                    col.prop(cbk, "use_pass_ambient_occlusion",icon='MATSHADERBALL')
                    col = split.column(align=True)
                    col.prop(cbk, "use_pass_glossy",icon='NODE_MATERIAL')
                    #col.prop(cbk, "use_pass_subsurface",icon='SHADING_RENDERED')
                    col.prop(cbk, "use_pass_emit",toggle=True,text="Emit",icon='LIGHT_HEMI')
                else:
                    row = box.row(align=True)
                    row.prop(cbk, "use_pass_diffuse",icon='MATERIAL_DATA')
                    row.prop(cbk, "use_pass_glossy",icon='NODE_MATERIAL')
            elif cscene.bake_type in {'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}:
                row = box.row(align=True)
                row.use_property_split = False
                row.prop(cbk, "use_pass_direct", toggle=True,icon='EMPTY_SINGLE_ARROW')
                row.prop(cbk, "use_pass_indirect", toggle=True,icon='INDIRECT_ONLY_OFF')
                row.prop(cbk, "use_pass_color", toggle=True,icon='COLOR')
            if cbk.use_selected_to_active == False:
                box.prop(cbk, "use_selected_to_active",expand=False,text="Selection to Active",icon='PIVOT_BOUNDBOX')
            if rd.use_bake_multires:
                row = box.row(align=True)
            else:
                if cbk.use_selected_to_active:
                    row = box.row(align=True)
                    row.prop(cbk, "use_selected_to_active",expand=False,text="",icon='PIVOT_BOUNDBOX')
                    row.label(text="Use Selected to Active")
                    if cbk.use_cage:
                        row.prop(cbk, "use_cage", text="",icon='SHADING_BBOX')
                        row.prop(cbk, "cage_object", text="")
                        row = box.row(align=True)
                        row.label(icon="BLANK1")
                    else:
                        row.prop(cbk, "use_cage", text="Cage",icon='SHADING_BBOX')
                        row = box.row(align=True)
                        row.label(icon="BLANK1")
                    row.prop(cbk, "cage_extrusion", text="Extrusion")
                    row.prop(cbk, "max_ray_distance", text="Ray Distasnce")  
       #OUTPUT
        box.label(text="Output",icon='OUTPUT')
        scene = context.scene
        cscene = scene.cycles
        cbk = scene.render.bake
        rd = scene.render
        if rd.use_bake_multires:
            row = box.row(align=True)
            row.prop(rd, "bake_margin",text="")
            row.prop(rd, "bake_margin_type", text="")
            row.separator()
            row.prop(rd, "use_bake_clear",text="",icon='IMAGE_PLANE')
            if rd.bake_type == 'DISPLACEMENT':
                row.prop(rd, "use_bake_lores_mesh",text="",icon='MOD_REMESH')
        else:
            row = box.row(align=True)
            if cbk.target == 'IMAGE_TEXTURES':
                row.label(icon='TEXTURE')
                row.prop(cbk, "margin",text="")
                row.prop(cbk, "use_clear",text="",icon='IMAGE_PLANE')
                row.prop_enum(cbk, "target",'VERTEX_COLORS',text="",icon='VERTEXSEL')
            else:
                row.label(icon='VERTEXSEL')
                row.prop_enum(cbk, "target",'IMAGE_TEXTURES',text="Switch to Image",icon='FILE_IMAGE')
                      
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        scene = context.scene
        row = box.row(align=True)
        row.operator("scene.light_cache_bake", text="Bake Indirect Lighting", icon='RENDER_STILL')
        row.operator("scene.light_cache_bake", text="Bake Cubemap Only", icon='LIGHTPROBE_CUBEMAP').subset = 'CUBEMAPS'
        row = box.row(align=True)
        row.operator("scene.light_cache_free", text="Delete Lighting Cache",icon='X')
        row.prop(teevee, "gi_auto_bake",icon='FILE_REFRESH')
        row = box.row(align=True)
        cache_info = scene.eevee.gi_cache_info
        if cache_info:
            row.label(text=cache_info)
        row.label(icon='MATERIAL')
        row.prop(teevee, "gi_diffuse_bounces")
        row.label(icon='NODE_MATERIAL')
        row.prop(teevee, "gi_glossy_clamp")
        row = box.row(align=True)
        row.prop(teevee, "gi_cubemap_resolution",text="",icon='ALIASED')
        row.prop(teevee, "gi_visibility_resolution", text="",icon='FILE_VOLUME')
        row = box.row(align=True)
        row.prop(teevee, "gi_irradiance_smoothing")
        row.prop(teevee, "gi_filter_quality")
        row = box.row(align=True)
        row.prop(teevee, "gi_cubemap_display_size", text="Cubemap Size")
        row.prop(teevee, "gi_show_cubemaps", text="", toggle=True)
        row.prop(teevee, "gi_irradiance_display_size", text="Irradiance Size")
        row.prop(teevee, "gi_show_irradiance", text="", toggle=True)  

class TB_Bake_UI_3D(bpy.types.Panel):
    bl_label = "Bake Panel"
    bl_idname = "TBPNL_PT_Bake_UI_3D"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    bl_options = {'DEFAULT_CLOSED'}
    @classmethod
    def poll(cls, context):
        return bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES'
    def draw_header(self, context):
        layout = self.layout
        layout.label(text='',icon='SCENE')       
    def draw(self, context):
        tbbakedraw(self,context)