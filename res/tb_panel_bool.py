import bpy

class tb_wm_bool_c(bpy.types.PropertyGroup):
    #UI
   #3D
    header_icons: bpy.props.BoolProperty(default=False)
    keymap_bool: bpy.props.BoolProperty(default=False)
   #UV
    tb_uv_seam: bpy.props.BoolProperty(default=False)
    tb_uv_snap: bpy.props.BoolProperty(default=False)     
    tb_uv_snap: bpy.props.BoolProperty(default=False)     
    tb_uv_weld: bpy.props.BoolProperty(default=False)
    tb_uv_island: bpy.props.BoolProperty(default=True)
    tb_uv_proj: bpy.props.BoolProperty(default=False)
    tb_uv_snap_sel: bpy.props.BoolProperty(default=False)
    tb_uv_snap_pix: bpy.props.BoolProperty(default=False)
 
   #Data 
    tb_ob_view: bpy.props.BoolProperty(default=True)
    tb_kmr_guides: bpy.props.BoolProperty(default=False)
    tb_over_mesh_re: bpy.props.BoolProperty(default=False)
    tb_obj_vrtx: bpy.props.BoolProperty(default=False)
    tb_obj_vrtx_col: bpy.props.BoolProperty(default=False)
    tb_obj_attr: bpy.props.BoolProperty(default=False)
    tb_obj_col_attr: bpy.props.BoolProperty(default=False)
    #tb_obj_vrtx_col_sculpt: bpy.props.BoolProperty(default=False)
    tb_obj_facemap: bpy.props.BoolProperty(default=False)
    tb_obj_uvmap: bpy.props.BoolProperty(default=False)
    tb_obj_mat: bpy.props.BoolProperty(default=False)
    tb_obj_mat_set: bpy.props.BoolProperty(default=False)
    tb_obj_shap: bpy.props.BoolProperty(default=False)
    tb_obj_rel: bpy.props.BoolProperty(default=False)
    tb_obj_font_font: bpy.props.BoolProperty(default=False)
    tb_obj_curve_prop: bpy.props.BoolProperty(default=False)
    tb_ob_view: bpy.props.BoolProperty(default=False)
    tb_arm_view: bpy.props.BoolProperty(default=False)
    tb_arm_def: bpy.props.BoolProperty(default=False)
    tb_arm_ik: bpy.props.BoolProperty(default=False)
    tb_arm_lay: bpy.props.BoolProperty(default=False)
    tb_arm_bone_rel: bpy.props.BoolProperty(default=False)
    tb_arm_bone: bpy.props.BoolProperty(default=False)
    tb_arm_lib: bpy.props.BoolProperty(default=False)
   #OVERLAYS
    tb_over: bpy.props.BoolProperty(default=False)
    tb_over_sha: bpy.props.BoolProperty(default=False)
    tb_over_grid: bpy.props.BoolProperty(default=False)
    tb_over_mesh_edit: bpy.props.BoolProperty(default=False)
    tb_over_mesh_edge: bpy.props.BoolProperty(default=False)
    tb_over_mesh_normal: bpy.props.BoolProperty(default=False)
    tb_over_mesh_index: bpy.props.BoolProperty(default=False)
    tb_over_ex_col: bpy.props.BoolProperty(default=False)
    tb_over_sculpt_cursor: bpy.props.BoolProperty(default=False)
    
   #TOOL
    tb_obj_option: bpy.props.BoolProperty(default=False)
    tb_obj_snap: bpy.props.BoolProperty(default=False)
    tb_obj_prop: bpy.props.BoolProperty(default=False)
   #SHADER 
    tb_over_world: bpy.props.BoolProperty(default=False)
    tb_ren_pass: bpy.props.BoolProperty(default=False)
   #REN
    tb_ren_pstyle: bpy.props.BoolProperty(default=False)
    tb_ren_opt: bpy.props.BoolProperty(default=True)
    tb_ren_denoise: bpy.props.BoolProperty(default=False)
    tb_ren_mb: bpy.props.BoolProperty(default=False)
    tb_ren_meta: bpy.props.BoolProperty(default=False)
    tb_ren_post: bpy.props.BoolProperty(default=False)
    tb_ren_free: bpy.props.BoolProperty(default=False)
    tb_ren_col: bpy.props.BoolProperty(default=False)
    tb_ren_vol: bpy.props.BoolProperty(default=False)
    tb_ren_sam: bpy.props.BoolProperty(default=False)
    tb_ren_sha: bpy.props.BoolProperty(default=False)
    tb_ren_sub: bpy.props.BoolProperty(default=False)
    tb_ren_simply: bpy.props.BoolProperty(default=False)
    tb_ren_simplyfy: bpy.props.BoolProperty(default=False)
    tb_ren_lgh: bpy.props.BoolProperty(default=False)
    tb_ren_hair: bpy.props.BoolProperty(default=False)
    tb_ren_res: bpy.props.BoolProperty(default=False)
    tb_ren_bake: bpy.props.BoolProperty(default=False)
    tb_ren_pref: bpy.props.BoolProperty(default=False)
    tb_ren_film: bpy.props.BoolProperty(default=False)
    tb_ren_pass: bpy.props.BoolProperty(default=False)
    tb_ren_grease: bpy.props.BoolProperty(default=False)
    tb_ren_out: bpy.props.BoolProperty(default=False)
    tb_ren_out_enc: bpy.props.BoolProperty(default=False)
    tb_ren_out_aud: bpy.props.BoolProperty(default=False)
    tb_ren_out_meta: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_bloom: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_depth: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_ao: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_ssr: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_sub: bpy.props.BoolProperty(default=False)
    tb_ren_eevee_mb: bpy.props.BoolProperty(default=False)
   #MESH
    tb_mesh_clean: bpy.props.BoolProperty(default=True)
   #SCULPT
    tb_sculpt_brush: bpy.props.BoolProperty(default=False)
    tb_sculpt_txtr: bpy.props.BoolProperty(default=False)
    tb_sculpt_falloff: bpy.props.BoolProperty(default=False)
    tb_sculpt_stroke: bpy.props.BoolProperty(default=False)
   #brush
    tb_brush_advanced: bpy.props.BoolProperty(default=False)
    tb_brush_automask: bpy.props.BoolProperty(default=False)
    tb_brush_mirror: bpy.props.BoolProperty(default=False)
    tb_brush_option: bpy.props.BoolProperty(default=True)
    tb_brush_palette: bpy.props.BoolProperty(default=False)
    tb_paint_txtr: bpy.props.BoolProperty(default=False)
    tb_paint_mask_txtr: bpy.props.BoolProperty(default=False)
   #FILE_EXPLORER 
    tb_fe_recursion: bpy.props.BoolProperty(default=False)      
   #TRANSFORMS
    tb_set_3dc: bpy.props.BoolProperty(default=False)
    tb_set_loc: bpy.props.BoolProperty(default=False)
    tb_set_ori: bpy.props.BoolProperty(default=False)
    tb_set_dim: bpy.props.BoolProperty(default=False)   
    tb_set_dim_proportional: bpy.props.BoolProperty(default=False)
    tb_set_dim_proportional_factor: bpy.props.FloatProperty(default=False)        
    tb_set_dim_proportional_axis : bpy.props.EnumProperty(
        name = "Proportional dimension focused axis",
        description = "Axis to execute Proportional Dimension operation",
        items= [('X','X','X', '', 0),
                ('Y','Y','Y', '', 1),
                ('Z','Z','Z', '', 2)
        ])     
     

bpy.utils.register_class(tb_wm_bool_c)
bpy.types.WindowManager.tb_wm_bool = bpy.props.PointerProperty(type=tb_wm_bool_c)