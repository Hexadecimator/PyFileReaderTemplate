def main():
    # change file to your file
    with open('YOURTEXTFILEHERE.txt') as filetoparse:
        lines = filetoparse.readlines()

        for line in lines:
            print(line)

main()


