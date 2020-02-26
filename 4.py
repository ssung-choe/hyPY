
import random

ans1 = "잘 쉬는게 혁신이야!"
ans2 = "여러분들이 하고 싶은 것을 하세요!"
ans3 = "신이 나! 신이 나! 엣헴 엣헴 신이 나!"
ans4 = "눈치 챙겨!"

print("펭-하! 환영해요! 펭수 띵언 궁금하죠?")

question = input ("궁금하면! 질문 입력 후 엔터! \n>")

print ("궁금?...")

choice = random.randint(1, 4)

if choice == 1:
    answer=ans1
elif choice == 2:
    answer=ans2
elif choice == 3:
    answer=ans3
else:
    answer=ans4


print("펭수 띵언 한번 더!")

question = input ("궁금하면! 질문 입력 후 엔터를 누세요. \n")


input ("\n\n 언터치면 펭-빠!")


