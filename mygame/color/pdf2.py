path ="lcdpython.pdf"
def parse():
    # 
    with open(path, 'rb') as fp:
    # 以二进制读模式打开
    #用文件对象来创建一个pdf文档分析器
        praser = PDFParser(fp)
    # 创建一个PDF文档
        doc = PDFDocument()
    # 连接分析器 与文档对象
        praser.set_document(doc)
        doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
        doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    #需要写出编码格式
                    with open(r'1.txt', 'a',encoding='utf-8') as f:
                        results = x.get_text()
                        print(results)
                        f.write(results + '\n')

if __name__ == '__main__':

    parse()
