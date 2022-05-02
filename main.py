import os
import sys
import trim.trim as trim

# get input argument
srcdir = str(sys.argv[1])
print(f"Renaming in {srcdir}")

for file in os.listdir(srcdir):
  # trim timestamp from file name
  dstfile = trim.file(file)  
  # rename file
  os.rename(f'{srcdir}/{file}',f'{srcdir}/{dstfile}')

print(os.listdir(srcdir))
