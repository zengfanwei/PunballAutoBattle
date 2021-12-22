# -*- encoding=utf8 -*-
__author__ = "stars"

from airtest.core.api import *
import requests
import json
using("config.air")
from config import Headers, SignInUrl, ChangeUrl, DoType


class UserData:
    def __init__(self, gameuid):
        self.gameuid = str(gameuid)

    def _request(self, *args, **kwargs):
        res = requests.request(*args, **kwargs)
        return res

    def signin(self):
        url = SignInUrl.replace("9999999", self.gameuid)
        print(url)
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("登录弹球后台工具失败！"))
        return resdata

    def change_data(self, module, num):  # 通用修改数据的方法，不包括发道具、重置分享领取记录、
        url = ChangeUrl.replace("xxx", DoType[module]).replace("999", str(num))
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("修改账号数据失败！"))
        return res

    def add_prop(self, num, itemid, level):  # 添加道具
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=3&resNum={0}&itemId={1}&otherData={2}".format(str(num), str(itemid), str(level))
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        Headers["Cookie"] = str(res.request.headers["Cookie"])
        if resdata["code"] != 0:
            raise (Exception("给账号添加道具失败！"))
        return res

    def delete_equipment(self):  # 删除装备
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=59&resNum=1&itemId=1020001&otherData=1"
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("删除账号装备失败！"))
        return res

    def delete_account(self):  # 删除账号
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=22&resNum=1&itemId=1040031&otherData=1"
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("删除账号失败！"))
        return res

    def create_new_uid(self):
        self.delete_account()
        punball = PunballApi()
        newdate = punball.login()
        uid = newdate["userId"]
        with open(self.userdata_path, "w") as f:
            f.write(uid)


if __name__ == '__main__':
    user = UserData(90000428)
#     print(user.signin())
#     # user.create_new_uid()
#     # user.add_prop(1, 3020106, 20)
#     user.delete_equipment()
