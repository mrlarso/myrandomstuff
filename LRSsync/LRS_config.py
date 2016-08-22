"""
LRS_Sync syncs xapi statments between two LRSs. Currently the functionality only exists to push
statements from one LRS (Local LRS) to another (Remote LRS)

Enter the correct information for the LRS below and run LRS_Sync.py to push statements
"""

# Source of statements
local_lrs_credentials = {
"endpoint":"http://lrs.tunapanda.org/data/xAPI/",
"username":"4429f0474aa7e82b23d73e2d6bfa59e634baeb56",
"password":"b7dd813c7ffe8bc92fe7edfa07943944857c0c1e"
}

#Destination of statements
remote_lrs_credentials = {
"endpoint":"http://lrs.tunapanda.org/data/xAPI/",
"username":"8337556b1002d3f86bbbe2011b5cd35afc2f18ab",
"password":"7dc75f0aee21c46ac4e62fd29fca48046b393190"
}

#Optional - only collect statements from local LRS if created in local LRS after date (YYYY-MM-DD):
#date = "2015-01-01"

#If using LRS_Save.py or LRS_Upload.py, choose the filename to write the statements to.
writefile = "localLRSstatements.json"

#If exporting statements to LRS from file, indicate the filename to read from.
readfile = "localLRSstatements.json"
