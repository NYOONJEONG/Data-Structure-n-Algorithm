# 이것이 코딩테스트다 
## ch6. 정렬

### 2. 위에서 아래로

N = int(input())
result = []
for _ in range(N):
    result.append(int(input()))

for i in reversed(sorted(result)):
    print(i,end=" ")


### 3. 성적이 낮은 순서로 학생 출력하기
N = int(input())

input_data = []
for _ in range(N):
    name_score= input().split()
    input_data.append((name_score[0], int(name_score[1])))

for data in sorted(input_data, key=lambda x : x[1]):
    print(data[0], end=" ")

### 4. 두 배열의 원소 교체
N, K = map(int, input().split())
A = list(map(int, input().split()))
B= list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i]<B[i]:
        A[i], B[i] = B[i], A[i]
    else: break


print(sum(A))