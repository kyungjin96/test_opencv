import rospy, cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import String
import numpy as np




rospy.init_node('planner_node')
bridge = CvBridge()
pub =rospy.Publisher('/motor_commands',String, queue_size=10)
di = True




def callback(data):


    cv2_img = bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2_img = cv2.cvtColor(cv2_img ,cv2.COLOR_BGR2GRAY)
    left_img = cv2_img[720:780,220:285]
    right_img = cv2_img[720:780,485:550]
    rr_img = cv2_img[730:792,740:792]
    ll_img = cv2_img[730:792,5:57]

    cv2.imshow('callback',cv2_img)
    key=cv2.waitKey(2)
 
    if np.all(left_img > 90) and np.all(right_img > 90):
        di='GO'
        pub.publish(di)
        rospy.sleep(0.01)
    elif np.all(left_img < 90) and np.all(right_img < 90):
        di='BACK'
        pub.publish(di)
        rospy.sleep(0.01)
    elif np.all(left_img > 90):
        di='LEFT'
        pub.publish(di)
        rospy.sleep(0.01)
    elif np.all(right_img > 85):
        di='RIGHT'
        pub.publish(di)
        rospy.sleep(0.01)
    elif np.all(rr_img>90):
        di='RIGHT'
        pub.publish(di)
        rospy.sleep(0.01)
    elif np.all(ll_img>90):
        di='LEFT'
        pub.publish(di)
        rospy.sleep(0.01)
        




def main():
    # rospy.init_node('planner_node')
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()

    


if __name__ == '__main__' :
    main()