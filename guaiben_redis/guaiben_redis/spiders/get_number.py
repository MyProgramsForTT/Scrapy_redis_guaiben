import pymysql

class output_id_data(object):
    """
    同步操作
    """
    def search_id(name_data):
        db = pymysql.connect(
            host='47.113.205.237', port=3306, user='root', password='820197450zhao', db='xiaoshuo', charset='utf8')
        cur = db.cursor()
        sql_id = '''select id from books where name='{}' '''.format(name_data)
        book_id = cur.execute(sql_id)
        fields = cur.fetchall()
        book_id = (fields[0])[0]
        return(book_id)
    def numbers(s):  # 转换数字
        dic_num = {"1": "一", "2": "二", "3": "三", "4": "四",
                "5": "五", "6": "六", "7": "七", "8": "八", "9": "久", }
        dic_unit = {1: "", 2: "十", 3: "百", 4: "千", 5: "万"}
        fs = []
        daxie = ""
        num = str(s)
        lennum = len(num)
        if lennum >= 1:
            for item in num:
                if int(item) > 0:
                    fs.append(dic_num[item])
                    fs.append(dic_unit[lennum])
                elif int(item) == 0:
                    fs.append("零")
                lennum -= 1
        while fs[-1] == "零":
            fs.pop()
        daxie = "".join(fs)
        if daxie[0:2] == '一十':
            end = daxie.replace('一十', '十')
            return(end)
        else:
            return(daxie)

