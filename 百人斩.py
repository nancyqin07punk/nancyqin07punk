#作者于2020-10-04加入的攻略：达成‘打破换弹必死定律’成就三秒后输入07可解锁没什么用的隐藏书信。
import time
import random
print("某南文游之百人斩")
print("请输入散弹枪或双刀来选择武器！")
weapon=input()
gun=['散弹枪']
if weapon in gun:
    print("成功装备散弹枪！")
    time.sleep(3)
else:
    print("成功装备双刀！")
    time.sleep(3)
print("战斗开始！put your hands on the keyboard!")
time.sleep(3)
if weapon in gun:
    print("你用散弹枪击杀1人！还剩99人！")
    double_kill=[2,4,6,8,10,12,14,16,18,20]
    real=random.randint(1,20)
    time.sleep(1)
    if real in double_kill:
        print("穿透一击！你使用散弹枪击杀2人！还剩97人！")
    else:
        print("你使用散弹枪击杀1人！还剩98人！")
    time.sleep(3)
    if real in double_kill:
        print("你使用散弹枪击杀1人！还剩96人！")
    else:
        print("你使用散弹枪击杀1人！还剩97人！")
    time.sleep(3)
    if real in double_kill:
        print("你使用散弹枪击杀1人！还剩95人！")
    else:
        print("你使用散弹枪击杀1人！还剩96人！")
    time.sleep(3)
    if real in double_kill:
        print("你使用散弹枪击杀1人！还剩94人！")
    else:
        print("你使用散弹枪击杀1人！还剩95人！")
    print("没子弹了！大招已就绪!")
    print("请输入换弹或者大招来决定操作！")
    scene_skill=input()
    kill=['大招']
    if scene_skill in kill:
         print("你发动了杀神一击！一切都结束了......")
         time.sleep(1)
         print("‘垃圾玩意儿！’唯一一名幸存者说道。")
         time.sleep(1)
         print("请你输入换弹或者徒手肉搏！")
         fight=['徒手肉搏']
         decide=input()
         if decide in fight:
             print("1 连击！")
             time.sleep(0.5)
             print("2 连击！")
             time.sleep(0.5)
             print("3 连击！")
             time.sleep(0.5)
             print("4 连击！")
             time.sleep(0.5)
             print("5 连击！")
             time.sleep(0.5)
             print("幸存者被你打成重伤......'老子不服气！！！'")
             time.sleep(1)
             print("此时正好有两个大招！地狱之火和夜凯！")
             print("请输入对应的大招！")
             nightmare=input()
             fight_skill=['地狱之火']
             if nightmare in fight_skill:
                 blood=[13,14,35,37,36,46,27,38,65,75,68]
                 attack=random.randint(1,80)
                 if attack in blood:
                    print("血量不足！无法发动此技能！")
                    time.sleep(1)
                    print:("幸存者打出了刺拳！你尽力看了看地板上的血......")
                    time.sleep(1)
                    print("在生命的最后一刻，你听见幸存者笑道：‘兵者，诡道也！’")
                    time.sleep(1)
                    print("百人斩任务失败！")
                    time.sleep(1)
                    print("获得成就：悲情结局")
                    time.sleep(1)
                    print("NANCY QIN秦某南作品 QQ：2164558817")
                    print("微博：https://weibo.com/nancyqin07punk/")
                    time.sleep(3)
                 else:
                    print("地狱之火发射成功！随着时间推移，幸存者变成了原子......")
                    time.sleep(1)
                    print("百人斩任务成功！")
                    time.sleep(1)
                    print("获得成就：科学的魅力")
                    time.sleep(1)
                    print("NANCY QIN秦某南作品 QQ：2164558817")
                    print("微博：https://weibo.com/nancyqin07punk/")
                    time.sleep(3)
             else:
                     respawn=[12,53,25,26,82,73,16,18]
                     alive=random.randint(1,85)
                     if alive in respawn:
                         print("你向幸存者发动了夜凯！你快要挂了！")
                         time.sleep(1)
                         print("这时，一位会阴阳遁之术的路人路过！他复活了你！")
                         time.sleep(1)
                         print("百人斩任务成功！")
                         time.sleep(1)
                         print("获得成就：王者归来")
                         time.sleep(1)
                         print("NANCY QIN秦某南作品 QQ：2164558817")
                         print("微博：https://weibo.com/nancyqin07punk/")
                         time.sleep(3)
                     else:
                         print("你向幸存者发动了夜凯！你快要挂了！")
                         time.sleep(1)
                         print("没人愿意理你......你与幸存者同归于尽。")
                         time.sleep(1)
                         print("百人斩任务失败！")
                         time.sleep(1)
                         print("获得成就：同归于尽")
                         time.sleep(1)
                         print("NANCY QIN秦某南作品 QQ：2164558817")
                         print("微博：https://weibo.com/nancyqin07punk/")
                         time.sleep(3)
         else:
             print("换弹成功！你将五发子弹都怼在幸存者身上了！")
             time.sleep(1)
             print("你望了望满是子弹壳和血的地板。")
             time.sleep(1)
             print("百人斩任务成功！")
             time.sleep(1)
             print("获得成就：打破换弹必死定律")
             time.sleep(1)
             print("NANCY QIN秦某南作品 QQ：2164558817")
             print("微博：https://weibo.com/nancyqin07punk/")
             time.sleep(3)
             bonus=input()
             target=['07']
             if bonus in target:
                 print("恭喜你发现隐藏书信！总之，百人斩2将使用pygame，并且加入地狱模式万人斩！！！")
                 print("undefined 2020.01.14")
                 time.sleep(3)
    else:
        print("士兵们趁你换弹时将你击杀......")
        time.sleep(1)
        print("百人斩任务失败！")
        time.sleep(1)
        print("未获得成就")
        time.sleep(1)
        print("NANCY QIN秦某南作品 QQ：2164558817")
        print("微博：https://weibo.com/nancyqin07punk/")
        time.sleep(3)
