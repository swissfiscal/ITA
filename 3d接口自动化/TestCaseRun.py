#-*- encoding: utf-8 -*-
'''
Created on 2015年9月10日

@author: Administrator
'''
from run import C_CaseRun
# null=None    
if __name__ == '__main__':
    ConfName='conf.ini'
    #实例化C_CaseRun类,此时已经执行了init中的内容
    TestRun=C_CaseRun(ConfName)
    #独立接口,返回一个列表，
    #若需将结果写入html:
    # 1.将多个结果放入一个元祖中处理。
    # 2.在执行用例的时候就把结果写入html
    #遍历host
    filename = r'C:\WINDOWS\system32\drivers\etc\HOSTS'
    # host替换
    host_list = [
        '10.1.1.22',
        '10.1.1.25',
        '10.1.1.29',
        '10.1.1.35',
        '10.1.1.40',
        '10.1.1.41',
        '10.1.1.42',
        '10.1.1.43',
        '10.1.1.44',
        '10.1.1.79',
        '10.1.1.80',
    ]
    oldhost = '10.1.1.80 api1.admin.mnmnh.com'
    api_ym = ' api1.admin.mnmnh.com'
    for i in host_list:
        newhost = i + api_ym
        with open(filename) as f:
            input = f.read()
        output = input.replace(oldhost, newhost)
        oldhost = newhost
        with open(filename, 'w') as f:
            f.write(output)
        #修改好host执行执行接口调用
        #TestRun.IDPDTCaseRun('GetDesignMaterialListByCategoryIdEx', newhost=i)
        #TestRun.IDPDTCaseRun('GetDesignMaterialListByCategoryIdEx', newhost=i)
        TestRun.IDPDTCaseRun('DesignMaterial_GetCategoryAndMaterialList', newhost=i)
        #TestRun.IDPDTCaseRun('GetDesignMaterialContentList', newhost=i)
        # try:
        #     tempresult = TestRun.IDPDTCaseRun('GetDesignMaterialListByCategoryIdEx',newhost=i)
        #     tempresult2 = TestRun.IDPDTCaseRun('DesignMaterial_GetCategoryAndMaterialList', newhost=i)
        # except Exception,e:
        #     print e
    print('new over', newhost)

    # temp_result=TestRun.IDPDTCaseRun('GetDesignMaterialListByCategoryIdEx')
    # for i in range(len(temp_result)):
    #     print(i,':',temp_result[i])
    # #组合接口
    # temp_Cresult=TestRun.CombCaseRun("me")
    # temp_Cresult=TestRun.CombCaseRun("sign")
    #
#     for i in range(len(temp_Cresult)):
#         print(i,':',temp_Cresult[i])