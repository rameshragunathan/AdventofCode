file = open("input.txt","r")
area=0
for line in file:
    fields=sorted([int(_) for _ in (line.split('x'))])
    length=fields[0]
    width=fields[1]
    height=fields[2]

    area=area +( (2*(length*width)) + (2*(width*height)) + (2*(height*length)) + (length*width))

print (str(length) +" " +str(width) + " "+ str(height))
print (area)




