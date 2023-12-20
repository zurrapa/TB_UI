import bpy
from bpy.types import Panel

tbrenresdef = ["tb_ren_res","Resolution", 'MOD_MULTIRES']
tbrenoutdef = ["tb_ren_out","Output", 'OUTPUT']
tbrensamdef = ["tb_ren_sam","Sampling", 'IMGDISPLAY']
tbrenperfdef = ["tb_ren_pref","Performance", 'PREFERENCES']
tbrenfilmdef = ["tb_ren_film","Film", 'RENDER_STILL']
tbrencoldef = ["tb_ren_col","Color", 'COLOR']
tbrenshadef = ["tb_ren_sha","Shadow", 'MOD_OPACITY']
tbrenvoldef = ["tb_ren_vol","Volumetrics", 'VOLUME_DATA']
tbrenmbdef = ["tb_ren_mb","Motion Blur",'FORCE_CURVE']
tbrengreasedef = ["tb_ren_grease","Grease Pencil", 'GREASEPENCIL']
tbrenfreedef = ["tb_ren_free","Freestyle", 'OUTLINER_OB_GREASEPENCIL']
tbrenlightdef = ["tb_ren_lgh","Light Path",'LIGHT_DATA']
tbrensimplydef = ["tb_ren_simply","Simplify",'MOD_DECIM']
tbrenssdef = ["tb_ren_sub","Subsurface Scatter",'SHADING_RENDERED']
tbrenhairdef = ["tb_ren_hair","Hair",'CURVES_DATA']
tbrenssrdef = ["tb_ren_eevee_ssr","Screen Space Reflection",'LIGHTPROBE_PLANAR']
cntb_ren_bloom = ["tb_ren_eevee_bloom","Bloom",'LIGHT_SUN']

cntb_ren_ao = ["tb_ren_eevee_ao","Ambient Oclussion",'MATSHADERBALL']
cntb_ren_df = ["tb_ren_eevee_depth","Depth of Field",'CON_CAMERASOLVER']

def tbrenderresolution(self,context,layout,mode):
    context = bpy.context   
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    wm = context.window_manager
    tbb = wm.tb_wm_bool

    defcontext = tbrenresdef
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
            row = layout.row(align= True)     
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])   
            strresx = str(bpy.context.scene.render.resolution_x)
            strresy = str(bpy.context.scene.render.resolution_y)
            strres = strresx + "x" + strresy
            #row.popover(panel='RENDER_PT_presets',icon='PRESET',text=strres)
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])   
        strresx = str(bpy.context.scene.render.resolution_x)
        strresy = str(bpy.context.scene.render.resolution_y)
        strres = strresx + "x" + strresy
        row.popover(panel='RENDER_PT_presets',icon='PRESET',text=strres)

    row.popover(panel='RENDER_PT_format_presets',icon='PRESET',text="")
    split = layout.split(factor=0.7, align=True)
    col = split.column(align=True)
    col.label(text="Resolution")
    col.prop(rd, "resolution_x", text="X")
    col.prop(rd, "resolution_y", text="Y")
    col.prop(rd, "resolution_percentage", text="%")
    col = split.column(align=True)
    col.label(text="Aspect Ratio")
    col.prop(rd, "pixel_aspect_x", text="X")
    col.prop(rd, "pixel_aspect_y", text="Y")   
    if rd.use_border:
        col = col.split(factor=0.8,align=True)          
        col.prop(rd,"use_crop_to_border",icon='SELECT_SET')
        col.prop(rd,"use_border",icon='OBJECT_HIDDEN',text="")
    else:
        col.prop(rd,"use_border",icon='OBJECT_HIDDEN')
def tbrenderout(self,context,layout,mode):
    context = bpy.context   
    scene = context.scene
    rd = scene.render
    image_settings = rd.image_settings
    seevee = scene.eevee 
    cscene = scene.cycles
    wm = context.window_manager
    tbb = wm.tb_wm_bool   
    
    defcontext = tbrenoutdef
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1]) 
    row = layout.row(align= True)
    row.prop(rd, "filepath", text="")
    row.prop(rd, "use_overwrite",text="",icon='DECORATE_OVERRIDE')
    if rd.image_settings.file_format == 'JPEG2000':
        split = layout.split(factor=0.5, align=True)
    if rd.image_settings.file_format == 'TIFF':
        split = layout.split(factor=0.2, align=True)
    else:
        split = layout.split(factor=0.7, align=True)
    col = split.column(align=True)
    col.prop(rd.image_settings, "file_format",text="")
    if rd.image_settings.file_format == 'JPEG2000':
        col = split.column(align=True)
        col.prop(rd.image_settings,"jpeg2k_codec",text="")
    if rd.image_settings.file_format == 'TIFF':
        col = split.column(align=True)
        col.prop(rd.image_settings,"tiff_codec",text="")
    col = split.column(align=True)
    col.prop(rd, "use_file_extension",text="",icon='FILE')
    if rd.image_settings.file_format == 'BMP' or rd.image_settings.file_format == 'IRIS' or rd.image_settings.file_format == 'PNG' or rd.image_settings.file_format == 'JPEG' or rd.image_settings.file_format == 'JPEG2000' or rd.image_settings.file_format == 'TARGA_RAW' or rd.image_settings.file_format == 'CINEON' or rd.image_settings.file_format == 'DPX' or rd.image_settings.file_format == 'OPEN_EXR_MULTILAYER' or rd.image_settings.file_format == 'OPEN_EXR' or rd.image_settings.file_format == 'HDR' or rd.image_settings.file_format == 'TIFF':
        col = split.column(align=True)
        col.prop(rd, "use_placeholder",icon='SORTBYEXT',text="")
    col = split.column(align=True)
    col.prop(rd, "use_render_cache",icon='FILE_CACHE',text="")
    if rd.image_settings.file_format == 'BMP' or rd.image_settings.file_format == 'IRIS' or rd.image_settings.file_format == 'PNG' or rd.image_settings.file_format == 'JPEG' or rd.image_settings.file_format == 'TARGA' or rd.image_settings.file_format == 'TARGA_RAW' or rd.image_settings.file_format == 'CINEON' or rd.image_settings.file_format == 'DPX' or rd.image_settings.file_format == 'OPEN_EXR_MULTILAYER' or rd.image_settings.file_format == 'OPEN_EXR' or rd.image_settings.file_format == 'HDR' or rd.image_settings.file_format == 'TIFF' or rd.image_settings.file_format == 'AVI_JPEG' or rd.image_settings.file_format == 'AVI_RAW' or rd.image_settings.file_format == 'FFMPEG':
        split = layout.split( align=True)
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_mode","BW",icon='IMAGE_ALPHA',text="BW")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings, "color_mode","RGB",icon='IMAGE_RGB',text="RGB")
    if rd.image_settings.file_format == 'IRIS' or rd.image_settings.file_format == 'PNG' or rd.image_settings.file_format == 'TARGA' or rd.image_settings.file_format == 'TARGA_RAW' or rd.image_settings.file_format == 'DPX' or rd.image_settings.file_format == 'OPEN_EXR_MULTILAYER' or rd.image_settings.file_format == 'OPEN_EXR' or rd.image_settings.file_format == 'TIFF':   
        col = split.column(align=True)
        col.prop_enum(rd.image_settings, "color_mode","RGBA",icon='IMAGE_RGB_ALPHA',text="RGBA")
    if rd.image_settings.file_format == 'PNG' or rd.image_settings.file_format == 'TIFF':
        split = layout.split(factor=0.69,align=True)
        col = split.column(align=True)
        col.prop(rd.image_settings,"compression",text="Compresion")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_depth","8",text="8")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_depth","16",text="16")
    if rd.image_settings.file_format == 'JPEG' or rd.image_settings.file_format == 'AVI_JPEG':
        split = layout.split(align=True)
        col = split.column(align=True)
        col.prop(rd.image_settings,"quality",text="Quality")
    if rd.image_settings.file_format == 'JPEG2000':
        split = layout.split(factor=0.7,align=True)
        col = split.column(align=True)
        col.prop(rd.image_settings,"quality",text="Quality")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_depth","8",text="8")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_depth","12",text="12")
        col = split.column(align=True)
        col.prop_enum(rd.image_settings,"color_depth","16",text="16")
        split = layout.split(factor=0.3,align=True)
        col = split.column(align=True)
        col.prop(rd.image_settings,"use_jpeg2k_ycc",text="YCC")
        col = split.column(align=True)
        col.prop(rd.image_settings,"use_jpeg2k_cinema_preset",text="Cinema")
        col = split.column(align=True)
        col.prop(rd.image_settings,"use_jpeg2k_cinema_48",text="Cinema(48)")
       #VIDEO
        if rd.image_settings.file_format == 'FFMPEG':
            cw = tbb.tb_ren_out_enc
            cwt = "tb_ren_out_enc"
            cwtt = "Encoder"
            cwi = 'RENDER_ANIMATION'
            if cw == False:
                row = layout.row(align=False)                    
                row.prop(tbb, cwt,text=cwtt,icon=cwi)
            if cw:
                ffmpeg = rd.ffmpeg
                row = layout.row(align= True)
                row.prop(tbb, cwt,text="",icon=cwi)
                row.label(text=cwtt)
                row .prop(rd.ffmpeg, "format",text="")
                row.prop(ffmpeg, "use_autosplit",text="Autosplit",toggle=True)
                ffmpeg = context.scene.render.ffmpeg
                needs_codec = ffmpeg.format in {'AVI', 'QUICKTIME', 'MKV', 'OGG', 'MPEG4', 'WEBM'}
                if needs_codec:
                    split = layout.split(align=True)
                    col = split.column(align=True)
                    col.prop(ffmpeg, "codec",text="")
                if needs_codec and ffmpeg.codec == 'NONE':
                    return
                if ffmpeg.codec == 'DNXHD':
                    col = layout.column(align=True)
                    col.prop(ffmpeg, "use_lossless_output",text="Losseless",toggle=True)
                use_crf = needs_codec and ffmpeg.codec in {'H264', 'MPEG4', 'WEBM'}
                if use_crf:
                    col = split.column(align=True)
                    col.prop(ffmpeg, "constant_rate_factor",text="")
                col = split.column(align=True)
                col.prop(ffmpeg, "ffmpeg_preset",text="")
                row = layout.row(align= True)
                row.prop(ffmpeg, "gopsize",text="Keyframe Interval")
                if ffmpeg.use_max_b_frames:
                    row.prop(ffmpeg, "max_b_frames", text="")
                row.prop(ffmpeg, "use_max_b_frames", text="",icon='EVENT_B')
                if not use_crf or ffmpeg.constant_rate_factor == 'NONE':
                    col = layout.column()
                    sub = col.column(align=True)
                    sub.prop(ffmpeg, "video_bitrate")
                    sub.prop(ffmpeg, "minrate", text="Minimum")
                    sub.prop(ffmpeg, "maxrate", text="Maximum")
                    col.prop(ffmpeg, "buffersize", text="Buffer")
                    col.separator()
                    col.prop(ffmpeg, "muxrate", text="Mux Rate")
                    col.prop(ffmpeg, "packetsize", text="Mux Packet Size")
           #AUDIO
            if tbb.tb_ren_out_enc and tbb.tb_ren_out_aud == False:
                row = layout.row(align=True)
            cw = tbb.tb_ren_out_aud
            cwt = "tb_ren_out_aud"
            cwtt = "Audio"
            cwi = 'PLAY_SOUND'
            if tbb.tb_ren_out_aud == False:
                row.prop(tbb, cwt,text=cwtt,icon=cwi)
            if cw:
                row = layout.row(align= True)            
                row.prop(tbb, cwt,text="",icon=cwi)
                row.label(text=cwtt)            
                ffmpeg = rd.ffmpeg
                if ffmpeg.format != 'MP3':
                    layout.prop(ffmpeg, "audio_codec", text="")
                if ffmpeg.audio_codec != 'NONE':
                    layout.prop(ffmpeg, "audio_bitrate")
                    layout.prop(ffmpeg, "audio_volume", slider=True)
    row = layout.row(align=True)
    if tbb.tb_ren_post or tbb.tb_ren_meta  or bpy.context.scene.render.use_multiview:
        bor = layout.box()
   #POST 
    if tbb.tb_ren_post:
        box = bor.box()
        row = box.row(align= True)            
        row.prop(tbb, "tb_ren_post",text="",icon='SEQ_SPLITVIEW')
        row.label(text="Post-procesing")        
        row = box.row(align= True)
        rd = context.scene.render
        row.prop(rd, "use_compositing",icon='NODE_COMPOSITING')
        row.prop(rd, "use_sequencer",icon='SEQUENCE')
        row.prop(rd, "dither_intensity", text="Dither", slider=True)
   #META
    if tbb.tb_ren_meta :
        box = bor.box()
        row = box.row(align= True)     
        row.prop(tbb, "tb_ren_meta",text="",icon='ALIGN_TOP')
        row.label(text="Metadata")        
        row.prop(context.scene.render,"use_stamp",icon='OUTPUT') 
        row.separator()
        if rd.use_sequencer:
            row.prop_enum(rd,"metadata_input","SCENE",text="",icon='SCENE_DATA')
            row.prop_enum(rd,"metadata_input","STRIPS",text="",icon='SEQ_STRIP_META')            
        split = box.split( align=True)
        col = split.column(align=True)
        col.prop(rd, "use_stamp_time", text="Time",icon="SORTTIME")
        col.prop(rd, "use_stamp_frame", text="Frame",icon='TEMP')
        col.prop(rd, "use_stamp_camera", text="Camera",icon='CAMERA_DATA')
        col.prop(rd, "use_stamp_scene", text="Scene",icon='SCENE_DATA')
        col.prop(rd, "use_stamp_sequencer_strip", text="Strip Name",icon='SEQ_STRIP_DUPLICATE')
        col.prop(rd, "use_stamp_hostname", text="Hostname",icon='RENDER_ANIMATION')
        if rd.use_stamp_note == False:
            col.prop(rd, "use_stamp_note", text="Note",icon='GREASEPENCIL')
        col = split.column(align=True)
        col.prop(rd, "use_stamp_render_time", text="Render Time",icon='TIME')
        col.prop(rd, "use_stamp_frame_range", text="Frame_Range",icon='MOD_TIME')            
        col.prop(rd, "use_stamp_lens", text="Lens",icon='CON_CAMERASOLVER')
        col.prop(rd, "use_stamp_filename", text="Filename",icon='FILE_TEXT')
        col.prop(rd, "use_stamp_memory", text="Memory",icon='MEMORY')
        col.prop(rd, "use_stamp_date", text="Date",icon='SORTTIME')
        col.prop(rd, "use_stamp_marker", text="Marker",icon='MARKER')
        if rd.use_stamp_note:
            row = box.row(align= True)
            row.prop(rd, "use_stamp_note", text="",icon='GREASEPENCIL')
            row.prop(rd, "stamp_note_text", text="")
        if scene.render.use_stamp:
            row = box.row(align= True)   
            row.label(icon='FILE_FONT')
            row.prop(rd, "stamp_font_size", text="Font Size")
            row.prop(rd, "stamp_foreground", text="",slider=True)
            row = box.row(align= True)   
            row.label(icon='IMAGE_BACKGROUND')
            row.prop(rd, "stamp_background", slider=True,text="")
            row.prop(rd, "use_stamp_labels", text="Include Labels",icon='FONTPREVIEW')
   #Stereoscopy
    if bpy.context.scene.render.use_multiview:
        row = layout.row(align= True)
        box = bor.box()
        row = box.row(align=True)
        row.prop(context.scene.render,"use_multiview",text="",icon='CAMERA_STEREO')
        row.label(text="Stereoscopy")
        scene = context.scene
        rd = scene.render
        rv = rd.views.active
        layout.active = rd.use_multiview
        basic_stereo = rd.views_format == 'STEREO_3D'
        row = box.row(align= True)
        row.label(icon='BLANK1')
        row.prop(rd, "views_format",expand=True)
        if basic_stereo:
            row = box.row()
            row.template_list("RENDER_UL_renderviews", "name", rd, "stereo_views", rd.views, "active_index", rows=2)
            row = box.row()
            row.use_property_split = True
            row.use_property_decorate = False
            row.prop(rv, "file_suffix",text="",icon='FILE')
        else:
            row = layout.row()
            row.template_list("RENDER_UL_renderviews", "name", rd, "views", rd.views, "active_index", rows=2)
            col = row.column(align=True)
            col.operator("scene.render_view_add", icon='ADD', text="")
            col.operator("scene.render_view_remove", icon='REMOVE', text="")
            row = layout.row()
            row.use_property_split = True
            row.use_property_decorate = False
            row.prop(rv, "camera_suffix",text="",icon='FILE')      
   #REN
    bor = layout.box()
    if tbb.tb_ren_post == False:
        row = bor.row(align= False)                        
        row.prop(tbb, "tb_ren_post",text="Post Processing",icon='SEQ_SPLITVIEW')
    if tbb.tb_ren_meta == False:
        if tbb.tb_ren_post:
            row = bor.row(align= True)                        
        row.prop(tbb, "tb_ren_meta",text="Metadata",icon='ALIGN_TOP')
    if bpy.context.scene.render.use_multiview == False:
        row = bor.row(align= False) 
        row.prop(context.scene.render,"use_multiview",text="Stereoscopy",icon='CAMERA_STEREO') 
