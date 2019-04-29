# SETUP
import urllib2, csv
from bs4 import BeautifulSoup

# SETUP CSV
csvfile = open('billtest.csv', 'a')
billtest_writer = csv.writer(csvfile)

# GETTING THE WEBSITE
url = 'https://www.senate.mo.gov/19info/BTS_Web/TrulyAgreed.aspx?SessionType=R'
html = urllib2.urlopen(url).read()

# PROCESSING THE HTML
soup = BeautifulSoup(html, 'html.parser')

# SCRAPING THE DATA

tables = soup.find_all('table', {'id': 'Table2'})

for table in tables:
    
    rows = table.find_all('tr')

    for row in rows:
        output_row = []

        cells = row.find_all('td')

        for cell in cells:
            output_row.append(cell.text)

    billtest_writer.writerow(output_row)