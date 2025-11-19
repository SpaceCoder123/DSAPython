class RecursionProblems:
    def getTotal(self, number):
        if(number <= 0):
            return 0
        if(number == 1):
            return 1
        return number%10 + self.getTotal(number//10)

    def palindrome(self, string, start, end):
        if(start>=end):
            return True
        return string[start] == string[end] and self.palindrome(string, start+1, end-1)

    # You are given a number n. You need to recursively find the nth term of the series S that is given by:
    # S(n) = n+ n*(S(n-1)) and S(0) = 1

    def theSequence(self, n):
        if(n == 0):
            return 1
        self.theSequence(n-1)

    def printElements(self, arr,n):
        if(n==0):
            return 0 
        self.printElements(arr,n-1)
        return 0

    def CountDigits(self, n):
        if(n<1):
            return 0
        return self.CountDigits(n//10) + n%10

    def recursiveSum(self, n):
        if(n<=1):
            return 1
        return self.recursiveSum(n-1) * n

    def fibonacci(self,n):
        if(n==0):
            return 0
        if(n==1):
            return 1
        return self.fibonacci(n-1)+self.fibonacci(n-2)

    def nCr(self,n,r):
        if(r==1):
            return n
        if(n==r):
            return 1
        return self.nCr(n-1,r-1) + self.nCr(n-1,r)

    def isPalin(self,N):
        result = self.checkPalindrome(N, 0, len(N)-1)
        return 1 if(result == True) else 0 

    def checkPalindrome(self,N, startIndex, endIndex):
        if(startIndex >= endIndex):
            return True
        return N[startIndex] == N[endIndex] and self.checkPalindrome(N, startIndex+1, endIndex-1)

    def ropeCuttingProblem(self, n, a, b, c):
        if n == 0:
            return 0
        
        if n <= 1:
            return -1
        
        res = max(self.ropeCuttingProblem(n-a, a,b,c), self.ropeCuttingProblem(n-b, a,b,c), self.ropeCuttingProblem(n-c, a,b,c))
        
        if(res == -1):
            return -1
        
        return res + 1

    def power_set(self,s):
        result = []
        powerSet = 2**len(s)
        for i in range(powerSet):
            str = ""
            binary = bin(i)[2:].zfill(len(s))
            for j in range(len(binary)):
                if binary[j] == "1":
                    str += s[j]
            result.append(str)
        return result

    def sumOfDigits(self,number):
        if  number == 0:
            return 0
        else:
            return (number % 10) + self.sumOfDigits(number//10)

    def countZero(self,number):
        if number == 0:
            return 0
        if number % 10 == 0:
            return 1 + self.countZero(number // 10)
        else:
            return self.countZero(number // 10)

    def countOccurances(self, list, target):
        if(len(list) == 0):
            return 0
        
        if(list[0] == target):
            return 1+ self.countOccurances(list[1:], target)
        else:
            return self.countOccurances(list[1:], target)
        
    # 53. Maximum Subarray
    def maxSubArraySum(self,arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        
        maxSum = arr[0]
        localSum = arr[0]
        
        for i in range(1,n):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            
            
            maxSum = arr[0]
            localSum = arr[0]
            
            for i in range(1,n):
                localSum = max(arr[i], arr[i] + localSum)
                maxSum = max(localSum, maxSum)
            return maxSum

    def RecursionSubset(self,nums, rest):
        if len(rest) == 0:
            return [nums]
        
        curr = rest[:1]
        left = self.RecursionSubset(nums+curr, rest[1:])
        right = self.RecursionSubset(nums, rest[1:])

        left.extend(right)     
        return left

    def bracketGenerator(self,string, counter, limit):

        if(counter == limit):
            return [string]
        
        left = self.bracketGenerator("()"+string, counter+1, limit)
        middle = self.bracketGenerator("("+string+")", counter+1, limit)
        right = self.bracketGenerator(string+"()", counter+1, limit)

        left.extend(middle)
        left.extend(right)

        return list(set(left))

    def reverseNumber(self,number, reversed = 0):
        if number <= 0:
            return reversed
        remainder = number % 10
        reversed = (reversed * 10) + remainder
        return self.reverseNumber(number // 10, reversed)

    def pow(base, exponent):
        if exponent == 0:
            return 1
        if exponent % 2 == 0:
            return pow(base * base, exponent//2) 
        else:
            return base * pow(base, exponent-1)
    # print(reverse_exponentiation(3))

    def reverse_exponentiation(self,n):
        return pow(n,self.reverseNumber(n))

    def reverseNumber(self,number, reversed = 0):
        if number == 0:
            return reversed
            
        remainder = number % 10
        reversed = ( reversed * 10 ) + remainder
        return self.reverseNumber(number // 10, reversed)


    def pow(self,base, exponent):
        if exponent == 0:
            return 1
        if exponent > 0:
            if exponent % 2 == 0:
                return pow(base * base, exponent//2)
            else:
                return base * pow(base, exponent - 1)
        else:
            if exponent % 2 == 0:
                return pow(1/(base * base), -exponent//2)
            else:
                return 1/(base * pow(base, -exponent - 1))

    def bracketGenerator(self, number):
        brackets = []
        
        def bracketHelper(string, left, right):
            if len(string) == 2 * number:
                brackets.append(string)
                return
            
            if left < number:
                bracketHelper(string + "(", left + 1, right)
            
            if right < left:
                bracketHelper(string + ")", left, right + 1)

        bracketHelper("", 0, 0)
        return brackets

    def permute(self,string):
        string.sort()
        permutationsResult = []

        def permutations(index):
            n = len(string)
            if index == n:
                permutationsResult.append(string[:])
                return 
            for i in range(index, n):
                string[i] , string[index] = string[index] , string[i]
                permutations(index+1)
                string[i] , string[index] = string[index] , string[i]

        permutations(0)
        return permutationsResult

    def duplicatesPermutations(self,elements):
        result = []

        def permutations(index):
            n = len(elements)
            if index == n and elements not in result:
                result.append(elements[:])
                return 
            
            for i in range(index, n):
                elements[i] , elements[index] = elements[index] , elements[i]
                permutations(index+1)
                elements[i] , elements[index] = elements[index] , elements[i]
        permutations(0)
        return result
    
    def subsets(self, nums):
        result = []
        def backtrack(path, k):
            result.append(path[:])
            for i in range(k, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        backtrack([],0)        
        return result
    
    def subsetsWithDup(self, nums):
        result = []
        def backtrack(path, k):
            result.append(path[:])
            for i in range(k, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        backtrack([],0)        
        return result
    
    def combine(self, n, level):
        nums = list(range(1, n+1))
        result = []
        def backtrack(path, k, level):
            if len(path) ==  level:
                result.append(path[:])
            elif len(path) > level:
                return
            for i in range(k, len(nums)):
                path.append(nums[i])
                backtrack(path, i+1, level)
                path.pop()
        backtrack([],0,level)        
        return result

    def combinationSum(self, nums, target):
        result = []
        def backtrack(path, target, index):
            if target < 0:
                return
            if target == 0:
                result.append(path[:])
                return
            for i in range(index, len(nums)):
                number = target - nums[i] 
                path.append(nums[i])
                backtrack(path, number, i)
                path.pop()
        backtrack([], target,0)        
        return result
