#!/usr/bin/python3
import random, os
from time import sleep
from colors import color

# clear screen
def clear():    
    os.system(['clear', 'cls'][os.name == 'nt'])



banners = []

banner_1 = \
"""
_________________________________________________________________________
 ╔═╗┬ ┬┌─┐┌┬┐┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┬  ┬┌─┐┌┬┐  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
 ║  │ │└─┐ │ │ ││││  ╠═╝├─┤└─┐└─┐│  │└─┐ │   ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
 ╚═╝└─┘└─┘ ┴ └─┘┴ ┴  ╩  ┴ ┴└─┘└─┘┴─┘┴└─┘ ┴   ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

banners.append(banner_1)

banner_2 = \
"""
   _   _   _   _   _   _     _   _   _   _   _   _   _   _     _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( C | u | s | t | o | m ) ( P | a | s | s | l | i | s | t ) ( G | e | n | e | r | a | t | o | r )
  \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""

banners.append(banner_2)

banner_3 = \
"""
_____________________________________________________________________________________________________________________
 ____ _  _ ____ ___ ____ _  _     ___  ____ ____ ____ _    _ ____ ___    ____ ____ _  _ ____ ____ ____ ___ ____ ____ 
 |    |  | [__   |  |  | |\/|     |__] |__| [__  [__  |    | [__   |     | __ |__  |\ | |__  |__/ |__|  |  |  | |__/
 |___ |__| ___]  |  |__| |  |     |    |  | ___] ___] |___ | ___]  |     |___]|___ | \| |___ |  \ |  |  |  |__| |  \ 
_____________________________________________________________________________________________________________________
"""

banners.append(banner_3)

banner_4 = \
"""
 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |C|u|s|t|o|m| |P|a|s|s|l|i|s|t| |G|e|n|e|r|a|t|o|r|
 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
"""

banners.append(banner_4)

banner_5 = \
"""
 ______________________________________________________________________________________________________________________
|   ____          _                    ____               _ _     _      ____                           _              |
|  / ___|   _ ___| |_ ___  _ __ ___   |  _ \ __ _ ___ ___| (_)___| |_   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  |
| | |  | | | / __| __/ _ \| '_ ` _ \  | |_) / _` / __/ __| | / __| __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| |
| | |__| |_| \__ \ || (_) | | | | | | |  __/ (_| \__ \__ \ | \__ \ |_  | |_| |  __/ | | |  __/ | | (_| | || (_) | |    |
|  \____\__,_|___/\__\___/|_| |_| |_| |_|   \__,_|___/___/_|_|___/\__|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|    |
|______________________________________________________________________________________________________________________|

"""

banners.append(banner_5)



help_banner = \
"""
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  |  Provide details about the target like their name (first, mid, last) |
  |  dates of importance, and other significant words/ details           |
  |  related to their lives (like pet names, favourite role models, etc) |
  |                                                                      |
  |  You can leave any field empty for which details are not available   |
  |  (details fields) or you don't want to change the setting (settings) |
  |  {}Note:-{} {}The default values for the settings fields are{}               |
  |  {}highlighted{}, which will be used if you leave the fields empty{}       |
  |                                                                      |
  |  You can choose to transform the basic details as follows:-          |
  |   * Case transformations  : {}mYpAsSwOrD{}                               |
  |   * Leet transformations  : {}my1337P@$$w0rd{}                           |
  |   * Space transformations : {}my_Secret-Password{}                       |
  |  {}Note:-{} {}If you choose to enable Case Transformations,{}                |
  |         {}the cases of your input will not matter, and all cases will{}  |
  |         {}be used, otherwise, words will be formed using only{}          |
  |         {}the cases in which the input is provided{}                     |
  |                                                                      |
  |                                             created by ~ {}Ricky-001{}   |
  |                   {}{}https://github.com/Ricky-001/custompass_generator{}  |
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""".format(color.PURPLE,color.END, color.ORANGE,color.END, color.YELLOW,color.ORANGE,color.END, color.RED,color.END, color.RED,color.END, color.RED,color.END, color.PURPLE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.GREEN,color.END, color.BLUE,color.UNDERLINE,color.END)




show = random.randint(0, 4)
print(banners[show])

clear()
'''
for i in range(5):
  if i==0:
    print(color.BLUE + color.BOLD + banners[i] + color.END)
  elif i==1:
    print(color.YELLOW + color.BOLD + banners[i] + color.END)
  elif i==2:
    print(color.GREEN + color.BOLD + banners[i] + color.END)
  elif i==3:
    print(color.RED + color.BOLD + banners[i] + color.END)
  elif i==4:
    print(color.CYAN + color.BOLD + banners[i] + color.END)
'''

for line in banner_5.split('\n'):
  print(line)
  sleep(0.05)