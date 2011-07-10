/*
Author: Matteo Romanello
email: matteo.romanello@gmail.com
*/

lexer grammar cp_lexer;

options {
  backtrack=true;
  language = Python;
}

INT :	'0'..'9'+;

PUNTO	:	DOT;
VIRGOLA	:	COMMA;
HYPHEN:	HYPHEN_fr;
SEMICOL:';';
fragment HYPHEN_fr	:	'-';
fragment DOT	:	'.';
fragment COMMA	:	',';
fragment CHAR	:	('A'..'Z'|'a'..'z'|'\u00E0'..'\u00FF');
fragment PUNCT	:	(DOT|COMMA|HYPHEN_fr)+;

// we should add the non breaking space as well 
WS:	(' ' |'\t' |'\r' |'\n')+ {$channel=HIDDEN;}	;
fragment R_C_BR:(')'|')' COMMA);
BRACKETS:	( '(' | R_C_BR )+ {self.skip();};
LITERAL	:	(CHAR+ PUNCT* CHAR*);