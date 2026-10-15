from bs4 import BeautifulSoup

def _to_cents(text):
    dollars = text.strip().replace('$', '').replace(',', '')
    return int(round(float(dollars) * 100))


def count_matches(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.select(selector))


def select_texts(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.text for tag in soup.select(selector)]


def select_attr(html, selector, attr):
    soup = BeautifulSoup(html, 'html.parser')
    return [tag[attr] for tag in soup.select(selector)]


def extract_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.text.strip() for tag in soup.select('.title')]


def extract_prices_cents(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [_to_cents(tag.text) for tag in soup.select('.price')]


def count_free_shipping(html):
    soup = BeautifulSoup(html, 'html.parser')
    return len(soup.select('.free-shipping'))


def first_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('a[href]')
    if not links:
        return None
    return links[0]['href']


def extract_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    listings = []
    for item in soup.select('.item'):
        title = item.select_one('.title')
        price = item.select_one('.price')
        listings.append({
            'name': title.text.strip(),
            'price_cents': _to_cents(price.text),
            'url': title['href'],
        })
    return listings