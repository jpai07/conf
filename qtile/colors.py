import json
import os
from colorschemes import *

# path = os.path.expanduser('~/.config/qtile/colorschemes/blaze.json')
path = os.path.expanduser('~/.config/qtile/colorschemes/ghost.json')
# path = os.path.expanduser('~/.config/qtile/colorschemes/reaper.json')
# path = os.path.expanduser('~/.config/qtile/colorschemes/nord.json')

with open(path, 'r') as file:
    color = json.load(file)
    file.close()