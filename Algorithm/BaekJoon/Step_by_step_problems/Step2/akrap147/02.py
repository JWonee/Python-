#  백준 조건문 2번 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 9498
a = input()
a = int(a)
if (90<=a ):
  print("A")
elif (80<= a < 90) :
  print("B")
elif (70<= a < 80) :
  print("C")
elif (60<= a < 70) :
  print("D")
else:
  print("F")
  
 
