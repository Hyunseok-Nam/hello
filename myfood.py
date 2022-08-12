import random

# 화면에 음식리스트를 출력하는 기능
def print_list(foodlist):
    for i, food in enumerate(foodlist): # foodlist에 인덱스도 추가 
        print(f"{i+1}. {food}")


def print_list2(foodlist):    #  위의 것을 가로로
    str = ""
    for i, food in enumerate(foodlist): # foodlist에 인덱스도 추가 
        # print(f"{i+1}. {food}")
        str += f"{i+1}. {food} "
    print(str)    


# 음식 리스트를 추천해주는 기능
def print_rand_list(foodlist):
    for i in range(5):     # range(5)= [0,1,2,3,4]
        food = random.choice(foodlist)
        print(f"{i+1}. {food}")