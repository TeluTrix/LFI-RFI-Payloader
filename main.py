import requests
import re
import sys
import os

urls = []
payloads = []

print("LFI/RFI Payload Loader - google.com")

#Get Paths
urlsPath = input("Drag the urls file in: ")
payloadsPath = input("Drag the payloads file in: ")

#Get urls in an array
urlsFile = open(urlsPath, "r")
urls = urlsFile.readlines()

#Get payloads in an array
payloadsFile = open(payloadsPath, "r")
payloads = payloadsFile.readlines()