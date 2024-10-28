import os
from urllib.request import urlretrieve
import re
import math
import urllib

# References:
# https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories
# https://realpython.com/python-download-file-from-url/

ERROR_TOLERANCE = 5

def download_files(url, dest_folder='./default/'):
  if url is None or "".__eq__(url.strip()):
    print("No url has been provided! Exiting...")
    return
  
  if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

  # Find the base filename:
  filename = url.split('/')[-1]
  next_filename = filename
  base_url = url.split(filename)[0]

  # Find out the extension:
  extension = '.' + filename.split('.')[-1]
  
  # Build the full url with the next filename (for now it's just the first filename):
  full_url = base_url + next_filename

  # Build the full filename with the destination folder to save:
  full_filename_path_to_save = dest_folder + '/' + next_filename

  # Download the first file:
  try:
    file, header = urlretrieve(full_url, full_filename_path_to_save)
    print(f"Successfully downloaded {full_url} and saved as {full_filename_path_to_save}")
    # print(file)
    # print(header)
  except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, IOError):
    print(f"Failed to download {full_url}!")
  
  # Now check if the filename contains the numeric sequence:
  base_seq = re.findall(r"[0-9]+", filename.lower())
   
  if len(base_seq) == 0:
    print("No numeric sequence found! Nothing else to download!")
  elif len(base_seq) == 1:
    num_seq = base_seq[0]
    len_num_seq = len(num_seq)
    base_filename = filename.split(num_seq)[0]
    num = int(num_seq)
    next_num = num + 1
    
    # Start downlaoding the sequence of files.
    error_count = 0
    while (next_num < pow(10, len_num_seq) and error_count <= ERROR_TOLERANCE):
      # Now build the next filename in the sequence.
      leading_zeros = len_num_seq - int(math.log10(next_num)) - 1
      next_num_str = '0' * leading_zeros + str(next_num)
      next_filename = base_filename + next_num_str + extension

      # Build the full url with the filename:
      full_url = base_url + next_filename

      # Build the full filename with the destination folder to save:
      full_filename_path_to_save = dest_folder + '/' + next_filename
      
      # Download the next file:
      try:
        file, header = urlretrieve(full_url, full_filename_path_to_save)
        print(f"Successfully downloaded {full_url} and saved as {full_filename_path_to_save}")
        # print(file)
        # print(header)
      except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, IOError):
        print(f"Failed to download {full_url}!")
        error_count += 1
      
      # Increment the file number:
      next_num += 1

    print("Nothing more to downlaod! Good bye!")

URL = (
        "https://api.worldbank.org/v2/en/indicator/"
        "NY.GDP.MKTP.CD?downloadformat=csv"
      )

# commands used in solution video for reference
if __name__ == '__main__':
    # download_files(URL, './data')
    download_files('http://699340.youcanlearnit.net/image001.jpg', './images')