def tbrendersamples(self,context,layout,mode):
   #DEF    
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    defcontext = tbrensamdef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])              
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])   
   #START    
    row.prop(rd, "use_high_quality_normals",icon='NORMALS_FACE',text="")            
    row.popover(panel='CYCLES_PT_sampling_presets',icon='PRESET',text="Preset")  
    row = layout.row(align= True)                        
    if bpy.context.scene.render.engine == 'BLENDER_WORKBENCH':
        props = scene.display
        row = layout.row()
        row.prop(props, "render_aa", text="",icon='SCENE')
        row.prop(props, "viewport_aa", text="",icon='SCENE_DATA')
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        row = layout.row(align=True)
        row.label(icon='SCENE')
        row.prop(seevee, "taa_render_samples", text="Render")
        row.label(icon='SCENE_DATA')
        row.prop(seevee, "taa_samples", text="Viewport")
        row.prop(seevee, "use_taa_reprojection",text="",icon='SEQ_HISTOGRAM')
    if bpy.context.scene.render.engine == 'CYCLES':
        cw = tbb.tb_ren_sam_viewport
        cwt = "tb_ren_sam_viewport"
        cwtt = "Viewport Sampling"
        cwi = 'SCENE_DATA'
        if cw == False:
            layout.prop(tbb, cwt,text=cwtt,icon=cwi)
        if cw:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, cwt,text="",icon=cwi)                  
            row.label(text="Viewport")
            strres = str(bpy.context.scene.cycles.preview_samples)
            row.popover(panel='CYCLES_PT_viewport_sampling_presets',icon='PRESET',text=strres)        
            row = box.row(align= True)   
            row.prop(cscene,"preview_adaptive_min_samples")
            row.prop(cscene,"preview_samples")  
            row = box.row(align= True)   
            if cscene.use_preview_adaptive_sampling:
                row.prop(cscene,"use_preview_adaptive_sampling",text="",icon='MOD_NOISE')
                row.prop(cscene,"preview_adaptive_threshold")
            else:
                row.prop(cscene,"use_preview_adaptive_sampling",icon='MOD_NOISE')
            row = box.row(align= True)   
            if cscene.use_preview_denoising:
                row.prop(cscene,"preview_denoiser")
                row.prop(cscene,"preview_denoising_input_passes")
                row = box.row(align= True)
                row.prop(cscene,"preview_denoising_start_sample")
                if cscene.preview_denoiser == 'OPENIMAGEDENOISE':
                    row.prop(cscene,"preview_denoising_prefilter")
                    
        #Advanced    
        cw = tbb.tb_ren_sam_adv
        cwt = "tb_ren_sam_adv"
        cwtt = "Advance Settings"
        cwi = 'PREFERENCES'
        if cw == False:
            layout.prop(tbb, cwt,text=cwtt,icon=cwi)
        if cw:
            box = layout.box()
            row = box.row(align= True)            
            row.prop(tbb, cwt,text="",icon=cwi)
            row.label(text=cwtt)
            row = box.row(align=True)
            row.prop(cscene, "seed")
            row.prop(cscene, "use_animated_seed", text="", icon='TIME')
            if cscene.use_adaptive_sampling:
                row.prop(cscene,"use_adaptive_sampling",icon='STICKY_UVS_DISABLE')                    
            if cscene.use_adaptive_sampling == False:
                row.prop(cscene,"use_adaptive_sampling",text="",icon='STICKY_UVS_DISABLE')
                row.prop(cscene, "sampling_pattern", text="")
            row.prop(cscene, "use_square_samples",icon='MESH_PLANE',text="")
            if cscene.use_adaptive_sampling:
                row = box.row(align=True)
                row.prop(cscene, "adaptive_threshold", text="Noise Threshold")
                row.prop(cscene, "adaptive_min_samples", text="Min Samples")                                                      
            split = box.split(factor=0.9,align=True)
            col = split.column(align=True)
            col.prop(cscene, "min_light_bounces")
            col.prop(cscene, "min_transparent_bounces")
            col.prop(cscene, "light_sampling_threshold", text="Light Threshold")
            col = split.column(align=True)
            col.prop(cscene, "sample_all_lights_direct", text="",icon='SORT_DESC')
            col.prop(cscene, "sample_all_lights_indirect",text="",icon='INDIRECT_ONLY_OFF')
            for view_layer in scene.view_layers:
                if view_layer.samples > 0:
                    layout.separator()
                    layout.row().prop(cscene, "use_layer_samples")
                    break
            row = box.row(align= True)                                
            row.label(icon='OUTLINER_OB_GREASEPENCIL')      
            row.prop(context.scene.grease_pencil_settings,"antialias_threshold",slider=True)                             
