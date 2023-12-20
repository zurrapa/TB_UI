import bpy

class TB_WORKSPACE_LT(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_lt"
    bl_label = "switch to workspace_LT"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["LT"]
        return {'FINISHED'}

class TB_WORKSPACE_UV(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_uv"
    bl_label = "switch to workspace_UV"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["UV"]
        return {'FINISHED'}

class TB_WORKSPACE_AN(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_an"
    bl_label = "switch to workspace_AN"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["AN"]
        return {'FINISHED'}


class TB_WORKSPACE_NGS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_ngs"
    bl_label = "switch to workspace_NGS"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["NGS"]
        return {'FINISHED'}
    
class TB_WORKSPACE_NS(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_ns"
    bl_label = "switch to workspace_NS"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["NS"]
        return {'FINISHED'}
     
class TB_WORKSPACE_NG(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_ng"
    bl_label = "switch to workspace_NG"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["NG"]
        return {'FINISHED'}
    
class TB_WORKSPACE_SCR(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_scr"
    bl_label = "switch to workspace_SCR"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["SCR"]
        return {'FINISHED'}
    
class TB_WORKSPACE_CM(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "context.tb_workspace_cm"
    bl_label = "switch to workspace_CM"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.context.window.workspace = bpy.data.workspaces["CM"]
        return {'FINISHED'}

    