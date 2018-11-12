from utils import wordcloud_util
import matplotlib.pyplot as plt

from utils.mongo_utils import search
from utils.playplay_config import mongo_url, gather_coll, gather_db


def wordcloud_svc(wc_path="./data/1.jpg"):
    news_text = ""
    results = search(url=mongo_url,
                     db=gather_db,
                     coll_name=gather_coll,
                     filter={})
    for result in results:
        print(result["content"])
        news_text = news_text + result["content"] + "\n"
    wordcloud = wordcloud_util.gen_wordcloud(news_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # plt.show()
    plt.savefig(wc_path)


