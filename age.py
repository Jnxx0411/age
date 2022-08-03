driving = input('請問你有開過車嗎? ')
if driving != '有' and driving != '沒有':
	raise SystemExit

age = input('請問年齡為? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼在開車')
if driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('再過幾年你就可以開車了')