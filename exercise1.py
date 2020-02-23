arxio= input ("Δώσε μου το όνομα του αρχείου που θέλεις να επεξεργαστώ:")
file=open(arxio, "r")
fonhenta= ['a', "i", "e", "u", "o"]
w= file.read()
w = w.split()
w.sort(key=len)
for x in range(1,6):
    string = w[len(w)-x]
    string=string[::-1]
    for gramma in  string:
        if gramma in fonhenta:
            string= string.replace(gramma,'')
    print(string)
