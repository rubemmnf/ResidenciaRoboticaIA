def fib(n):
    if n in {0,1}:
        return n
    else: 
        return fib(n-1)+fib(n-2)
    
nums = []
for i in range(10):
    nums.append(str(fib(i))+'\n')

# print(nums)
# nums = [str(fib(i)) for i in range(10)]
# print(nums)

with open('fib.txt', 'w') as arquivo:
    #o que writelines faz é exatamente o que tem comentado agora
    # for num in nums:
    #     arquivo.write(num)
    arquivo.writelines(nums)
    
    
    # for num in nums:
    #     arquivo.write(str(num)+'\n')

