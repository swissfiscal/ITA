#-*- encoding: utf-8 -*-
#“reload(sys)  sys.setdefaultencoding( "utf-8" )
import json
class HtmlForm(object):
    def CreatHtml( self, in_tittle, in_str, in_list, in_filename ):
        str_html = '<!DOCTYPE html>'
        str_html += '<html>'
        str_html += '<head>'
        str_html += '<meta charset="utf-8">'
        str_html += '<style>'
        str_html += 'body{word-wrap: break-word;word-break: break-all;}'
        str_html += 'td,th{word-wrap: break-word;word-break: break-all;}'
        str_html += '</style>'
        str_html += '</head>'
        str_html += '<body>'
        str_html += '<h1 align="center">'
        str_html += in_tittle
        str_html += '</h1>'
        i = 0
        for temp_str in in_str:
            i += 1
            str_html += '<p>' 
            str_html += '<tittle>'
            str_html += temp_str
            str_html += '</tittle>'          
            str_html += '</p>'
        str_html += '<table border="1" width="80%" align="center">'
        str_html += '<tr>'
        str_html += '<col width="100">'
        str_html += '<col>'
        str_html += '<col>'
        str_html += '<col>'
        # list_i=0
        #获取用例长度
        list_len = len(in_list)
        #读取key用于生成表格头
        for list_i in in_list[0]:
            str_html += '<td>'
            for key in list_i:
                str_html +=str(key)
            str_html += '</td>'
        str_html += '</tr>'
        #遍历用例长度
        for i in range(list_len):
            str_html += '<tr>'
            # if in_list[i][4]['Result'] != 'pass':
            #     fail_count=fail_count+1
            for list_i in in_list[i]:
                str_html += '<td>'
                for key in list_i:
                    #如果是 unicode则编码成ascii
                    if type(list_i[key]) == unicode:
                        # tempdic = json.loads(list_i[key])
                        list_i[key]=json.loads(list_i[key])
                        # print  'tempdic:', tempdic
                        # print  'tempdic type:',type(tempdic)
                        # list_i[key]=list_i[key].encode('ascii','ignore')
                    # str_html += str(list_i[key]).decode('ascii', 'ignore')
                    resp_str=str(list_i[key])
                    if len(resp_str)>100:
                        resp_str=resp_str[:100]+'......'
                    str_html += resp_str
                str_html += '</td>'
            str_html += '</tr>'
        str_html += '</body>'
        str_html += '</html>'
        f1 = open(in_filename, 'w')
        f1.write(str_html)
        f1.close()