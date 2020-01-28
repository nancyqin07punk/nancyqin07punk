#至一千年后的你 BY NANCY QIN秦某南
import time
import datetime

now_str = datetime.datetime.now().strftime('%Y-%m-%d')
now = datetime.datetime.strptime(now_str, "%Y-%m-%d")
future = datetime.datetime.strptime("3020-02-02", "%Y-%m-%d")
days = (future - now).days
print(days)
print("上面的数字，是本程序消失之前所能在北极保存的最大期限（除非有人愿意接手）,单位为天。")
time.sleep(1)
print("......虽然我是从2020年穿越过来的，那时候我还是个五年级小学生，但一千年之后，我的尸体可能都不存在，留下的可能连原子都不剩......")
time.sleep(1)
print("首先是现状。最近，一个名为'2019-ncov‘的新型冠状病毒疯狂传播，各种商店关闭，人们躺在家里娱乐。")
time.sleep(1)
print("一个名叫'微信'的手机应用里传着’熏醋能预防病毒‘等说法，但，这是假的。")
time.sleep(1)
print("再来是个人。最近，我正在开发一款名为“死士之刃”的游戏，如果不能保存到北极的话，或许会永久消失......")
time.sleep(1)
print("就算看到了，也请原谅我的拙劣动画和代码，毕竟在那个时代还需要手写代码，就连我使用的库pygame也是手动编出来的。")
time.sleep(1)
print("说实话，那时候虽然有了CG技术，但是我只能一个人单打独斗，所以......")
time.sleep(1)
print("也许得一千年之后再见了！")
