try:
    with open("text.txt") as file:
        file.seek(0)
        first_char=file.read(1)
        if not first_char:
            print ("Το αρχείο είναι άδειο")
        else:
            file.seek(0)
            fi={}
            def freq(str):
                str=str.split()
                str2=[]
                for i in str:
                    if i not in str2:
                        str2.append(i)
                for i in range(0,len(str2)):
                    s=0
                    for j in str2[i]:
                        fi[i]=fi.get(i,0)+1
                        s=s+1
                        f=int(str2[i].count("f"))
                        c=int(str2[i].count("c"))
                        k=int(str2[i].count("k"))
                        r=int(str2[i].count("r"))
                        bad=f+c+k+r
                        good=int(s-bad)
                    if bad>good:
                        print(str2[i], ":bad word")
                    else:
                        print(str2[i], ":good word")
            def main():
                with open ("text.txt", "r") as myfile:
                    str=myfile.read().replace(",", "\n").replace(".", " ").replace("\n", " ")
                freq(str)
                
            if __name__=="__main__":
                main()
                
except FileNotFoundError:
    print ("Το αρχείο δεν βρέθηκε")
                   
