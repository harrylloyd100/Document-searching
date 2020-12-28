import numpy as np
import math

def calc_angle(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    cos_theta = np.dot(x, y) / (norm_x * norm_y)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def Dict(filename):
    input_file = open(filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    Dict.word_list = file_contents.split()
    Dict.dictionary = dict.fromkeys(Dict.word_list)
    wordCount = len(Dict.dictionary)
    print("Words in dictionary: " + str(wordCount))

def get_vector(array, dict):

    vector = [array.count(word) if word in array else 0 for word in dict]
    return np.array(vector)

def countarray(id, doc):
    f = open(doc, 'r+')
    lines = [line for line in f.readlines()]
    f.close()
    for i in lines:
        return lines[id].split()

def queryvect(q,index):
    array = []
    for i in index:
        if i in q:
            array.append(1)
        else:
            array.append(0)
    return np.array(array)

def InvertIndex(filename):
    ld={}
    ln=0
    for line in open(filename):
        ln+=1
        l = line.split()
        for word in l:
            if word not in ld:
                ld[word]=[]
                ld[word].append(1)
                ld[word].append([ln])
            else:
                ld[word][0]+=1
                ld[word][1].append(ln)
    for k in ld:
        ld[k][1] = set(ld[k][1])
    return ld

def DocSearch(Query):
    dict = InvertIndex('docs.txt')
    for line in open(Query):
        dict_angle = {}
        line = line.replace('\n','')
        line2 = line.split()
        print('Query: ', line)
        print('Relevant Documents: ',removesyntax(Search(line2, dict,)))
        for i in Search(line2, dict,):
            docvect = get_vector(countarray((i - 1), 'docs.txt'), Dict.dictionary)
            angle = calc_angle(docvect, queryvect(line2, dict))
            dict_angle[i] = angle
            dict_angle = {k: v for k, v in sorted(dict_angle.items(), key=lambda item: item[1])}
            a_list = list(dict_angle.items())
        for x in a_list:
            print(x[0], x[1])


def Search(q, index):
    matches = []
    for i in q:
        matches.extend(index[i][1])
    return list(set([x for x in matches if matches.count(x) == len(q)]))

def removesyntax(result):
    remove = result
    remove = str(remove)
    values = ['[',',',']']
    for change in values:
         remove = remove.replace(change, '')
    return remove


def main(docs, queries):
    Dict(docs)
    DocSearch(queries)

if __name__ == "__main__":
    main("docs.txt", "queries.txt")
