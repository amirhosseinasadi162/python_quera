###Adds even and odd numbers in the list and prints the result### 
def sum_number():
    lis = []
    lis_even = []
    lis_odd = []
    count_number = int(input("count number : "))
    i = 1
    while i<= count_number:
        lis_number = int(input("enter number: "))
        lis.append(lis_number)
        i +=1
        
                
    for i in lis:
        if i % 2 == 0:
            lis_even.append(i)
        else:
            lis_odd.append(i)
            
    print(f"sum even number = {sum(lis_even)}")
    print(f"sum odd number = {sum(lis_odd)}")

sum_number()
    
        