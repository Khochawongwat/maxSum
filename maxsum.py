def maxCrossSum(arr, left, mid, right):
    x, left_sum = 0, float("-inf")
    for i in range(mid, left - 1, -1):
        x = x + arr[i]
        if x > left_sum:
            left_sum = x

    x, right_sum = 0, float("-inf")
    for i in range(mid + 1, right + 1):
        x = x + arr[i]
        if x > right_sum:
            right_sum = x

    return max(left_sum + right_sum, left_sum, right_sum)


def maxSubArraySum(arr, left, right):
    if left == right:
        return arr[left]

    m = (left + right) // 2
    return max(
        maxSubArraySum(arr, left, m),
        maxSubArraySum(arr, m + 1, right),
        maxCrossSum(arr, left, m, right),
    )
