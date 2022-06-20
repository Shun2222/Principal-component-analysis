import xlrd
import pprint
import matplotlib.pyplot as  plt
import numpy as np
from scipy import optimize as opt
def fit_func(x, a, b):
    return a* x + b
def fit_func2(x, a, b, c):
    return a * x**2 + b * x + c
def func(x, y):
	x1 = x.flatten()
	y1 = y.flatten()
	res = opt.curve_fit(fit_func, x1, y1)
	x2 = []
	x3 = []
	a = res[0][0]
	b = res[0][1]
	print("a={}".format(a))
	print("b={}".format(b))
	for i in np.arange(np.min(x1), np.max(x1), 0.1):
		x2.append(a * i + b)
		x3.append(i)
		plt.plot(np.array(x3), np.array(x2))

def func2(x, y):
	x1 = x.flatten()
	y1 = y.flatten()
	res = opt.curve_fit(fit_func2, x1, y1) 
	x2 = []
	x3 = []
	a = res[0][0]
	b = res[0][1]
	c = res[0][2]
	print("a={}".format(a))
	print("b={}".format(b))
	print("c={}".format(c))
	for i in np.arange(np.min(x1), np.max(x1), 0.1):
		x2.append(a * i**2 + b * i + c)
		x3.append(i)
	plt.plot(np.array(x3), np.array(x2))

print('パスの記入をしてください')
p = input()
wb = xlrd.open_workbook(p)
sheets = wb.sheets()
sheet = wb.sheet_by_name('Sheet1')
bool = 'false'
while bool == 'false':
	print('x座標')
	print('行の入力(0から始まる)')
	start_rowx = input()
	end_rowx = input()
	print('列の入力(0から始まる)')
	start_colx = input()
	end_colx = input()
	x = np.array([sheet.row_values(row, int(start_colx), int(end_colx) + 1) for row in range(int(start_rowx), int(end_rowx) + 1)])
	
	print('ｙ座標')
	print('行の入力(0から始まる)')
	start_rowy = input()
	if start_rowy == 'same':
		start_rowy = start_rowx
	end_rowy = input()
	if end_rowy == 'same':
		end_rowy = end_rowx
	print('列の入力(0から始まる)')
	start_coly = input()
	if start_coly[:4] == 'next':
		start_coly = int(start_colx) + int(start_coly[4])
	end_coly = input()
	if end_coly[:4] == 'next':
		end_coly = int(end_colx) + int(end_coly[4])
	y = np.array([sheet.row_values(row, int(start_coly), int(end_coly) + 1) for row in range(int(start_rowy), int(end_rowy) + 1)])
	lab = input('label:')
	plt.scatter(x, y, label=str(lab))
	plt.legend()
	print('Please write 1, 2, 1,2 or nothing')
	f = input()
	if f == '1':
		func(x, y)
	elif f == '2':
		func2(x, y)
	elif f == '1,2':
		func(x, y)
		func2(x, y)
	print('end?')
	if input() == 'end':
			bool=''
plt.grid(True)
plt.show()