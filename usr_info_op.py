def write_in_file(user, write_type='w'):  # 字典写入文件
	if write_type == 'a':
		fp = open("usr_info", 'a+')
		fp.write(str(user))
		fp.close()
		return 1
	fp = open("usr_info", 'w+')
	fp.write(str(user))
	fp.close()
	return 1


def load_from_file():
	# 从文件中读取字典,返回一个字典对象
	user = {}
	try:
		fp = open("usr_info", 'r+')
		if user.get("admin", 'a') is None:
			user.update({"admin": "admin"})
			write_in_file(user)
	except OSError:
		user.update({"admin": "admin"})
		write_in_file(user)
		load_from_file()
		return user
	user = eval(fp.read())
	fp.close()
	return user
