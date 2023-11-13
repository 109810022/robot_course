import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

#建立ImageSubscriber物件，作為接收圖片端
class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber') #繼承，初始化
    #建立接收端節點
    self.subscription = self.create_subscription(
      Image, 
      'img', 
      self.listener_callback, 
      10)
    self.br = CvBridge()#建立資料轉換橋梁(因為ROS2及cv2讀取、儲存圖片格式不一樣)
   
  def listener_callback(self, data):#建立callback函式(當收到訊息時觸發)
    self.get_logger().info('Receiving image')#輸出接收到訊息
    #將cv2讀取的圖片轉換成ROS2格式，並顯示在螢幕上 
    current_frame = self.br.imgmsg_to_cv2(data)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(0)
  
def main(args=None):
  rclpy.init(args=args)#初始化
  image_subscriber = ImageSubscriber()#實體化pub
  rclpy.spin(image_subscriber) #等待接收訊息

  
if __name__ == '__main__':
  main()
