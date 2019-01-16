def main():
    f = open("File_made_by_file_handling.txt", "w+")

    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))

    f.close()
    f = open("File_made_by_file_handling.txt", "a+")
    for i in range(2):
        f.write("Append line %d\r\n" % (i + 1))

    f = open("File_made_by_file_handling.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)


    f.close()


if __name__ == "__main__":
    main()
