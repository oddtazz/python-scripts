#!/usr/bin/python
import os

def whois(domain):
  info = os.system('/usr/bin/whois domain 1&2>> /home/gaurav/result.txt')

wordlist = raw_input("Enter the full path of the wordlist for whois: \n")
f = open(wordlist, mode="r")
while 1:
  line = f.readline()
  domain = line[0:-3] + ".in"
  print line.rstrip('\n') + " = " + domain
  print whois(domain)
  if not line:
    break
  pass

exit()
