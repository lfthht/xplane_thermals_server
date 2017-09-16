"""
Thermal simulator  Ver .03  
  ** Works on Xplane 10.30 and above only **
  
  The plugin then reads the lift value of the plane current position and applies
  the lift & roll values. 
  
  Author: Alex Ferrer
  License: GPL 
"""
import urllib2

readvars = urllib2.urlopen("http://www.lufthoheit.com/Clients/xplane/python_test.py").read()

stringvars = map(str.strip, readvars.split(','))
var1 = float(stringvars[0])
var2 = float(stringvars[1])
var3 = bool(stringvars[2])
var4 = float(stringvars[3])
var5 = int(stringvars[4])
var6 = stringvars[5]