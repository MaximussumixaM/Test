#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#The overall run time complexity should be O(log (m+n)).
#
# 
#
#Example 1:
#
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:
#
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
#
#Constraints:
#
#nums1.length == m
#nums2.length == n
#0 <= m <= 1000
#0 <= n <= 1000
#1 <= m + n <= 2000
#-106 <= nums1[i], nums2[i] <= 106

import sys
from typing import List


def findMedianSortedArrays1(nums1: List[int], nums2: List[int]) -> float:
    # Check if nums1 is smaller than nums2
    # If not, then we will swap it with nums2
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    # Lengths of two arrays
    m = len(nums1)
    n = len(nums2)
    # Pointers for binary search
    start = 0
    end = m
    # Binary search starts from here
    while start <= end:
        # Partition indices for both the arrays
        partition_nums1 = (start + end) // 2
        partition_nums2 = (m + n + 1) // 2 - partition_nums1
        # Edge cases
        # If there are no elements left on the left side after partition
        maxLeftNums1 = -sys.maxsize if partition_nums1 == 0 else nums1[partition_nums1 - 1]
        # If there are no elements left on the right side after partition
        minRightNums1 = sys.maxsize if partition_nums1 == m else nums1[partition_nums1]
        # Similarly for nums2
        maxLeftNums2 = -sys.maxsize if partition_nums2 == 0 else nums2[partition_nums2 - 1]
        minRightNums2 = sys.maxsize if partition_nums2 == n else nums2[partition_nums2]
        # Check if we have found the match
        if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
            # Check if the combined array is of even/odd length
            if (m + n) % 2 == 0:
                return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2
            else:
                return max(maxLeftNums1, maxLeftNums2)
        # If we are too far on the right, we need to go to left side
        elif maxLeftNums1 > minRightNums2:
            end = partition_nums1 - 1
        # If we are too far on the left, we need to go to right side
        else:
            start = partition_nums1 + 1
    # If we reach here, it means the arrays are not sorted
    raise Exception("IllegalArgumentException")
def findMedianSortedArrays2(nums1: List[int], nums2: List[int]) -> float:
    num = nums1 + nums2
    num = sorted(num)
    l = len(num)
    if l % 2 == 0:
        return (num[l//2-1]+num[l//2])/2*1.0
    else:
        return num[l//2]*1.0
def findMedianSortedArrays3(nums1: List[int], nums2: List[int]) -> float:
    MAX_VALUE = float('Inf')
    MIN_VALUE = -float('Inf')

    # Получить количество элементов списка
    m = len(nums1)
    n = len(nums2)
    if m == 0:  # nums1 пусто
        # Вот маленький трюк
        # n - нечетное число, nums2 [int ((n-1) / 2)] и nums2 [int (n / 2)] - одно и то же число, то есть медиана
        # n является четным, nums2 [int ((n-1) / 2)] и nums2 [int (n / 2)] - два средних числа соответственно
        # Это потому, что int (n / 2) округлено в меньшую сторону, int (1.5) == 1
        # Функция округления также может быть реализована оператором '//'
        return float((nums2[int((n - 1) / 2)] + nums2[int(n / 2)]) / 2)
    if n == 0:  # Аналогично, nums2 пусто
        return float((nums1[(m - 1) // 2] + nums1[m // 2]) / 2)

    if m > n:  # Чтобы повысить эффективность, убедитесь, что обход цикла является коротким списком
        return Solution.findMedianSortedArrays(self, nums2, nums1)

    # Когда оба списка не пусты
    # Инициализация диапазона обрезки
    size = m + n
    CutL = 0
    CutR = m
    cut1 = m // 2  # Краткий список позиций реза

    while cut1 <= m:  # Найти позицию, которая удовлетворяет l1 <r2 и l2 <r1
        cut1 = (CutR - CutL) // 2 + CutL  # Краткий список позиций реза
        cut2 = size // 2 - cut1  # Длинный список позиций реза

        # Добавьте MIN_VALUE и MAX_VALUE к двум концам списка, чтобы два особых случая ребер можно было обрабатывать вместе с обычными случаями
        # Два особых случая ребер: 1. max (nums1) <min (nums2) 2. min (nums1)> max (nums2)
        # Получить значение резки с обеих сторон
        l1 = MIN_VALUE if cut1 == 0 else nums1[cut1 - 1]  # Эквивалентно тринокулярному оператору '?:' в Java, только когда min (nums1)> max (nums2), l1 принимает значение MIN_VALUE
        l2 = MIN_VALUE if cut2 == 0 else nums2[cut2 - 1]  # То же, что и выше, не можете получить особую ситуацию?
        r1 = MAX_VALUE if cut1 == m else nums1[cut1]  # Только когда max (nums1) <min (nums2, l1 принимает значение MIX_VALUE
        r2 = MAX_VALUE if cut2 == n else nums2[cut2]

        if l1 > r2:  # l1> r2, cut1 нужно переместить влево
            CutR = cut1 - 1
        elif l2 > r1:  # l2> r1, cut1 должен двигаться вправо
            CutL = cut1 + 1
        else:  # Познакомьтесь с l1 <r2 и l2 <r1
            if size % 2 == 0:  # Общее количество элементов в обоих списках четное
                l = l1 if l1 > l2 else l2
                r = r1 if r1 < r2 else r2
                return float((l + r) / 2)
            else:  # Общее количество элементов в обоих списках нечетное
                r = r1 if r1 < r2 else r2
                return float(r)
nums1 = [1,2,8]
nums2 = [3,4,5]
print(findMedianSortedArrays1(nums1,nums2))
print(findMedianSortedArrays2(nums1,nums2))
print(findMedianSortedArrays3(nums1,nums2))