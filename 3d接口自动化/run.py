#-*- encoding: utf-8 -*-
'''
Created on 2015��9��5��
@author: Administrator
'''
import configparser
import time
from ReadExcel import TestCase
from CompareExcept import common_fun
from confighttp_Requests import Confighttp
from Report import HtmlForm
#执行测试用例的类。
class C_CaseRun(object):
    '''初始化组合用例路径得到：
        1、用例根路径。
        2、用例配置路径。
        3、独立用例路径
        4、组合用例路径
    '''
    global null
    null='None'
    #用例总路径
    CasePath=''
    #用例配置路径
    CaseConfPath=''
    #独立接口用例路径
    IndependentPath=''
    #组合用例路径
    CombPath=''
    #独立配置结果
    Dic_IConf={}
    #组合配置结果
    Dic_CConf={}
#初始执行时读取配置文件，并获取用例根路径
#     def __init__(self):
#         self.name=C_CaseRun
#加强prinTV
    def printTV(self,**variable):
        for i in variable:
            temp=i+": Type:"+str(type(variable[i]))+'Value:'+str(variable[i])
            print(temp)
    '''
__init_功能：初始化该类所需要的属性。
    '''
    def __init__(self,ConfName):
        self.name=C_CaseRun
        config=configparser.ConfigParser()
        config.read(ConfName)
        #用例根路径
        self.CasePath=config.get("Path", "CasePath")
        #组合用例路径
        self.CombPath=self.CasePath+config.get("Path", "CombPath")
        #独立用例路径
        self.IndependentPath=self.CasePath+config.get("Path", "IndependentPath")
        #配置路径
        self.CaseConfPath=self.CasePath+config.get("Path","ConfigPath")
        self.CaseConfPath=self.CaseConfPath+'InterfaceConfig.xlsx'
        self.Dic_IConf=self.__ReadCaseConf('Independent')
        self.Dic_CConf=self.__ReadCaseConf('Comb')
    '''函数名：__ReadCaseConf
输入：用例配置路径(CaseConfPath)。
输出：输出：以接口名(IntfaceName)为key，以接口所对应的行数据为value的字典。
依赖函数：ReadExcel.TestCase.ListCase()
    '''
    def __ReadCaseConf(self,sheetnames):
        list_CaseConf=[]
        Dic_Conf_Result={}
        TempConfig=TestCase()
        i=-1
        TempConfig.ListCase(self.CaseConfPath,sheetnames, list_CaseConf)
        list_CaseConf=TempConfig.list_testcase
        for TempDic in list_CaseConf:
            i=i+1
            key=TempDic['IntfaceName']  
            value=list_CaseConf[i]
            Dic_Conf_Result[key]=value
        return Dic_Conf_Result
    '''函数名：IDPDTCaseRun
输入：用例路径:CasePath(配置文件获取),接口名：ITFCName
输出：失败得到
依赖函数：ReadCaseConf    
    '''    
    def IDPDTCaseRun(self,ITFCName,newhost):
        tempIndependentPath=self.IndependentPath
        self.IndependentPath=self.IndependentPath+ITFCName+'.xlsx'
        list_CaseRun=[]
        list_result=[]
        #用例绝对路径
        print(self.IndependentPath)
        HtmlFormA=HtmlForm()
        TempIndependent=TestCase()
        TempIndependent.ListCase(self.IndependentPath,'TestCase', list_CaseRun)
        list_CaseRun=TempIndependent.list_testcase
        IndependentConf=self.Dic_IConf[ITFCName]
        ConfighttpA=Confighttp()
        common_funA=common_fun()
        #判断请求方式并根据结果发送相应报文
        if IndependentConf['RequestType']=='post':
            Temp_url=IndependentConf['URL']
            payload=eval(IndependentConf['Request_Data'])#此时是字符需转成字典。
            # print 'Request_Data',IndependentConf['Request_Data']
            #headers = {"content-type": "application/json"}

            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
                'Connection': 'keep-alive',
                'Content-Length': '512',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'SID=cad5; APISID=api3; SID=cad5',
                'Host': 'api1.admin.mnmnh.com',
                'Origin': 'http://img3.admin.mnmnh.com',
                'Referer': 'http://img3.admin.mnmnh.com/upfile/V2//HouseType.swf?r=20170415002',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                'X-Requested-With': 'ShockwaveFlash/20.0.0.228',
            }
            #找机会处理下
            #遍历list_CaseRun
            Templist_Dicresponse=[]
            dic_post_payload={}
            #temp_result=[]
            #遍历执行每条用例
            for case_dic in list_CaseRun:
            #遍历请求数据
                temp_listdic=[]
                for key in payload:
                    #将用例中的字段通过配置文件中的Request_Data映射
                    Temp_payload=case_dic[payload[key]]
                    dic_post_payload[key]=Temp_payload
                Requests=dic_post_payload
                json_response=ConfighttpA.post(Temp_url, Requests, headers)
                Response=json_response
                temp_result=common_funA.ERcompare(case_dic['except'], json_response)
                Templist_Dicresponse.append(temp_result)
                Case_ID=case_dic['case_id']
                Description=case_dic['description']
                Result=temp_result
                temp_listdic.append({'Case_ID':Case_ID})
                temp_listdic.append({'Description':Description})                
                temp_listdic.append({'Request':str(Requests)})
                temp_listdic.append({'Response':Response})
                temp_listdic.append({'Result':Result})
