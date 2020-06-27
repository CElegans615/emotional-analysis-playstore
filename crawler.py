# play store scraping
    ## will update play_store library according this

top_url = "https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c"
top_header = {'Cookie': 'SIDCC=AJi4QfHy9QcZrXojfIKpfS_rakQmyhRHpR26qbckZ4VFy6Nk0FbxLszloy_kCPbXwfECR0-HJg8; OTZ=5473977_20_20__20_; _ga=GA1.3.3381249.1590742600; _gid=GA1.3.700538980.1590742600; 1P_JAR=2020-5-29-8; NID=204=o6jpsIkEzFO0mDDZbiGC_79jvzx1TGMKn6xw9zgpQNHcJi_29XoXTQ9F30IZcakDfeFJrgbPAOsftAgoRnpaOGaUetj9SkWCRqAUud_MilSvt8GUg2-Q6sxCwOydKH0RJIU6jL8b43aey6QNDpCAKEIIR0OrM9MfN1vtAoygWKwT3nUst5vDa5_wzTCdyJtZhRfbrAR1jc_N7e5Dckyhj4n_NTUKimEspx4EEpP04ccLH6gWl1xnWqIjzJviOePc0r2YU_YAHY9fl4F1; SID=wwd8W936S50SRjRGxW9iZ49_Vo39x4rGbRX8PJscFnEbg-I9L1uZxDqk4W4DOBrOiZyZIg.; __Secure-3PSID=wwd8W936S50SRjRGxW9iZ49_Vo39x4rGbRX8PJscFnEbg-I9iOcqsqRHPvn-JjoKve0z0w.; SEARCH_SAMESITE=CgQItY8B; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=rebor2dlivekirax2@gmail.com; APISID=d96xznRjEj0wNwFH/AOhCZ3AOL0sKx2RXk; HSID=AGfk9W9hq1jIbSnev; SAPISID=6ZKCP1xnHlT6M39w/Aw2ESV4fRw6sGgCjk; SSID=A0HtVxb2-Oy9-Q5EG; __Secure-3PAPISID=6ZKCP1xnHlT6M39w/Aw2ESV4fRw6sGgCjk; __Secure-APISID=d96xznRjEj0wNwFH/AOhCZ3AOL0sKx2RXk; __Secure-HSID=AGfk9W9hq1jIbSnev; __Secure-SSID=A0HtVxb2-Oy9-Q5EG; ANID=AHWqTUn1aCRbGSIf1xoh0QgjcTjCYeT1aQd7Lke6qLt3QmuPq98yBGyO0rSV_ihl; CONSENT=YES+KR.ko+'}
# url, header for top game chart

paid_url = "https://play.google.com/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfcGFpZF9HQU1FEAcYAw%3D%3D:S:ANO1ljLtt38&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19wYWlkX0dBTUUQBxgD:S:ANO1ljJCqyI"
paid_header = {'Cookie': 'SIDCC=AJi4QfEJ6tFjp0zpGMK'}
# url, header for top paid chart

mar_url = "https://play.google.com/store/apps/collection/cluster?clp=0g4YChYKEHRvcGdyb3NzaW5nX0dBTUUQBxgD:S:ANO1ljLhYwQ&gsr=ChvSDhgKFgoQdG9wZ3Jvc3NpbmdfR0FNRRAHGAM%3D:S:ANO1ljIKta8"
mar_header = {'Cookie': 'SIDCC=AJi4QfHuigYNWLej4h'}
# url, header for top margin chart

class chart:
    def __init__(self, url, header):
        # list of tuples (game_name, id, rate, dev_id, category, etc)
        # searchable according to many different criteria

        ## making soup object
        import requests
        from utils import tuple_maker

        response = requests.get(url, headers = header)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text)

        ## parsing soup object
        import re

        list = soup.body.find_all("script", text = re.compile("AF_initDataCallback"))

        if url == top_url:
            pre_chart = list[6].contents[0].string
        elif url == paid_url:
            pre_chart == list[7].contents[0].string
        else:
            pre_chart = list[5].contents[0].string
        
        pre_chart = pre_chart[pre_chart.find("return"):pre_chart.find("}")-1]    

        pattern = r""".*\bhttps://lh3.googleusercontent.com/\b[\w-]+"].*"""
        pre_chart = re.sub(re.compile(r"""\n("""+pattern+r""")\n"""), r""" \1 """, pre_chart)
        pre_chart_list = re.split(re.compile(pattern, re.M), pre_chart)

        front = r"""\n]\n,\d+,\d+]\n,"""
        chart_list = []
        for m in pre_chart_list:
            if m.startswith(front):
                chart_list.append(utils.tuple_maker(m))

    
    # def search(self):
        # search basic game info
        # return /tuple/

    # def reviews(self):
        # return list of tuples (review, rate, thumbs_up) of game
        # return /list_of_tuples/