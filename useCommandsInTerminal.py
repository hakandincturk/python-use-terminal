import os
import shlex
import subprocess
import sys
from colorama import init, Fore

# os.chdir('/Users/hakan')
init(autoreset=True)

commands = [
  ['clear'],
  ['pwd'],
  ['cd', '/Users/hakan'],
  ['pwd'],
  ['cd', 'code/mdp-projects/cimsa'],
  ['ls', '-la'],
  ['cd', 'cimsa-hr-portal-frontend'],
  ['git', 'checkout', 'dev'],
  ['git', 'pull', 'origin', 'dev'],
]

for i in commands:
  print(Fore.LIGHTCYAN_EX + 'COMMAND --> ' + str(i))
  try:
    if i[0] == 'cd':
      os.chdir(i[1])
    else:
      command = subprocess.call(i)
  except Exception as e:
    # print('an error: ', str(e))
    print(str(Exception(e)))
    break

