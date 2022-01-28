import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(arr.sum())
# print(arr.mean())

# arr3 = np.array(1,2,3,4,5) #에러남 [1,2,3,4,5] 리스트 형태로 넣어줘야한다.

# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr2)

# print(arr2.shape)
# li = [1,2,3,4,5]
# print(li)

# print(arr2[0])
# print("") # 한줄 띄기
# print(arr1[0].mean())
# print("") # 한줄 띄기
# print(arr2[0][0])
# print("") # 한줄 띄기
# print(arr1[0][0])


# list1 = [[1,2,3],[4,5,6]] # 2차원 리스트 선언
# print(list1)
# print(list1[:][2]) #오류발생함
#
# np_arr = np.array(list1) # numpy 2차원 배열 선언
# print(np_arr)
# print(np_arr[:,2])

# arr3 = np.array([[1,2],[3,4]])
# print(arr3.transpose()) # 전치행렬로 변환


arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])

arr_sum = arr4 + arr5 # 배열의 + 연산 -> [5,7,9]
print(arr_sum)

list1 = [1,2,3]
list2 = [4,5,6]
list_sum = list1 + list2 # 리스트의 + 연산 -> [1,2,3,4,5,6]
print(list_sum)

arr_multi = arr4 * arr5 # 배열의 * 연산
print(arr_multi)

print(arr4 + 1) # arr4의 원소마다 1이 더해짐
# print(list1 + 1) # error 발생

print("---------------------------------------")
arr6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr7 = np.array([[2,8,4],[1,2,9],[5,1,2]])

arr_index_sum = arr6[:,0] + arr7[:,0]
print(arr_index_sum)

list3 = [1,2,3,4,5,6,7,8,9]
arr8 = np.array(list3)
arr9 = arr8 > 5
print(arr9)

arr10 = np.random.random(5) # 0~1 사이에서 5개의 랜덤수 출력
print(arr10)
print(np.all(arr10 >= 0.3)) # 모든 원소가 0.3 이상이면 True 아니면 False (and 조건)
print(np.any(arr10 >= 0.3)) # 한개의 원소만 0.3 이상이면 True (or조건)
print("---------------------------------------")

print(np.linspace(0,12,4)) #등간격 나누기 0~12사이를 4개로 나눈다