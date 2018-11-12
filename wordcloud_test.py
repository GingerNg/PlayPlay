from utils import wordcloud_util
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = "yes-minister-cn.txt"
    with open(filename, "rb") as f:
        mytext = f.read()
    wordcloud = wordcloud_util.gen_wordcloud(mytext)
    # %pylab inline

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # plt.show()

    plt.savefig("./data/1.jpg")

    print("success")