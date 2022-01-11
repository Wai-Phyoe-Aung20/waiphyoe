from netmiko import ConnectHandler
from getpass import getpass
import time 
from datetime import datetime

user_list={'Admin':'pwd-admin'}
tempt=0
while tempt<3:
   username=input("Type your name here:>>")
   password=input("Type your password here:>>")
      
   if password==user_list['Admin']:
      username=input ('Enter Username:>> ')
      password=getpass()

      R01={'host':'192.168.114.5','username':username,'password':'admin','device_type':'cisco_ios'}
      cmd=ConnectHandler(**R01)
      print (cmd.find_prompt())
      config_cmd=cmd.send_command('show version')
      print (config_cmd)
      break
   else:
      print ("Type Again===>")
      tempt+=1
 

