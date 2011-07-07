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

doc	:	(citation)+;

citation	: (ref (ref_separator ref)*)
->
^(CITATION ref ref*)
;

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


