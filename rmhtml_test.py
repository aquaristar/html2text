import sys
import os
import re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

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

file = open("examples.txt", "r")

content = file.read()

#exit()

#while(1):
try:
    #content = raw_input()
    if ( content.strip() == '' ): 
    	#break
        exit()
    print content+"\n"
    content = rem_html_comment(content)
    print content+"\n"
    content = strip_tags(content)
    print content+"\n"
    exit()
#        content = replace_comma_to_space(content)
    #content = replace_quote(content)
#        content = add_double_quotes(content)
    content = rem_hex_string(content)
    content = rem_color_value(content)
    content = rem_html_comment(content)
    content = ' '.join( content.split() )
    

    print (content)
except KeyboardInterrupt:
    print ("keyboard error")
    #break
    
except EOFError:
    print ("eof error")
    #break
        
exit()