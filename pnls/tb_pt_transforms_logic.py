import bpy
#LOCATION
def tsobjlocx(context):
    bpy.context.object.location[0] = 0
def tsobjlocy(context):
    bpy.context.object.location[1] = 0  
def tsobjlocz(context):
    bpy.context.object.location[2] = 0
#ROTATION
def tsobjrotx(context):
    bpy.context.object.rotation_euler[0] = 0    
def tsobjroty(context):
    bpy.context.object.rotation_euler[1] = 0   
def tsobjrotz(context):
    bpy.context.object.rotation_euler[2] = 0

#CURSOR 3D
def ts3dcrslocx(context):
    bpy.context.scene.cursor.location[0] = 0  
def ts3dcrslocy(context):
    bpy.context.scene.cursor.location[1] = 0  
def ts3dcrslocz(context):
    bpy.context.scene.cursor.location[2] = 0  
def ts3dcrsrotx(context):
    bpy.context.scene.cursor.rotation_euler[0] = 0   
def ts3dcrsroty(context):
    bpy.context.scene.cursor.rotation_euler[1] = 0   
def ts3dcrsrotz(context):
    bpy.context.scene.cursor.rotation_euler[2] = 0
def ts3dcrsrot(context):
    bpy.context.scene.cursor.rotation_euler[1] = 0
    bpy.context.scene.cursor.rotation_euler[2] = 0
    bpy.context.scene.cursor.rotation_euler[0] = 0  