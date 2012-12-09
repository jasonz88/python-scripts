hash = {}
input_file = open('HashInt.txt')
for line in input_file:
        Num = int(line.rstrip('\n')) 
        if Num in hash: hash[Num] += 1
        else: hash[Num] = 1
                
def TargetSum(T, Hash):
        for element in Hash:
                if T-element in Hash:
                        return 1
        return 0
        
data = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
result = [TargetSum(i, hash) for i in data]        
print result