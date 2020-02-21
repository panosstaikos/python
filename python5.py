file=open("text.txt","r")
lexeis=[]
for line in file:
    line=line.strip()
    lexeis += line.split()
l=len(lexeis)
i=0
while i<l:
    if len (lexeis[i])>3:
        word=lexeis[i]
        new_word=word[1:] + "ay"
        print (new_word)
        i=i+1
    else:
        print (lexeis[i])
        i=i+1
        
               
