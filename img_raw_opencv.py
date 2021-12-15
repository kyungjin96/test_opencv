import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Float64
from cv_bridge import CvBridge
import sys
bridge = CvBridge()
rospy.init_node('img_raw_opencv')
left_pub= rospy.Publisher('/right_wheel_controller/command',Float64, queue_size=10 )
right_pub= rospy.Publisher('/left_wheel_controller/command',Float64, queue_size=10 )
left_dir = 0.0
right_dir = 0.0

def gogo():
    left_dir = 0.5
    right_dir = 0.5
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return

def stop():
    left_dir = 0.0
    right_dir = 0.0
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return

def back():
    left_dir = -0.7
    right_dir =-0.7
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return
def left():
    left_dir = -0.3
    right_dir =0.5
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return
def right():
    left_dir = 0.5
    right_dir =-0.3 
    left_pub.publish(left_dir)
    right_pub.publish(right_dir)
    rospy.sleep(0.01)
    return


def callback(data):

    cv2_img = bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2.imshow('callback',cv2_img)
    key=cv2.waitKey(1)
    
    if key == ord('w'):
        gogo()
    elif key == ord('x'):
        stop()
    elif key == ord('s'):
        back()
    elif key == ord('a'):
        left()
    elif key == ord('d'):
        right()
    else :
        sys.exit
           




if __name__ == '__main__' :
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()
         

