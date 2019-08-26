import requests, os, bs4

url = 'http://quick-e-recipes.com'
os.makedirs('quick-e-recipes', exist_ok=True)

while not url.endswith('id8.html'):
    """download the page"""
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.content, 'html.parser')

    #Find the url of the links
    link_elem = soup.select('a.NavBar.vertical')

    if link_elem == []:
        print('\nCould Not Find Any Links...')
    else:
        page_url = 'http://quick-e-recipes.com/' + link_elem[0].get('href')
        """download the page"""
        print('Downloading page %s...' % (page_url))
        res = requests.get(page_url)
        res.raise_for_status()

    """Save the page"""
    page_file = open(os.path.join('quick-e-recipes', os.path.basename(page_url)), 'wb')
    for chunk in res.iter_content(1000000):
        page_file.write(chunk)
    page_file.close()
