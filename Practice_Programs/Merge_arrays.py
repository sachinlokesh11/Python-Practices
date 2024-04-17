# Given two sorted integer arrays `X[]` and `Y[]` of size `m` and `n` each where `m >= n` and `X[]`
# has exactly `n` vacant cells, merge elements of `Y[]` in their correct position in array `X[]`,
# i.e., merge `(X, Y)` by keeping the sorted order.
#
# Input : Two arrays X[] and Y[] where vacant cells in X[] is represented by 0.
#
# X[] = [0, 2, 0, 3, 0, 5, 6, 0, 0]
# Y[] = [1, 8, 9, 10, 15]
#
# Output: X[] = [1, 2, 3, 5, 6, 8, 9, 10, 15]


array = [0, 2, 0, 3, 0, 5, 6, 0, 0]
array2 = [1, 8, 9, 10, 15]
array1 = []
final_array = []

for x in array:
    if x == 0:
        continue
    array1.append(x)

i = j = k = 0
while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        final_array.append(array1[i])
        i += 1
    else:
        final_array.append(array2[j])
        j += 1
    k += 1

if i == len(array1):
    final_array += array2[j:]
else:
    final_array += array1[i:]

print(final_array)

