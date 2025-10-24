fin= open("bob.txt","w")
fin.write('Hello Bob')
fin.write('\n')
fin.close()

fin= open("bob.txt","r")
for line in fin:
    print(line)
fin.close()