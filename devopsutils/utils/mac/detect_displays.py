import subprocess
import shlex


#todo: move this to devops-utils
def _run_command(cmd):

  args = shlex.split(cmd) 
  pipe = subprocess.Popen(args, stdout=subprocess.PIPE)

  return pipe.communicate()


if __name__ == "__main__":

  command = 'defaults read /Library/Preferences/com.apple.windowserver.plist' 

  print _run_command(command)

  
  
 

