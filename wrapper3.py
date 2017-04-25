import os
text = raw_input('Enter the Text you want to speak\n')
speak= "espeak -s 125 -v en+m3 -p 25 '" + text  + "'"
os.system(speak)