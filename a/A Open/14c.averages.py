# STEP 1: Complete analyze function to return 5 values
#    - minimum
#    - maximum
#    - mean (a.k.a. average)
#    - median (center point)
#    - mode (most repeated)
def analyze(nums):
    return (min(nums), max(nums), sum(nums)/len(nums), median(nums), mode(nums))

# STEP 2: Complete median function to return center number
#         WITHOUT using built-in function
def median(nums):
    numsList = list(nums)
    numsList.sort()
    if (len(nums)%2 != 0):
        mid = len(nums) // 2
        return numsList[mid]
    else:
        mid = len(nums) // 2
        mid1 = mid - 1
        return (numsList[mid] + numsList[mid1])/2

# STEP 3: Complete mode function to return most-repeated number
#         WITHOUT using built-in function
# BONUS B: Catch special case where more than one value repeats the most
def mode(nums):
    count = {}
    for num in nums:
        if not(num in count):
            count[num] = 1
        else:
            count[num] += 1
    sortedCount = sorted(count.items(), key=lambda item: item[1])
    if (set(count.values()) == {count[nums[0]]}):
        return sortedCount[0][0]
    else:
         return sortedCount[-1][0]
    # return dict(sorted(count.items(), key=lambda item: item[1])))

# DO NOT EDIT - sample data for checking your work
sample1 = 1,2,3,4,5,6,7,8,9
sample2 = [37,45,23,65,75,34,23,23,23,65,12,99]
print(('min', 'max', 'mean', 'median', 'mode'))
print(analyze(sample1))
print(analyze(sample2))

# BONUS A: Print more samples as you see fit
