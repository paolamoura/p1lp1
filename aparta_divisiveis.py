def eh_divisivel(num, k):
    return num % k == 0


def aparta(nums, k):
    cont_divisiveis = 0
    i = len(nums) - 1
    while i >= 0:
        if eh_divisivel(nums[i], k):
            cont_divisiveis += 1
            j = i
            while j < len(nums) - 1 and not eh_divisivel(nums[j + 1], k):
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j += 1
        i -= 1
    return cont_divisiveis


v = [21, 10, 11, 7, 8, 2, 17, 6, 28, 24]
assert aparta(v, 3) == 3
assert v == [10, 11, 7, 8, 2, 17, 28, 21, 6, 24]
