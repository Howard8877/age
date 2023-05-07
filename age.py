age = input('請問你幾歲?:')
age = int(age)
driving = input('請問你有開過車嗎?:')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
if driving == '有':
	if age >= 18:
		print('很棒')
	else:
		print('無照駕駛!')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照')
	else:
		print('很好沒偷開車')

		

		
