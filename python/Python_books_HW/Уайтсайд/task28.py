def count_peaks_valleys(price_action: list[int]) -> tuple[int, int]:
    '''Function that finds peaks and valleys amount in graphic'''
    peaks = 0
    valleys = 0
    n = len(price_action)
    for i in range(1, n - 1):
        if price_action[i - 1] < price_action[i] > price_action[i + 1]:
            peaks += 1
        elif price_action[i - 1] > price_action[i] < price_action[i + 1]:
            valleys += 1
    return (peaks, valleys)
print(count_peaks_valleys([1, 2, 3, 2, 1]))
print(count_peaks_valleys([1, 2, 3, 2, 1, 2]))
print(count_peaks_valleys([7, 6, 5, 10, 11, 12, 10, 9, 10]))