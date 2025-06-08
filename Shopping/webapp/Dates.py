

def get(num):
	import datetime
	d=datetime.datetime.now() + datetime.timedelta(days=num)
	d=str(d)
	d=d.split()
	print(d)
	print(d[0])
	return d[0]
if __name__ == '__main__':
	print(get(2))

