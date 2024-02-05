# 이것이 코딩테스트다  
## ch7. 이진 탐색

### 2. 부품찾기
N = 5
have = [8,3,7,9,2]
M= 3
need = [5,7,9]
for i in need:
    if i in have : print('yes', end=" ")
    else : print('no', end=" ")

### 3. 떡볶이 떡 만들기
N, M  = 4,6
height = [19,15,10,17]
start = 0 
end = max(height)
output= 0
while start <= end : 
    total =0
    mid = (start+end)//2
    for i in height:
        if i > mid:
            total += i -mid
    if total < M :
        end = mid-1
    else: 
        output = mid
        start = mid+ 1
print(output)