# hello-world
my 1st info


data = []

count = data.__len__()
count1 = count + 1

while count1 > 0 :
    sample = input("Enter the value to the list \n")
    data.insert(count1,sample)
    
    count1 = count1 + 1
    print(data)
    t = input("Whether to continue or exit from the loop")
    if t == "break" :
        print("exit from the loop")
        break
    else:
        continue