#                 print("temp_listdic",temp_listdic)
#                 print(temp_listdic)
                list_result.append(temp_listdic)
#                 self.printTV(Request=dic_post_payload,\
#                         Case_ID=case_dic['case_id'])   
            #将结果写入html
#             return Templist_Dicresponse                      
        else:
            pass
        fail_count=0
        for i in list_result:
            if i[4]['Result'] != 'pass':
                fail_count = fail_count+1
        print  'fail_count:',fail_count

        Temptime = time.strftime('%Y%m%d%H%m%S', time.localtime(time.time()))

        if fail_count > 0:
            p_in_filename=self.CasePath+'Report\Independent\\'+'Fail_'+newhost+'_'+Temptime+'_'+ITFCName+'.html'
        else:
            p_in_filename=self.CasePath+'Report\Independent\\'+'Pass_'+newhost+'_'+Temptime+'_'+ITFCName+'.html'

        HtmlFormA.CreatHtml(in_tittle=ITFCName, in_str='test', in_list=list_result, \
        in_filename=p_in_filename)
        #路径还原
        self.IndependentPath=tempIndependentPath
        print ITFCName,"Run Over Time:",Temptime
    '''函数名：CompCaseRun
输入：用例路径:CasePath,接口名：ITFCName
输出：失败得到
依赖函数：ReadCaseConf
    ''' 
    def CombCaseRun(self,ITFCName):
        print('CombPath',self.CombPath)
        temp_CombPath=self.CombPath
        self.CombPath=self.CombPath+ITFCName+'.xlsx'
        list_CaseRun=[]
        TempComp=TestCase()
        HtmlFormA=HtmlForm()
        #得到用例列表。
        TempComp.ListCase(self.CombPath,'TestCase', list_CaseRun)
        list_CaseRun=TempComp.list_testcase
#         print("list_CaseRun",list_CaseRun)
        CombConf=self.Dic_CConf[ITFCName]
        ConfighttpA=Confighttp()
        common_funA=common_fun()
        #判断请求方式并根据结果发送相应报文
        #注意当前仅适用于只需关联一个独立接口的情况，需改进
        relevance_Interface=eval(CombConf['relevance_Interface'])
        #根据关联接口映射到独立接口信息
#         print('relevance_Interface',type(relevance_Interface),relevance_Interface)
        print('errorinfo:',relevance_Interface)
        temp_key=relevance_Interface["InterfaceName"]
#         print("temp_key",temp_key)
        IndependentConf=self.Dic_IConf[temp_key]
        Templist_Dicresponse_comb=[]
        print("IndependentConf",IndependentConf)
        #映射到独立接口。
        #注意此处较繁琐，以后将该代码独立出来。用于处理独立接口。
#         for i in range(len(list_CaseRun)):
        '''
        获取关联值：
        1、映射关联接口。
        2、往关联接口发送数据。
        3.取关联接口发送送据后的返回报文。
        4.获取需要的关联值
        '''
        if IndependentConf['RequestType']=='post':
            Temp_url=IndependentConf['URL']
#             payload=eval(IndependentConf['Request_Data'])
            #headers = {"content-type": "application/json"}

            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
                'Connection': 'keep-alive',
                'Content-Length': 512,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'SID=cad5; APISID=api3; SID=cad5',
                'Host': 'api1.admin.mnmnh.com',
                'Origin': 'http://img3.admin.mnmnh.com',
                'Referer': 'http://img3.admin.mnmnh.com/upfile/V2//HouseType.swf?r=20170415002',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
                'X-Requested-With': 'ShockwaveFlash/20.0.0.228',
            }
            print(len(list_CaseRun))
            #用于存放测试结果
            
            list_result=[]
            #遍历执行用例列表
            for i in range(len(list_CaseRun)):
                #用于存放每一条用例的执行结果
                temp_listdic=[]
                #用于获取关联
                print("次数：",i,)
                temp_dic=list_CaseRun[i]
                if temp_dic['RunFlag']=='1':
                    pass
#                 print(temp_dic)
                Case_ID=temp_dic['case_id']
                Description=temp_dic['Description']
                payload=eval(IndependentConf['Request_Data'])
                for temp_key in payload:
                    temp_relvence_key="relevance_"+payload[temp_key]
                    payload[temp_key]=temp_dic[temp_relvence_key]
                print("关联数据：",payload)
                json_response=ConfighttpA.post(Temp_url, payload, headers)
                print("关联返回报文：",type(json_response),json_response)
#                 json_response=eval(json_response)
#                 print(json_response['userinfo']['token'])
                #将从关联接口中得到的报文转换问字典并临时存放在temp_dic中。
                temp_dic=eval(json_response)
#                 print(relevance_Interface)
                #将需要关联的值放入 temp_dic_relevance中
                temp_dic_relevance=relevance_Interface['relevanceValue']
                
                #强制转行关联结果，如果是字典再处理
