import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

#建立ImagePublisher物件，作為發送圖片端
class ImagePublisher(Node):
  def __init__(self):
    super().__init__('image_publisher') #繼承，初始化
    self.publisher_ = self.create_publisher(Image, 'img', 10) #建立發送端節點
    self.br = CvBridge() #建立資料轉換橋梁(因為ROS2及cv2讀取、儲存圖片格式不一樣)

  def pub(self,img_root:str='test.jpg'):#定義物件動作(傳送訊息)
    #將圖片路徑初始定義為"test.py"
    self.cap = cv2.imread(img_root) #讀取路徑上的圖片
    self.publisher_.publish(self.br.cv2_to_imgmsg(self.cap)) #將cv2讀取的圖片轉換成ROS2格式，並發送  

def main(args=None):
  rclpy.init(args=args)#初始化
  image_publisher = ImagePublisher() #實體化pub
  image_publisher.pub() #發送訊息
  rclpy.spin(image_publisher) #等待發送訊息
  
  
if __name__ == '__main__':
  main()
