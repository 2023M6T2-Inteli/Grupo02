import rclpy
from sensor_msgs.msg import LaserScan
import numpy as np
import math

global_ranges = []

def margem_de_segurança():
    frente_primeiro_quadrante = np.array(global_ranges[0:8]) 
    frente_segundo_quadrante = np.array(global_ranges[352:359])
    return frente_primeiro_quadrante + frente_segundo_quadrante

def margem_segura():
    print("Margem segura", margem_de_segurança().all(math.inf))

# Função de callback para processar os dados do LIDAR
def lidar_callback(msg):
    # Acesse os dados do LIDAR
    ranges = msg.ranges
    global_ranges = ranges
    print("Esses são os ranges:", ranges)
    print("Margem de segurança: ", margem_de_segurança())
    

# Inicialize o nó ROS
rclpy.init()
node = rclpy.create_node('lidar_listener')

# Crie um assinante para o tópico do LIDAR
subscription = node.create_subscription(msg_type=LaserScan,
                                        topic='/scan',
                                        callback=lidar_callback,
                                        qos_profile=10)

# Mantenha o programa em execução
print("Rodando")
rclpy.spin(node)