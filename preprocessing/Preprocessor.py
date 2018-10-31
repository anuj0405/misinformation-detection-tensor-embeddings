from utils import Config
from utils.ArticlesProvider import ArticlesProvider


class Preprocessor:
    def __init__(self, config: Config, articles: ArticlesProvider):
        self.config = config
        self.articles = articles

    def preprocess(self):
        raise NotImplementedError
