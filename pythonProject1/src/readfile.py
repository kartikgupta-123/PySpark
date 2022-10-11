f = open("D:\\usdata.csv")

data= f.read()
print(data)

f.close()

b= open('newfile', 'a')

b.write('write something new append')

b.close()

