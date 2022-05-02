
def file(inputfile: str):
  # Strip timestamp out and concat file name and extension
  file_name = inputfile.split('(')[0].rstrip()
  if not inputfile == file_name:
    file_ext = inputfile.split('(')[1].split('.')[1]
    return f'{file_name}.{file_ext}'
  return f'{file_name}'
