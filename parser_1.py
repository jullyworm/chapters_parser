import bs4
from os import walk

pyth_html_dir = 'path to direction of html pages'
pyth_text_dir = 'path to direction of texts'

def parser(filename):
    doc = open(pyth_html_dir + str(filename), 'r', encoding="utf8")
    html = doc.read()
    doc.close()
    filename = filename[:-5]
    doc_text = open(pyth_text_dir + str(filename) + '.txt', 'w', encoding="utf8")
    soup = bs4.BeautifulSoup(html, 'html.parser')

    data = soup.find("div", attrs={"class":"content-text"})
    titles = soup.find("select", attrs={"onchange":"go_chapter(this.value);"})
    for title in titles:
        if isinstance(title, bs4.element.Tag):
            if title.attrs.get('selected') != None:
                doc_text.write(title.text)
    for tag in data:
        doc_text.write('\t')
        doc_text.write(tag.text)
        doc_text.write('\n')
    doc_text.close

def fb2_writer():
    fb2_doc = open('C:/Users/missc/OneDrive/Документы/зп главы html/Книга.txt', 'w', encoding="utf8")
    pretext = "<?xml version=\"1.0\" encoding=\"utf-8\"?> \n <description>\n <title-info>\n <author> \n<first-name>Имя</first-name>\n<last-name>Фамилия</last-name>\n</author>\n <book-title>Название</book-title>\n <annotation>\n Описание </annotation>\n<lang>ru</lang> \n </title-info>\n <document-info>\n<author>\n<first-name>Имя</first-name>\n<last-name>Фамилия</last-name>\n</author>\n</document-info>\n</description>\n<body>\n"
    fb2_doc.write(pretext)
    f = []
    for (dirpath, dirnames, filenames) in walk(pyth_text_dir):
        f.extend(filenames)
        break
    f.sort()
    for filename in f:
        doc = open(pyth_text_dir + str(filename), 'r', encoding="utf8")
        fb2_doc.write("<section>\n<title>")
        lines = doc.readlines()
        fb2_doc.write(lines[0])
        fb2_doc.write("</title><empty-line/>\n")
        for line in lines:
            if(line == lines[0]): continue
            fb2_doc.write("<p>"+str(line)+"</p>\n")
        fb2_doc.write("</section>\n")
    aftertext = "</body>"
    fb2_doc.write(aftertext)
    fb2_doc.close()


def parser_chapters():
    f = []
    for (dirpath, dirnames, filenames) in walk(pyth_html_dir):
        f.extend(filenames)
        break
    f.sort()
    for filename in f:
        parser(filename)

parser_chapters()
fb2_writer()