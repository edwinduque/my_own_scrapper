class ArticlePage(NewsPage):

    def __init__(self, news_site_uid, url):
        self._url = url
        super().__init__(news_site_uid, url)

    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else ''

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        print(result[0].text)
        return result[0].text if len(result) else ''

    @property
    def url(self):
        return self._url