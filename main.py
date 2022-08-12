import pandas as pd
data = pd.read_csv('/movie.csv', encoding='cp949', index_col="순위")
data

num = int(input("검색하고 싶은 갯수를 입력하세요 : "))
data[0:num]

filtering = input("내용을 얻고 싶은 구역을 입력하세요 : ")
data[filtering].unique()

# 문자필터링
key1 = input("필터링할 구역을 입력하세요 : ")
key2 = input("필터링할 내용을 입력하세요 : ")
res = data[key1] == key2
data[res]

# 숫자필터링 

intdata = pd.read_csv('/content/MyDrive/MyDrive/movie.csv', encoding='cp949', index_col='순위', thousands = ',') 

key1 = input("필터링할 구역을 입력하세요 : ")
key2 = int(input("원하는 숫자를 입력하세요 : "))

boolKey = input("입력한 숫자 보다 작은 결과를 원하면 1, 큰 값을 원하면 2, 같은 값을 원하면 3을 입력하세요 : ")

if boolKey == '1' :
  res = intdata[key1] < key2
elif boolKey == '2' :
  res = intdata[key1] > key2
elif boolKey == '3' :
  res = intdata[key1] == key2

intdata[res].iloc[:,[0,2,3,4,6]].astype({'매출액': 'int'})
