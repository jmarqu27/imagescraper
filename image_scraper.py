from bs4 import BeautifulSoup
import requests
import os

# Get URL from user
url = input("Enter the URL: ")

# reuests content from URL
webpage_response = requests.get(url)

# Parse HTML doc to BeautifulSoup object
webpage = webpage_response.text
soup = BeautifulSoup(webpage, "html.parser")

# Find all img tags on the webpage
images = soup.find_all("img")
# Print the list of img tags for visual
#print(images)



