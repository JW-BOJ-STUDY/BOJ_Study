
from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeomVertexData, Geom, GeomVertexWriter, GeomTriangles, GeomNode, LVector3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # GeomVertexData를 만듭니다.
        vdata = GeomVertexData('sphere', self.vertexFormat, Geom.UHStatic)

        # GeomVertexWriter를 사용하여 버텍스 데이터를 추가합니다.
        vertex = GeomVertexWriter(vdata, 'vertex')
        texcoord = GeomVertexWriter(vdata, 'texcoord')
        normal = GeomVertexWriter(vdata, 'normal')
        for i in range(0, 32):
            angle1 = i / 16.0 * 3.14159
            z = 0.5 * math.sin(angle1)
            r = 0.5 * math.cos(angle1)
            for j in range(0, 16):
                angle2 = j / 8.0 * 3.14159
                x = r * math.sin(angle2)
                y = r * math.cos(angle2)
                vertex.addData3f(x, y, z)
                texcoord.addData2f(i / 16.0, j / 8.0)
                normal.addData3f(x, y, z)

        # GeomTriangles를 사용하여 인덱스 데이터를 추가합니다.
        triangles = GeomTriangles(Geom.UHStatic)
        for i in range(0, 31):
            for j in range(0, 15):
                p1 = i * 16 + j
                p2 = i * 16 + j + 1
                p3 = (i + 1) * 16 + j
                p4 = (i + 1) * 16 + j + 1
                triangles.addVertices(p1, p2, p3)
                triangles.addVertices(p2, p4, p3)
        triangles.closePrimitive()

        # Geom을 생성하고, GeomTriangles를 추가합니다.
        geom = Geom(vdata)
        geom.addPrimitive(triangles)

        # GeomNode를 생성하고, 해당 노드에 Geom을 추가합니다.
        node = GeomNode('sphere')
        node.addGeom(geom)

        # 구체를 표시하기 위해 NodePath를 생성합니다.
        np = self.render.attachNewNode(node)

        # 구체를 렌더링합니다.
        np.setTwoSided(True)
        np.setTransparency(1)
        np.setAlphaScale(0.7)
        np.setColor(1, 0, 0, 1)
        np.setPos(0, 0, 0)
        np.reparentTo(self.render)

app = MyApp()
app.run()