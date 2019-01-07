def main():
    f = open('text_written_line_by_line.txt', 'r')
    f1 = f.readlines()
    i = 1
    str1 = 'Hello'
    str2 = '!'
    for x in f1:
        if i % 2 == 1:
            print(str1 + " " + x.upper())
        i = i + 1


    f.close()


if __name__ == "__main__":
    main()