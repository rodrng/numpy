import numpy as np

#rand 함수
arr1 = np.random.rand(5) # 5개의 랜덤수(난수) 어레이를 생성
print(arr1)

print("")
arr2 = np.random.rand(2,3) # 0~1사이에 2행 3열 2차원
print(arr2)

print("-------------------------------")
# randint 함수
arr3 = np.random.randint(3, size=5) # 0 <= n < 3 (n은 정수) 인 난수 5개 출력
# [0, 3) -> 이상 3미만
print(arr3)