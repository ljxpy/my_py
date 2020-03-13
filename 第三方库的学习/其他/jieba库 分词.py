#jieba 库的使用总结
import jieba
jieba.lcut("中国是一个伟大的国家")
#['中国', '是', '一个', '伟大', '的', '国家']
jieba.lcut("中国是一个伟大的国家", cut_all=True)
#['中国', '国是', '一个', '伟大', '的', '国家']
jieba.lcut_for_search("中华人民共和国是伟大的")
#['中华', '华人', '人民', '共和', '共和国', '中华人民共和国', '是', '伟大', '的']
jieba.add_word("蟒蛇语言")
a = jieba.lcut("python是蟒蛇语言")
#['python', '是', '蟒蛇语言']
print(a)