#                 print(type(temp_dic['userinfo']))
                print("temp_dic is:",type(temp_dic),temp_dic)
                for temp_key in  temp_dic:
                    print(temp_key)
                #判断temp_dic是否有双层字典，若有二层字典则将二层字典赋值给temp_dic_two
                    if type(temp_dic[temp_key]) is dict:
                        temp_dic_two=temp_dic[temp_key]
                        print("temp_dic_two",temp_dic_two)
                        break
                    else:
                        temp_dic_two=temp_dic 
                #遍历temp_dic_relevance利用key将得到的关联值存入temp_dic_relevance
                for temp_key in temp_dic_relevance:                  
                    if temp_key in temp_dic_two.keys():
                        temp_dic_relevance[temp_key]=temp_dic_two[temp_key]
                    else:
                        print('relevance fail\'s key is:',temp_key)
                        continue
                #获取的关联值
#                 print(temp_dic_relevance)
#                 print(list_CaseRun[i])
                #将关联值与用例值组装
                #1.将组合接口映射到组合接口文档中
                temp_dic_case=list_CaseRun[i]#组合用例
                temp_dic_comb=self.Dic_CConf[ITFCName]
                if temp_dic_comb['RequestType']=='post':
                    temp_url_comb=temp_dic_comb['URL']
                    temp_payload_comb=eval(temp_dic_comb['Request_Data'])
                    headers = {"content-type": "application/json"}
                    temp_result_comb=[]
                    print("要发送的数据:",temp_payload_comb)
                    print("完整用例:",type(temp_dic_case),temp_dic_case)
                    #先将用例文件中值映射到要要发送的数据中
                    print(temp_payload_comb)
                    print("temp_dic_case",temp_dic_case)
                    #遍历要发模板中的requests
                    for temp_key_comb in temp_payload_comb:
                        temp_list=[]
                        #将字典存放在temp_list中，用于后续关联
                        for temp_key in temp_dic_case:
                            temp_list.append(temp_key)
                        print("temp_list",temp_list) 
                        #将value临时存放在一个变量中。
                        temp_value=temp_payload_comb[temp_key_comb]
                        if temp_value[:5]!='$data':
                            temp_payload_comb[temp_key_comb]=temp_dic_case['data_'+temp_key_comb]
                        else:
                            pass
                        print(temp_payload_comb)
                    #关联值组装
                    for i in temp_list:    
                        if i[:5]=='$data':
                            print('i值：',i)
                            print('原用例值',temp_dic_case[i])
                            print(temp_dic_case)
                            temp_a=temp_dic_case[i]
                            print(temp_payload_comb)
                            temp_value=temp_payload_comb[i[6:]]
                            print(temp_value)
                            temp_b=temp_value
                            print('a:',type(temp_a),temp_a)
                            print('b:',temp_b)
                        else:
                            continue
                    if temp_a==temp_b:
                        print('a is b')
                        temp_payload_comb[temp_key_comb]=temp_dic_case[temp_value]
                        #将关联值组装到需要发送的变量中
                        for temp_key_comb in temp_dic_relevance:
                            temp_payload_comb[temp_key_comb]=temp_dic_relevance[temp_key_comb]
                    else:
                        for temp_key_comb in temp_dic_relevance:
                            temp_payload_comb[temp_key_comb]=temp_a
                    print("最终需要发送的数据为：",temp_payload_comb)
                    Requests=temp_payload_comb
                    #发送数据
                    json_response=ConfighttpA.post(temp_url_comb, temp_payload_comb, headers)
                    print("注册返回报文：",json_response)
                    Response=json_response
                    print("temp_dic_case:",temp_dic_case)
                    temp_result_comb=common_funA.ERcompare(temp_dic_case['except'], json_response)
                    Result=temp_result_comb
                    print("测试结果：",temp_result_comb)
                    print('Templist_Dicresponse_comb ',type(Templist_Dicresponse_comb))
                    Templist_Dicresponse_comb.append(temp_result_comb) 
                else:
                    pass
                temp_listdic.append({'Case_ID':str(Case_ID)})
                temp_listdic.append({'Description':Description})
#                     print('Request:',i,':',type(Requests))
#                    
                temp_listdic.append({'Request':str(Requests)})
                temp_listdic.append({'Response':str(Response)})
#                     print(type(Response))
                temp_listdic.append({'Result':Result})
#                     print("temp_listdic",temp_listdic)
#                     print(temp_listdic)
                print('temp_listdic:',temp_listdic)
                list_result.append(temp_listdic)
#                     print('list_result1',list_result)                           
        else:#关联接口暂时未考虑get
            pass
        Temptime=time.strftime('%Y%m%d%H%m%S',time.localtime(time.time()))

        print('list_result',list_result)

        HtmlFormA.CreatHtml(in_tittle=ITFCName, in_str='test', in_list=list_result, \
        in_filename=self.CasePath+'Report\comb\\'+Temptime+'_'+ITFCName+'.html')
        self.CombPath=temp_CombPath
        print ITFCName,"run over",Temptime
# if __name__ == '__main__':
#     print("hello world")
