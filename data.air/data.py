# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *
import requests
import json
using("config.air")
from config import BodyData, Header, Url, Token, Platform


def login(devId, platformUid):
    BodyData.update({"command": 10101})
    BodyData['commonParams']['deviceId'] = devId
    BodyData['commonParams']['platformUid'] = platformUid
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    Token = response['accessToken']
    Platform = platformUid


def addResource(item,num,level=0):
    BodyData.update({"command": 9003, "resType": 3, "itemId": item, "resNum": num, "otherData": level, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)


def removeequipment():
    BodyData.update({"command": 9003, "resType": 59, "itemId": 1020001, "resNum": 1, "otherData": 1, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)






                      

