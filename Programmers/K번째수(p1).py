def solution(array, commands):
    answer = []
    for i,j,k in commands :
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


# 이해 아직 못함
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


# i번째 숫자부터 j번째 숫자까지 자르고 정렬한다. 그 후 k번째 숫자를 고른다.

# i, j, k 는 commands 배열에 주어진다.

# 따라서 cmd배열을 i,j,k 로 받는다 예를 들어 cmd=[[2, 5, 3], [4, 4, 1], [1, 7, 3]] 이라면

# for i, j, k in cmd: 했을시

# 첫번째: i=2, j=5, k=3

# 두번째: i=4, j=4, k=1

# 세번째: i=1, j=7, k=3

# 이런식으로 실행된다. 

# 내장함수인 sorted()를 이용하여 (sort()는 원본을 바꾸고 리턴x, sorted는 원본 냅두고 바뀐값을 리턴)

# arr[i-1:j] (i부터 j까지 자르는데 배열은 0부터 시작하므로 i에 -1을 해줬다. j는 문자열 슬라이싱이 뒤에 있는 숫자-1 까지 이므로 그냥 j로 써주면 j-1까지만 찾게 된다.)


 
# 그 중에서 [k-1]번째 수를 ans배열에 추가해준다. (k번째 숫자를 고르는데 배열이 0부터 이므로 -1 해준다.)