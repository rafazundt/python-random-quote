newQuote = input("What is your favourite quote? ")

f = open("quotes.txt", "a")
f.write("\n" + newQuote)
f.close()

f = open("quotes.txt", "r")
print(f.read())