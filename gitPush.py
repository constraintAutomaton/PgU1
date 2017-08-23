import os
import pexpect

message = input('entrez le message du commit: ')
os.system('cd /home/pi/Documents/Python_project/PgU1_code\ngit add .\ngit commit -m"{}"\ngit push orgin master'.format(message)) 
git.send('git add .')
git.send('git commit -m"{}"'.format(message))
git.send('git push orgin master')
