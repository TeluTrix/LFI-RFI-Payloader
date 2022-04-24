import requests
import re
import sys
import os

urls = []
payloads = []

print("LFI/RFI Payload Loader - github.com/TeluTrix/LFI-RFI-Payloader")

#Get Paths
urlsPath = input("Drag the urls file in / or enter its path: ")
payloadsPath = input("Drag the payloads file in / or enter its path: ")

#Get urls in an array
urlsFile = open(urlsPath, "r")
urls = urlsFile.readlines()

#Get payloads in an array
payloadsFile = open(payloadsPath, "r")
payloads = payloadsFile.readlines()

print("[" + str(len(urls)) + "] - Urls Loaded")
print("[" + str(len(payloads)) + "] - Payloads Loaded")