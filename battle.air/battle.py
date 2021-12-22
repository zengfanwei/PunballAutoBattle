# -*- encoding=utf8 -*-
__author__ = "zengf"

import random
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
using("config.air")
from config import TargetChapter, Equipments
# using("DataSetting.air")
# from DataSetting import UserData
using("data.air")
from data import *

w, h = device().get_current_resolution()
poco = UnityPoco()
poco.use_render_resolution(True,device().get_render_resolution())
# user = UserData(10618220)
login('fd2b61f64d569ea41f8c574e0eae43d1', 'a_2375628593256291647')


def choose_chapter(chapter):  # 选择指定章节
    print(chapter)
    nowChapter = poco("Text_ChapterName").get_text().split(".")[0]
    poco("MainUIPanel(Clone)").child("ScrollView").child("ScrollView").child("Viewport").offspring("LevelItem").offspring("ImageIcon").click()
    target = "第{0}章".format(chapter)
    while not poco(text=target).exists():
        if int(nowChapter) > int(chapter):
            poco.swipe((0.5, 0.75), (0.5, 0), duration=0.3)  # 向上滑动
        else:
            poco.swipe((0.5, 0.25), (0.5, 1), duration=0.3)  # 向下滑动
    sleep(2)
    p = poco(text=target).get_position()
    while p[1] < 0.05 or p[1] > 0.95:
        if p[1] < 0.1:
            poco.swipe((0.5, 0.25), (0.5, 1))  # 向下滑动
        if p[1] > 0.75:
            poco.swipe((0.5, 0.75), (0.5, 0))  # 向上滑动
        p = poco(text=target).get_position()
    if p[1] > 0.5:
            poco.swipe((0.5, 0.75), (0.5, 0.25))  # 向上滑动
    else:
            poco.swipe((0.5, 0.25), (0.5, 0.5))  # 向下滑动
    sleep(2)
    poco(text=target).click()
    poco("Text_Start").click()
    
def battle():   # 战斗
    poco("Item0").child("SkillButton").wait_for_appearance()
    poco("Item0").child("SkillButton").click()
    sleep(2)
    while not poco("BuyRebornDialog").exists() and not poco("TestGameOverUIPanel").exists():
        if poco("ChooseSkillUIPanel").exists():
            poco("Item0").child("SkillButton").click()
        touch(v=(0.16*w, 0.8*h), duration=0.5)
        touch(v=(0.84*w, 0.8*h), duration=0.5)
        
    if poco("BuyRebornDialog").exists():
        poco(texture="UICommon_Close").click()
    sleep(2)
    # 处理用户升级
    if poco("ExpLevelUpUIPanel").exists():
        poco("TextClose").click()
    sleep(5)
    poco("childParent").click()
    sleep(1)
    if poco("childParent").exists():
        poco("childParent").click()
        sleep(2)
    # 处理金猪弹窗
    if poco("PiggyUnlockPanel").exists():
        poco("DecorateTop").click()
        poco(texture="UICommon_Close").click()
    if poco("PiggyPurchasePanel").exists():
        poco(texture="UICommon_Close").click()
    # 处理限时礼包弹窗
    if poco("SuperLimitGiftPanel").exists():
        poco("level").click()
        
def remove_equipment():   # 脱装备
    poco(texture="MainUI_Button_Equip").click()
    sleep(2)
    equip = "EquipBG"
    for i in range(6):
        poco(equip+str(i)).click()
        poco("wear").click()
    sleep(1)
    poco(texture="MainUI_Button_Home").click()
            
def wear_equipment():   # 穿装备
    poco(texture="MainUI_Button_Equip").click()
    sleep(2)
    for i in range(6):
        if h < 2*w:
            touch(v=(0.16*w, 0.7*h), duration=0.5)
        if h == 2*w:
            touch(v=(0.16*w, 0.62*h), duration=0.5)
        if h > 2*w:
            touch(v=(0.16*w, 0.55*h), duration=0.5)
        sleep(1)
        poco("ButtonWear").click()
    sleep(1)
    poco(texture="MainUI_Button_Home").click()
        
def app_home():  # 且后台再回来同步数据
    device().home()
    device().start_app("com.habby.punball")
    
def add_equipment(chapter):  # 后台添加装备
    for e in Equipments.keys():
        addResource(random.choice(Equipments[e]),1,60)
        # user.add_prop(1, e, 60)
        
for chapter in TargetChapter:
    removeequipment()
    add_equipment(chapter)
    app_home()
    wear_equipment()
    choose_chapter(chapter)
    battle()
    remove_equipment()
    # user.delete_equipment()
    removeequipment()

