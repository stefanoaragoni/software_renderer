from texture import Texture
from gl import Render

def glpoint():
    r = Render()
    t = Texture()

    r.glCreateWindow(500,500)

    r.glClearColor(0,0.7098,0.8862)
    r.glClear()

    r.glViewPort(0,0,500,500) 

    r.glColor(1,1,1)
    
    r.lookAt(eye=[0,0,1],center=[0,0,0],up=[0,1,0])

    #------------------ORIGINAL
    """modelo 1 (10/50)"""
    t.read('./models/trex.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/trex.obj', translate=(-1,-4,0), scale=(3,3,3), rotate=(0,100,0), texture=t)
    r.draw('TRIANGLES')

    """modelo 1 (10/50)"""
    t.read('./models/dino.bmp')
    r.active_texture = t
    r.active_shader = r.shader
    r.glLoad('./models/dino.obj', translate=(-1,-4,0), scale=(0.05,0.05,0.05), rotate=(0,100,0), texture=t)
    r.draw('TRIANGLES')

    


    r.glFinish()

glpoint()


