


import random as r

def get():
	op=""
	for i in range(6):
		op+=str(r.randint(1,9))
	print(op)
	return op

if __name__ == '__main__':
	get()
