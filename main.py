import os

os.system("pip install webbot")

from webbot import Browser

web = Browser()
web.go_to('https://khedmatma.ir/')

