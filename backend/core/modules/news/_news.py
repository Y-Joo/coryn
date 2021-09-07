def create_news(_type, _title, _source, _link, _upload_date, _release_date):
    news = {
        'type': _type,
        'title': _title,
        'source': _source,
        'link': _link,
        'upload_date': _upload_date,
        'release_date': _release_date,
    }
    return news
