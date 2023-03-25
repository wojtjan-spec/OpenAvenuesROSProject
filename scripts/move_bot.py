import rospy 
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('publisher')
    pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)
    rate = rospy.Rate(10)
    move = Twist()
    move.linear.x = 0.5
    move.angular.z = 0.5

    while not rospy.is_shutdown():
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptEXception:
        pass
