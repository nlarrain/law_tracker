#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:38:37 2020

@author: nico
"""
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Read list of keywords
words = []
keywords = open("keywords.txt", "r")

for line in keywords:
        line = line.strip()
        words.append(line)

# Configure the request method with a set of headers
cookies = {
    '_ga': 'GA1.2.2082727479.1607082199',
    '_gat': '1',
    '_gid': 'GA1.2.140147224.1607468886',
    '__utma': '99603356.2082727479.1607082199.1607082256.1607092249.2',
    '__utmz': '99603356.1607082256.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',}

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en-us',
    'Host': 'www.senado.cl',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    'Referer': 'https://www.senado.cl/appsenado/templates/tramitacion/index.php?',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',}

def get_projects (keyword):

    # Get the source code

    params = (
        ('mo', 'tramitacion'),
        ('ac', 'boletin_x_fecha'),
        ('palabra', keyword),
        ('tipo_palabra', '2'),
        ('etc', '1607468907057'),
        )

    result = requests.get('https://www.senado.cl/appsenado/index.php', headers=headers, params=params, cookies=cookies)
    html_source = result.text

    # Variables to store the info
    project = []

    # Parse the second <tbody> element in the html code 

    bs = BeautifulSoup(html_source,'html.parser')
    info = bs.find('div',class_ = 'box_2')

    for case in info.findAll('tr'):
        info = []
        for data in case.findAll('td'):
            info.append(data.get_text())
        
        project.append(info)


    df = pd.DataFrame(project, columns = ['fecha', 'boletin', 'titulo' , 'status','fecha_sort', 'boletin'])

    #Delete the first row and trim the strings
    df = df.iloc[1:]
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df

# Dataframe to hold the scraping results
final = []

for word in words:
    aux = get_projects(word)
    final.append(aux)


