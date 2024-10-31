def openAndPrint():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def main():
    openAndPrint()

main()