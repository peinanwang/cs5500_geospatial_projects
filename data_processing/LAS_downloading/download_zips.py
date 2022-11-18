"""
Download all zip file links from a given URL to a text file line by line,
then download the zip files from text file.
"""
import requests

# Creating a new text file to store the zip file links
newfile = open('LiDAR_zip_list','w')

#Fetching the links for the zip file and downloading the files to current location
with open('LiDAR_zip_list.txt', 'r') as links:
    for link in links:
        if link:
            filename1= link.split('/')[-1]
            filename= filename1[:-1]
            print(filename + ' file started to download')
            response = requests.get(link[:-1])

            # Writing the zip file into local file system
            with open(filename,'wb') as output_file:
                output_file.write(response.content)
            print(filename + 'file is downloaded')
