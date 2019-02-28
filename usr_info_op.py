def write_in_file(user, write_type='w'):
    # 字典写入文件，默认写入为覆盖写入
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
        # 文件存在
        fp = open("usr_info", 'r+')
        write_type = 'a'
        # 写入方式以“a”（追加写入）进行
        if user.get("admin") is None:
            user.update({"admin": "admin"})
            write_in_file(user,write_type)
    except OSError:
        # 文件不存在，系统错误
        user.update({"admin": "admin"})
        write_in_file(user)
        load_from_file()
        return user
    user = eval(fp.read())
    fp.close()
    return user
