def openAndPrint():
    with open("books/frankensein.txt") as f:
        file_contents = f.read()

def main():
    openAndPrint()

main()