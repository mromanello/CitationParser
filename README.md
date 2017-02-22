CitationParser
==============

Canonical references (e.g. "Hom. *Il.* 1,124-125") use punctuation symbols in a consistent way, meaning that we can define a formal grammar to process them. 

When encountering the reference "Hom. *Il.* 1,124-125", the human reader will parse it as follows:

* the text preceding the numbers contains information about work and author being cited
* the hyphen is used to specify a range of text passages, e.g. lines 124 to 125;
* the semicolon separates a reference from another within the sanme citation (is common to chain together references to mutiple of the same work or of different works);
* the comma separates the hierarchical levels of the work being cited. In the example above 1,124-5 stands for from Book 1, Line 124 to Book 1, Line 125
* when the citation scope is a range, the identical hierarchical level are collapsed: 1.124 - 1.125 can be written as both 1.124-125 or 1.124 s. without any loss of information for the human reader.

The CitationParser is composed by a lexer, a parser and a tree parser written in ANTLR and compiled into Python code. The parsed reference is then serialized into JSON.

An example:

    >>> cp = CitationParser()
    >>> cp.parse("Hom. Il. 1,124-125")
    [{'work': u'Hom. Il.', 'scp': {'start': ['1', '124'], 'end': ['1', '125']}


