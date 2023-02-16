import random, sys
qtde = int(sys.argv[1])
nums = [str(random.randint(0,100000))+'\n' for i in range(qtde)]
with open('nums.txt', 'w') as arquivo:
    arquivo.writelines(nums)
