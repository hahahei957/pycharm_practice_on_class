import jieba
import wordcloud
import matplotlib.image as mpimg # mpimg 用于读取图片
f = open("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/电动车.txt","r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)                 # 将文本中的关键字根据出现频率提取出来
print(ls)
text = ' '.join(ls)
# 读取图片对应的像素点，并绘制成函数
mask = mpimg.imread("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/heart.jpg")

w = wordcloud.WordCloud(width=800,height=600,
    background_color ="white",font_path='C:/Users/acer/AppData/Local/Microsoft/Windows/Fonts/锐字锐线怒放黑简1.0.TTF',   # 字体的路径，需要从属性里面的
    scale=32,           # 调整图片清晰度：scale属性，该值越大越清楚，我设置的是scale=32。
    mask=mask)          # mask默认是一个长方形

w.generate(text)
w.to_file("D:/Users/acer/Desktop/所有的文件/大数据课件/大数据第4章/ch4案例资料/电动车1.jpg")










