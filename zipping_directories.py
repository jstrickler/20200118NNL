import shutil

shutil.make_archive("myfiles", "zip", 'DATA')
shutil.make_archive("myfiles", "tar", 'DATA')
shutil.make_archive("myfiles", "gztar", 'DATA')
