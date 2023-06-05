import os

os.system("pip install webbot")

os.system("pip install selenium==3.141.0")

from webbot import Browser

web = Browser()
web.go_to('https://khedmatma.ir/')

