import os
# use os to call these commands
# git clone https://github.com/ArtLabss/open-data-anonimizer.git
# cd open-data-anonimizer
# pip install -r requirements.txt
# make bootstrap
# pip install cape-privacy==0.3.0 --no-deps

os.system("git clone https://github.com/ArtLabss/open-data-anonimizer.git")
# os.system("cd open-data-anonimizer")
os.system("pip install -r open-data-anonimizer/requirements.txt")
os.system("cd open-data-anonimizer")
os.system("make bootstrap")
os.system("pip install cape-privacy==0.3.0 --no-deps")