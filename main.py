def openAndPrint():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def main():
    openAndPrint()

main()