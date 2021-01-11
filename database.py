import os
import pickle
from datetime import datetime
from typing import Dict

# class datapt:
#     timestamp: datetime = None,
#     value = 0.0

#     def __init__(self, timestamp: datetime, value: float):
#         self.timestamp = timestamp
#         self.value = value
    
#     def str(self):
#         return '(' + self.timestamp.strftime('%H:%M:%S') + ', ' \
#                 + str(self.value) + ')'

class database:
    filename = ""

    def __init__(self, filename: str):
        self.filename = filename
        if not os.path.exists(filename):
            #create the file
            print("creating " + filename)
            file = open(filename, 'wb')
            pickle.dump({'null': {datetime.now(): 0.0}}, file)
            file.close()
        # file = open(filename, 'r')
        # text = file.read()
        # self.json = json.loads(text)
        # file.close
    
    def add_datapt(self, itemname: str, timestamp: datetime, value: float):
        alldata = self.get_all_data()
        if not itemname in alldata:
            alldata[itemname] = {}
        alldata[itemname][timestamp] = value
        outfile = open(self.filename, 'wb')
        pickle.dump(alldata, outfile)
        outfile.close()
    
    def get_all_data(self):
        file = open(self.filename, 'rb')
        alldata = pickle.load(file)
        file.close()
        return alldata
    
    def get_item_data(self, itemname: str) -> Dict[datetime, float]:
        alldata = self.get_all_data()
        return alldata[itemname]