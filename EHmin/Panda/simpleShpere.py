from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionSphere, CollisionNode, Material, LVecBase4

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        def draw_sphere(self, center, radius):
            sphere = CollisionSphere(center[0], center[1], center[2], radius)

            # CollisionNode를 생성하고, 해당 노드에 CollisionSphere를 추가합니다.
            cnode = CollisionNode('sphere')
            cnode.addSolid(sphere)

            # 구체를 표시하기 위해 NodePath를 생성합니다.
            sphere_np = self.render.attachNewNode(cnode)
            sphere_np.setPos(center)

              # 구체를 렌더링합니다.
            mat = Material()
            mat.setDiffuse(LVecBase4(1, 0, 0, 1))  # 빨간색으로 변경

            # 구체에 Material 객체를 적용합니다.
            sphere_np.setMaterial(mat, 1)
            
            sphere_np.reparentTo(self.render)  # 구체를 루트 노드(render)에 추가합니다.
            sphere_np.show()

        # 구체의 중심점과 반지름을 지정합니다.
        
        center = (0, 0, 0)
        center2 = (1,1,1)
        radius = 1

        draw_sphere(self, center, radius)
        draw_sphere(self, center2, radius)
        self.camera.setPos(0, 0, 10)
        self.camera.lookAt(0, 0, 0)
        
        

app = MyApp()
app.run()

# from direct.showbase.ShowBase import ShowBase
# from panda3d.core import CollisionSphere, CollisionNode, Material, LVecBase4, DirectionalLight

# class MyApp(ShowBase):
#     def __init__(self):
#         ShowBase.__init__(self)
        
#         dlight = DirectionalLight('dlight')
#         dlnp = self.render.attachNewNode(dlight)
#         dlnp.setHpr(180, -20, 0)
#         self.render.setLight(dlnp)
        
#         # 구체의 중심점과 반지름을 지정합니다.
#         center = (0, 0, 0)
#         radius = 1

#         # CollisionSphere를 생성합니다.
#         sphere = CollisionSphere(center[0], center[1], center[2], radius)

#         # CollisionNode를 생성하고, 해당 노드에 CollisionSphere를 추가합니다.
#         cnode = CollisionNode('sphere')
#         cnode.addSolid(sphere)

#         # 구체를 표시하기 위해 NodePath를 생성합니다.
#         sphere_np = self.render.attachNewNode(cnode)
#         sphere_np.setBin("fixed", 0)
#         sphere_np.setTextureOff()
#         sphere_np.setPos(center)

#         # 구체의 색상을 변경하기 위해 Material 객체를 생성합니다.
#         mat = Material()
#         mat.setDiffuse(LVecBase4(1, 0, 0, 1))  # 빨간색으로 변경
#         # mat.setColor(1,0,0,1)

#         # 구체에 Material 객체를 적용합니다.
#         sphere_np.setMaterial(mat, 1)
#         sphere_np.set_color(1, 0, 0, 1)

#         # 구체를 렌더링합니다.
#         sphere_np.show()

#         # 빛을 추가합니다.

# app = MyApp()
# app.run()