import requests
from bs4 import BeautifulSoup
import csv

HN_BASE_URL = 'https://news.ycombinator.com/news'
NUMBER_OF_ARTICLES = 50
OUTPUT_FILE = './WebScraping/hackernews/top_hacker_news.csv'


class NewsArticle:
    def __init__(self, title, user_id, points, comments, link):
        self.title = title
        self.user_id = user_id
        self.points = points
        self.comments = comments
        self.link = link
    
    def to_csv_row(self):
        return [self.title, self.user_id, self.points, self.comments, self.link]

    def __str__(self):
        return f"Title: {self.title}\nUser ID: {self.user_id}\nPoints: {self.points}\nComments: {self.comments}\nLink: {self.link}\n"


def write_articles_to_csv(articles, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for article in articles:
            writer.writerow(article.to_csv_row())


def read_articles_from_csv(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            yield NewsArticle(row[0], row[1], int(row[2]), int(row[3]), row[4])


def get_top_news():
    HN_URL = HN_BASE_URL
    top_articles = []
    while len(top_articles) < NUMBER_OF_ARTICLES:
        response = requests.get(HN_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('tr', class_='athing')
        for article in articles:
            title_tag = article.select_one('span.titleline a')
            title = title_tag.get_text() if title_tag else 'N/A'
            link = title_tag['href'] if title_tag and 'href' in title_tag.attrs else 'N/A'

            article_id = article.get('id')

            score_tag = soup.find('span', class_='score',
                                  id=f'score_{article_id}')
            points = int(score_tag.get_text().split()[0]) if score_tag else 0

            user_tag = article.find_next_sibling(
                'tr').find('a', class_='hnuser')
            user_id = user_tag.get_text() if user_tag else 'N/A'

            comments_tag = article.find_next_sibling(
                'tr').find('a', string=lambda x: 'comment' in x)
            comments = int(comments_tag.get_text().split()
                           [0]) if comments_tag else 0

            top_articles.append(NewsArticle(
                title, user_id, points, comments, link))
            if len(top_articles) == NUMBER_OF_ARTICLES:
                break

        page_param = f'p={len(top_articles) // 30 + 1}'
        HN_URL = f'{HN_BASE_URL}?{page_param}'
        if not HN_URL:
            break
    return top_articles


# Example usage:
top_news = get_top_news()
write_articles_to_csv(top_news, OUTPUT_FILE)

# Once we have this data, we can perform any logical operation based on the requirement.
top_news = read_articles_from_csv(OUTPUT_FILE)
for article in top_news:
    print(article)