def tbrenderpref(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenperfdef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
   #START    
    row = layout.row(align=True)    
    if bpy.context.scene.render.engine == 'CYCLES':  
        row = layout.row(align=True)       
        row.label(icon='VIEW_ORTHO')                                                   
        row.separator()          
        row.prop(rd, "tile_x", text="X")
        row.separator()                                                                                                   
        row.prop(rd, "tile_y", text="Y")
        row = layout.row(align=True)                               
        row.separator()                    
        row.label(icon='BLANK1')
        row.prop(cscene, "tile_order", text="")
        row.prop(cscene, "use_progressive_refine",icon='PROPERTIES')
        row = layout.row(align=True)       
        row.label(icon='PROP_PROJECTED')                                                   
        row.separator()          
        row.prop(context.scene.cycles,"debug_use_hair_bvh",icon='CURVES_DATA')        
        row.separator()                                        
        if bpy.context.scene.cycles.debug_use_spatial_splits:                                
            row.prop(context.scene.cycles,"debug_use_spatial_splits",text="",icon='TIME')                                                                        
            row.prop(context.scene.cycles,"debug_bvh_time_steps")             
        else:
            row.prop(context.scene.cycles,"debug_use_spatial_splits",icon='TIME')                                                                                                    
        row = layout.row(align=False)       
        row.label(icon='SCENE_DATA')                                                   
        row.prop(context.scene.render,"use_save_buffers",icon='FILE_TICK')                        
        row.prop(context.scene.render,"use_persistent_data",icon='FILE_IMAGE')                                                
        row = layout.row(align=True)       
        row.label(icon='SCENE')                                                   
        row.separator()      
        row.prop(context.scene.render,"preview_pixel_size",text="")  
        row.separator()                    
        row.prop(context.scene.render,"preview_start_resolution")             
        row = layout.row(align=True)
        row.label(icon='OUTLINER_DATA_CURVES')
        row.prop(context.scene.render,"threads_mode",text="")
        if rd.threads_mode == 'FIXED':
            row.separator()
            row.prop(context.scene.render,"threads")
    else:
        row.prop(rd, "use_high_quality_normals",icon='NORMALS_FACE')   
def tbrenderfilm(self,context,layout,mode):
   #DEF 
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    defcontext = tbrenfilmdef
    context = bpy.context   
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])  
   #START    
    row = layout.row(align=True)           
    if bpy.context.scene.render.engine == 'BLENDER_WORKBENCH':
        row.prop(rd, "film_transparent", text="Transparent",icon='IMAGE_RGB_ALPHA')
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        row.prop(rd, "filter_size")
        row = layout.row(align=True)
        row.prop(rd, "film_transparent", text="Transparent",icon='IMAGE_RGB_ALPHA')
        if seevee.use_overscan:
            row = layout.row(align=True)     
            row.prop(seevee, "use_overscan", text="",icon='ZOOM_ALL')
            row.prop(seevee, "overscan_size", text="Size",icon='ZOOM_ALL')
        else:
            row.prop(seevee, "use_overscan", text="Overscan",icon='ZOOM_ALL')
    if bpy.context.scene.render.engine == 'CYCLES':
        row.prop(cscene, "film_exposure")
        row = layout.row(align=True)
        row.prop(cscene, "pixel_filter_type", text="")
        if cscene.pixel_filter_type != 'BOX':
            row.prop(cscene, "filter_width", text="Width")
        if bpy.context.scene.render.film_transparent == False:
            row = layout.row(align=True)
            row.prop(rd, "film_transparent", text="Transparent",icon='IMAGE_RGB_ALPHA')
        if bpy.context.scene.render.film_transparent:
            if bpy.context.scene.cycles.film_transparent_glass:
                row = layout.row(align=True)
                row.prop(rd, "film_transparent", text="",icon='IMAGE_RGB_ALPHA')
                row.prop(cscene, "film_transparent_glass", text="Glass",icon='IMAGE_RGB')
            if bpy.context.scene.cycles.film_transparent_glass == False:
                row = layout.row(align=True)
                row.prop(rd, "film_transparent", text="Transparent",icon='IMAGE_RGB_ALPHA')
                row.prop(cscene, "film_transparent_glass", text="Glass",icon='IMAGE_RGB')
        if bpy.context.scene.cycles.film_transparent_glass  and  bpy.context.scene.render.film_transparent:
            row.prop(cscene, "film_transparent_roughness", text="Roughness Threshold")
    cw = tbb.tb_ren_vol
    cwt = "tb_ren_vol"
    cwtt = "Volume"
    cwi = 'VOLUME_DATA'
    if cw:
        box = layout.box()                
        row = box.row(align= True)            
        row.prop(tbb, cwt,text="",icon=cwi)
        row.label(text=cwtt)
        row.prop(seevee, "volumetric_tile_size",text="")
        row = box.row(align=True)
        row.label(icon='BLANK1') 
        row.prop(seevee, "volumetric_samples")
        row.prop(seevee, "volumetric_sample_distribution", text="Distribution")
        row = box.row(align=True)
        row.label(icon='BLANK1')                
        row.prop(seevee, "volumetric_start")
        row.prop(seevee, "volumetric_end")
        row = box.row(align=True)
        row.label(icon='BLANK1')
        row.prop(seevee, "use_volumetric_lights",text="Lights",icon='LIGHT_SPOT')
        if bpy.context.scene.eevee.use_volumetric_lights:
            row.prop(seevee,"volumetric_light_clamp",text="Clamping")
        if bpy.context.scene.eevee.use_volumetric_lights == False and bpy.context.scene.eevee.use_volumetric_shadows == False:
            row.separator()
        if bpy.context.scene.eevee.use_volumetric_lights or bpy.context.scene.eevee.use_volumetric_shadows:
            row = box.row(align=True)
            row.label(icon='BLANK1')
        row.prop(seevee, "use_volumetric_shadows",text="Shadows",icon='OVERLAY')
        if bpy.context.scene.eevee.use_volumetric_shadows:
            row.prop(seevee,"volumetric_shadow_samples",text="Samples")

def tbrendercolor(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    defcontext = tbrencoldef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    view = scene.view_settings
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
    row = layout.row(align=True)
    row.prop(scene.display_settings, "display_device",text="")
    row.prop(scene.sequencer_colorspace_settings, "name", text="",icon='SEQUENCE')
    row = layout.row(align=True)
    row.prop(view, "view_transform",icon='RESTRICT_VIEW_ON')
    row.prop(view, "look",icon='HIDE_OFF')
    row = layout.row(align=True)
    row.prop(view, "exposure")
    row.prop(view, "gamma")
    layout.prop(view, "use_curve_mapping", text=" Curves",icon='NORMALIZE_FCURVES')
    if view.use_curve_mapping:
        layout.template_curve_mapping(view, "curve_mapping", type='COLOR', levels=True)

def tbrendersimplify(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrensimplydef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    layout = self.layout
    if tbb.tb_ren_pstyle == False:
        layc = layout.box()
        row = layc.row(align= True)   
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])             
        row.prop(rd, "use_simplify",text="Enable Simplify",icon='PROP_OFF')
    else: 
        layc = layout  
    if bpy.context.scene.render.use_simplify:
        row = layc.row(align=True)
        row.prop(rd, "use_simplify_smoke_highres", text="High-resolution Smoke",icon='MOD_FLUID')
        split = layc.split( align=True)
        col = split.column(align=True)
        col.label(text="Render",icon='SCENE')
        if bpy.context.scene.render.engine == 'CYCLES':
            col.prop(rd, "simplify_subdivision_render", text="Max Subdivision")
            col.prop(rd, "simplify_child_particles_render", text="Child Particles")
            col.prop(cscene, "texture_limit_render", icon='TEXTURE',text="")
            col.prop(cscene, "ao_bounces_render", text="AO Bounces")
            col.prop(cscene,"use_camera_cull",text="Use Camera Cull",icon='CAMERA_DATA')
            if bpy.context.scene.cycles.use_camera_cull:
                col.prop(cscene, "camera_cull_margin")
            col = split.column(align=True)
            col.label(text="Viewport",icon='SCENE_DATA')
            col.prop(rd, "simplify_subdivision", text="Max Subdivision")
            col.prop(rd, "simplify_child_particles", text="Child Particles")
            col.prop(cscene, "texture_limit", icon='TEXTURE',text="")
            col.prop(cscene, "ao_bounces", text="AO Bounces")
            col.prop(cscene, "use_distance_cull",text="Use Distance Cull",icon='DRIVER_DISTANCE')
            if bpy.context.scene.cycles.use_distance_cull:
                col.prop(cscene, "distance_cull_margin", text="Distance")
            col.prop(rd, "simplify_volumes")
        if bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'BLENDER_WORKBENCH':
            col.prop(rd, "simplify_subdivision_render", text="Max Subdivision")
            col.prop(rd, "simplify_child_particles_render", text="Max Child Particles")
            col = split.column(align=True)
            col.label(text="Viewport",icon='SCENE_DATA')
            col.prop(rd, "simplify_subdivision", text="Max Subdivision")
            col.prop(rd, "simplify_child_particles", text="Max Child Particles")
            col.prop(rd, "simplify_volumes")
        if bpy.context.scene.render.simplify_gpencil == False:
            layc.prop(rd, "simplify_gpencil",text="Grease Pencil",icon='OUTLINER_OB_GREASEPENCIL')
        if bpy.context.scene.render.simplify_gpencil:
            row = layc.row(align=True)
            row.prop(rd, "simplify_gpencil",text="",icon='OUTLINER_OB_GREASEPENCIL')
            row.label(text="Gpencil")
            split = layc.split( align=True)
            col = split.column(align=True)
            col.prop(rd, "simplify_gpencil_onplay", text="Playback Only",icon='PLAY')
            col.prop(rd, "simplify_gpencil_modifier", text="Modifiers",icon='MODIFIER')
            col.prop(rd, "simplify_gpencil_antialiasing", text="Layers Blending",icon='ANTIALIASED')
            col = split.column(align=True)
            col.prop(rd, "simplify_gpencil_shader_fx", text="ShaderFX",icon='SHADERFX')
            col.prop(rd, "simplify_gpencil_tint", text="Layers Tinting",icon='NODE_COMPOSITING')
            col.prop(rd, "simplify_gpencil_view_fill",icon='CURVE_NCIRCLE')
