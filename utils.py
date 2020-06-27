import re

def tuple_maker(raw_info):
    ## import str, return tuple
    ## (name, dev, dev_id, descript, star, game_id)

    g_list = re.compile(r"""\b(\d\.\d+)\b|\B"(.*?)"\B""", re.M).findall(raw_info)
    
    name = g_list[0][1]
    dev = g_list[1][1]
    dev_id = re.compile(r""".*u00d\b(.*)""").findall(g_list[2][1])[0]
        # need improvement
    descript = g_list[3][1]
    star = g_list[5][0]
    game_id = g_list[8][1]
    
    g_tuple = tuple(name, dev, dev_id, descript, star, game_id)

    return g_tuple

def page_opener():
    ## open page of url
    ## return /soup/

# def url_gen():
    ## generate urls of charts
    ## return /str/

# def review_collector():
    ## collect reviews of game
    ## return /list_of_tuples/