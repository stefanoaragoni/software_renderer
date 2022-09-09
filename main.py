from texture import Texture
from gl import Render

def glpoint():
    r = Render()
    t = Texture()

    r.glCreateWindow(500,500)

    r.glClearColor(0,0,0) #parametros en rango de 0 a 1
    r.glClear()

    r.glViewPort(0,0,500,500) 

    r.glColor(0,0,0) #parametros en rango de 0 a 1
    
    r.active_shader = r.shader

    #------------------ORIGINAL
    r.lookAt(eye=[0,0,1],center=[0,0,0],up=[0,1,0])
    r.glLoad('./models/sphere.obj', translate=(-1,-1,0), scale=(5,5,5), rotate=(0,0,0))

    r.draw('TRIANGLES')
    r.glFinish()

glpoint()

