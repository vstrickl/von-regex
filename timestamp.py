import re

with open('transcripts/Mom_2023_Clip-1.txt') as f:
    fin = f.read()
  
z = re.sub(pattern="\d{2};\d{2};\d{2};\d{2}\s-\s\d{2};\d{2};\d{2};\d{2}",repl="", string=fin)
print(z)
