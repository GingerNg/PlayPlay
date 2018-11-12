
from wordcloud import WordCloud
import jieba

def gen_wordcloud(word_text):
    """
    生成词云
    :return:
    """
    mytext = " ".join(jieba.cut(word_text))

    return WordCloud(font_path="./simsun.ttf").generate_from_text(mytext)


