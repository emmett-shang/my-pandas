def main():

    f = open('text_written_line_by_line.txt','w+')
    for i in range(10):
        f.write("%d\r\n" % (i + 1))

    f = open('text_written_line_by_line.txt','r')
    f1 = f.readlines()
    for x in f1:
        print(x)

    f.close()


if __name__ == "__main__":
    main()