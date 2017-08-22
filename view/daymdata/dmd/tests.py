from django.test import TestCase

# Create your tests here.
import requests


url="http://wx21.xunxianw.com/index.php?g=Wap&m=Voteimg&a=vote&td_channelid=110114000000&ADTAG=110114000000&vote_id=2173&token=zwkcom1501591964&id=2173"
header={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; 1503-M02 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.2 TBS/036558 Safari/537.36 MicroMessenger/6.3.25.861 NetType/WIFI Language/zh_CN"}
response=requests.get(url,headers=header)


print response.content