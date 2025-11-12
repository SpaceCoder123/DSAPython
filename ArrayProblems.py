class ArraysProblems:
    # Left Rotate by d Places
    def rotateArray(self, arr, d): 
        n = len(arr)
        if n <= 1:
            return arr
        
        d = d % n 
        return arr[d:] + arr[:d]

    # O(n) time complexity
    # O(n) space complexity

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotateArray(self, arr, d):
        n = len(arr)
        if n <= 1:
            return
        d = d % n
        self.reverse(arr, 0, n-d - 1)
        self.reverse(arr, n-d, n - 1)
        self.reverse(arr, 0, n - 1)
        return arr


    # O(n) time complexity
    # O(1) space complexity


    # 442. Find All Duplicates in an Array
    def findDuplicates(self, nums):
        items = []
        value = 0
        for i in range(len(nums)):
            value = abs(nums[i])
            if(nums[value-1] < 0):
                items.append(value)
            nums[value - 1] = -nums[value - 1]
        return items

    # 448. Find All Numbers Disappeared in an Array
    def findDisappearedNumbers(self, nums):
        items = []
        value = 0
        for i in range(len(nums)):
            value = abs(nums[i])
            if(nums[value-1] < 0):
                continue
            nums[value - 1] = -nums[value - 1]

        for i in range(len(nums)):
            if(nums[i] > 0):
                items.append(i+1)
        return items

    # 268. Missing Number

    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        arraySum = sum(nums)
        return total - arraySum

    def maximumSubarraySum(self, arr, k):
        n = len(arr)
        if k > n:
            return []
        
        total = 0
        for i in range(k):
            total+= arr[i]

        curr = total
        left = 0
        right = k

        while right < n:
            curr = curr - arr[left]
            curr += arr[right] 
            right+=1
            left+=1
            if(curr>total):
                total = curr
        return total

    def longestEvenSubArray(self, arr):
        return arr

    def majorityElement(arr):
        n = len(arr)
        if n == 0: 
            return 0
        if n == 1:
            return arr[0]
        
        curr = arr[0]
        count = 0
        for i in range(1,n):
            if arr[i] == curr:
                count+=1
            if arr[i] != curr:
                if count == 0:
                    curr = arr[i]
                else:
                    count-=1

        majorityCount = 0
        for i in range(n):
            if(arr[i] == curr):
                majorityCount+=1
        
        
        return curr if majorityCount > n // 2 else -1

    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0 
        
        for price in prices[1:]:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfitMed(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        maxProfit = 0
        for i in range(1, n):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                maxProfit+=profit
        return maxProfit


    # print(maxProfitMed([2, 1, 4, 5, 2, 9, 7]))


    # 42. Trapping Rain Water , LeetCode Hard

    def trap(self, height):
        
        n = len(height)
        highTowers = [0] * n
        high = height[0]
        for i in range(n):
            if height[i] > high:
                highTowers[i] = height[i]
                high = height[i]
            else:
                highTowers[i] = high

        lowTowers = [0] * n
        low = height[n-1]
        for i in range(n):
            if height[n-i-1] > low:
                lowTowers[n-i-1] = height[n-i-1]
                low = height[n-i-1]
            else:
                lowTowers[n-i-1] = low

        total = 0
        for i in range(n):
            curr = min(highTowers[i], lowTowers[i]) - height[i]
            if curr > 0:
                total+=curr
        return total

    def trapOptimal(self, height):
        n = len(height)
        left = 0
        right = n - 1

        leftMax = height[left]
        rightMax = height[right]

        waterCollected = 0
        while(left<=right):
            if(height[left] <= height[right]):
                if(height[left] > leftMax):
                    leftMax = height[left]
                else:
                    waterCollected += max(leftMax,height[left])- height[left] 
                left+=1
            else:
                if(height[right] > rightMax):
                    rightMax = height[right]
                else:
                    waterCollected += max(rightMax,height[right])- height[right] 
                right-=1
        return waterCollected


    # print(trapOptimal([0,1,0,2,1,0,1,3,2,1,2,1]))

    def maxCards(self, cards, k):
        n = len(cards)
        total = sum(cards[:k])
        max_total = total

        for i in range(k, k + n):
            total += cards[i % n] - cards[(i - k) % n]
            max_total = max(max_total, total)

        return max_total        