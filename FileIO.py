try:
    f = open('f://io.txt' , 'r' )
    print f.read()
finally:
    if f:
        f.close()

with open('f://io.txt' , 'r' ) as f:
    for line in f.readlines():
        print (line.strip())
        # print f.read(2)
        # print f.readlines()
fi = open('f://PyWork/13.jpg' , 'wb')
fi.write('123123123123')
fi.close()