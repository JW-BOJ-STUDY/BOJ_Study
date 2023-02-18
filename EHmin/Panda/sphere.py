from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Geom, GeomVertexData, GeomVertexFormat, GeomVertexWriter
from panda3d.core import GeomTriangles, GeomNode
from panda3d.core import Point3
import math

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # 구체의 반지름과 분할 수를 정의합니다.
        radius = 1
        subdivisions = 32

        # 구체의 정점 데이터를 생성합니다.
        format = GeomVertexFormat.getV3()
        vdata = GeomVertexData('sphere', format, Geom.UHStatic)
        vertex = GeomVertexWriter(vdata, 'vertex')
        for i in range(subdivisions):
            for j in range(subdivisions):
                theta = (i / subdivisions) * 2 * math.pi
                phi = (j / subdivisions) * math.pi
                x = radius * math.sin(phi) * math.cos(theta)
                y = radius * math.sin(phi) * math.sin(theta)
                z = radius * math.cos(phi)
                vertex.addData3f(x, y, z)

        # 구체의 삼각형 데이터를 생성합니다.
        tris = GeomTriangles(Geom.UHStatic)
        for i in range(subdivisions):
            for j in range(subdivisions):
                a = i * subdivisions + j
                b = (i + 1) % subdivisions * subdivisions + j
                c = i * subdivisions + (j + 1) % subdivisions
                tris.addVertices(a, b, c)
                tris.closePrimitive()

                a = (i + 1) % subdivisions * subdivisions + j
                b = (i + 1) % subdivisions * subdivisions + (j + 1) % subdivisions
                c = i * subdivisions + (j + 1) % subdivisions
                tris.addVertices(a, b, c)
                tris.closePrimitive()

        # 구체의 노드를 생성하고, 삼각형과 정점 데이터를 추가합니다.
        geom = Geom(vdata)
        geom.addPrimitive(tris)
        node = GeomNode('sphere')
        node.addGeom(geom)

        # 구체를 렌더링합니다.
        sphere = self.render.attachNewNode(node)
        sphere.set_color(1,0,0,1)
        sphere.setPos(0,0,0)
        sphere.setTwoSided(True)
        
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms aon the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        
        # self.camera.setPos(0, 0, 10)
        # self.camera.lookAt(0, 0, 0)

app = MyApp()
app.run()
