import numpy as np
list = [[1,2,3],[4,5,6],[6,7,8],[9,10,11],[12,13,14]] # 5행 3열 2차원 리스트

arr1 = np.array(list)
print(arr1)

np.sum(arr1[0])
print("")
# print(np.sum(arr1[0]))
print(np.sum(arr1, axis=0)) # 0 행 축으로 더한다 // 1 열 기준으로 더한다
print("")

arr2 = np.random.randint(10, size=(5,3,2)) # 3행2열 2차원 배열을 5개 만드는 3차원 배열
print(arr2)
print("")
print(np.sum(arr2, axis=0))
print("")
print(np.sum(arr2, axis=1))