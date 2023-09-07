filename= input("Enter the file name:")
n = input("Enter the number of lines to be displayed:")
word = input("Enter the word to be searched:")
word_count=0
with open(filename,'r') as file:
    for i in range (n):
        line = file.readline()
        print(line)
    word_count = line.count(word)
print(f"The word {word} occurs {word_count} times in the file")