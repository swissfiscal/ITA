import  requests
import json
#200
payload={'params':'{authCode:\"irpW4HPUO2Hl/9ovh5x/fLF5KqO2s6R16u4w4IPPIe1fmH4RwXE9OoIu9s6+rHAADnDD7z3kP4rF6mUk2vvKlokKEdfxjbO/io/rwGnHSGy2rRC5xVluq1LCtQVBK7HwU27umjwmFEk=\",categoryTags:\"\",Category:\"237816\",SubApp:\"cupboard\",pageIndex:\"1\",pageSize:\"500\",HasRelation:\"true\",width:\"\",depth:\"\",height:\"\"}','command':'DesignMaterial/GetCategoryAndMaterialList'}
#200

#payload={"params":{"authCode":"irpW4HPUO2Enwq+E38z8zhPbYly2WMmK3/tvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS+XjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo/JXbGwd4=","categoryId":"150868","isRender":"true","categoryTagIds":"","IsTagOr":"false","orderBy":"","pageIndex":"1","pageSize":"20","materialName":"","isMyProduct":"false","organId":"","deptId":"","token":""},"command":"DesignMaterial/GetDesignMaterialListByCategoryIdEx"}
#
#jsonstr=json.dumps(payload);
#print  jsonstr
# payload={"params":{"authCode":"irpW4HPUO2Enwq+E38z8zhPbYly2WMmK3/tvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS+XjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo/JXbGwd4=","categoryId":"150868","isRender":"true","categoryTagIds":"","IsTagOr":"false","orderBy":"","pageIndex":"1","pageSize":"20","materialName":"","isMyProduct":"false","organId":"","deptId":"","token":""},"command":"DesignMaterial/GetDesignMaterialListByCategoryIdEx"}
#payload={'authCode':'irpW4HPUO2Enwq+E38z8zhPbYly2WMmK3/tvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS+XjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo/JXbGwd4=','categoryId':'150868','isRender':'true','categoryTagIds':'','IsTagOr':'false','orderBy':'','pageIndex':'1','pageSize':'20','materialName':'','isMyProduct':'false','organId':'','deptId':'','token':'','command':'DesignMaterial/GetDesignMaterialListByCategoryIdEx'}
#payload={'authCode':'irpW4HPUO2Enwq+E38z8zhPbYly2WMmK3/tvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS+XjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo/JXbGwd4=','categoryId':'150868','isRender':'true','categoryTagIds':'','IsTagOr':'false','orderBy':'','pageIndex':'1','pageSize':'20','materialName':'','isMyProduct':'false','organId':'','deptId':'','token':''}
#payload={'params:':'%7b%22authCode%22%3a%22irpW4HPUO2Enwq%2bE38z8zhPbYly2WMmK3%2ftvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS%2bXjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo%2fJXbGwd4%3d%22%2c%22categoryId%22%3a%22150868%22%2c%22isRender%22%3a%22true%22%2c%22categoryTagIds%22%3a%22%22%2c%22IsTagOr%22%3a%22false%22%2c%22orderBy%22%3a%22%22%2c%22pageIndex%22%3a%221%22%2c%22pageSize%22%3a%2220%22%2c%22materialName%22%3a%22%22%2c%22isMyProduct%22%3a%22false%22%2c%22organId%22%3a%22%22%2c%22deptId%22%3a%22%22%2c%22token%22%3a%22%22%7d','command': 'DesignMaterial%252fGetDesignMaterialListByCategoryIdEx'}
#payload={'params:':'%7b%22authCode%22%3a%22irpW4HPUO2Enwq%2bE38z8zhPbYly2WMmK3%2ftvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS%2bXjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo%2fJXbGwd4%3d%22%2c%22categoryId%22%3a%22150868%22%2c%22isRender%22%3a%22true%22%2c%22categoryTagIds%22%3a%22%22%2c%22IsTagOr%22%3a%22false%22%2c%22orderBy%22%3a%22%22%2c%22pageIndex%22%3a%221%22%2c%22pageSize%22%3a%2220%22%2c%22materialName%22%3a%22%22%2c%22isMyProduct%22%3a%22false%22%2c%22organId%22%3a%22%22%2c%22deptId%22%3a%22%22%2c%22token%22%3a%22%22%7d','command':'DesignMaterial%252fGetDesignMaterialListByCategoryIdEx'}
#payload={'authCode':'irpW4HPUO2Enwq+E38z8zhPbYly2WMmK3/tvKLAFTYjenCscwQqpfyql6Ft6P4ErAHJJSLIS+XjdfRSby7CVFJzylTqJ22SM5gIkpb6j2ftJ9ybxJqFMTvKVagNIQBv28xo/JXbGwd4=','categoryId':'150868','isRender':'true','categoryTagIds':'','IsTagOr':'false','orderBy':'','pageIndex':'1','pageSize':'20','materialName':'','isMyProduct':'false','organId':'','deptId':'','token':''}
#payload={'k':'1'}
print  payload
reqheaders={
	'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
'Connection':'keep-alive',
'Content-Length':512,
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'SID=cad5; APISID=api3; SID=cad5',
'Host':'api1.admin.mnmnh.com',
'Origin':'http://img3.admin.mnmnh.com',
'Referer':'http://img3.admin.mnmnh.com/upfile/V2//HouseType.swf?r=20170415002',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
'X-Requested-With':'ShockwaveFlash/20.0.0.228',
}
#reqheaders = {"content-type": "application/json"}
r=requests.post('http://api1.admin.mnmnh.com/Web3D.axd?m=DesignMaterial/GetCategoryAndMaterialList', headers=reqheaders,data=payload)
# r=requests.post('http://httpbin.org/post', data = {'key':'value'})
print r.text
print len((r.text))
