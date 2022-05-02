import os
import sys
import trim.trim as trim

def main():
  # get input argument
  srcdir = str(sys.argv[1])
  print(f"Trimming file names in {srcdir}")
  
  for file in os.listdir(srcdir):
    # trim timestamp from file name
    dstfile = trim.file(file)  
    # rename file
    os.rename(f'{srcdir}/{file}',f'{srcdir}/{dstfile}')
  
  print(os.listdir(srcdir))
  
if __name__ == '__main__':
  main()
