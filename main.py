from crawler.crawler import download_pictures


def main():
    img_number = int(input("How many images do you want to download:"))
    search = input("What do you want to search:")
    download_pictures(img_number, search)


if __name__ == '__main__':
    main()
