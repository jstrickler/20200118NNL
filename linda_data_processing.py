

# 1. read master input info dict of config info
#      make changes to master input file as needed using REs

# 2. for each input file:
#       compose command line
        "C:\someapp\bin\myprogram.exe file_name option option ..."
#       use os.popen(to run external cmd with input file and get the output)

