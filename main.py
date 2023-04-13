import requests
import lxml.html as html
import sexy_filter

events_results = {}
locations_results = {}
dates_results = {}

base_url = 'https://i.ticketweb.com/search'
# After analyzing the HTML from https://www.ticketweb.com/search?q=
# I noticed that it gets the events information from this URL 
# So, I had to scrap from here

print('\n ###################### Coded By @nonskilledeveloper #######################\n')

try:
    max_pages = int(input('Write here the number of pages you want to scrape (Max 99): '))
    if max_pages > 99:
        max_pages = 99
        print('There are only 99 pages, I will assume that you want 99')
    elif max_pages < 1:
        max_pages = 1
        print('The minimum number of pages is 1, I will assume that you want 1')
except ValueError as valuError:
    print('We do not accept float numbers, letters or symbols.\nError code: ',valuError)
    quit()

for i in range(max_pages):

    response = requests.get(base_url)

    params = {
        'q': '',
        'page': i+1
    }

    headers = {
    'sec-gpc': '1',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Brave";v="110"',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'sec-ch-ua-mobile': '?1',
    'sec-fetch-mode': 'navigate',
    'Accept-Language': 'es-419,es;q=0.7',
    'sec-fetch-dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'User-Agent': 'nonskilledeveloper-Browser-v0.1',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua-platform': '"tacOS"',
    'upgrade-insecure-requests': '1'
    }
    
    print('\nScraping page', i+1, 'out of', max_pages, '\n')

    response = requests.get(base_url, params=params, headers=headers)

    html_response = html.fromstring(response.text)

    sexy_filter.get_data(html_response, events_results, locations_results, dates_results)

    for n in range(20):
        print('<><><><><><> Event #'+str(n+1)+' <><><><><><>')
        print('Event name:')
        print(events_results[n])
        print('Event Location:')
        print(locations_results[n])
        print('Event date:')
        print(dates_results[n])

# It's possible to save this information in a CSV file or send it to another server
# It would be interesting to do it