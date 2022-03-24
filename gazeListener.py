import os
import time
import xml.etree.ElementTree as ET
import json
import re
import lxml
from opengaze import OpenGazeTracker
from std_msgs.msg import String, Float64MultiArray
import rospy
import numpy as np



class EyeGazeListener():

    # Construct the path to the log file.
    DIRNAME = os.path.dirname(os.path.abspath(__file__))
    FNAME = os.path.join(DIRNAME, '%s.tsv' % (time.strftime("%Y-%m-%d_%H-%M-%S")))

    def __init__(self):
        
        self.tracker = OpenGazeTracker(logfile=self.FNAME, debug=False, callback=self.onMessage)
        time.sleep(1.0)
        self.pub = rospy.Publisher('gazeTracker', Float64MultiArray, queue_size = 10)
        rospy.init_node('talker', anonymous=True)
        self.rate = rospy.Rate(50) # 50hz
        self.gaze_list = ['TIME', 'LPOGX', 'LPOGY', 'LPOGV', 'RPOGX', 'RPOGY', 'RPOGV', 'BPOGX', 'BPOGY', 'BPOGV']

        self.tracker.start_recording()

    def talker(self, data):
        rospy.loginfo(data)
        self.pub.publish(data)
        self.rate.sleep()

    def onMessage(self, e):

        self.data = e
        gaze_array = []
        for key in self.gaze_list:
            gaze_array.append(np.nan if self.data[key] == 'nan' else float(self.data[key]))

        Gaze_data = Float64MultiArray()
        Gaze_data.data = gaze_array
        self.talker(Gaze_data)    

def main():

    egl = EyeGazeListener()


if __name__=="__main__":
    main()
