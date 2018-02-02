"""
练习
"""
citys={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for province in citys.keys():
    print(province)
while True:
    inProvince = input("请输入您选择的省份(q: 退出):").strip()
    if inProvince not in citys and inProvince != "q":
        print("您的输入有误,请重新输入!")
        continue
    elif inProvince == "q":
        print("您已退出!")
        exit()
    else:
        while True:
            for city in citys[inProvince].keys():
                print(city)
            inCity = input("请输入您选择的城市(q: 退出,b:返回省份选择):").strip()
            if inCity not in citys[inProvince] and inCity != "q" and inCity != "b":
                print("您的输入有误,请重新输入!:")
            elif inCity == "q":
                print("您已退出!")
                exit()
            elif inCity == "b":
                print("请重新选择省份!")
                break
            else:
                for county in citys[inProvince][inCity]:
                    print(county)
                exit()

