# 음식 리스트 중에서 
# 그 중 하나를 추천

import random

# 음식리스트 중에서
foodlist = ["짜장면", "스시", "피자", "치킨", "커리"]
# print(foodlist[2])

# 그 중 하나를 추천
food = random.choice(foodlist)
print(food)

# for 반복문
'''
for i in range(5):     # range(5)= [0,1,2,3,4]
    print(i+1)         # i+1로 하는 경우 결과 : 1 2 3 4 5
print("종료")    
'''

# 5번을 연속으로 추천해보자
for i in range(5):     # range(5)= [0,1,2,3,4]
    food = random.choice(foodlist)
    # print(i+1 + ". " + food)
    print(f"{i+1}. {food}")
print("종료")       





