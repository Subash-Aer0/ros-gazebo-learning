import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class DriveLog(Node):

    def __init__(self):
        super().__init__("DriveLog")

        self.subscriber = self.create_subscription(
            String, "vel", self.listener_callback, 10
        )

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):

    rclpy.init(args=args)

    drivelog = DriveLog()
    rclpy.spin(drivelog)

    drivelog.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
