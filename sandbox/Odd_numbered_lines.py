def main():
    f = open('text_written_line_by_line.txt', 'r')
    f1 = f.readlines()
    i = 1
    for x in f1:
        if i % 2 == 1:
            print(x)
        i = i + 1

    f.close()


if __name__ == "__main__":
    main()
