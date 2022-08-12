import myfood    # 모듈화 하는 방법. myfood.py에 print_list, print_random_list 함수 지정하고 호출할 떈 함수 앞에 myfood. 추가

foodlist = ["짜장면", "스시", "피자", "치킨", "커리"]

# 위 리스트를 출력
myfood.print_list(foodlist)

# 리스트 중에 먹고 싶은 메뉴가 없다면
'''
addfood = input("추가하고 싶은 음식을 입력하세요 : ")
print(f"고객님께서 입력하신 음식은 : {addfood}입니다.")

foodlist.append(addfood)
'''

# 리스트 중에 먹고 싶은 메뉴가 없다면
# 사용자가 입력을 한다(계속)
# 만약에 '그만'을 입력하면 입력이 끝나고 
# 음식 리스트를 출력하고 추천메뉴가 출력

while True:
    addfood = input("추가하고 싶은 음식을 입력하세요 : ")
    print(f"고객님께서 입력하신 음식은 : {addfood}입니다.")
    # 만약에 입력한 글자가 "그만"과 같다면 무한반복을 멈춤
    if addfood == "그만":
        break   # 여기서 멈춰야 "그만"이 foodlist에 어펜드 되지 않음
    foodlist.append(addfood)
 

# 음식리스트 출력
myfood.print_list2(foodlist)
print("당신의 음식 데이터를 AI가 분석해서 5개를 추천합니다.")

# 우리가 추가해서 그 중에서 또 추천했으면 좋겠다.
myfood.print_rand_list(foodlist)