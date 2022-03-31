



## 6:

l1=[]
list_neg=0
list_pos=0

while True:
    l=int(input('Enter a num: '))
    l1.append(l)
    if l<0:
        list_pos= l
    else:
        list_neg= l 

    print(f'list_pos= {list_pos }, list_neg {list_neg }')
    
            
