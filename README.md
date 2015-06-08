CitationParser
==============

The CitationParser (CiPa) is composed by a lexer, a parser and a tree parser written in ANTLR and compiled into Python code.

The idea behind CiPa id pretty simple. Canonical citations are constructed using punctuation symbols in a consistent way, so that we can define a syntax to extract their meaning. Once extracted the meaning is then formalised into JSON as intermendiate representation format.

Given for example the citation """ Hom. Il. 1, 124 - 125 """, to a human reader the following facts are known:
* the hyphen is used to specify a range of text passages, from X to Y
* the characetr string preceding the numbers contains information about work and author being cited
* the semicolon separates a reference from another within the sanme citation (is common to chain together references to mutiple of the same work or of different works) 
* the comma separates the heirarchical level of the work being cited. In the example above 1,124-5 stands for from Book 1, Line 124 to Book 1, Line 125
* when the citation scope is a range, the identical hierarchical level are collapsed: 1.124 - 1.125 can be written as 1.124-125 or 1.124 s. without any loss of information for the human reader

So, given the input:
	Hom. Il. 1, 124 - 125
the output of the citation parser expressed in JSON is:
	"[{'work': u'Hom. Il.', 'scp': {'start': ['1', '124'], 'end': ['1', '125']}
	
## Compile the ANTLR grammar files

From the directory `./citation_parser/antlr/`, run:

    java -cp ../../lib/antlr-3.1.2.jar org.antlr.Tool -o ~/Downloads/ cp_lexer.g cp_parser.g cp_treeparser.g

