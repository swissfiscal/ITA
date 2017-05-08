class HtmlForm(object):
#     def __init__(self):
#         self.name=LT_HtmlForm
    def CreatHtml( self, in_tittle, in_str, in_list, in_filename ):
#         self.in_tittle
        str_html = ''
        str_html += '<html>'
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

        str_html += '<table border="1" width="50%" align="center">'
        list_len = len(in_list)
        str_html += '<tr>'
        for key in sorted(in_list[0].keys()):  
            str_html += '<td>'
            str_html += str(key)
            str_html += '</td>'
        str_html += '</tr>' 
        for i in range(list_len):
            str_html += '<tr>'
            for key in sorted(in_list[i].keys()):
                str_html += '<td>'
                str_html += str(in_list[i][key])
                str_html += '</td>'
            str_html += '</tr>'
        str_html += '</body>'
        str_html += '</html>'
        f1 = open( in_filename, 'w')
        f1.write(str_html)
        f1.close()