def tbrendergrease(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrengreasedef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
    row = layout.row(align=True)
    row.prop(context.scene.grease_pencil_settings,"antialias_threshold")

def tbrenderfreestyle(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenfreedef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    view = scene.view_settings
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
        row.prop(context.scene.render,"use_freestyle",text="",icon='PROP_ON')


    if bpy.context.scene.render.use_freestyle:
        row = layout.row(align=True)
        row.prop_enum(rd, "line_thickness_mode","ABSOLUTE")
        row.prop_enum(rd, "line_thickness_mode","RELATIVE")
        if rd.line_thickness_mode == 'ABSOLUTE':
            row = layout.row(align=True)
            row.prop(rd, "line_thickness")
        if bpy.context.scene.render.use_freestyle == False:
            row.prop(context.scene.render,"use_freestyle",text="Enable Freestyle",icon='OUTLINER_OB_GREASEPENCIL')                
        if bpy.context.scene.render.use_freestyle:
            cw = tbb.tb_lay_free
            cwt = "tb_lay_free"
            cwtt = "Advance Settings"
            cwi = 'OUTLINER_OB_GREASEPENCIL'
            if cw == False:
                if tbb.tb_lay_fil or bpy.context.scene.render.engine == 'BLENDER_EEVEE':
                    box = layout.box()
                    row = box.row(align= False)            
                row.prop(tbb, cwt,text=cwtt,icon=cwi)
            if cw:
                box = layout.box()
                row = box.row(align= True)            
                row.prop(tbb, cwt,text="",icon=cwi)
                row.label(text=cwtt)                            
                if bpy.context.scene.render.use_freestyle or bpy.context.scene.view_layers["Z_WORKFLOW"].use_freestyle:
                    view_layer = context.view_layer
                    freestyle = view_layer.freestyle_settings
                    row.prop(freestyle, "mode", text="")
                    row.prop(freestyle, "use_view_map_cache", text="",icon='FILE_CACHE')
                    row.prop(context.scene.render,"use_freestyle",text="",icon='X')                
                    row = box.row(align=True)
                    row.label(text="",icon='DRIVER_ROTATIONAL_DIFFERENCE')
                    split = box.split()
                    col = split.column()
                    row.prop(freestyle, "crease_angle")
                    col.prop(freestyle, "use_culling",icon='XRAY')                    
                    col = split.column()
                    col.prop(freestyle, "use_smoothness",icon='FACESEL')
                    # Advanced options are hidden by default to warn new users
                    row = box.row(align=True)
                    row.prop(freestyle, "sphere_radius")
                    row.prop(freestyle, "kr_derivative_epsilon")
                    if freestyle.mode == 'SCRIPT':
                        row = box.row(align=True)
                        row.label(icon='BLANK1')
                        row.prop(freestyle, "use_ridges_and_valleys",icon='ROOTCURVE')
                        row.prop(freestyle, "use_suggestive_contours",icon='MOD_EDGESPLIT')
                    if freestyle.mode == 'SCRIPT':
                        row = box.row()
                        row.operator("scene.freestyle_module_add", text="",icon='ADD')
                        row.label(text="Style modules:")
                        for module in freestyle.modules:
                            box.context_pointer_set("freestyle_module", module)
                            row = box.row(align=True)
                            row.prop(module, "use", text="")
                            row.prop(module, "script", text="")
                            row.operator("scene.freestyle_module_open", icon='FILEBROWSER', text="")
                            row.operator("scene.freestyle_module_remove", icon='X', text="")
                            row.operator("scene.freestyle_module_move", icon='TRIA_UP', text="").direction = 'UP'
                            row.operator("scene.freestyle_module_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                    if freestyle.mode == 'EDITOR':
                        #row.prop(freestyle, "",icon='PREFERENCES')
                        col.prop(freestyle, "use_material_boundaries",icon='MATERIAL')
                        view_layer = context.view_layer
                        freestyle = view_layer.freestyle_settings
                        lineset = freestyle.linesets.active
                        layout.active = view_layer.use_freestyle
                        row = box.row()
                        rows = 4 if lineset else 2
                        row.template_list("VIEWLAYER_UL_linesets","",freestyle,"linesets",freestyle.linesets,"active_index",rows=rows)
                        sub = row.column(align=True)
                        sub.operator("scene.freestyle_lineset_add", icon='ADD', text="")
                        sub.operator("scene.freestyle_lineset_remove", icon='REMOVE', text="")
                        sub.menu("RENDER_MT_lineset_context_menu", icon='DOWNARROW_HLT', text="")
                        if lineset:
                            sub.separator()
                            sub.separator()
                            sub.operator("scene.freestyle_lineset_move", icon='TRIA_UP', text="").direction = 'UP'
                            sub.operator("scene.freestyle_lineset_move", icon='TRIA_DOWN', text="").direction = 'DOWN'
                            row = box.row(align=True)
                            row.label(text="Selection By:",icon='RESTRICT_SELECT_OFF')
                            split = box.split(align=True)
                            col = split.column(align=True)
                            col.prop(lineset, "select_by_visibility", text="",icon='VIS_SEL_10')
                            col = split.column(align=True)
                            col.prop(lineset, "select_by_edge_types", text="",icon='EDGESEL')
                            col = split.column(align=True)
                            col.prop(lineset, "select_by_face_marks", text="", icon='FACESEL')
                            col = split.column(align=True)
                            col.prop(lineset, "select_by_collection", text="", icon='GROUP')
                            col = split.column(align=True)
                            col.prop(lineset, "select_by_image_border", text="", icon='SELECT_SET')
                            if lineset.select_by_visibility:
                                row = box.row(align=True)
                                row.label(text="Visibility:",icon='VIS_SEL_10')
                                row = box.row(align=True)
                                row.prop(lineset, "visibility", expand=True)
                                if lineset.visibility == 'RANGE':
                                    row = box.row(align=True)
                                    row.prop(lineset, "qi_start")
                                    row.prop(lineset, "qi_end")
                            if lineset.select_by_edge_types:
                                row = box.row(align=True)
                                row.label(text="Edge Types:",icon='EDGESEL')
                                row = box.row(align=False)
                                row.prop(lineset, "edge_type_negation", expand=True)
                                row.prop(lineset, "edge_type_combination", expand=True)
                                row = box.row(align=True)
                                row.prop(lineset,"select_silhouette")
                                row.prop(lineset,"exclude_silhouette",icon='X',text="")
                                row.prop(lineset, "select_border")
                                row.prop(lineset,"exclude_border",icon='X',text="")
                                row = box.row(align=True)
                                row.prop(lineset, "select_contour")
                                row.prop(lineset,"exclude_contour",icon='X',text="")
                                row.prop(lineset, "select_suggestive_contour")
                                row.prop(lineset,"exclude_suggestive_contour",icon='X',text="")
                                row = box.row(align=True)
                                row.prop(lineset, "select_ridge_valley")
                                row.prop(lineset,"exclude_ridge_valley",icon='X',text="")
                                row.prop(lineset, "select_crease")
                                row.prop(lineset,"exclude_crease",icon='X',text="")
                                row = box.row(align=True)
                                row.prop(lineset, "select_edge_mark")
                                row.prop(lineset,"exclude_edge_mark",icon='X',text="")
                                row.prop(lineset, "select_external_contour")
                                row.prop(lineset,"exclude_external_contour",icon='X',text="")
                                row = box.row(align=True)
                                row.prop(lineset, "select_material_boundary")
                                row.prop(lineset,"exclude_material_boundary",icon='X',text="")
                                row.label(text="")
                                row.label(text="",icon='BLANK1')
                            if lineset.select_by_face_marks:
                                row = box.row(align=True)
                                row.label(text="Face Marks:",icon='FACESEL')
                                row = box.row(align=True)
                                row.prop(lineset, "face_mark_negation", expand=True)
                                row.prop(lineset, "face_mark_condition", expand=True)
                            if lineset.select_by_collection:
                                row = box.row(align=True)
                                row.label(text="Collection:",icon='GROUP')
                                row = box.row(align=True)
                                row.prop(lineset, "collection", text="")
                                row.prop(lineset, "collection_negation", expand=True)
                        cw = tbb.tb_lay_free_line
                        cwt = "tb_lay_free_line"
                        cwtt = "Linestye"
                        cwi = 'LINE_DATA'
                        if cw == False:
                            row = box.row(align= False)            
                            row.prop(tbb, cwt,text=cwtt,icon=cwi)
                        if cw:
                            box = layout.box()
                            row = box.row(align= True)            
                            row.prop(tbb, cwt,text="",icon=cwi)
                            row.label(text=cwtt)                                   
                            view_layer = context.view_layer
                            lineset = view_layer.freestyle_settings.linesets.active
                            layout.active = view_layer.use_freestyle
                            if lineset is None:
                                return
                            linestyle = lineset.linestyle
                            box.template_ID(lineset, "linestyle", new="scene.freestyle_linestyle_new")
                            if linestyle is None:
                                return
                            row = box.row(align=True)
                            row.prop(linestyle, "panel", expand=True)
                            if linestyle.panel == 'STROKES':
                                # Chaining
                                row = box.row(align=True)
                                row.prop(linestyle, "use_chaining", text="",icon='LINKED')
                                row.label(text="Use Chaining:")
                                row = box.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "chaining", text="")
                                row.prop(linestyle, "use_same_object",text="",icon='OBJECT_DATA')
                                if linestyle.chaining == 'SKETCHY':
                                    row.prop(linestyle, "rounds")
                                # Second column
                                # Splitting
                                row = box.row(align=True)
                                row.label(text="Splitting:",icon='MOD_DISPLACE')
                                row.prop(linestyle, "material_boundary",text="",icon='MATERIAL_DATA')
                                row.prop(linestyle, "use_split_length", text="",icon='RADIOBUT_OFF')
                                sub = row.row()
                                sub.active = linestyle.use_split_length
                                sub.prop(linestyle, "split_length", text="2D Length")
                                split = box.split(align=True)
                                # First column
                                col = split.column()
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "use_angle_min", text="",icon='RADIOBUT_OFF')
                                sub = row.row()
                                sub.active = linestyle.use_angle_min
                                sub.prop(linestyle, "angle_min")
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "use_angle_max", text="",icon='RADIOBUT_OFF')
                                sub = row.row()
                                sub.active = linestyle.use_angle_max
                                sub.prop(linestyle, "angle_max")
                                # Second column
                                row = col.row(align=True)
                                row = col.row(align=True)
                                # End of columns
                                row = box.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "use_split_pattern", text="",icon='RADIOBUT_OFF')
                                sub = row.row(align=True)
                                sub.active = linestyle.use_split_pattern
                                sub.prop(linestyle, "split_dash1", text="D1")
                                sub.prop(linestyle, "split_dash2", text="D2")
                                sub.prop(linestyle, "split_dash3", text="D3")
                                row = box.row(align=True)
                                sub = row.row(align=True)
                                sub.label(icon='BLANK1')
                                sub.label(icon='BLANK1')
                                sub.active = linestyle.use_split_pattern
                                sub.prop(linestyle, "split_gap1", text="G1")
                                sub.prop(linestyle, "split_gap2", text="G2")
                                sub.prop(linestyle, "split_gap3", text="G3")

                                # Sorting
                                row = box.row(align=True)
                                row.prop(linestyle, "use_sorting", text="",icon='SORTSIZE')
                                row.label(text="Sorting:")
                                col = box.column()
                                col.active = linestyle.use_sorting
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "sort_key", text="")
                                sub = row.row()
                                sub.active = linestyle.sort_key in {'DISTANCE_FROM_CAMERA',
                                                                    'PROJECTED_X',
                                                                    'PROJECTED_Y'}
                                sub.prop(linestyle, "integration_type", text="")
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "sort_order", expand=True)

                                # Selection
                                row = box.row(align=True)
                                row.label(text="Selection:",icon='RESTRICT_SELECT_ON')
                                sub = row.row(align=True)
                                sub.prop(linestyle, "use_chain_count", text="",icon='RADIOBUT_OFF')
                                sub.active = linestyle.use_chain_count
                                sub.prop(linestyle, "chain_count")
                                split = box.split(align=True)
                                # First column
                                col = split.column()
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "use_length_min", text="",icon='RADIOBUT_OFF')
                                sub = row.row()
                                sub.active = linestyle.use_length_min
                                sub.prop(linestyle, "length_min")
                                row = col.row(align=True)
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "use_length_max", text="",icon='RADIOBUT_OFF')
                                sub = row.row()
                                sub.active = linestyle.use_length_max
                                sub.prop(linestyle, "length_max")

                                # Caps
                                box.label(text="Caps:",icon='CON_DISTLIMIT')
                                row = box.row(align=True)
                                row.prop(linestyle, "caps", expand=True)

                                # Dashed lines
                                row = box.row(align=True)
                                row.prop(linestyle, "use_dashed_line", text="",icon='DRIVER_DISTANCE')
                                row.label(text="Dashed Line:")
                                row = box.row(align=True)
                                row.active = linestyle.use_dashed_line
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "gap1", text="G1")
                                row.prop(linestyle, "gap2", text="G2")
                                row.prop(linestyle, "gap3", text="G3")
                                row = box.row(align=True)
                                row.active = linestyle.use_dashed_line
                                row.label(icon='BLANK1')
                                row.prop(linestyle, "dash1", text="D1")
                                row.prop(linestyle, "dash2", text="D2")
                                row.prop(linestyle, "dash3", text="D3")

                            elif linestyle.panel == 'COLOR':
                                box.prop(linestyle, "color", text="")
                                row = box.row(align=True)
                                row.label(icon='MODIFIER_DATA')
                                row.operator_menu_enum("scene.freestyle_color_modifier_add", "type", text="Add Modifier")
                                for modifier in linestyle.color_modifiers:
                                    self.draw_color_modifier(context, modifier)

                            elif linestyle.panel == 'ALPHA':
                                box.prop(linestyle, "alpha")
                                row = box.row(align=True)
                                row.label(icon='MODIFIER_DATA')
                                row.operator_menu_enum("scene.freestyle_alpha_modifier_add", "type", text="Add Modifier")
                                for modifier in linestyle.alpha_modifiers:
                                    self.draw_alpha_modifier(context, modifier)
                            elif linestyle.panel == 'THICKNESS':
                                box.prop(linestyle, "thickness")
                                col = box.column()
                                subcol = col.column()
                                subcol.active = linestyle.chaining == 'PLAIN' and linestyle.use_same_object
                                row = subcol.row()
                                row.prop(linestyle, "thickness_position", expand=True)
                                row = subcol.row()
                                row.prop(linestyle, "thickness_ratio")
                                row.active = (linestyle.thickness_position == 'RELATIVE')
                                row = box.row(align=True)
                                row.label(icon='MODIFIER_DATA')
                                row.operator_menu_enum("scene.freestyle_thickness_modifier_add", "type", text="Add Modifier")
                                for modifier in linestyle.thickness_modifiers:
                                    self.draw_thickness_modifier(context, modifier)

                            elif linestyle.panel == 'GEOMETRY':
                                row = box.row(align=True)
                                row.label(icon='MODIFIER_DATA')
                                row.operator_menu_enum("scene.freestyle_geometry_modifier_add", "type", text="Add Modifier")
                                for modifier in linestyle.geometry_modifiers:
                                    self.draw_geometry_modifier(context, modifier)

                            elif linestyle.panel == 'TEXTURE':
                                box.separator()
                                row = box.row()
                                row.prop(linestyle, "use_nodes",text="",icon='NODETREE')
                                row.prop(linestyle, "texture_spacing", text="Spacing Along Stroke")

                                box.label(text="Mind StyleLine Texture Properties", icon='TEXTURE')
                            elif linestyle.panel == 'MISC':
                                pass
