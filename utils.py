import torch
import clip

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    torch.cuda.set_device(device)
else:
    device = torch.device("cpu")

clip_model, preprocess = clip.load('ViT-B/32', device, jit=False)


def chunking_sentence(sentence, use_template=False, obj_part=False):
    '''
    template: A 3D rendering of xxx in unreal engine.
    '''
    from nltk import word_tokenize, pos_tag, RegexpParser

    # 定义一个函数来划分名词短语
    def extract_noun_phrases(sentence):
        def merge_(noun_phrases1, noun_phrases2):
            if len(noun_phrases2) == 0: return noun_phrases1

            idx_list = []
            for idx in range(len(noun_phrases1)):
                phrase1 = noun_phrases1[idx]
                for phrase2 in noun_phrases2:
                    if phrase1 in phrase2:
                        idx_list.append(idx)
            
            for idx in range(len(noun_phrases1)):
                if idx not in idx_list:
                    noun_phrases2.append(noun_phrases1[idx])

            # return noun_phrases2
            return sorted(noun_phrases2, key=lambda x: sentence.index(x))
        
        # 分词和词性标注
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)

        # 定义一个名词短语的分块语法规则
        grammar1 = r"""
            NP: {<DT|JJ|NN.*>+}
        """
        chunk_parser1 = RegexpParser(grammar1)
        tree1 = chunk_parser1.parse(tagged_words)
        # 提取名词短语
        noun_phrases1 = []
        for subtree in tree1.subtrees(filter=lambda t: t.label() == 'NP'):
            noun_phrase = ' '.join(word for word, tag in subtree.leaves())
            noun_phrases1.append(noun_phrase)

        # 定义名词短语的语法规则，包括介词短语
        grammar2 = r"""
        NP: {<DT|JJ|NN.*>+<IN><DT|JJ|NN.*>+}
        """
        chunk_parser2 = RegexpParser(grammar2)
        tree2 = chunk_parser2.parse(tagged_words)
        # 提取后跟介词短语的名词短语
        noun_phrases2 = []
        for subtree in tree2.subtrees():
            if subtree.label() == 'NP':
                noun_phrases2.append(" ".join(word for word, tag in subtree.leaves()))

        # print('noun_phrases1: ', noun_phrases1)
        # print('noun_phrases2: ', noun_phrases2)
        if obj_part:
            return noun_phrases1
        return merge_(noun_phrases1, noun_phrases2)

    def matching_object_from_sentence(text, sentence):
        pos = sentence.index(text)                      # 字符串匹配
        start_ = len(sentence[:pos].split(' ')) - 1
        end_ = start_ + len(text.split(' '))

        return start_, end_                             # 返回单词位置索引

    # 调用划分函数
    results = extract_noun_phrases(sentence if not use_template else ' '.join(sentence.split(' ')[4:-3]))
    # print(results)

    output = [matching_object_from_sentence(text, sentence) for text in results]

    return output
