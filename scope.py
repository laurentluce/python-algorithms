class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        
        diifer=[]
        for i in a:
            for j in a:
                diff=abs(i-j)
                diifer.append(diff)
                
                
        maximumDifference=max(diifer)
        self.maximumDifference=maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
