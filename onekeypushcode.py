import os

import os
import time


commit_log='"'+input('Enter commit log:')+'"'
os.system('git add .')
time.sleep(1)
os.system('git commit -m %s'%commit_log)
time.sleep(1)
os.system('git push origin master')