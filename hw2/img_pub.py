import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

class ImagePublisher(Node):
  def __init__(self):
    super().__init__('image_publisher')
    self.publisher_ = self.create_publisher(Image, 'img', 10)
    self.br = CvBridge()

  def pub(self,img_root:str = 'test.jpg'):
    self.cap = cv2.imread(img_root)
    self.publisher_.publish(self.br.cv2_to_imgmsg(self.cap))  

def main(args=None):
  rclpy.init(args=args)
  image_publisher = ImagePublisher()
  image_publisher.pub()
  rclpy.spin(image_publisher)
  
  
if __name__ == '__main__':
  main()
