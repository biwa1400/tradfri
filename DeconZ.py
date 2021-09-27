import requests as req
import json

class TRADFRImotionsensor:
    def __init__(self,battery,uniqueid,lastseen,presence,bridgeid):
        self.battery = battery
        self.uniqueid = uniqueid
        self.lastseen = lastseen
        self.presence = presence
        self.bridgeid = bridgeid

    def toJson(self):
        return json.dumps(self.__dict__)

def query():
    #1. connect to deConz
    resp = req.get("http://127.0.0.1/api/4028777175")
    ret = []
    attrList = json.loads(resp.text)
    sensorList = attrList['sensors']
    bridgeid = attrList['config']['bridgeid']


    for i in sensorList:
        sensor = sensorList[i]
        modelid =sensor['modelid']
        if(modelid == 'TRADFRI motion sensor'):
            battery = sensor['config']['battery']
            uniqueid = sensor['uniqueid']
            lastseen = sensor['lastseen']
            presence = sensor['state']['presence']
            ret.append(TRADFRImotionsensor(battery=battery,uniqueid=uniqueid,lastseen=lastseen,presence=presence,bridgeid=bridgeid))


    return ret
