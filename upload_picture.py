import argparse
import requests # to get image from the web
import shutil # to save it locally
import analyse_picture as a

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    #parser.add_argument('-d', '--destination', help='The name of the file to store the url in')

    args = parser.parse_args()
    
    #response = requests.get("https://i.imgur.com/ExdKOOz.png")
    response = requests.get(args.url)

    file = open("./Image/tmp_fruit.png", "wb")
    file.write(response.content)
    file.close()
    
    a.func()
    
    print('URL:', args.url)
    #print('Destination:', args.destination)
