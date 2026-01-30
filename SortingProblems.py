class SortingProblems:
    def asteroidsDestroyed(self, mass, asteroids):
        sum = mass
        asteroids.sort()
        for i in asteroids:
            if sum >= i:
                sum = sum+i
            else:
                return False
        return True
    
    def decodeString(self, s):
        
        return