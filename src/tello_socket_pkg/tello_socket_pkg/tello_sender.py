#!/usr/bin/env python3
import rclpy
import socket
from rclpy.node import Node
from std_msgs.msg import String

 
 
class UDPSender(Node): 
    def __init__(self):
      super().__init__("udp_sender") 
      self.suscriber_=self.create_subscription(String,'drone_command',self.command_callback,10)
      self.UDP_IP = '192.168.10.1'
      self.UDP_PORT=8889
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      
    def command_callback(self,msg):
        self.sock.sendto(msg.data.encode(),(self.UDP_IP, self.UDP_PORT))
        self.get_logger().info(f'Sent command: {msg.data}')
       
      
 
 
def main(args=None):
    rclpy.init(args=args)
    udp_sender = UDPSender() 
    rclpy.spin(udp_sender)
    udp_sender.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
