# Viết chương trình nhận vào số nguyên dương k và mảng gồm n số nguyên (n >= 1)
# In ra màn hình phần tử lớn thứ k trong mảng, nếu không tồn tại phần tử lớn thứ k thì in ra màn hình thông báo "Unable to get kth largest element".
k = int(input())
arr = list(map(int, input().split()))

unique_elements = sorted(list(set(arr)), reverse=True)

if k <= 0 or k > len(unique_elements):
    print("Unable to get kth largest element")
else:
    print(unique_elements[k - 1])
