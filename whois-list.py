#!/usr/bin/python
import whois

wordlist = raw_input("Enter the full path of the wordlist for whois: \n")
f = open(wordlist, mode="r")
while 1:
  line = f.readline()
  domain = line[0:-3] + ".in"
  print line.rstrip('\n') + " = " + domain
  try:
    info = whois.query(domain)
  except:
    print domain + " Might not be registred"
  if not line:
    break
  pass

exit()
