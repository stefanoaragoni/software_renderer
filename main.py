from texture import Texture
from gl import Render

def glpoint():
    r = Render()
    t = Texture()

    r.glCreateWindow(600,600)

    r.glClearColor(0,0.7098,0.8862)
    r.glClear()

    r.glViewPort(0,0,600,600) 

    r.glColor(1,1,1)
    
    r.lookAt(eye=[0,0.1,1],center=[0,0,0],up=[0,1,0])

    #BACKGROUND
    t.read('./models/landscape.bmp')
    r.pixels = t.pixels

    #------------------ORIGINAL
    """modelo 1 (10/50)
    t.read('./models/grass.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/grass.obj', translate=(-1,-5,0), scale=(1,1,1), rotate=(0,20,0), texture=t)
    r.draw('TRIANGLES')"""

    """modelo 2 (20/50)"""
    t.read('./models/tree.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/tree.obj', translate=(-5,-4,0), scale=(0.15,0.15,0.15), rotate=(0,20,0), texture=t)
    r.draw('TRIANGLES')
   
    """modelo 3 (30/50)"""
    t.read('./models/meteor.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/meteor.obj', translate=(2.2,1.7,0), scale=(0.1,0.1,0.1), rotate=(0,200,0), texture=t)
    r.draw('TRIANGLES')

    """modelo 4 (40/50)"""
    t.read('./models/trex.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/trex.obj', translate=(-1,-4,0), scale=(3,3,3), rotate=(0,100,0), texture=t)
    r.draw('TRIANGLES')



    r.glFinish()

glpoint()


