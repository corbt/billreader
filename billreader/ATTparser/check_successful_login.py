import subprocess
username = "8013680555"
password = "Stak3smarin3r"
file_output_name = "my_last_bill"


check_successful_download = int(subprocess.check_output(["./att_bill_retriever.sh", username, password, file_output_name]))
    
if check_successful_download == 200:
    print "your username and password are correct and your bill has been downloaded"
else:
    print "your username and password are not correct and your bill has not been downloaded"