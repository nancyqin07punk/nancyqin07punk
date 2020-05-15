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
print("......以上都是我在2020年2月编辑的原文......接下来开始正文")
time.sleep(1)
print("现在是2020年5月，‘2019-ncov’已经在国内基本得到控制，可是全球疫情还未结束。")
time.sleep(1)
print("没什么可以说的了.......")
time.sleep(1)
print("也许得一千年之后再见了！")