else:
    print("你进入了武器库，发现有两种刀：立体机动美工刀和自爆飞刀。")
    print("请输入美工刀或者飞刀！")
    motion=['美工刀']
    knife=input()
    if knife in motion:
        time.sleep(1)
        print("你拿起了立体机动美工刀。")
        time.sleep(1)
        print("战斗开始！！！现在要飞起来吗？(请输入是或不是）")
        fly_motion=input()
        fly=['是']
        if fly_motion in fly:
            print("你飞起来了！！！")
            time.sleep(1)
            print("凭借你熟练的身段，你一举斩杀了3人！！！还剩97人！")
            print("此时，你想滑地还是飞天呢？（请输入对应文字）")
            body_motion=['飞天']
            choice=input()
            if choice in body_motion:
                time.sleep(1)
                print("你模仿着经典动作，还一边大喊：老子发过誓的！！！")
                time.sleep(1)
                print("你一举砍了96个人！！！你看了看沾上了血的立体机动美工刀和手......")
                time.sleep(1)
                print("你决定砍最后一个人的哪个部位？(后颈或手臂）")
                crush=input()
                body_part=['后颈']
                if crush in body_part:
                    print("最后一个人也倒下了！！！")
                    time.sleep(1)
                    print("百人斩任务成功！")
                    time.sleep(1)
                    print("获得成就：自由之翼")
                    time.sleep(1)
                    print("NANCY QIN秦某南作品 QQ：2164558817")
                    print("微博：https://weibo.com/nancyqin07punk/")
                    time.sleep(3)
                else:
                    print("他突然把你推到地上......你只能尽力看见刀光剑影和飙血效果了......")
                    time.sleep(1)
                    print("百人斩任务失败！")
                    time.sleep(1)
                    print("获得成就：将意义托付给下一个生者")
                    time.sleep(1)
                    print("NANCY QIN秦某南作品 QQ：2164558817")
                    print("微博：https://weibo.com/nancyqin07punk/")
                    time.sleep(3)
            else:
                print("这时突然跑出来一个名叫熊还(hai)梓的人，将立体机动美工刀摧毁......")
                time.sleep(1)
                print("那些死士们也冲上来了！！！")
                time.sleep(1)
                print("百人斩任务失败！")
                time.sleep(1)
                print("获得成就：为自由而死")
                time.sleep(1)
                print("NANCY QIN秦某南作品 QQ：2164558817")
                print("微博：https://weibo.com/nancyqin07punk/")
                time.sleep(3)
        else:
            print("你斩杀了1人！还有99个人！")
            time.sleep(1)
            print("就在此时，立体机动装置出了故障，猛然把你带到了超合金天花板上......")
            time.sleep(1)
            print("百人斩任务失败！")
            time.sleep(1)
            print("获得成就：人型装甲弹")
            time.sleep(1)
            print("NANCY QIN秦某南作品 QQ：2164558817")
            print("微博：https://weibo.com/nancyqin07punk/")
            time.sleep(3)
    elif knife=='飞刀':
        time.sleep(1)
        print("你拿起了自爆飞刀。")
        time.sleep(1)
        print("战斗开始！！！你选择先发制人还是后发制人？(输入对应文字）")
        front=['先发制人']
        action=input()
        if action in front:
            print("此时，一个穿着深蓝铠甲的战士走了过来......")
            time.sleep(1)
            print("’鼠辈，安敢抄我武器？‘你只看到了地板上的血......")
            time.sleep(1)
            print("百人斩任务失败！")
            time.sleep(1)
            print("获得成就：抄袭之人")
            time.sleep(1)
            print("NANCY QIN秦某南作品 QQ：2164558817")
            print("微博：https://weibo.com/nancyqin07punk/")
            time.sleep(3)
        else:
            print("你上去就徒手干掉了一个穿着深蓝铠甲自称’亚诺方舟‘的家伙！还剩99个人！")
            time.sleep(1)
            print("随后，一阵震耳欲聋的爆炸声响起......")
            time.sleep(1)
            print("百人斩任务成功！")
            time.sleep(1)
            print("获得成就：核爆探员")
            time.sleep(1)
            print("NANCY QIN秦某南作品 QQ：2164558817")
            print("微博：https://weibo.com/nancyqin07punk/")
            time.sleep(3)
            
    else:
        print("你两种刀都没拿起来，还快速地抽出了一把狗腿刀！")
        time.sleep(1)
        print("战斗开始！！！不过有一个人把刀插到你的额头上......")
        time.sleep(1)
        print("你这辈子听到的最后一句话是：’XXS竟敢把CF武器拿来百人斩！‘")
        time.sleep(1)
        print("百人斩任务失败！")
        time.sleep(1)
        print("获得成就：XXS")
        time.sleep(1)
        print("NANCY QIN秦某南作品 QQ：2164558817")
        print("微博：https://weibo.com/nancyqin07punk/")
        time.sleep(3)
        
            
                   
