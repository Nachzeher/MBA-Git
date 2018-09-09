sum = 0
count = 0

while True:
    inp = raw_input("Enter a Number: ")
    if inp == "done":
        break
    try:
        Tnum = abs(float(inp))
    except:
        Tnum = -1
    #or use continue like this:
    #try:
    #   num = float(inp)
    #except: 
    #   print "Invalid input"
    #   continue
    # and no Tnum<0 and else below
    if Tnum > 0:
        num = float(inp)
        sum = sum + num
        count = count + 1    
        #print num,sum,count       
    else: 
        print "Invalid input"
average = sum/count
print int(sum), count, average