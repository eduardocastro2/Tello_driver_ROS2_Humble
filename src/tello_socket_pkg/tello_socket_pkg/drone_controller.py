#!/usr/bin/env python3
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String

class DroneController(Node): 
    def __init__(self):
      super().__init__("drone_controller") 
      self.publisher_=self.create_publisher(String,'drone_command',10)
      time.sleep(1)
      
    def send_commands(self):
        self.publisher_.publish(String(data='command'))
        time.sleep(1)
        self.publisher_.publish(String(data='takeoff'))
        time.sleep(10)
        self.publisher_.publish(String(data='land'))
        time.sleep(5)
 
 
def main(args=None):
    rclpy.init(args=args)
    drone_controller = DroneController() 
    drone_controller.send_commands()
    drone_controller.destroy_node()
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
