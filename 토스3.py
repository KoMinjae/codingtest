
user_input = list(map(int,input().split()))
answer=dict()
answers=""
for i in user_input:
	if i not in answer:
		answer[i]=str(compute(i))

for i in user_input:
	answers+=answer[i]
print(answers)
	