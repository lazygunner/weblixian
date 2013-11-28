import re

links = []

def add(link):
    p = re.compile(r'\s')
    link_group = p.split(link)
    for link in link_group:
        #check the link wether in the list
        if(links.count(link) != 0):
            continue
        links.append(link)
    return link_group.pop(0)

def add_link_list(link):
    link_list = map(lambda xx:xx['ed2k_link'], link)
    print link_list
    links.append(link_list)
    return link_list.pop(0)

def get_first():
    try:    
        link = links.pop(0)
        if(link != ''):
            links.insert(0, link)
            return link
    except:
        return ''
        


def get_all():
    return links

def pop_link():
    return links.pop(0);