#CYCLES
def tbrenderlight(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenlightdef
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    layout = self.layout
    if tbb.tb_ren_pstyle == False:
        layc = layout.box()
        row = layc.row(align= True)            
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
        row.popover(panel='CYCLES_PT_integrator_presets',icon='PRESET',text="Preset")                                 
    else: 
        layc = layout  
    row = layc.row(align=True)
    row.label(icon='BLANK1')
    row.prop(context.scene.cycles,"max_bounces")
    row = layc.row(align=True)
    row.label(icon='BLANK1')
    row.prop(cscene, "caustics_reflective",icon='INDIRECT_ONLY_OFF')
    row.prop(cscene, "caustics_refractive",icon='DECORATE_LIBRARY_OVERRIDE')
    row = layc.row(align=True)
    row.label(icon='MATERIAL')
    row.prop(cscene, "diffuse_bounces", text="Diffuse")
    row.label(icon='SHADING_RENDERED')
    row.prop(cscene, "transmission_bounces", text="Transmission")
    row = layc.row(align=True)
    row.label(icon='NODE_MATERIAL')
    row.prop(cscene, "glossy_bounces", text="Glossy")
    row.prop(cscene, "blur_glossy")
    row = layc.row(align=True)
    row.label(icon='GHOST_DISABLED')
    row.prop(cscene, "transparent_max_bounces", text="Transparency")
    row.label(icon='MOD_FLUID')
    row.prop(cscene, "volume_bounces", text="Volume")
    row = layc.row(align=True)
    row.label(text="Volumes",icon='MOD_FLUID')
    row.prop(cscene, "volume_step_rate", text="Step Size")
    row.prop(cscene, "volume_max_steps", text="Max Steps")
    row = layc.row(align=True)
    row.label(text="Clamping")
    row.prop(cscene, "sample_clamp_direct", text="Direct Light")
    row.prop(cscene, "sample_clamp_indirect", text="Indirect Light")
#EEVEE
def tbrenderbloom(self,context,layout,mode):   
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = cntb_ren_bloom 
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
        row.prop(seevee, "use_bloom",text="Use bloom",icon='PROP_ON') 
   #START    
   
   #START    
    row = layout.row(align=True)                
    if bpy.context.scene.eevee.use_bloom:
        split = layout.split(align=True)
        col = split.column(align=True)
        col.prop(seevee, "bloom_color",text="")
        col.prop(seevee, "bloom_threshold")
        col.prop(seevee, "bloom_knee")
        col = split.column(align=True)
        col.prop(seevee, "bloom_intensity")
        col.prop(seevee, "bloom_radius")
        
        col.prop(seevee, "bloom_clamp")     
def tbrenderssr(self,context,layout,mode):
    #DEF 
    scene = context.scene
    seevee = scene.eevee 
    layout = self.layout
    row = layout.row()                               
    if bpy.context.scene.eevee.use_ssr:
        split = layout.split(align=True)
        col = split.column(align=True)
        col.active = seevee.use_ssr
        col.prop(seevee, "use_ssr_refraction", text="Refraction",icon='INDIRECT_ONLY_OFF')
        col.prop(seevee, "ssr_quality")
        col.prop(seevee, "ssr_max_roughness")
        col = split.column(align=True)
        col.prop(seevee, "use_ssr_halfres",icon='MOD_DECIM')
        col.prop(seevee, "ssr_thickness")
        col.prop(seevee, "ssr_border_fade")
        col.prop(seevee, "ssr_firefly_fac")
def tbrenderao(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = cntb_ren_ao
    scene = context.scene
    seevee = scene.eevee
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
#START
    if bpy.context.scene.eevee.use_gtao == False:
        row.separator()
        row.prop(seevee,"use_gtao",icon='PROP_OFF',text="Enable Ambient Occlusion")
    if bpy.context.scene.eevee.use_gtao:
        row.label(text=defcontext[1])   
        row.separator()                    
        row.prop(seevee,"use_gtao",text="",icon='PROP_ON')        
    if bpy.context.scene.eevee.use_gtao:            
        row = layout.row()  
        row.prop(seevee, "gtao_distance")
        split = layout.split(align=True)
        col = split.column(align=True)
        col.prop(seevee, "gtao_factor")
        col.prop(seevee, "use_gtao_bent_normals",icon='NORMALS_FACE')
        col = split.column(align=True)
        col.prop(seevee, "gtao_quality")
        col.prop(seevee, "use_gtao_bounce",icon='INDIRECT_ONLY_OFF')
def tbrendermb(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    context = bpy.context   
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:    
            cw = tbb.tb_ren_mb
            cwt = "tb_ren_mb"
            cwtt = "Motion Blur"
            cwi = 'FORCE_CURVE'
            layc = layout.box()
            row = layc.row(align= True)  
            row.prop(tbb, cwt,text="",icon=cwi)
   #START   
    box = layout.box()
    row = box.row()
    if mode == "DOCK":
        row.prop(tbb,"tb_ren_mb",text="",icon='FORCE_CURVE') 
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        if bpy.context.scene.eevee.use_motion_blur:
            if mode != "Panel":
                row.prop(context.scene.eevee,"use_motion_blur",text="",icon='PROP_ON')
            row.prop(seevee, "motion_blur_position", text="")
            row.prop(seevee, "motion_blur_shutter")
            row = box.row(align=False)
            row.prop(seevee, "motion_blur_depth_scale")
            row.prop(seevee, "motion_blur_steps")
            row.prop(seevee, "motion_blur_max")
        else:
            row.prop(context.scene.eevee,"use_motion_blur",text="Use Motion Blur",icon='PROP_ON')
    if bpy.context.scene.render.engine == 'CYCLES':
        if bpy.context.scene.render.use_motion_blur:
            row.prop(context.scene.render,"use_motion_blur",text="",icon='PROP_ON')
            row.prop(cscene, "motion_blur_position", text="")
            row.prop(rd, "motion_blur_shutter")
            row = box.row(align=False)                    
            row.prop(cscene, "rolling_shutter_type", text="")
            row.prop(cscene, "rolling_shutter_duration")
            split = box.split(factor=0.92,align=True)
            col = split.column()
            col.template_curve_mapping(rd, "motion_blur_shutter_curve")
            col = split.column()
            col.label()
            col.operator("render.shutter_curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
            col.operator("render.shutter_curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
            col.operator("render.shutter_curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
            col.operator("render.shutter_curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
            col.operator("render.shutter_curve_preset", icon='LINCURVE', text="").shape = 'LINE'
            col.operator("render.shutter_curve_preset", icon='NOCURVE', text="").shape = 'MAX'
        else:
            row.prop(context.scene.render,"use_motion_blur",icon='PROP_ON')
def pnltb_ren_df(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = cntb_ren_df 
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1]) 
    box = layout.box()                
    row = box.row(align= True)      
    row.prop(seevee,"bokeh_max_size",text="Size",icon='CAMERA_DATA')
    row = layout.row(align=True)
    row.prop(seevee, "bokeh_threshold")
    row.prop(seevee, "bokeh_neighbor_max")
    row.prop(seevee, "bokeh_denoise_fac")
    row = layout.row(align=True)
    row.prop(seevee, "use_bokeh_high_quality_slight_defocus",icon='FORCE_TEXTURE')
    if seevee.use_bokeh_jittered == False:
        row.prop(seevee, "use_bokeh_jittered",icon='CON_CAMERASOLVER')
    else:
        row = layout.row(align=True)
        row.prop(seevee, "use_bokeh_jittered",icon='CON_CAMERASOLVER')
        row.prop(seevee, "bokeh_overblur")      
def tbrenderss(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenssdef 
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee     
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])

    row = layout.row(align=True)
    row.prop(seevee, "sss_samples",text="Samples")  
    row.prop(seevee, "sss_jitter_threshold") 
def tbrendershadows(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool     
    defcontext = tbrenshadef
    scene = context.scene
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if tbb.tb_ren_pstyle == False:
        layc = layout.box()
        row = layc.row(align= True)    
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])    
    else: 
        layc = layout 
    row = layc.row(align=True)
    #START 
    row.prop(seevee, "shadow_cube_size", text="")
    row.prop(seevee, "shadow_cascade_size", text="")
    row.prop(seevee, "use_soft_shadows",text="",icon='MOD_SMOOTH')
    row = layc.row(align=True)                            
    row.prop(seevee, "light_threshold",text="Threshold")
    row.separator()
    row.prop(seevee, "use_shadow_high_bitdepth",icon='MOD_MULTIRES')
def tbrendervolume(self,context,layout,mode): 
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenvoldef 
    scene = context.scene
    scene = context.scene
    seevee = scene.eevee 
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])
    row = layout.row(align=True)            
    row.prop(seevee, "volumetric_tile_size",text="")
    row = layout.row(align=True)
    row.prop(seevee, "volumetric_samples")
    row.prop(seevee, "volumetric_sample_distribution", text="Distribution")
    row = layout.row(align=True)            
    row.prop(seevee, "volumetric_start")
    row.prop(seevee, "volumetric_end")
    row = layout.row(align=True)
    row.prop(seevee, "use_volumetric_lights",text="Lights",icon='LIGHT_SPOT')
    if seevee.use_volumetric_lights:
        row.prop(seevee,"volumetric_light_clamp",text="Clamping")
    if seevee.use_volumetric_lights == False and seevee.use_volumetric_shadows == False:
        row.separator()
    if seevee.use_volumetric_lights or seevee.use_volumetric_shadows:
        row = layout.row(align=True)
        row.label(icon='BLANK1')
    row.prop(seevee, "use_volumetric_shadows",text="Shadows",icon='OVERLAY')
    if seevee.use_volumetric_shadows:
        row.prop(seevee,"volumetric_shadow_samples",text="Samples")
def tbrenderhair(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    defcontext = tbrenhairdef 
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1])   
   #START    
    row = layout.row(align=True)    
    if bpy.context.scene.render.engine == 'CYCLES':        
        ccscene = scene.cycles_curves
        row.prop(ccscene, "shape", text="")
        if ccscene.shape == 'RIBBONS':
            row.separator()
            row.prop(context.scene.cycles_curves,"subdivisions") 
    else: 
        row.prop(rd, "hair_type", expand=True)
        row.prop(rd, "hair_subdiv")   
        #not shape on EEVEE 3.9
        #row.prop(cscene, "shape", text="")   
def tbrendershadow(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenshadef 
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1]) 
    box = layout.box()                
    row = box.row(align= True)             
    row.prop(seevee, "shadow_cube_size", text="")
    row.prop(seevee, "shadow_cascade_size", text="")
    row.prop(seevee, "use_soft_shadows",text="",icon='MOD_SMOOTH')
    row = box.row(align= True)                            
    row.label(icon='BLANK1')
    row.separator()
    row.prop(seevee, "light_threshold",text="Threshold")
    row.separator()
    row.prop(seevee, "use_shadow_high_bitdepth",icon='MOD_MULTIRES')

