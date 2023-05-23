from sensor_msgs.msg import LaserScan
import numpy as np

class Lidar():
    def __init__(self, node):
        self.ranges_ = []

        self.subscription_ = node.create_subscription(
            msg_type=LaserScan,
            topic='/scan',
            callback=self.lidar_callback,
            qos_profile=10
        )
        
    def lidar_callback(self, msg):
        self.ranges_ = msg.ranges
        print("Ranges: ", self.ranges_)
        
    def margem_de_segurança(self):
        frente_primeiro_quadrante = np.array(self.ranges_[0:8]) 
        frente_segundo_quadrante = np.array(self.ranges_[352:359])
        return np.concatenate([frente_primeiro_quadrante, frente_segundo_quadrante])
    
    def margem_segura(self):
        print("Margem de segurança: ", self.margem_de_segurança())
        print("Margem segura", len(set(self.margem_de_segurança())))
        if len(set(self.margem_de_segurança())) == 1:
            return True
        else:
            return False
