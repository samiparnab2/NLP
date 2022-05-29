ip=input('enter path to input file')
maxSz=int(input('enter max size of each block in MB'))
maxSz*=1024
maxSz*=1024
inf=open(ip,'rb')
fno=1
while True:

    data=inf.read(maxSz)
    if not data :
        break
    opf=open('p'+str(fno),'wb')
    opf.write(data)
    opf.close()
    fno+=1
inf.close()