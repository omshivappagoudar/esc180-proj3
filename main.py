from synonyms import *

if __name__ == "__main__":
    print(cosine_similarity({"a": 1, "b": 2, "c": 3},{"b": 4, "c": 5, "d": 6}))
    # print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
    # ["i", "am", "a", "spiteful", "man"],
    # ["i", "am", "an", "unattractive", "man"],
    # ["i", "believe", "my", "liver", "is", "diseased"],
    # ["however", "i", "know", "nothing", "at", "all", "about", "my",
    # "disease", "and", "do", "not", "know", "for", "certain",
    # "what", "ails", "me"]])) 
    print(run_similarity_test("test.txt", {}, cosine_similarity))
    test = 'I!HOPE!YOU!ARE!HAVING!A!GOOD!DAY!!!'
    print(test.split("!"))