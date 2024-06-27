from bs4 import BeautifulSoup
import requests
import os

def create_dir(images):
    """
    This function gets user input for a new directory for the images
    to be downloaded to, then calls the download_images function
    """

    # Create the new directory
    try:
        # Get new directory name from user
        dir_name = input("Enter the NEW directory: ")
        os.mkdir(dir_name)
    except:
        print("Directory already exists")
        create_dir(images)
    
    # Function call to start downloading images
    download_images(images, dir_name)


def download_images(images, dir_name):
    pass


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

create_dir(images)