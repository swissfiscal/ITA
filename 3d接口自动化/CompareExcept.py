#-*- encoding: utf-8 -*-
import json
class common_fun:
    def ERcompare(self,json_except,json_response):
        dic_except=json.loads(json_except)
        dic_result=json.loads(json_response)
        count_k=0
        for k in sorted(dic_except.keys()):
            count_k=count_k+1
            #将预期与实际都转成字符后比较
            if str(dic_except[k])!=str(dic_result[k]):
                result="The result is fail,\nAnd the error key:"+str(k)+"\nThe reslut value is:"+str(dic_result[k])+"\nThe except value is:"+str(dic_except[k])
                break
            else:
                result='pass'
        return result
    
