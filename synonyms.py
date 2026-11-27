'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):

    numerator = 0
    denominator = norm(vec1) * norm(vec2)

    for x in vec1:
        if x in vec2:
            numerator += vec1[x] * vec2[x]

    return numerator/denominator

def build_semantic_descriptors(sentences):

    semantic_descriptors = {}

    for sentence in sentences:

        unique_words = {}
        for word in sentence: ## Only count new words once per sentence
            unique_words[word] = None

        for word1 in unique_words:
            if word1 not in semantic_descriptors:
                semantic_descriptors[word1] = {}

            for word2 in unique_words:
                if word1 != word2:
                
                    if word2 not in semantic_descriptors[word1]:
                        semantic_descriptors[word1][word2] = 0
                    semantic_descriptors[word1][word2] += 1

    return semantic_descriptors


def build_semantic_descriptors_from_files(filenames):
    all_sentences =  []
    sentence_spacers = ["!", "?"]
    additional_punctuation = [",", "-", "--", ":", ";"]

    for filename in filenames:
        file_in = open(filename, "r", encoding='latin1')
        text = file_in.read()
        file_in.close()
            
        for punctuation in additional_punctuation:
            text = text.replace(punctuation, " ")
        for spacer in sentence_spacers:
            text = text.replace(spacer, ".")

        text = text.lower()
        sentences = text.split(".")
        for i in range(len(sentences)):
            sentences[i] = sentences[i].split()

        all_sentences.extend(sentences)

    return build_semantic_descriptors(all_sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    if word not in semantic_descriptors or semantic_descriptors[word] == {}:
        return choices[0]
    
    vec_word = semantic_descriptors[word]
    results = []

    for choice in choices:

        if choice not in semantic_descriptors or semantic_descriptors[choice] == {}:
            results.append(-1)
        else:
            results.append(similarity_fn(vec_word, semantic_descriptors[choice]))

    index = results.index(max(results))
    return choices[index]



def run_similarity_test(filename, semantic_descriptors, similarity_fn):

    count_correct = 0
    count_total = 0

    with open(filename, 'r', encoding='latin-1') as file_in:

        for line in file_in:
            line = line.strip().split()
            word = line[0]
            choices = line[2:]
            answer = line[1]
            most_similar = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
            if most_similar == answer:
                count_correct += 1
            count_total += 1

    return 100 * (count_correct/count_total)


