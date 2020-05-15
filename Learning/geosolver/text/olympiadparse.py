from pyparsing import *
import string
from geosolver.text.syntax_parser import SyntaxParse, stanford_parser
from geosolver.ontology.ontology_definitions import signatures, FunctionSignature, VariableSignature
from geosolver.text.rule import TagRule
from geosolver.text.semantic_tree import SemanticTreeNode
from geosolver.utils.num import is_number
from geosolver.database.states import Question

__author__ = 'minjoon'

def questions_to_syntax_parses(questions, parser=True):
    syntax_parses = {pk: {number: stanford_parser.get_best_syntax_parse(words, parser=parser)
                          for number, words in question.sentence_words.items()} # break into sentences first
                     for pk, question in questions.items()}
    return syntax_parses

def annotation_to_semantic_tree(syntax_parse, annotation_string):
    words = syntax_parse.words
    def span_f(a, b, c):
        if len(c) == 1:
            if c[0] == 'i':
                return 'i'
            else:
                return int(c[0]), int(c[0])+1
        else:
            return int(c[0]), int(c[1])+1

    def tag_f(a, b, c):
        assert len(c) == 1
        if c[0][0].isupper() or is_number(c[0]):
            return 'function', c[0]
        else:
            return 'variable', c[0]

    def expr_f(a, b, c): # c[0] = (function/variable, signature = type)
        # c[1] = relation name
        # c[2] = what it connects to -> arguments
        local_span = c[1]
        children = c[2:]
        type_, s = c[0]
        name = "_".join(words[idx] for idx in range(*local_span))
        if s in signatures:
            signature = signatures[s]
        elif type_ == 'function' and len(children) == 0:
            # Constant number
            signature = FunctionSignature(name, 'number', [], name=name)
        elif type_ == 'variable' and len(children) == 0:
            signature = VariableSignature((local_span, s), s, name=name)
        else:
            raise Exception("local span: %r, children: %r, type: %r, s: %r"
                            % (local_span, children, type_, s))
        content = TagRule(syntax_parse, local_span, signature)
        return SemanticTreeNode(content, children)

    current = Word(alphanums)
    span = (Word(nums) + Literal(":").suppress() + Word(nums)) | Word(nums)
    string = Literal("[").suppress() + Word(alphanums+"_") + Literal("]").suppress()
    tag = current.setParseAction(tag_f) + Literal("@").suppress() + span.setParseAction(span_f) + Optional(string).suppress()
    expr = Forward()
    expr << (tag + Optional(Literal("(").suppress() + expr +
                           ZeroOrMore(Literal(",").suppress() + expr) + Literal(")").suppress()))
    tokens = expr.setParseAction(expr_f).parseString(annotation_string)
    return tokens[0]

def is_valid_annotation(syntax_parse, annotation_string):
    try:
        annotation_to_semantic_tree(syntax_parse, annotation_string)
        return True
    except:
        return False

# copied from geoserver_interface.py

# read file time
testfile = open("olycases.txt", "r+")
questions = {}
olyqs = testfile.readlines()
key = 0
for quest in olyqs:
    temp_filepath = ''
    choices = {"1": "2*sqrt(17)", "2": "sqrt(17)", "3": "17", "4": "2023"} #  {int(number): text for number, text in pair['choices'].items()}
    answer = "17"  # pair['answer']
    split_words = quest.split('.')  # pair['text'].split('.')
    new_split_words = [string for string in split_words if string and string != "\n"]
    sentence_words = {}
    for i in range(len(new_split_words)):
        sentence = new_split_words[i]
        word_break = sentence.split()
        exclude = set("!(),:;?@[]{}~")
        new_words = []
        for j in word_break:
            currword = ''
            addendums = []
            for ch in j:
                if ch not in exclude:
                    currword += ch
                else:
                    addendums.append(ch)
            new_words.append(currword)
            for punct in addendums:
                new_words.append(punct)
        new_words.append('.')
        temp_dict = {j: new_words[j] for j in range(len(new_words))}
        sentence_words[i] = temp_dict
    sentence_expressions = {}
    choice_words = {}
    choice_expressions = {}
    qu = Question(key, quest, sentence_words, sentence_expressions, temp_filepath, choice_words, choice_expressions, answer, choices)
    questions[qu.key] = qu
    key += 1
# '''Let Gamma be the circumcircle of acute triangle ABC. Points D and E are on segments AB and AC respectively
# such that AD = AE. The perpendicular bisectors of BD and CE intersect minor arcs AB and AC of Gamma at
# points F and G respectively. Prove that lines DE and FG are either parallel or they are the same line.'''


# SYNTAX PARSING !!!!

#pair = {"answer": "17", "text": "In the figure above, line AB, line CD, and line EF intersect at P.", "key": 17, "choices": {"1": "2*sqrt(5)", "2": "8", "3": "10", "4": "16"}}
# temp_filepath = ''
# choices = {"1": "2*sqrt(17)", "2": "sqrt(17)", "3": "17", "4": "2023"} #  {int(number): text for number, text in pair['choices'].items()}
# answer = "17"  # pair['answer']
# split_words = pair['text'].split('.')
# new_split_words = [string for string in split_words if string]
# sentence_words = {}
# for i in range(len(new_split_words)):
#     sentence = new_split_words[i]
#     word_break = sentence.split()
#     exclude = set("!(),:;?@[]{}~")
#     new_words = []
#     for j in word_break:
#         currword = ''
#         addendums = []
#         for ch in j:
#             if ch not in exclude:
#                 currword += ch
#             else:
#                 addendums.append(ch)
#         new_words.append(currword)
#         for punct in addendums:
#             new_words.append(punct)
#     new_words.append('.')
#     temp_dict = {j: new_words[j] for j in range(len(new_words))}
#     sentence_words[i] = temp_dict
# #{int(number): {int(index): word for index, word in words.items()} for number, words in pair['sentence_words'].items()}
# sentence_expressions = {}
# choice_words = {}
# choice_expressions = {}
# qu = Question(pair['key'], pair['text'], sentence_words, sentence_expressions, temp_filepath, choice_words, choice_expressions, answer, choices)
# questions[qu.key] = qu
syntax_parse = questions_to_syntax_parses(questions)
print(syntax_parse)
for sentparse in syntax_parse.values():
    for key, sparse in sentparse.items():
        print(sparse.words)

# ANNOTATIONS
# annotations = {0: 'IsLine@5(line@6)', 1: 'IsLine@8(line@9)', 2: 'IsLine@12(line@13)', 3: 'CC@11(line@6, line@9)', 4: 'CC@11(line@6, line@13)',
# 5: 'IntersectAt@14(line@6, point@16)'}
# semantic_trees = [annotation_to_semantic_tree(syntax_parse[17][0], annotation) for annotation in annotations.values()]
# print(semantic_trees)
