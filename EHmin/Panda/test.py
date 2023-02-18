from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import BoundingSphere
from panda3d.core import LPoint3
from panda3d.core import CollisionSphere, CollisionNode

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        

        # Load the environment model. 
        # self.boat = self.loader.loadModel("avikus_boat.gltf")s
        
        # #load Boat map
        # self.boat = self.loader.loadModel("avikus_boat.glb")
        # self.boat.reparentTo(self.render)
        
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms aon the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        
        
        # self.sphere = BoundingSphere(LPoint3(10,10,10), 10)
        # self.sphere.reparentTo(self.render)
        

app = MyApp()
app.run()