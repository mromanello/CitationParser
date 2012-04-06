# $ANTLR 3.1.2 cp_parser.g 2012-04-06 11:54:46

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
CHAR=12
LITERAL=17
INT=4
EOF=-1
VIRGOLA=8
REF=18
PUNTO=6
BRACKETS=16
EDITOR=21
WS=14
SCOPE=22
LEVEL=27
HYPHEN=10
COMMA=7
SEMICOL=11
START=25
HYPHEN_fr=9
SCOPE_S=23
END=26
DOT=5
PUNCT=13
CITATION=19
SCOPE_R=24
WORK=20
R_C_BR=15

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INT", "DOT", "PUNTO", "COMMA", "VIRGOLA", "HYPHEN_fr", "HYPHEN", "SEMICOL", 
    "CHAR", "PUNCT", "WS", "R_C_BR", "BRACKETS", "LITERAL", "REF", "CITATION", 
    "WORK", "EDITOR", "SCOPE", "SCOPE_S", "SCOPE_R", "START", "END", "LEVEL"
]




class cp_parser(Parser):
    grammarFileName = "cp_parser.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        Parser.__init__(self, input, state)


        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )






                
        self._adaptor = CommonTreeAdaptor()


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class doc_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "doc"
    # cp_parser.g:35:1: doc : ( citation )+ ;
    def doc(self, ):

        retval = self.doc_return()
        retval.start = self.input.LT(1)

        root_0 = None

        citation1 = None



        try:
            try:
                # cp_parser.g:35:5: ( ( citation )+ )
                # cp_parser.g:35:7: ( citation )+
                pass 
                root_0 = self._adaptor.nil()

                # cp_parser.g:35:7: ( citation )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == INT or LA1_0 == LITERAL) :
                        alt1 = 1


                    if alt1 == 1:
                        # cp_parser.g:35:8: citation
                        pass 
                        self._state.following.append(self.FOLLOW_citation_in_doc104)
                        citation1 = self.citation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, citation1.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "doc"

    class citation_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "citation"
    # cp_parser.g:37:1: citation : ( ref ( ref_separator ref )* ) -> ^( CITATION ref ( ref )* ) ;
    def citation(self, ):

        retval = self.citation_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ref2 = None

        ref_separator3 = None

        ref4 = None


        stream_ref = RewriteRuleSubtreeStream(self._adaptor, "rule ref")
        stream_ref_separator = RewriteRuleSubtreeStream(self._adaptor, "rule ref_separator")
        try:
            try:
                # cp_parser.g:37:10: ( ( ref ( ref_separator ref )* ) -> ^( CITATION ref ( ref )* ) )
                # cp_parser.g:37:12: ( ref ( ref_separator ref )* )
                pass 
                # cp_parser.g:37:12: ( ref ( ref_separator ref )* )
                # cp_parser.g:37:13: ref ( ref_separator ref )*
                pass 
                self._state.following.append(self.FOLLOW_ref_in_citation115)
                ref2 = self.ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_ref.add(ref2.tree)
                # cp_parser.g:37:17: ( ref_separator ref )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == SEMICOL) :
                        alt2 = 1


                    if alt2 == 1:
                        # cp_parser.g:37:18: ref_separator ref
                        pass 
                        self._state.following.append(self.FOLLOW_ref_separator_in_citation118)
                        ref_separator3 = self.ref_separator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ref_separator.add(ref_separator3.tree)
                        self._state.following.append(self.FOLLOW_ref_in_citation120)
                        ref4 = self.ref()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ref.add(ref4.tree)


                    else:
                        break #loop2






                # AST Rewrite
                # elements: ref, ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 38:1: -> ^( CITATION ref ( ref )* )
                    # cp_parser.g:39:1: ^( CITATION ref ( ref )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CITATION, "CITATION"), root_1)

                    self._adaptor.addChild(root_1, stream_ref.nextTree())
                    # cp_parser.g:39:16: ( ref )*
                    while stream_ref.hasNext():
                        self._adaptor.addChild(root_1, stream_ref.nextTree())


                    stream_ref.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "citation"

    class ref_separator_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "ref_separator"
    # cp_parser.g:45:1: ref_separator : SEMICOL ->;
    def ref_separator(self, ):

        retval = self.ref_separator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMICOL5 = None

        SEMICOL5_tree = None
        stream_SEMICOL = RewriteRuleTokenStream(self._adaptor, "token SEMICOL")

        try:
            try:
                # cp_parser.g:45:14: ( SEMICOL ->)
                # cp_parser.g:45:16: SEMICOL
                pass 
                SEMICOL5=self.match(self.input, SEMICOL, self.FOLLOW_SEMICOL_in_ref_separator145) 
                if self._state.backtracking == 0:
                    stream_SEMICOL.add(SEMICOL5)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 45:24: ->
                    root_0 = None


                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "ref_separator"

    class ref_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "ref"
    # cp_parser.g:47:1: ref : ( work )* scp ( editor )* -> ^( REF ( work )* scp ( editor )* ) ;
    def ref(self, ):

        retval = self.ref_return()
        retval.start = self.input.LT(1)

        root_0 = None

        work6 = None

        scp7 = None

        editor8 = None


        stream_work = RewriteRuleSubtreeStream(self._adaptor, "rule work")
        stream_scp = RewriteRuleSubtreeStream(self._adaptor, "rule scp")
        stream_editor = RewriteRuleSubtreeStream(self._adaptor, "rule editor")
        try:
            try:
                # cp_parser.g:47:4: ( ( work )* scp ( editor )* -> ^( REF ( work )* scp ( editor )* ) )
                # cp_parser.g:47:6: ( work )* scp ( editor )*
                pass 
                # cp_parser.g:47:6: ( work )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == LITERAL) :
                        alt3 = 1


                    if alt3 == 1:
                        # cp_parser.g:0:0: work
                        pass 
                        self._state.following.append(self.FOLLOW_work_in_ref154)
                        work6 = self.work()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_work.add(work6.tree)


                    else:
                        break #loop3


                self._state.following.append(self.FOLLOW_scp_in_ref157)
                scp7 = self.scp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_scp.add(scp7.tree)
                # cp_parser.g:47:16: ( editor )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == LITERAL) :
                        LA4_2 = self.input.LA(2)

                        if (self.synpred4_cp_parser()) :
                            alt4 = 1




                    if alt4 == 1:
                        # cp_parser.g:0:0: editor
                        pass 
                        self._state.following.append(self.FOLLOW_editor_in_ref159)
                        editor8 = self.editor()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_editor.add(editor8.tree)


                    else:
                        break #loop4



                # AST Rewrite
                # elements: scp, work, editor
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 48:1: -> ^( REF ( work )* scp ( editor )* )
                    # cp_parser.g:49:1: ^( REF ( work )* scp ( editor )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REF, "REF"), root_1)

                    # cp_parser.g:49:7: ( work )*
                    while stream_work.hasNext():
                        self._adaptor.addChild(root_1, stream_work.nextTree())


                    stream_work.reset();
                    self._adaptor.addChild(root_1, stream_scp.nextTree())
                    # cp_parser.g:49:17: ( editor )*
                    while stream_editor.hasNext():
                        self._adaptor.addChild(root_1, stream_editor.nextTree())


                    stream_editor.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "ref"

    class scp_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "scp"
    # cp_parser.g:52:1: scp : ( scp_single | scp_range ) ;
    def scp(self, ):

        retval = self.scp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        scp_single9 = None

        scp_range10 = None



        try:
            try:
                # cp_parser.g:52:4: ( ( scp_single | scp_range ) )
                # cp_parser.g:52:6: ( scp_single | scp_range )
                pass 
                root_0 = self._adaptor.nil()

                # cp_parser.g:52:6: ( scp_single | scp_range )
                alt5 = 2
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # cp_parser.g:52:7: scp_single
                    pass 
                    self._state.following.append(self.FOLLOW_scp_single_in_scp183)
                    scp_single9 = self.scp_single()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, scp_single9.tree)


                elif alt5 == 2:
                    # cp_parser.g:52:18: scp_range
                    pass 
                    self._state.following.append(self.FOLLOW_scp_range_in_scp185)
                    scp_range10 = self.scp_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, scp_range10.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "scp"

    class work_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "work"
    # cp_parser.g:54:1: work : ( ( LITERAL )+ ) -> ^( WORK ( LITERAL )+ ) ;
    def work(self, ):

        retval = self.work_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LITERAL11 = None

        LITERAL11_tree = None
        stream_LITERAL = RewriteRuleTokenStream(self._adaptor, "token LITERAL")

        try:
            try:
                # cp_parser.g:54:5: ( ( ( LITERAL )+ ) -> ^( WORK ( LITERAL )+ ) )
                # cp_parser.g:55:1: ( ( LITERAL )+ )
                pass 
                # cp_parser.g:55:1: ( ( LITERAL )+ )
                # cp_parser.g:55:2: ( LITERAL )+
                pass 
                # cp_parser.g:55:2: ( LITERAL )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LITERAL) :
                        LA6_2 = self.input.LA(2)

                        if (self.synpred6_cp_parser()) :
                            alt6 = 1




                    if alt6 == 1:
                        # cp_parser.g:0:0: LITERAL
                        pass 
                        LITERAL11=self.match(self.input, LITERAL, self.FOLLOW_LITERAL_in_work194) 
                        if self._state.backtracking == 0:
                            stream_LITERAL.add(LITERAL11)


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1






                # AST Rewrite
                # elements: LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 56:1: -> ^( WORK ( LITERAL )+ )
                    # cp_parser.g:57:1: ^( WORK ( LITERAL )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(WORK, "WORK"), root_1)

                    # cp_parser.g:57:8: ( LITERAL )+
                    if not (stream_LITERAL.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_LITERAL.hasNext():
                        self._adaptor.addChild(root_1, stream_LITERAL.nextNode())


                    stream_LITERAL.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "work"

    class editor_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "editor"
    # cp_parser.g:60:1: editor : ( LITERAL ) -> ^( EDITOR LITERAL ) ;
    def editor(self, ):

        retval = self.editor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LITERAL12 = None

        LITERAL12_tree = None
        stream_LITERAL = RewriteRuleTokenStream(self._adaptor, "token LITERAL")

        try:
            try:
                # cp_parser.g:60:7: ( ( LITERAL ) -> ^( EDITOR LITERAL ) )
                # cp_parser.g:61:1: ( LITERAL )
                pass 
                # cp_parser.g:61:1: ( LITERAL )
                # cp_parser.g:61:2: LITERAL
                pass 
                LITERAL12=self.match(self.input, LITERAL, self.FOLLOW_LITERAL_in_editor214) 
                if self._state.backtracking == 0:
                    stream_LITERAL.add(LITERAL12)




                # AST Rewrite
                # elements: LITERAL
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 62:1: -> ^( EDITOR LITERAL )
                    # cp_parser.g:63:1: ^( EDITOR LITERAL )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EDITOR, "EDITOR"), root_1)

                    self._adaptor.addChild(root_1, stream_LITERAL.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "editor"

    class lev_sep_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "lev_sep"
    # cp_parser.g:67:1: lev_sep : ( VIRGOLA | PUNTO ) ;
    def lev_sep(self, ):

        retval = self.lev_sep_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set13 = None

        set13_tree = None

        try:
            try:
                # cp_parser.g:67:8: ( ( VIRGOLA | PUNTO ) )
                # cp_parser.g:67:9: ( VIRGOLA | PUNTO )
                pass 
                root_0 = self._adaptor.nil()

                set13 = self.input.LT(1)
                if self.input.LA(1) == PUNTO or self.input.LA(1) == VIRGOLA:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set13))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "lev_sep"

    class level_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "level"
    # cp_parser.g:69:1: level : INT ( lev_sep INT )* -> ^( LEVEL INT ) ( ^( LEVEL INT ) )* ;
    def level(self, ):

        retval = self.level_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INT14 = None
        INT16 = None
        lev_sep15 = None


        INT14_tree = None
        INT16_tree = None
        stream_INT = RewriteRuleTokenStream(self._adaptor, "token INT")
        stream_lev_sep = RewriteRuleSubtreeStream(self._adaptor, "rule lev_sep")
        try:
            try:
                # cp_parser.g:69:6: ( INT ( lev_sep INT )* -> ^( LEVEL INT ) ( ^( LEVEL INT ) )* )
                # cp_parser.g:70:1: INT ( lev_sep INT )*
                pass 
                INT14=self.match(self.input, INT, self.FOLLOW_INT_in_level242) 
                if self._state.backtracking == 0:
                    stream_INT.add(INT14)
                # cp_parser.g:70:5: ( lev_sep INT )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == PUNTO or LA7_0 == VIRGOLA) :
                        alt7 = 1


                    if alt7 == 1:
                        # cp_parser.g:70:6: lev_sep INT
                        pass 
                        self._state.following.append(self.FOLLOW_lev_sep_in_level245)
                        lev_sep15 = self.lev_sep()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_lev_sep.add(lev_sep15.tree)
                        INT16=self.match(self.input, INT, self.FOLLOW_INT_in_level247) 
                        if self._state.backtracking == 0:
                            stream_INT.add(INT16)


                    else:
                        break #loop7



                # AST Rewrite
                # elements: INT, INT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:1: -> ^( LEVEL INT ) ( ^( LEVEL INT ) )*
                    # cp_parser.g:72:1: ^( LEVEL INT )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LEVEL, "LEVEL"), root_1)

                    self._adaptor.addChild(root_1, stream_INT.nextNode())

                    self._adaptor.addChild(root_0, root_1)
                    # cp_parser.g:72:14: ( ^( LEVEL INT ) )*
                    while stream_INT.hasNext():
                        # cp_parser.g:72:14: ^( LEVEL INT )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(LEVEL, "LEVEL"), root_1)

                        self._adaptor.addChild(root_1, stream_INT.nextNode())

                        self._adaptor.addChild(root_0, root_1)


                    stream_INT.reset();



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "level"

    class scp_single_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "scp_single"
    # cp_parser.g:75:1: scp_single : ( level ) -> ^( SCOPE_S level ) ;
    def scp_single(self, ):

        retval = self.scp_single_return()
        retval.start = self.input.LT(1)

        root_0 = None

        level17 = None


        stream_level = RewriteRuleSubtreeStream(self._adaptor, "rule level")
        try:
            try:
                # cp_parser.g:75:11: ( ( level ) -> ^( SCOPE_S level ) )
                # cp_parser.g:76:1: ( level )
                pass 
                # cp_parser.g:76:1: ( level )
                # cp_parser.g:76:2: level
                pass 
                self._state.following.append(self.FOLLOW_level_in_scp_single273)
                level17 = self.level()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_level.add(level17.tree)




                # AST Rewrite
                # elements: level
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 77:1: -> ^( SCOPE_S level )
                    # cp_parser.g:78:1: ^( SCOPE_S level )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SCOPE_S, "SCOPE_S"), root_1)

                    self._adaptor.addChild(root_1, stream_level.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "scp_single"

    class scp_range_return(ParserRuleReturnScope):
        def __init__(self):
            ParserRuleReturnScope.__init__(self)

            self.tree = None




    # $ANTLR start "scp_range"
    # cp_parser.g:81:1: scp_range : ( level HYPHEN level ) -> ^( SCOPE_R ^( START level ) ^( END level ) ) ;
    def scp_range(self, ):

        retval = self.scp_range_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HYPHEN19 = None
        level18 = None

        level20 = None


        HYPHEN19_tree = None
        stream_HYPHEN = RewriteRuleTokenStream(self._adaptor, "token HYPHEN")
        stream_level = RewriteRuleSubtreeStream(self._adaptor, "rule level")
        try:
            try:
                # cp_parser.g:81:10: ( ( level HYPHEN level ) -> ^( SCOPE_R ^( START level ) ^( END level ) ) )
                # cp_parser.g:82:1: ( level HYPHEN level )
                pass 
                # cp_parser.g:82:1: ( level HYPHEN level )
                # cp_parser.g:82:2: level HYPHEN level
                pass 
                self._state.following.append(self.FOLLOW_level_in_scp_range291)
                level18 = self.level()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_level.add(level18.tree)
                HYPHEN19=self.match(self.input, HYPHEN, self.FOLLOW_HYPHEN_in_scp_range293) 
                if self._state.backtracking == 0:
                    stream_HYPHEN.add(HYPHEN19)
                self._state.following.append(self.FOLLOW_level_in_scp_range295)
                level20 = self.level()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_level.add(level20.tree)




                # AST Rewrite
                # elements: level, level
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 83:1: -> ^( SCOPE_R ^( START level ) ^( END level ) )
                    # cp_parser.g:84:1: ^( SCOPE_R ^( START level ) ^( END level ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SCOPE_R, "SCOPE_R"), root_1)

                    # cp_parser.g:84:11: ^( START level )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(START, "START"), root_2)

                    self._adaptor.addChild(root_2, stream_level.nextTree())

                    self._adaptor.addChild(root_1, root_2)
                    # cp_parser.g:84:26: ^( END level )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(END, "END"), root_2)

                    self._adaptor.addChild(root_2, stream_level.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass

        return retval

    # $ANTLR end "scp_range"

    # $ANTLR start "synpred4_cp_parser"
    def synpred4_cp_parser_fragment(self, ):
        # cp_parser.g:47:16: ( editor )
        # cp_parser.g:47:16: editor
        pass 
        self._state.following.append(self.FOLLOW_editor_in_synpred4_cp_parser159)
        self.editor()

        self._state.following.pop()


    # $ANTLR end "synpred4_cp_parser"



    # $ANTLR start "synpred6_cp_parser"
    def synpred6_cp_parser_fragment(self, ):
        # cp_parser.g:55:2: ( LITERAL )
        # cp_parser.g:55:2: LITERAL
        pass 
        self.match(self.input, LITERAL, self.FOLLOW_LITERAL_in_synpred6_cp_parser194)


    # $ANTLR end "synpred6_cp_parser"




    # Delegated rules

    def synpred6_cp_parser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred6_cp_parser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_cp_parser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_cp_parser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\1\uffff\1\4\3\uffff\1\4"
        )

    DFA5_min = DFA.unpack(
        u"\3\4\2\uffff\1\4"
        )

    DFA5_max = DFA.unpack(
        u"\1\4\1\21\1\4\2\uffff\1\21"
        )

    DFA5_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1\1\uffff"
        )

    DFA5_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\4\1\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\4\5\uffff"
        u"\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\uffff\1\2\1\uffff\1\2\1\uffff\1\3\1\4\5\uffff"
        u"\1\4")
    ]

    # class definition for DFA #5

    DFA5 = DFA
 

    FOLLOW_citation_in_doc104 = frozenset([1, 4, 17])
    FOLLOW_ref_in_citation115 = frozenset([1, 11])
    FOLLOW_ref_separator_in_citation118 = frozenset([4, 11, 17])
    FOLLOW_ref_in_citation120 = frozenset([1, 11])
    FOLLOW_SEMICOL_in_ref_separator145 = frozenset([1])
    FOLLOW_work_in_ref154 = frozenset([4, 17])
    FOLLOW_scp_in_ref157 = frozenset([1, 17])
    FOLLOW_editor_in_ref159 = frozenset([1, 17])
    FOLLOW_scp_single_in_scp183 = frozenset([1])
    FOLLOW_scp_range_in_scp185 = frozenset([1])
    FOLLOW_LITERAL_in_work194 = frozenset([1, 17])
    FOLLOW_LITERAL_in_editor214 = frozenset([1])
    FOLLOW_set_in_lev_sep231 = frozenset([1])
    FOLLOW_INT_in_level242 = frozenset([1, 6, 8])
    FOLLOW_lev_sep_in_level245 = frozenset([4])
    FOLLOW_INT_in_level247 = frozenset([1, 6, 8])
    FOLLOW_level_in_scp_single273 = frozenset([1])
    FOLLOW_level_in_scp_range291 = frozenset([10])
    FOLLOW_HYPHEN_in_scp_range293 = frozenset([4])
    FOLLOW_level_in_scp_range295 = frozenset([1])
    FOLLOW_editor_in_synpred4_cp_parser159 = frozenset([1])
    FOLLOW_LITERAL_in_synpred6_cp_parser194 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("cp_parserLexer", cp_parser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
