import os
import subprocess
INITIAL_PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def startproject(projectname):
    print("Creating project...")
    subprocess.call(["cp", "-r", os.path.join(INITIAL_PROJECT_PATH, "../startproject/"), "."])
    subprocess.call(["mv", "startproject", projectname])
    print("Project creation successful!")

def main(argv):
    if argv[1] == "startproject":
        startproject(argv[2])
    else:
        print("Please enter a valid command.  So far startproject is the only one.")
    return 0

if __name__=="__main__":
    import sys
    code = main(sys.argv)
    sys.exit(code)
