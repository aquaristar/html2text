import sys
import os
import re
from bs4 import BeautifulSoup

def replace_comma_to_space(param):
    return param.replace(",", "")

def replace_quote(param):
	return param.replace('%1D', '"')

def add_double_quotes(param):
    return param.replace('"', '""')

def rem_hex_string(param):
    result = re.sub(r'%0([a-zA-Z_0-9]*)+',r'', param)
    return result

def rem_color_value(param):
    result = re.sub(r'%([0-9_a-zA-F]{8})',r'', param)
    return result

def rem_html_comment(param):
    result = re.sub("(<!--.*?-->)", "", param, flags=re.MULTILINE)
    return result

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

while(1):
    try:
        content = raw_input()
        if ( content.strip() == '' ): 
        	break

        # print (content)
        # print ("\n\n")
        content = rem_html_comment(content)
        # print (content)
        # print ("\n\n")
        content = rem_color_value(content)
        # print (content)
        # print ("\n\n")
        content = rem_hex_string(content)
        # print (content)
        # print ("\n\n")

        #content = replace_comma_to_space(content)
        content = replace_quote(content)
        #content = add_double_quotes(content)

        soup = BeautifulSoup(content, 'html.parser')
        text_elements = soup.findAll(text=True)
        #print (text_elements)
        #print ("\n\n")
         
        visible_text_elements = filter(visible, text_elements)
        #print list(visible_text_elements)
        
        result = ''
        for text_e in visible_text_elements:
            result = result + text_e
        print (result)
        
    except KeyboardInterrupt:
        #print ("keyboard error")
        break
        
    except EOFError:
        #print ("eof error")
        break
        
exit()