
def file(inputfile: str):

  split_char = '(2'
  # Strip timestamp out and concat file name and extension
  file_name = inputfile.split(split_char)[0].rstrip()
  if not inputfile == file_name:
    file_ext = inputfile.split(split_char)[1].split('.')[1]
    return f'{file_name}.{file_ext}'
  return f'{file_name}'
