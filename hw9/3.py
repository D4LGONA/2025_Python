def extract_number(s):
    # 문자열에서 숫자만 추출하여 정수로 변환
    return int(''.join(filter(str.isdigit, s)))

def selection_sort_by_number(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if extract_number(arr[j]) < extract_number(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = ['1488e', '14a6d', '15acd', '47b2', 'af8e', '13584', '17d1a', '15ad8', '95a5', '7a1f']

sorted_data = selection_sort_by_number(data)

print("정렬 전 데이터 :", ' '.join(data))
print("정렬 후 데이터 :", ' '.join(sorted_data))
