from bs4 import BeautifulSoup
import sys
import os
import re
import html2text

def rem_hex_string(param):
    result = re.sub(r'%0([a-zA-Z_0-9]*)+',r'', param)
    return result

def rem_color_value(param):
    result = re.sub(r'%([0-9-a-zA-F]{8})',r'', param)
    return result

def rem_html_comment(param):
    result = re.sub(r'<!--.*-->',r'', param)
    return result

file = open("examples.txt", "r")

content = file.read()
# print (content)
# print ("\n\n")
# h = html2text.HTML2Text()
# h.ignore_links = True
# print (h.handle(content))
# exit()

#exit()

#while(1):
print (content)
print ("\n\n")
content = rem_html_comment(content)
print (content)
print ("\n\n")
content = rem_color_value(content)
print (content)
print ("\n\n")
content = rem_hex_string(content)
print (content)
print ("\n\n")

try:
    # soup = BeautifulSoup(content, 'html.parser')
    # text_elems = soup.find_all('p', text=True)
    soup = BeautifulSoup(content, 'html.parser')
    text_elements = soup.findAll(text=True)
    print (text_elements)
    print ("\n\n")

    def visible(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
     
    result = filter(visible, text_elements)
    
    print list(result)
    
    content = ''
    for text_element in result:
        content = content + text_element
    print (content)
except KeyboardInterrupt:
    print ("keyboard error")
    #break
    
except EOFError:
    print ("eof error")
    #break
        
exit()