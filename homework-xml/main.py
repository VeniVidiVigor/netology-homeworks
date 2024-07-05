import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    # Ваш алгоритм
    data = root.findall("channel/item")
    words = []
    counts = {}
    for i in data:
        i = i.find('description').text
        for x in i.split():
            if len(x) > word_max_len:
                words.append(x)
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1
    d = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    all_words = list(d)
    return all_words[:10]


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))
