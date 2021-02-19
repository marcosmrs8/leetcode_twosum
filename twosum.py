def twoSum(numbers, target) :
    i = 0
    f = len(numbers) - 1

    while i < f:
        soma = numbers[i] + numbers[f]
        if soma == target:
            return [i+1, f+1]
        elif soma < target:
            i += 1
        else:
            f -= 1



print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))