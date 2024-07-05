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
        dir_name = input("Enter a the output directory: ")
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
                print(image_url)
                url_path = image_url.rsplit('/', 1)[0]
                filename = image_url.rsplit('/', 1)[1]
                print(url_path)
                print(filename)
                url_split = os.path.basename(image_url).partition("?")[0]
                image_url = url_path + '/' + url_split
                print(image_url)
                print(url_split)
                print()
            except:
                try:
                    image_url = image["data-src"]
                    print(image_url)
                    url_path = image_url.rsplit('/', 1)[0]
                    filename = image_url.rsplit('/', 1)[1]
                    print(url_path)
                    print(filename)
                    url_split = os.path.basename(image_url).partition("?")[0]
                    image_url = url_path + '/' + url_split
                    print(image_url)
                    print(url_split)
                    print()
                except:
                    try:
                        image_url = image["data-srcset"]
                        print(image_url)
                        url_path = image_url.rsplit('/', 1)[0]
                        filename = image_url.rsplit('/', 1)[1]
                        print(url_path)
                        print(filename)
                        url_split = os.path.basename(image_url).partition("?")[0]
                        image_url = url_path + '/' + url_split
                        print(image_url)
                        print(url_split)
                        print()
                    except:
                        try:
                            image_url = image["data-original"]
                            print(image_url)
                            url_path = image_url.rsplit('/', 1)[0]
                            filename = image_url.rsplit('/', 1)[1]
                            print(url_path)
                            print(filename)
                            url_split = os.path.basename(image_url).partition("?")[0]
                            image_url = url_path + '/' + url_split
                            print(image_url)
                            print(url_split)
                            print()
                        except:
                            try:
                                image_url = image["data-fallback-src"]
                                print(image_url)
                                url_path = image_url.rsplit('/', 1)[0]
                                filename = image_url.rsplit('/', 1)[1]
                                print(url_path)
                                print(filename)
                                url_split = os.path.basename(image_url).partition("?")[0]
                                image_url = url_path + '/' + url_split
                                print(image_url)
                                print(url_split)
                                print()
                            except:
                                pass
            
            # Get image content
            try:
                r = requests.get(image_url).content

                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    # TODO: Write files with filename vs current  generic 'imagex'
                    with open(f"{dir_name}/image{i+1}.jpg", "wb+") as f:
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