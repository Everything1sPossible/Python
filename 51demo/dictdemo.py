id_db = {
    "1": {
        "name": "jack",
        "sex": "男",
        "age": 22
    },
    2: {
        "name": "lucy",
        "sex": "女",
        "age": 20
    }
}
print(id_db)
# 移除
id_db.pop("1")
print(id_db)
# 获取
print(id_db.get(2))
# 更新
id_db2 = {
    2: {
        "name": "jack2"
    }
}
id_db.update(id_db2)
print(id_db)
