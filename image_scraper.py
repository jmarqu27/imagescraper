from bs4 import BeautifulSoup
import requests
import os

def create_dir(images):
    """
    Get user input for a new directory for the images to be downloaded 
    to, then call the download_images function.
    """
    # TODO: Get outfile directory from user

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
    """
    Look for different type of HTML img source attributes, 
    then downloads all images in the webage.
    """

    # Counter for number of actual images downloaded
    counter = 0
    filename = ""

    # Check if there are images to download
    if len(images) > 0:
        for i, image in enumerate(images):
            try:
                image_url = image["src"]
                filename = image_url.rsplit('/', 1)[-1]
                print(image_url)
                print(filename)
                print()
            except:
                try:
                    image_url = image["data-src"]
                    filename = image_url.rsplit('/', 1)[-1]
                    print(image_url)
                    print(filename)
                    print()
                except:
                    try:
                        image_url = image["data-srcset"]
                        filename = image_url.rsplit('/', 1)[-1]
                        print(image_url)
                        print(filename)
                        print()
                    except:
                        try:
                            image_url = image["data-original"]
                            filename = image_url.rsplit('/', 1)[-1]
                            print(image_url)
                            print(filename)
                            print()
                        except:
                            try:
                                image_url = image["data-fallback-src"]
                                filename = image_url.rsplit('/', 1)[-1]
                                print(image_url)
                                print(filename)
                                print()
                            except:
                                pass
            
            # Get image content
            try:
                r = requests.get(image_url).content

                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    # TODO: Adjust filename to remove characters after its file extention (i.e. .jpg, .png, etc)
                    # TODO: Save images to output directory provided in create_dir function
                    with open(f"{dir_name}/{filename}", "wb+") as f:
                        f.write(r)
                    counter += 1
            except:
                pass
        
        # Summary of total images downloaded / total images found on page
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