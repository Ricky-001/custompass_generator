#!/usr/bin/python3
import random, os
from .statics import color
from time import sleep

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

##########################################################################################################################

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
  |  The script automatically searches for songs and their lyrics        |
  |  based on the artist names provided (if any song exists) and adds    |
  |  the lyrics as some of the passphrases to be used against the target |
  |     {}[Ensure network connection for this feature to work]{}             |
  |                                                                      |
  |  You can choose to transform the basic details as follows:-          |
  |   * Case transformations  : {}mYpAsSwOrD{}                               |
  |   * Leet transformations  : {}my1337P@$$w0rd{}                           |
  |   * Space transformations : {}my_Secret-Password{}                       |
  |  {}Note:-{} {}If you choose to enable Case Transformations,{}                |
  |         {}the cases of your input will not matter, and all cases{}       |
  |         {}will be used, otherwise, words will be formed using only{}     |
  |         {}the cases in which the input is provided{}                     |
  |                                                                      |
  |                                             created by ~ {}Ricky-001{}   |
  |                   {}{}https://github.com/Ricky-001/custompass_generator{}  |
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""".format(color.PURPLE,color.END, color.ORANGE,color.END, color.YELLOW,color.ORANGE,color.END, color.YELLOW,color.END, color.RED,color.END, color.RED,color.END, color.RED,color.END, color.PURPLE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.ORANGE,color.END, color.GREEN,color.END, color.BLUE,color.UNDERLINE,color.END)


def show():
  show = random.randint(0, 4)

  if show==0:
    for line in banners[show].split('\n'):
      print(color.BLUE + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==1:
    for line in banners[show].split('\n'):
      print(color.YELLOW + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==2:
    for line in banners[show].split('\n'):
      print(color.GREEN + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==3:
    for line in banners[show].split('\n'):
      print(color.RED + color.BOLD + line + color.END)
      sleep(0.05)
  elif show==4:
    for line in banners[show].split('\n'):
      print(color.CYAN + color.BOLD + line + color.END)
      sleep(0.05)

  for line in help_banner.split('\n'):
    print(line)
    sleep(0.03)
  sleep(1)