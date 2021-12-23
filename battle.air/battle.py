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
import logging
import os
from concurrent_log_handler import ConcurrentRotatingFileHandler
logger = logging.getLogger(__name__)
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
filehandler = ConcurrentRotatingFileHandler(filename="./autobattle.log", maxBytes=5 * 1024 * 1024, backupCount=2, encoding='utf-8')
filehandler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(filehandler)

w, h = device().get_current_resolution()
poco = UnityPoco()
poco.use_render_resolution(True, device().get_render_resolution())
# user = UserData(10618220)
login('fd2b61f64d569ea41f8c574e0eae43d1', 'a_2375628593256291647')


def choose_chapter(chapter):  # 选择指定章节
    logger.info("开始选择章节！")
    logger.info("需要选择的章节id：{}".format(chapter))
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
    while p[1] < 0.1 or p[1] > 0.9:
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
    logger.info("成功选择章节！")
    poco("Text_Start").click()
    
def battle(chapter):   # 战斗
    logger.info("开始战斗！")
    poco("Item0").child("SkillButton").wait_for_appearance()
    poco("Item0").child("SkillButton").click()
    sleep(2)
    while not poco("BuyRebornDialog").exists() and not poco("TestGameOverUIPanel").exists():
        if poco("ChooseSkillUIPanel").exists():
            skill = poco("Item0").child("SkillButton").child("Child").child("fg").child("SkillName").get_text()
            poco("Item0").child("SkillButton").click()
            logger.info("学习技能：{0}".format(skill))
        touch(v=(0.16*w, 0.8*h), duration=0.5)
        touch(v=(0.84*w, 0.8*h), duration=0.5)
    if poco("BuyRebornDialog").exists():
        poco(texture="UICommon_Close").click()
    sleep(3)
    logger.info("通关，到结算界面！")
    snapshot(filename=os.path.abspath(os.path.dirname(__file__))+'//chapter{0}.jpg'.format(chapter))
    # 处理用户升级
    if poco("ExpLevelUpUIPanel").exists():
        poco("TextClose").click()
        logger.info("玩家升级！")
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
        logger.info("玩家解锁金猪！")
    if poco("PiggyPurchasePanel").exists():
        poco(texture="UICommon_Close").click()
        logger.info("玩家弹出金猪广告！")
    # 处理限时礼包弹窗
    if poco("SuperLimitGiftPanel").exists():
        poco("level").click()
        logger.info("玩家弹出限时礼包！")
    logger.info("战斗结束，回到主界面！")
        
def remove_equipment():   # 脱装备
    logger.info("开始脱装备！")
    poco(texture="MainUI_Button_Equip").click()
    sleep(2)
    equip = "EquipBG"
    for i in range(6):
        poco(equip+str(i)).click()
        poco("wear").click()
    sleep(1)
    poco(texture="MainUI_Button_Home").click()
    logger.info("脱完装备，回到主界面！")
            
def wear_equipment():   # 穿装备
    logger.info("开始穿装备！")
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
    logger.info("穿完装备，回到主界面！")
        
def app_home():  # 且后台再回来同步数据
    device().home()
    logger.info("游戏切到后台！")
    device().start_app("com.habby.punball")
    logger.info("后台切回游戏！")
    
def add_equipment():  # 后台添加装备
    logger.info("开始添加装备！")
    # 添加10体力
    addResource(1040001,20,0)
    logger.info("添加20点体力！")
    for e in Equipments.keys():
        equip = random.choice(Equipments[e])
        addResource(equip,1,60)
        logger.info("添加了装备：{0}".format(str(equip)))
        # user.add_prop(1, e, 60)
    logger.info("添加装备结束！")
        
for chapter in TargetChapter:
    logger.info("开始测试！")
    removeequipment()
    logger.info("成功删除装备！")
    add_equipment()
    app_home()
    wear_equipment()
    choose_chapter(chapter)
    battle(chapter)
    remove_equipment()
    # user.delete_equipment()
    removeequipment()
    logger.info("成功删除装备！")
logger.info("测试结束！")


