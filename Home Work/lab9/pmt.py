number= [num]
value=' '  

while True: 
      try:
         num=int(input('Enter a number: ' ''))
      except:
        break
if 0<=num<99:     
      if num==0:
             #    value='nula'
            if num==273:
              #   value='dvesta'
                 
     
      print(number.dict)




numbers = []

while True:
      try:
 	      x = int( input("Please provide a number: ") )
      except:
            continue

      if x==0:
	      break
      else:
 	      numbers.append(x)

list_new = sorted(numbers)

for el in list_new:
	print(el)


