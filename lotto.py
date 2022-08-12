
import random

numbers = list(range(1,26,1))

for i in range(10):  
    대박숫자 = random.sample(numbers,5)
    print(f"{i+1}. {대박숫자}")
