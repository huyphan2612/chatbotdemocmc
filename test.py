import spacy
nlp = spacy.load('vi_core_news_md')
# doc = nlp('thời tiết Sài Gòn ngày hôm nay?')
doc = nlp('thời tiết Sài Gòn ngày hôm nay?')
# print(doc.pipe_names)
for token in doc:
    print(token.text, token.pos_, token.dep_)

# import spacy
# from spacy.matcher import PhraseMatcher
# from spacy.tokens import Span
#
# class EntityMatcher(object):
#     name = 'entity_matcher'
#
#     def __init__(self, nlp, terms, label):
#         patterns = [nlp(text) for text in terms]
#         self.matcher = PhraseMatcher(nlp.vocab)
#         self.matcher.add(label, None, *patterns)
#
#     def __call__(self, doc):
#         matches = self.matcher(doc)
#         for match_id, start, end in matches:
#             span = Span(doc, start, end, label=match_id)
#             doc.ents = list(doc.ents) + [span]
#         return doc
#
# nlp = spacy.load('vi_core_news_md')
# terms = (u'cat', u'dog', u'tree kangaroo', u'giant sea spider')
# entity_matcher = EntityMatcher(nlp, terms, 'ANIMAL')
#
# nlp.add_pipe(entity_matcher, after='ner')
# print(nlp.pipe_names)  # the components in the pipeline
#
# doc = nlp(u"thời tiết Sài Gòn ngày hôm nay?")
# print([(ent.text, ent.label_) for ent in doc.ents])
