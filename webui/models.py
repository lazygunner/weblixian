
links = []

def add(link):
    if(links.count(link) != 0):
        return -1
    links.append(link)
    return 0

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


