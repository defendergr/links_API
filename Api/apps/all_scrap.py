import json
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import os



def get_data():
    '''
    Extracts elements from the HTML content of the page.

    Args:
        None

    Returns:
        str: The HTML content of the page.
    '''

    # Create options for headless mode
    options = Options()
    options.add_argument('--headless')

    # Set the driver path based on the operating system
    if os.name == 'nt':
        service = Service(GeckoDriverManager().install())
    elif os.name == 'posix':
        if os.path.isfile('/usr/bin/geckodriver'):
            service = Service(executable_path='/usr/bin/geckodriver')
        else:
            service = Service(executable_path='/data/data/com.termux/files/usr/bin/geckodriver')

    # Create the webdriver instance
    driver = webdriver.Firefox(service=service, options=options)

    # Navigate to the specified URL
    driver.get(url='https://widget.streamsthunder.tv/?d=1&s=1&sp=1,2&ft=01&fs=16px&fw=700&tt=none&fc=333333&tc=333333&bc=E5E4E2&bhc=E5E4E2&thc=333333&pd=18px&br=1px&brc=434342&brr=15px&mr=1px&tm=333333&tmb=FFFFFF&wb=E5E4E2&bcc=E5E4E2&bsh=0px&sm=2&rdb=EBEBEB&rdc=333333&lk=1&fk=0')

    # Find all elements with the tag name 'h2'
    ele = driver.find_elements(By.TAG_NAME, 'h2')

    # Click on each displayed element
    for acord in range(0, len(ele)):
        if ele[acord].is_displayed():
            ele[acord].click()

    # Get the page source and close the driver
    scraped = driver.page_source
    driver.close()

    return scraped

def get_elements():
    '''
    Fetches data from a custom selenium server, extracts specific elements from the data using BeautifulSoup,
    and returns a list of titles and links related to games found on that data.
    Returns:
        tuple: Tuple containing lists of game titles and links.
    '''
    # Get data from the URL
    data = get_data()

    # Parse the the data as HTML content
    soup = BeautifulSoup(data, 'html.parser')

    # Find the main div containing the elements
    elements = soup.find('div', {'class': re.compile('accordion')})

    # Find all game titles and links
    games_titles = elements.find_all('h2', {'ui-accordion-header': ''})
    games_links = elements.find_all('div', {'ui-widget-content': ''})

    return games_titles, games_links


def get_games():
    '''
    Extracts information about sports matches from the data elements obtained by get_elements.
    Iterates through the elements, extracts details like timestamp, sport, country, and fixture
    based on specific conditions, and adds them to a list of matches.
    Returns:
        list: List of extracted match details.
    '''
    # Get titles and links from get_elements function
    titles, links = get_elements()
    matches = []

    # Iterate through titles to extract match details
    for item in (x.find_all('div') for x in titles):
        match = {}
        try:
            # Extract timestamp and add 2 hours
            if 'original_time' in str(item[0]):
                match["timestamp"] = item[0].text
                match["time"] = datetime.fromtimestamp(int(item[0].text)) + timedelta(hours=2)

            # Extract sport
            if 'sport' in str(item[1]):
                if 'basketball' in str(item[1]):
                    match["sport"] = "Basketball"
                elif 'football' in str(item[1]):
                    match["sport"] = "Football"
                else:
                    match["sport"] = str(item[1].span)

            # Extract country
            if 'country' in str(item[3]):
                if 'countries/' in str(item[3]):
                    n = str(item[3].span).find("countries/")
                elif 'competition/' in str(item[3]):
                    n = str(item[3].span).find("competition/") + 2
                match["country"] = str(item[3].span)[n + 10:].removesuffix(r'.png);"></span>')

            # Extract fixture
            if 'match' in str(item[4]):
                match["fixture"] = item[4].text.replace(' -   ', ' - ')

            # Initialize links
            match["links"] = ''

            # Check if fixture already exists in matches, then add match
            if match['fixture'] not in [x['fixture'] for x in matches]:
                matches.append(match)

        except Exception as e:
            print(e)

    return matches


def get_links():
    '''
    Extracts links for specific fixtures from data.
    Args:
        None
    Returns:
        list: List of matches containing fixture information and links that meet certain conditions.
    '''

    # Get titles and links from get_elements function
    titles, links = get_elements()

    matches = []

    for link in links:
        match = {}
        links = ''

        # Extract fixture information
        if link.findAll('p'):
            # Remove prefixes from fixture text
            fixture = link.findAll('p')[0].text.strip().removeprefix('Free Live Streaming Basketball').removeprefix('Free Live Streaming Football')
            match['fixture'] = fixture.split(' / ')[0].strip().replace(' -   ', ' - ')

        # Extract links with "flash" string
        for link in link.findAll('a'):
            link = link['href'].split("','")[0].replace('\n', '')
            if "flash" in str(link).lower():
                # print(link['href'], '\n')
                n = str(link).find("link=")
                pattern = r'btn-default=.*'
                # Process and format the links
                link = re.sub(pattern, '', str(link)[n + 5:]).strip().split('&')[0]
                if link.startswith('//'):
                    link = 'https:' + link
                if link.startswith('http'):
                    links += link + ","

        match['links'] = links.removesuffix(',')

        # Check conditions before adding to matches
        if 'fixture' in match.keys() and len(match['links']) > 1:
            matches.append(match)

    return matches


def add_links():
    '''
    This function matches links to games based on fixture equality
    and appends the links to the respective games.
    Then removes any trailing commas from the links and returns the updated list of matches.

    Returns:
        list: List of matches with appended links.
    '''
    # Get matches and links
    matches = get_games()
    links = get_links()

    # Add links to matches
    for match in matches:
        for link in links:
            if match['fixture'].strip() == link['fixture'].strip():
                match['links'] += link['links'] + ","

        # Remove trailing commas
        match['links'] = match['links'].removesuffix(',,')

    return matches


def games(args=None):
    '''
    This function defines a game processing mechanism based on the provided arguments.

    Args:
        args: The argument to specify the action. Default is None.

    Returns:
        str or dict: Returns different outputs based on the argument:
            - If args is None, a message to use the argument 'help'.
            - If args is 'help', instructions on how to use different arguments.
            - If args is 'json', the matches with links in JSON format.
            - If args is 'dict', the matches with links as a dictionary.
    '''
    accepted_args = ['json', 'dict', 'help']
    if args == None or args not in accepted_args:
        return "\tUse argument 'help' for more info."
    elif args == 'help':
        return "\tUse argument 'json' to get json format. \n\tUse argument 'dict' to get dictionary format. \n\tUse argument 'save' to save data in database."
    try:
        # Get matches with links
        matches = add_links()
        matches_with_links = []
        for match in matches:
            if len(match['links']) > 0:
                matches_with_links.append(match)

        if args == 'json':
            return json.dumps(matches_with_links, indent=4, default=str)
        elif args == 'dict':
            return matches_with_links

    except Exception as e:
        return str(e)


# print(games('json'))
# print(*get_links(), sep='\n')
