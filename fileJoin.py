ip=input('enter path to input files')
opname=input('enter name of the output file')
maxSz=int(input('enter no of files'))
inf=open(opname,'wb')
fno=1
while fno<=maxSz:
    opf=open(ip+'\p'+str(fno),'rb')
    data=opf.read()
    inf.write(data)
    opf.close()
    fno+=1
inf.close()