import time
from datetime import date

import feedparser

NEWS_URL = 'https://techfeed.io/feeds/categories/all'


def fetch_news(url: str):
    """RSSフィードを解析して返す"""
    return feedparser.parse(url)


def extract_ranking(data: dict):
    """ランキング記事のみを抽出して返す"""
    data_list = []

    for entry in data['entries']:
        if '/entries' in entry['id']:
            tmp = {
                'url': entry['link'],
                'title': entry['title'],
                'update': time.strftime('%Y-%m-%d', entry['updated_parsed'])
            }
            data_list.append(tmp)
    return data_list


def format_ranking(data: list):
    """ランキング記事をMarkdown形式で整形して返す"""
    data_list = []

    for idx, item in enumerate(data, start=1):
        tmp = f'### {idx}. [{item["title"]}](<{item["url"]}>)  {item["update"]}'
        data_list.append(tmp)
    return data_list


def main():
    """メインで実行する処理"""
    data = fetch_news(NEWS_URL)
    ranking = extract_ranking(data)
    show_rankings = format_ranking(ranking)

    title = f'## {date.today()}  TechFeedのランキング'
    message = '\n'.join([title] + show_rankings)
    return message
