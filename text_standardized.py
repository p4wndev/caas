import re
import hashlib

def remove_special_chars(string):
  pattern = r'[*,/:,?\'",<>|]'
  return re.sub(pattern, '', string)

def encode_string(string):
    hashed_string = hashlib.sha256(string.encode()).hexdigest()
    return hashed_string[:255]