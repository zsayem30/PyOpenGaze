import os
import time
import xml.etree.ElementTree as ET
import json
import re
import lxml
from std_msgs.msg import String
from opengaze import OpenGazeTracker

from std_msgs.msg import String
 

class EyeGazeListner():

    # Construct the path to the log file.
    DIRNAME = os.path.dirname(os.path.abspath(__file__))
    FNAME = os.path.join(DIRNAME, '%s.tsv' % (time.strftime("%Y-%m-%d_%H-%M-%S")))

    def __init__(self):
        self.tracker = OpenGazeTracker(logfile=self.FNAME, debug=False, callback=self.onMessage)
        time.sleep(1.0)

        # CALIBRATION
        # # Reset the calibration to its default points.
        # tracker.calibrate_reset()
        # # Start the calibration.
        # tracker.calibrate_start(True)positionalon_result()
        # 	time.sleep(0.1)

        # Start the streaming of data.
        self.tracker.start_recording()

        # Stop the streaming of data.
        self.tracker.stop_recording()

        # Close the connection.
        self.tracker.close()


    def onMessage(self, e):
        # print(type(e))

        
        # print(type(e.get("CNT")))
    
        # print(e.keys())

        self.data = e
    
        # print(self.data['CNT'])
        # print(json.dumps(self.data, sort_keys=True, indent=4))

   
    def getEyeGaze(self):

        return self.data
        
    # def getCount(self):

    #     try:
    #         return self.data["CNT"]

    #     except Exception as e:
            
    #         return None



def main():
    egl = EyeGazeListner()
    # print(egl.getEyeGaze())

if __name__=="__main__":
    main()
