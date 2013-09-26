import re

links = []

def add(link):
    p = re.compile(r'\s')
    link_group = p.split(link)
    for link in link_group: 
        if(links.count(link) != 0):
            continue
        links.append(link)
    return link_group.pop(0)

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


