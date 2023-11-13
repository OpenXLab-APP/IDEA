import subprocess
import os

build_install_command = "cd models/UniPose/ops && python setup.py build install"
subprocess.run(build_install_command, shell=True, check=True)

home_directory = "/home/xlab-app-center/"
os.chdir(home_directory)

app_command = "python app-1.py"
subprocess.run(app_command, shell=True, check=True)
