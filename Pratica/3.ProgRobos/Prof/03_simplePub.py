#! /usr/bin/python3

# Importação da biblioteca ROS para Python
import rospy
# Importação da biblioteca de mensagens padrões
from std_msgs.msg import Int32

# Criação do nó com o nome simple_publisher
rospy.init_node('simple_publisher')

# Criação do publisher no topic counter duma variável de tipo Int32
pub = rospy.Publisher('counter', Int32, queue_size=1)

# Definição da frequência do laço while
rate = rospy.Rate(2)

count = 0

# Em loop até a detecção de Ctrl+c
while not rospy.is_shutdown():

    # Publicação da mensagem no topico
    pub.publish(count)

    count += 1
    # Esperar pelo fim do tempo do laço
    rate.sleep()
