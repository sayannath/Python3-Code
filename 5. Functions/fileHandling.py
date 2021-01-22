def main():
    file = open("sample.txt", "a+")
    for i in range(20):
        file.write("I love Python %d\n" %(i+1))
    file.close()


if __name__ == "__main__":
    main()