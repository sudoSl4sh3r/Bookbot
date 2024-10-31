def openAndPrint():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def countWords():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        words = contents.split()
        counter = 0
        for word in words:
            counter += 1
        return print(f"The book has {counter} words.")

def main():
    openAndPrint()
    countWords()

main()