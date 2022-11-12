sequel = input().split(" ")

for i in range(0, len(sequel)):
	sequel[i] = int(sequel[i])

sequel2 = list(sequel)

for i in range(0, len(sequel)):
	for j in range(0, len(sequel)):
		if(sequel[i] < sequel[j]):
			temp = sequel[i] 
			sequel[i] = sequel[j]
			sequel[j] = temp

print(sequel)
print(sequel2)