def validBraces(string):
  s = ['()','[]','{}']
  if s[0] in string:
      string = string.replace(s[0], '')
      if string:
          return validBraces(string)
      else:
          return True
  elif s[1] in string:
      string = string.replace(s[1], '')
      if string:
          return validBraces(string)
      else:
          return True
  elif s[2] in string:
      string = string.replace(s[2], '')
      if string:
          return validBraces(string)
      else:
          return True
  else:
      return False