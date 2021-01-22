def main():
    try:
        file = open("same.txt", "r")
        print("File Opened successfully!")
    except IOError:
        print("File does not exist!")

if __name__ == "__main__":
    main()