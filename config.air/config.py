# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *

TargetChapter = ["20", "25", "30", "35"]
Equipments = {
    "1":[3010114, 3010214, 3010314, 3010314], "2":[3020114, 3020214, 3020314, 3020414], "3":[3030114, 3030214, 3030314, 3030414], 
    "4":[3040114, 3040214, 3040314, 3040414], "5":[3050114, 3050214, 3050314, 3050414], "6":[3060114, 3060214, 3060314, 3060414]}
MaxChapter = 100
Version = 14
Url = 'https://test-punball-v2.habby.com/internal'
Header = {"Content-Type":"application/json"}
Token = ""
Platform = ""
BodyData={
    "command":0,
    "commonParams": {
        "platformUid": Platform,
        "version": Version,
        "deviceId": "",
        "accessToken": ""
    },
    "secret": "acc2eadf31b2729a26efa8589a5dceb4",
}
SignInUrl = "https://wiki-punball.habby.com/login?serverIdx=0&userId=9999999"
ChangeUrl = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=xxx&resNum=999&itemId=1010001&otherData=999"
Headers = {
  'Cookie': 'connect.sid=s%3ATqcWzY0Uj7A7z-T_FKOTHBMsQ5j4G2A4.vcV3nkouF39%2FEblY%2BTsUsMoQVQueHpOqixDVB2HDzu4'
}
DoType = {"coin": "1", "diamonds": "2", "energy": "30", "level": "19", "exp": "25", "mask": "13", "level_id": "4",
          "level_length": "29", "last_login": "33", "login_days": "75", "money": "88", "big_chest": "34",
          "small_chest": "39", "reset_talent": "41", "small_talent": "72", "big_talent": "73", "reset_dailyshop": "36",
          "reset_share": "74", "dailyshop_refresh": "84", "reset_level_chest": "38", "reset_ad": "52",
          "buy_energy_time": "71", "reset_energy_buy": "76", "clear_equipment": "59", "clear_scroll": "80"}


