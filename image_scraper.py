from bs4 import BeautifulSoup
import requests
import os

def create_dir(images):
    """
    Get user input for a new directory for the images to be downloaded 
    to, then call the download_images function.
    """
  
    # Create the new directory for output
    try:
        # Get new directory name or from user
        dir_name = input("Enter the output directory: ")
        os.mkdir(dir_name)
    except:
        print("Directory already exists")
        create_dir(images)
    
    # Function call to start downloading images
    download_images(images, dir_name)



def parse_image(original_image_url):
    print(original_image_url)
    # Gets the URL path before the filename
    url_path = original_image_url.rsplit('/', 1)[0]
    print(url_path)
    # Removes '?' and everything after the filename extension
    filename = os.path.basename(original_image_url).partition("?")[0]
    # Combines URL path and filename
    new_image_url = url_path + '/' + filename
    print(new_image_url)
    print(filename)
    print()

    return new_image_url, filename



def download_images(images, dir_name):
    """
    Looks for different types of HTML img source attributes, parses
    the URL using parse_image() function, then downloads all images
    in the webpage.
    """

    # Counter for number of actual images downloaded
    counter = 0
    filename = ""

    # Check if there are images to download
    if len(images) > 0:
        for i, image in enumerate(images):
            try:
                image_url = image["src"]
                new_image_url, filename = parse_image(image_url)
            except:
                try:
                    image_url = image["data-src"]
                    new_image_url, filename = parse_image(image_url)
                except:
                    try:
                        image_url = image["data-srcset"]
                        new_image_url, filename = parse_image(image_url)
                    except:
                        try:
                            image_url = image["data-original"]
                            new_image_url, filename = parse_image(image_url)
                        except:
                            try:
                                image_url = image["data-fallback-src"]
                                new_image_url, filename = parse_image(image_url)
                            except:
                                pass
            
            # Get image content
            try:
                r = requests.get(new_image_url).content

                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{dir_name}/{filename}", "wb+") as f:
                        f.write(r)
                    # Counter for total number of images actually downloaded
                    counter += 1
            except:
                pass
        
        # Summary of total images actually downloaded / total images found on page
        print(f"{counter}/{len(images)} images downloaded")


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
# print(images)

create_dir(images)