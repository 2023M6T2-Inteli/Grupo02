from sensor_msgs.msg import LaserScan
import numpy as np

class Lidar():
    def __init__(self, node):
        self.ranges_ = []
        self.permission = True
        
        self.subscription_ = node.create_subscription(
            msg_type=LaserScan,
            topic='/scan',
            callback=self.lidar_callback,
            qos_profile=10
        )
        
    # Recebe o array de distâncias do Lidar
    def lidar_callback(self, msg):
        self.ranges_ = msg.ranges
        # print("Ranges: ", self.ranges_)
        
    # Cria a margem de segurança
    def safety_margin(self):
        front_first_quadrant = np.array(self.ranges_[0:19])
        front_second_quadrant = np.array(self.ranges_[341:360])
        return np.concatenate([front_first_quadrant, front_second_quadrant])
    
    # Faz o Lidar parar de funcionar
    def kill_lidar(self):
        self.permission = False
    
    # Verifica se o turtlebot encontrou algum objeto na margem de segurança
    def check_safety_margin(self):
        # print("Margem de segurança: ", self.margem_de_segurança())
        # print("Margem segura", len(set(self.margem_de_segurança())))
        # Pra saber se tem algo na margem de segurança, precisamos verificar se há algum número dentro do array de segurança menor do que 30 cm (0.3)
        for i in self.safety_margin():
            if i < 0.3 and self.permission:
                return False
        return True
