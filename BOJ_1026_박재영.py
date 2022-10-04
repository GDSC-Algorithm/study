def s(a_list, b_list):
    result = 0
    for i in range(len(a_list)):
        result += a_list[i] * b_list[i]
    return result

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

# b_list값을 인덱스와 매칭하여 저장
b_dict = zip(b_list, range(n)) # key로 오름차순 정렬할 거기 때문에 key를 b_list로
b_dict = sorted(b_dict) # key 오름차순 정렬, 각각의 value값은 b_list에서의 인덱스

a_new = [0] * n
a_list.sort() # 최댓값 삭제 쉽게 하려고 정렬함

# b_list에서 가장 작았던 숫자의 인덱스에 a_list의 최댓값 넣기
for i in range(n):
    a_new[b_dict[i][1]] = a_list[-1] 
    a_list.pop()

print(s(a_new, b_list))