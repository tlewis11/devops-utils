import sys
import subprocess
import shlex

def run_bash_command(command, stdin=None):

  if stdin is not None:
    raise('stdin not yet implemented')  

  args = shlex.split(command)
  pipe = subprocess.Popen(args, stdout=subprocess.PIPE)

  return pipe.communicate()



if __name__ == '__main__': 
   
  command = sys.argv[1]

  print run_bash_command(command)
