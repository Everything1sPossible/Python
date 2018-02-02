"""
购物车demo
"""
# 商品字典
goods = {1: {
        "name": "矿泉水",
        "price": 1.00,
        "count": 5
    }, 2: {
        "name": "泡面",
        "price": 4.00,
        "count": 10
    }, 3: {
        "name": "火腿肠",
        "price": 2.50,
        "count": 5
    }, 4: {
        "name": "卫生纸",
        "price": 9.78,
        "count": 2
    }
}
goods_buy = {}
print("商品列表:")
for id in goods:
    print(str(id) + ':' + goods[id]["name"] + ' 价格:' + str(goods[id]["price"]) + ' 库存:' + str(goods[id]["count"]))
print()
while True:
    # 选择的商品编号
    choose_for_buyer = input("请选择商品(输入编号即可,按q退出):").strip()
    if choose_for_buyer in ['q', 'Q']:
        print("您已退出!")
        print("您的选择如下:".center(40,"*"))
        if len(goods_buy) == 0:
            print("您没有选择任何商品!")
        else:
            # 总价
            sum_price = 0.00
            for id_for_buyer in goods_buy:
                print(goods_buy[id_for_buyer]["name"] + ":" + str(goods_buy[id_for_buyer]["price"]) + "  " +
                      str(goods_buy[id_for_buyer]["count"]))
                sum_price += goods_buy[id_for_buyer]["price"] * goods_buy[id_for_buyer]["count"]
            print()
            print("总价为:\033[31;1m[%f]\033[0m" % sum_price)
        break
    elif not choose_for_buyer.isdigit():
        print("您的输入有误!")
    elif int(choose_for_buyer) not in goods.keys():
        print("您的选择有误,请重新选择!")
        continue
    else:
        while True:
            # 选择的商品数量
            count_for_buyer = input("请输入购买数量(u:返回上一级):")
            if count_for_buyer in ["u", "U"]:
                break
            elif not count_for_buyer.isdigit():
                print("您的输入有误!")
                continue
            elif int(count_for_buyer) > goods[(int(choose_for_buyer))]["count"]:
                print("超过库存!")
                continue
            else:
                try:
                    # 叠加选择的商品数量(初始数量+选择数量)
                    goods_buy_count = goods_buy[choose_for_buyer]["count"] + int(count_for_buyer)
                except KeyError:
                    # 报异常说明不存在,所以初始数量设为0
                    goods_buy_count = 0 + int(count_for_buyer)
                # 将用户选择加入购物车字典
                goods_buy.setdefault(int(choose_for_buyer), {"name": goods[(int(choose_for_buyer))]["name"],
                                                             "price": goods[(int(choose_for_buyer))]["price"],
                                                             "count": goods_buy_count})
                # 对选择的商品库存进行减少操作
                goods[(int(choose_for_buyer))]["count"] -= int(count_for_buyer)
                print("商品列表:")
                for id2 in goods:
                    print(str(id2) + ':' + goods[id2]["name"] + ' 价格:' + str(goods[id2]["price"]) + ' 库存:' + str(goods[id2]["count"]))
                print()
                break