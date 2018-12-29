def main():
    f = open("File_made_by_file_handling.txt", "w+")

    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))

    f.close()


if __name__ == "__main__":
    main()
