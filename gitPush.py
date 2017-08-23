import os

message = input('entrez le message du commit: ')
os.system('cd /home/pi/Documents/Python_project/PgU1_code\ngit add .\ngit commit -m"{}"\ngit push orgin master'.format(message)) 

