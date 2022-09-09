from texture import Texture
from gl import Render

def glpoint():
    r = Render()
    t = Texture()

    r.glCreateWindow(500,500)

    r.glClearColor(0,0,0) #parametros en rango de 0 a 1
    r.glClear()

    r.glViewPort(0,0,500,500) 

    r.glColor(1,1,1) #parametros en rango de 0 a 1
    
    r.lookAt(eye=[0,0,1],center=[0,0,0],up=[0,1,0])

    r.stars()

    #------------------ORIGINAL
    r.active_shader = r.shader
    r.glLoad('./models/sphere.obj', translate=(-1,-1,0), scale=(5,5,5), rotate=(0,0,0))
    r.draw('TRIANGLES')

    r.active_shader = r.shader2
    r.glLoad('./models/Ring.obj', translate=(-1,-1.3,0), scale=(3.3,2,3.3), rotate=(0,0,0))
    r.draw('RANDOM')

    r.active_shader = r.shader2
    r.glLoad('./models/Ring.obj', translate=(-0.95,-1.35,0), scale=(3.3,2,3.3), rotate=(0,0,0))
    r.draw('RANDOM')

    r.active_shader = r.shader2
    r.glLoad('./models/Ring.obj', translate=(-1.05,-1.25,0), scale=(3.3,2,3.3), rotate=(0,0,0))
    r.draw('RANDOM')

    r.glFinish()

glpoint()


