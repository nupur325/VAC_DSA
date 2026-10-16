def secondHighestElement(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num,0) + 1
    freq = sorted(set(count.values()), reverse = True)
    if len(freq) < 2:
        return -1
    second = freq[1]
    result = []
    for num in count:
        if count[num] == second:
            result.append(num)
    return min(result)
