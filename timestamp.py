import re

f = open('transcripts/Mom_2023_Clip-1.txt')
fin = f.read()
  
z = re.sub(pattern="\d{2};\d{2};\d{2};\d{2}\s-\s\d{2};\d{2};\d{2};\d{2}",repl="", string=fin)
print(z)