#EEVEE def
def tbrendereeveesub(self,context,layout,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = tbrenshadef 
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    scene = context.scene
    rd = scene.render
    seevee = scene.eevee 
    cscene = scene.cycles
    if mode == "Panel":
        if tbb.tb_ren_pstyle:
            layout = self.layout
        else:
            layout = layout.box()
            row = layout.row(align= True)            
            row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
            row.label(text=defcontext[1])               
    else:
        layout = layout.box()
        row = layout.row(align= True)           
        row.prop(tbb, defcontext[0],text="",icon=defcontext[2])
        row.label(text=defcontext[1]) 
    box = layout.box()                
    row = box.row(align= True)             
    row.prop(seevee, "shadow_cube_size", text="")
    row.prop(seevee, "shadow_cascade_size", text="")
    row.prop(seevee, "use_soft_shadows",text="",icon='MOD_SMOOTH')
    row = box.row(align= True)                            
    row.label(icon='BLANK1')
    row.separator()
    row.prop(seevee, "light_threshold",text="Threshold")
    row.separator()
    row.prop(seevee, "use_shadow_high_bitdepth",icon='MOD_MULTIRES')


def tbrenderdraw(self,context,mode):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool     
    rd = context.scene.render
    window = context.window
    screen = context.screen
    scene = context.scene
    view = scene.view_settings
    cscene = scene.cycles
    wscene = window.scene
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        seevee = bpy.context.scene.eevee         
    layout = self.layout
    box = layout.box()        
    row = box.row(align= True)
    #LAYERS
    row.prop(wscene,"camera",text="",icon='CAMERA_DATA')
    row.prop(wscene, "active_clip", text="")
    box.template_ID(window, "scene", new="scene.new",
                unlink="scene.delete")
    row.prop(wscene, "background_set",text="")
    row = box.row(align=True)
    row.template_search(window, "view_layer",wscene, "view_layers",new="scene.view_layer_add",unlink="scene.view_layer_remove")   
    #GENERALES 
    if tbb.tb_ren_pstyle == False:
        if tbb.tb_ren_res == False or tbb.tb_ren_out == False:
            box = layout.box()
            row = box.row()
        #START
        if tbb.tb_ren_res == False:
            row.prop(tbb, "tb_ren_res",text="Resolution",icon='MOD_MULTIRES')  
        if tbb.tb_ren_res:
            tbrenderresolution(self,context,layout,mode)
        if tbb.tb_ren_out == False:
            row.prop(tbb, "tb_ren_out",text="Output",icon='OUTPUT') 
        if tbb.tb_ren_out:
            tbrenderout(self,context,layout,mode)
        if tbb.tb_ren_sam == False:
            row.prop(tbb, "tb_ren_sam",text="Sampling",icon='IMGDISPLAY')      
        if tbb.tb_ren_sam:
            tbrendersamples(self,context,layout,mode)
        if tbb.tb_ren_pref == False:
            row.prop(tbb, "tb_ren_pref",text="Preferences",icon='PREFERENCES')  
        if tbb.tb_ren_pref:
            tbrenderpref(self,context,layout,mode)
        if tbb.tb_ren_film == False:
            row.prop(tbb, "tb_ren_film",text="Film",icon='RENDER_STILL')
        if tbb.tb_ren_film:
            tbrenderfilm(self,context,layout,mode)     
        #POSTPROCESS
        row = box.row(align=True)   
        if tbb.tb_ren_col == False:
            row.prop(tbb, "tb_ren_col",text="Color Management",icon='COLOR')
        if tbb.tb_ren_col:
            tbrendercolor(self,context,layout,mode)
        if tbb.tb_ren_col == False and tbb.tb_ren_free == False:
            row.separator()   

        defcontext = tbrenfreedef
        if tbb.tb_ren_free == False:
            row.prop(tbb, defcontext[0],text = defcontext[1], icon = defcontext[2]) 
            row.prop(context.scene.render, "use_freestyle", text="Use Freestyle",icon='PROP_OFF')   
        if tbb.tb_ren_free:
            tbrenderfreestyle(self,context,layout,mode)
        
        if tbb.tb_ren_free == False and tbb.tb_ren_grease == False:
            row.separator()                   

        defcontext = tbrengreasedef
        if tbb.tb_ren_grease == False:
            row.prop(tbb, defcontext[0],text = defcontext[1], icon = defcontext[2])  
        if tbb.tb_ren_grease:
            tbrendergrease(self,context,layout,mode)                                                        
                
        if bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES':
            row = box.row()                                  
            if tbb.tb_ren_mb == False:
                row.prop(tbb, "tb_ren_mb",text="Motion Blur",icon='FORCE_CURVE')
            if tbb.tb_ren_mb:
                tbrendermb(self,context,layout,mode)
        if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
            if tbb.tb_ren_eevee_bloom == False:
                row.prop(tbb, "tb_ren_eevee_bloom",text="Bloom",icon='LIGHT_SUN') 
            if tbb.tb_ren_eevee_bloom:             
                tbrenderbloom(self,context,layout,mode)
            defcontext = tbrenshadef
            if tbb.tb_ren_sha == False:
                row.prop(tbb, defcontext[0],text = defcontext[1], icon = defcontext[2]) 
            else:          
                tbrendershadows(self,context,layout,mode)     
            defcontext = tbrenvoldef
            if tbb.tb_ren_vol == False:
                row.prop(tbb, defcontext[0],text = defcontext[1], icon = defcontext[2]) 
            else:               
                tbrendervolume(self,context,layout,mode) 
            if tbb.tb_ren_eevee_ssr == False:
                row.prop(tbb, "tb_ren_eevee_ssr",text="Screen Space Reflection",icon='LIGHTPROBE_PLANAR') 
            if tbb.tb_ren_eevee_ssr:             
                tbrenderss(self,context,layout,mode)                                        
        if bpy.context.scene.render.engine == 'CYCLES':
            row = box.row(align=True)
            defcontext = tbrenlightdef
            if tbb.tb_ren_lgh == False:
                row.prop(tbb, defcontext[0],text = defcontext[1], icon = defcontext[2]) 
                row.popover(panel='CYCLES_PT_integrator_presets',icon='PRESET',text="")      
            if tbb.tb_ren_lgh:
                tbrenderlight(self,context,layout,mode)
        
        #SCENE
        row = box.row(align=True)  
        if tbb.tb_ren_simply == False:
            row.prop(tbb, "tb_ren_simply",text="Simplify",icon='MOD_DECIM')
            row.prop(rd, "use_simplify",text="",icon='PROP_OFF')
        if tbb.tb_ren_simply:
            tbrendersimplify(self,context,layout,mode)
        if tbb.tb_ren_simply == False and tbb.tb_ren_hair == False:
            row.separator()            
        if not tbb.tb_ren_hair:
            row.prop(tbb, "tb_ren_hair",text="Hair",icon='CURVES_DATA')
        if tbb.tb_ren_hair:
            tbrenderhair(self,context,layout,mode)                       
   #EEVEE
    # else:
        #if bpy.context.scene.render.engine == 'BLENDER_EEVEE':  
        #    box = layout.box()        
        #    row = box.row(align= True)
        #    if not tbb.tb_ren_eevee_depth:
        #        row.prop(tbb, "tb_ren_eevee_depth",text=cntb_ren_df[1],icon=cntb_ren_df[2])
        #    else:
        #        box = layout.box()  
        #        pnltb_ren_df(self,context,layout,mode)
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':     
        #DEPTH OF FIELD
        cw = tbb.tb_ren_eevee_depth
        cwt = "tb_ren_eevee_depth"
        cwtt = "Depth of Field"
        cwi = 'CON_CAMERASOLVER' 
        if cw:
            eeveescene = context.scene.eevee
            box = layout.box()
            row = box.row(align=True)
            row.prop(tbb, cwt,text="",icon=cwi)
            row.separator()
            row.label(text="Depth of Field")
            row.prop(eeveescene,"bokeh_max_size",text="Size",icon='CAMERA_DATA')
            row = box.row(align=True)
            row.prop(eeveescene, "bokeh_threshold")
            row.prop(eeveescene, "bokeh_neighbor_max")
            row.prop(eeveescene, "bokeh_denoise_fac")
            row = box.row(align=True)
            row.prop(eeveescene, "use_bokeh_high_quality_slight_defocus",icon='FORCE_TEXTURE')
            if eeveescene.use_bokeh_jittered == False:
                row.prop(eeveescene, "use_bokeh_jittered",icon='CON_CAMERASOLVER')
            else:
                row = box.row(align=True)
                row.prop(eeveescene, "use_bokeh_jittered",icon='CON_CAMERASOLVER')
                row.prop(eeveescene, "bokeh_overblur")                
        #Ambient Oclusion
        if tbb.tb_ren_eevee_ao and tbb.tb_ren_pstyle == False:       
            tbrenderao(self,context,layout,mode)
        #Screen Space Reflection
        cw = tbb.tb_ren_eevee_ssr
        cwt = "tb_ren_eevee_ssr"
        cwtt = "Screen Space Reflections"
        cwi = 'LIGHTPROBE_PLANAR'
        if cw:
            box = layout.box()   
            row = box.row()                                                    
            row.prop(wm.tb_wm_bool, "tb_ren_eevee_ssr" ,text="",icon=cwi)                
            if bpy.context.scene.eevee.use_ssr == False:
                row.prop(seevee,"use_ssr",icon='PROP_OFF')
            if bpy.context.scene.eevee.use_ssr:
                row.prop(seevee,"use_ssr",icon='PROP_ON',text="")
                row.label(text="Screen Space Refrection")
                split = box.split(align=True)
                col = split.column(align=True)
                col.active = seevee.use_ssr
                col.prop(seevee, "use_ssr_refraction", text="Refraction",icon='INDIRECT_ONLY_OFF')
                col.prop(seevee, "ssr_quality")
                col.prop(seevee, "ssr_max_roughness")
                col = split.column(align=True)
                col.prop(seevee, "use_ssr_halfres",icon='MOD_DECIM')
                col.prop(seevee, "ssr_thickness")
                col.prop(seevee, "ssr_border_fade")
                col.prop(seevee, "ssr_firefly_fac")
        cw = tbb.tb_ren_eevee_mb
        cwt = "tb_ren_eevee_mb"
        cwtt = "Motion Blur"
        cwi = 'FORCE_CURVE'
        if cw:                    
            if bpy.context.scene.eevee.use_motion_blur:
                box = layout.box()
                row = box.row(align=True)
                row.prop(seevee,"use_motion_blur",icon='FORCE_CURVE',text="")
                row.label(text="Motion Blur")
                row.prop(seevee, "motion_blur_samples")
                row.prop(seevee, "motion_blur_shutter")
       #SUBSURFACE_SCATER
        if tbb.tb_ren_eevee_sub:
            box = layout.box()                
            row = box.row(align= True)            
            row.prop(tbb, tb_ren_eevee_sub,text="",icon='SHADING_RENDERED')
            row.label(text="Shadow")                
            row.prop(seevee, "sss_samples",text="Samples")
            row = box.row(align=True)
            row.label(icon='BLANK1')
            row.separator()
            row.prop(seevee, "sss_jitter_threshold")
            box = layout.box()                
            row = box.row(align= True)            
            row.prop(tbb, cwt,text="",icon=cwi)
            row.label(text=cwtt)                    
            row.prop(seevee, "shadow_cube_size", text="")
            row.prop(seevee, "shadow_cascade_size", text="")
            row.prop(seevee, "use_soft_shadows",text="",icon='MOD_SMOOTH')
            row = box.row(align= True)                            
            row.label(icon='BLANK1')
            row.separator()
            row.prop(seevee, "light_threshold",text="Threshold")
            row.separator()
            row.prop(seevee, "use_shadow_high_bitdepth",icon='MOD_MULTIRES')

def tbrenderdrawpop(self,context):  
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool
    mode = "DOCK"
    rd = context.scene.render
    window = context.window
    screen = context.screen
    scene = context.scene
    view = scene.view_settings
    cscene = scene.cycles
    wscene = window.scene
    view_layer = context.view_layer
    cycles_view_layer = view_layer.cycles
    seevee = bpy.context.scene.eevee 
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        seevee = bpy.context.scene.eevee         
    layout = self.layout
    split = layout.split(align=True)
    layout = split.column(align=True)
    box = layout.box()    
    row = box.row(align= True)
    #LAYERS
    row.prop(wscene,"camera",text="",icon='CAMERA_DATA')
    row.prop(wscene, "active_clip", text="")
    box.template_ID(window, "scene", new="scene.new",
                unlink="scene.delete")
    row.prop(wscene, "background_set",text="")
    row = box.row(align=True)
    row.template_search(window, "view_layer",wscene, "view_layers",new="scene.view_layer_add",unlink="scene.view_layer_remove")
    #GENERALES 
    row = box.row(align=True)

    contextitem(self,context,layout,mode,row,tbrenresdef,tbrenderresolution)
    if not tbb.get(tbrenresdef[0]):
        row.popover(panel='RENDER_PT_format_presets',icon='PRESET',text="")
    row = box.row(align=True)
    contextitem(self,context,layout,mode,row,tbrenoutdef,tbrenderout)
    
    layout = split.column(align=True)
    if not (tbb.get(tbrenperfdef[0]) and tbb.get(tbrenfilmdef[0]) and tbb.get(tbrensamdef[0])):
        box = layout.box()    
    if not tbb.get(tbrensamdef[0]):
        row = box.row(align=True)
    contextitem(self,context,layout,mode,row,tbrensamdef,tbrendersamples) 
    if not tbb.get(tbrensamdef[0]):
        row.popover(panel='CYCLES_PT_sampling_presets',icon='PRESET',text="Preset")
    row = box.row(align=True)       
    contextitem(self,context,layout,mode,row,tbrenperfdef,tbrenderpref) 
    contextitem(self,context,layout,mode,row,tbrenfilmdef,tbrenderfilm) 
    #Post-Process Box
    layout = split.column(align=True)
    box = layout.box()    
    row = box.row(align=True)
    #Color Management 
    contextitem(self,context,layout,mode,row,tbrencoldef,tbrendercolor) 
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES':
    #Motion Blur 
        if not tbb.get(tbrenmbdef[0]):
            row.separator()       
        contextitem(self,context,layout,mode,row,tbrenmbdef,tbrendermb) 
        if not tbb.get(tbrenmbdef[0]):
            if bpy.context.scene.render.engine == 'CYCLES':
                row.prop(rd,"use_motion_blur",icon='PROP_ON',text="")    
            if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
                row.prop(seevee,"use_motion_blur",icon='PROP_ON',text="")    
        row = box.row(align=True)
    #Grease Pencil 
        contextitem(self,context,layout,mode,row,tbrengreasedef,tbrendergrease)  
        if tbb.tb_ren_free == False and tbb.tb_ren_grease == False:
            row.separator()                   
        contextitem(self,context,layout,mode,row,tbrenfreedef,tbrenderfreestyle)
        if tbb.tb_ren_free == False:
            row.prop(rd,"use_freestyle",icon='PROP_ON',text="")   
    #4ºCOLUMN
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE':
        layout = split.column(align=True)
        box = layout.box()    
        row = box.row(align=False)            
        contextitem(self,context,layout,mode,row,cntb_ren_bloom,tbrenderbloom)  
        contextitem(self,context,layout,mode,row,tbrenshadef,tbrendershadow)   
        row = box.row(align=False)           
        contextitem(self,context,layout,mode,row,tbrenvoldef,tbrendervolume)
        contextitem(self,context,layout,mode,row,tbrenssrdef,tbrenderssr)            
        row = box.row(align=False)           
        contextitem(self,context,layout,mode,row,tbrenssdef,tbrenderss)    
        contextitem(self,context,layout,mode,row,cntb_ren_df,pnltb_ren_df) 
        row = box.row(align=True)          
        contextitem(self,context,layout,mode,row,cntb_ren_ao,tbrenderao) 
        if not tbb.get(cntb_ren_ao[0]):
            row.prop(seevee,"use_gtao",text="",icon='PROP_ON')
    if bpy.context.scene.render.engine == 'CYCLES':
        layout = split.column(align=True)
        box = layout.box()                            
        row = box.row(align=True)
        #SCENE
        contextitem(self,context,layout,mode,row,tbrenlightdef,tbrenderlight) 
        if tbb.tb_ren_simply == False and not (tbb.get(tbrenlightdef[0])):
            row.separator()                      
        contextitem(self,context,layout,mode,row,tbrensimplydef,tbrendersimplify) 
        if not tbb.get(tbrensimplydef[0]):
            row.prop(rd, "use_simplify",text="",icon='PROP_OFF')
        row = box.row(align=True)  
    if bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES':
        if not tbb.get(tbrenhairdef[0]):
            row.separator()                    
        contextitem(self,context,layout,mode,row,tbrenhairdef,tbrenderhair) 

    
def contextitem(self,context,layout,mode,row,contextitem,classitem):
    wm = bpy.context.window_manager
    tbb = wm.tb_wm_bool    
    defcontext = contextitem
    if tbb.get(defcontext[0]):
        classitem(self,context,layout,mode)                                        
    else:             
        row.prop(tbb, defcontext[0],text=defcontext[1],icon=defcontext[2]) 

#____CLASS____#
class TB_PT_Render_UI_3D(bpy.types.Panel):
    bl_label = "Render Panel"
    bl_idname = "TB_PT_Set_Render_UI"
    bl_space_type = 'VIEW_3D' 
    bl_region_type = 'UI'
    bl_category = 'tb_pnl'
    bl_options = {'DEFAULT_CLOSED'}        
    def draw_header(self, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool    
        layout = self.layout
        layout.label(text='',icon='RESTRICT_RENDER_OFF')
        layout.prop(tbb,"tb_ren_pstyle",text="",icon='PROP_ON')  
    def draw(self, context):
        mode = "Panel"
        tbrenderdraw(self,context,mode)
class TB_PT_Render_UI_3D_RENDER(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Render"
    bl_parent_id = "TB_PT_Set_Render_UI"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        props = scene.eevee
        self.layout.label(icon='SCENE')
    def draw(self, context):
        layout = self.layout


class TB_PT_Render_UI_3D_RESOLUTION(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Resolution"
    bl_parent_id = "TB_PT_Set_Render_UI"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        props = scene.eevee
        self.layout.label(icon='MOD_MULTIRES')
    def draw(self, context):
        layout = self.layout
        mode = "Panel"
        tbrenderresolution(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_RESOLUTION(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = ""
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool   
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        layout = self.layout    
        row = layout.row(align=True)
        row.label(icon='MOD_MULTIRES')  
        row.label(text="Resolution") 
        strresx = str(bpy.context.scene.render.resolution_x)
        strresy = str(bpy.context.scene.render.resolution_y)
        strres = strresx + "x" + strresy
        row.popover(panel='RENDER_PT_presets',icon='PRESET',text=strres)
    def draw(self, context):
        layout = self.layout
        mode = "Panel"
        tbrenderresolution(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_OUTPUT(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Output"
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool        
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        props = scene.eevee
        self.layout.label(icon='OUTPUT')
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderout(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_SAMPLES(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = ""
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool        
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        layout = self.layout
        row = layout.row(align=True)
        row.label(icon='IMGDISPLAY')
        row.label(text="Samples")
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendersamples(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_PREF(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Performance"
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool          
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        layout = self.layout
        row = layout.row(align=True)
        row.label(icon='PREFERENCES')
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderpref(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_FILM(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Film"
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool        
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee 
        self.layout.label(icon='RENDER_STILL')
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderfilm(self,context,layout,mode)
class TB_PT_Render_UI_3D_RENDER_LIGHT(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = ""
    bl_parent_id = "TB_PT_Render_UI_3D_RENDER"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool       
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'CYCLES'
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee 
        layout = self.layout
        row = layout.row(align=True)
        row.label(icon='LIGHT_DATA')
        row = row.split(factor=0.5)
        row.label(text="Light Paths")
        maxbounces = str(bpy.context.scene.cycles.max_bounces)
        row.popover(panel='CYCLES_PT_integrator_presets',icon='PRESET',text = maxbounces)
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderlight(self,context,layout,mode)

#POST
class TB_PT_Render_UI_3D_POST_PROCESS(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Post Process"
    bl_parent_id = "TB_PT_Set_Render_UI"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool       
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        props = scene.eevee
        self.layout.label(icon='RENDER_STILL')
    def draw(self, context):
        layout = self.layout
#EEVEE
class TB_PT_Render_UI_3D_POST_BLOOM(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Bloom"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool   
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        self.layout.prop(seevee,"use_bloom",text="",icon='LIGHT_SUN')  
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderbloom(self,context,layout,mode)        
class TB_PT_Render_UI_3D_POST_SCREENSPACEREFLECTIONS(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Screen Space Reflections"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        self.layout.prop(seevee,"use_ssr",text="",icon='LIGHTPROBE_PLANAR') 
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderssr(self,context,layout,mode)      
class TB_PT_Render_UI_3D_POST_AMBIENT_OCCLUSION(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Ambient Occlusion"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool         
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        self.layout.prop(seevee,"use_gtao",text="",icon='MATSHADERBALL') 
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderao(self,context,layout,mode)      
class TB_PT_Render_UI_3D_POST_MOTIONBLUR(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Motion Blur"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool    
        return tbb.tb_ren_pstyle == True and (bpy.context.scene.render.engine == 'BLENDER_EEVEE' or bpy.context.scene.render.engine == 'CYCLES')
    def draw_header(self, context):
        scene = context.scene
        seevee = scene.eevee
        self.layout.prop(seevee,"use_motion_blur",text="",icon='FORCE_CURVE') 
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendermb(self,context,layout,mode)      
class TB_PT_Render_UI_3D_POST_DEPTHFIELD(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Depth of Field"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool   
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        self.layout.label(icon='CON_CAMERASOLVER')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        pnltb_ren_df(self,context,layout,mode)      
class TB_PT_Render_UI_3D_POST_SUBSURFACESCATTER(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Subsurface Scattering"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        self.layout.label(icon='SHADING_RENDERED')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderss(self,context,layout,mode) 
class TB_PT_Render_UI_3D_COLOR(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Color Managment"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool   
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        self.layout.label(icon='COLOR')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendercolor(self,context,layout,mode) 
class TB_PT_Render_UI_3D_SHADOW(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Shadow"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool  
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        self.layout.label(icon='MOD_OPACITY')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendershadows(self,context,layout,mode) 
class TB_PT_Render_UI_3D_VOLUME(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Volume"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True and bpy.context.scene.render.engine == 'BLENDER_EEVEE'
    def draw_header(self, context):
        self.layout.label(icon='VOLUME_DATA')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"    
        tbrendervolume(self,context,layout,mode) 
class TB_PT_Render_UI_3D_GREASE_PENCIL(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Grease Pencil"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        self.layout.label(icon='OUTLINER_OB_GREASEPENCIL')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendergrease(self,context,layout,mode) 
class TB_PT_Render_UI_3D_FREESTYLE(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Freestyle"
    bl_parent_id = "TB_PT_Render_UI_3D_POST_PROCESS"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        self.layout.prop(context.scene.render, "use_freestyle", text="",icon='OUTLINER_OB_GREASEPENCIL')           
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderfreestyle(self,context,layout,mode) 

#SCENE_LEVEL
class TB_PT_Render_UI_3D_SCENE_LEVEL(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Scene_Data"
    bl_parent_id = "TB_PT_Set_Render_UI"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        props = scene.eevee
        self.layout.label(icon='SCENE_DATA')
    def draw(self, context):
        layout = self.layout
class TB_PT_Render_UI_3D_RENDER_SIMPLY(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Simplify"
    bl_parent_id = "TB_PT_Render_UI_3D_SCENE_LEVEL"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        scene = context.scene
        self.layout.prop(scene.render, "use_simplify",text="",icon='MOD_DECIM')
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrendersimplify(self,context,layout,mode)
class TB_PT_Render_UI_3D_LEVEL_HAIR(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SCN"
    bl_label = "Hair"
    bl_parent_id = "TB_PT_Render_UI_3D_SCENE_LEVEL"
    bl_options = {'DEFAULT_CLOSED'}        
    @classmethod
    def poll(cls, context):
        wm = bpy.context.window_manager
        tbb = wm.tb_wm_bool 
        return tbb.tb_ren_pstyle == True
    def draw_header(self, context):
        self.layout.label(icon='CURVES_DATA')
    def draw(self, context):
        layout = self.layout
        mode = "panel"
        tbrenderhair(self,context,layout,mode)

class TB_PT_Render_PoP_3D(bpy.types.Operator):
    """Tooltip"""
    bl_label = "Render"
    bl_idname = "context.tbrenderpopup"
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self,width = 1200)
    def draw(self, context):
        tbrenderdrawpop(self,context)    
    def execute(self, context):
        return {'FINISHED'}    

