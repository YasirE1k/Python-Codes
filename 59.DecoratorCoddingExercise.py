def extra(func):
    def wrapper(list):
        sum_of_odd_numbers=0 
        sum_of_even_numbers=0
        odd_numbers=0
        even_numbers=0 
        
        for i in list:
            if(i%2==0):
                sum_of_even_numbers+=i
                even_numbers+=1
        
            else:
                sum_of_odd_numbers+=i
                odd_numbers+=1
        print("Average of even numbers:",sum_of_even_numbers/even_numbers)
        print("Average of odd numbers:",sum_of_odd_numbers/odd_numbers)

        func(list)
    return wrapper

@extra
def findAverage(list):
    k=0
    for i in list:
        k+=i
    print("Average",k/len(list))

findAverage([1,2,3,4,5,6])

