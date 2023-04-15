import re
from bs4 import BeautifulSoup
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

translator = Translator()


def allScrap():
    matches = []

    options = Options()
    options.add_argument('--headless')
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url='https://widget.streamsthunder.tv/?d=1&s=1&sp=1&ft=01&fs=16px&fw=700&tt=none&fc=333333&tc=333333&bc=E5E4E2&bhc=E5E4E2&thc=333333&pd=18px&br=1px&brc=434342&brr=15px&mr=1px&tm=333333&tmb=FFFFFF&wb=E5E4E2&bcc=E5E4E2&bsh=0px&sm=2&rdb=EBEBEB&rdc=333333&lk=1&fk=0')
    ele = driver.find_elements(By.TAG_NAME, 'h2')
    for acord in range(0, len(ele)):
        if ele[acord].is_displayed():
            ele[acord].click()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)
    links = soup.find_all('div', {'class': re.compile('e_4')})
    # print(*links, sep='\n')

    testList = []
    # testList += ''.join(testList)

    for item in links:
        # print(item.text)
        game = []
        links = []
        if 'Free Live' in item.text:
            game.append(item.text)

        if 'Flash' in item.text:
            for link in item.find_all('a'):
                links.append(link['href'])
        # print(game)
        # print(links)
        tupList = {'fixture':game, 'links': tuple(links)}
        testList.append(tupList)
    # print(*testList, sep='\n')

    for i in testList:
        match = {}
        # print(len(i['fixture'][0]))
        try:
            # print(len(i['links']))
            if len(i['fixture'][0]) > 0 and len(i['links']) > 0:
                try:
                    # print(i['fixture'][0])
                    text = i['fixture'][0]
                    fixture = text.replace('Free Live Streaming Football', '').strip().split('/')[0]
                    matchLinks = list(i['links'])
                    singleMatchLinks = []
                    for link in matchLinks:

                        if 'https://sport-play.live' in link:
                            pass
                        elif 'http://www.sports-stream.site' in link:
                            pass
                        elif 'https://spo-play.live' in link:
                            pass
                        elif 'acestream://' in link:
                            pass
                        elif 'https://varplatform.top' in link:
                            pass
                        elif 'https://daddylivehd.com' in link:
                            pass
                        elif 'https://lato.sx' in link:
                            pass
                        else:
                            ln = link.replace(
                                "javascript:void(window.open('https://cdn.stream-24.net/live/stream.php?t=Flash&link=",
                                '').split(',')[0]
                            if ln[:2] == '//':
                                ln = 'https:' + ln

                            rmid = re.sub(r'\&id=.*$', '', ln)

                            finalLink = rmid.replace('\n', '')
                            singleMatchLinks.append(finalLink)
                            # print(finalLink)
                    commaSepList = ',\n'.join(singleMatchLinks)
                    match['Match'] = fixture
                    match['Link'] = commaSepList
                    if len(singleMatchLinks) > 0:
                        matches.append(match)
                    else:
                        match.clear()
                    # print(fixture)

                except:
                    pass

        except IndexError:
            pass
    driver.quit()
    return matches


# allScrap()
print(*allScrap(), sep='\n')
