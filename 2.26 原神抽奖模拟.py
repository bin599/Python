#因为原神公告（https://ys.mihoyo.com/main/news/public）常驻5星角色祈愿的综合概率为1.600%，等于62.5分之一，四舍五入，63
#Demo版-2/26 Demo-2
import random
ch = random.randint(1,63)
if ch==1:
    print("五星角色：")
    five = random.randint(1,13)
    if five==1:
        print("魈")
    elif five==2:
        print("甘雨")
    elif five==3:
        print("达达利亚")
    elif five==4:
        print("刻晴")
    elif five==5:
        print("钟离")
    elif five==6:
        print("琴")
    elif five==7:
        print("迪卢克")
    elif five==8:
        print("温迪")
    elif five==9:
        print("可莉")
    elif five==10:
        print("谢菲尔")
    elif five==11:
        print("莫娜")
    elif five==12:
        print("七七")
    elif five==13:
        print("阿贝多")
else:
    print("四星角色：")
    four = random.randint(1,15)
    if four==1:
        print("安伯")
    elif four==2:
        print("丽莎")
    elif four==3:
        print("凯亚")
    elif four==4:
        print("芭芭拉")
    elif four==5:
        print("雷泽")
    elif four==6:
        print("班尼特")
    elif four==7:
        print("诺艾尔")
    elif four==8:
        print("砂糖")
    elif four==9:
        print("迪奥娜")
    elif four==10:
        print("北斗")
    elif four==11:
        print("凝光")
    elif four==12:
        print("香菱")
    elif four==13:
        print("行秋")
    elif four==14:
        print("重云")
    elif four==15:
        print("辛焱")