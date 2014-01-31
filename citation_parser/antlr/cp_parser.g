/*
Author: Matteo Romanello
email: matteo.romanello@gmail.com

The grammar parser for the citation parser to be used in combination with the citation extractor
but it may be used as a standalone piece of software.

*/

parser grammar cp_parser;
options {
	backtrack=true;
    language = Python;
    tokenVocab=cp_lexer;
    output=AST;
}

tokens{
	REF;
	CITATION;
	WORK;
	EDITOR;
	SCOPE;
	SCOPE_S;
	SCOPE_R;
	START;
	END;
	LEVEL;
}

// TODO: remove the doc element
// we loosely define the input, expected by this grammar
// as a sequence of citations

doc	:	(citation)+;

citation	: (ref (ref_separator ref)*)
->
^(CITATION ref ref*)
;

// reference separator: in a canonical citation
// a semicolon is used to separate multiple references

ref_separator: SEMICOL ->;

ref: work* scp editor*
->
^(REF work* scp editor*)
;

scp: (scp_single|scp_range);

work:
(LITERAL+)
->
^(WORK LITERAL+)
;

editor:
(LITERAL)
->
^(EDITOR LITERAL)
;

// TODO: change virgola and punto (name-wise)
lev_sep:(VIRGOLA|PUNTO);

level:
INT (lev_sep INT)*
->
^(LEVEL INT) ^(LEVEL INT)*
;

scp_single:
(level)
->
^(SCOPE_S level)
;

scp_range:
(level HYPHEN level)
->
^(SCOPE_R ^(START level) ^(END level))
;


