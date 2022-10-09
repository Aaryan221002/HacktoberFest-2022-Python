def solution(numbers):
    for i in range(len(numbers)-1):
        for j in range(i,len(numbers)):
            numbers[i],numbers[j]=numbers[j],numbers[i]
    return numbers 
        
   
