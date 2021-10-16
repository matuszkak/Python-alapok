nums = [3, 4, 9, 6, 2]

for num in nums:
    if num % 2 == 0:
        oszthatosag = 'osztható'
    else:
        oszthatosag = 'nem osztható'
    print(f'{num}: {oszthatosag}')
