# $ANTLR 3.1.2 cp_treeparser.g 2012-04-06 11:54:47

import sys
from antlr3 import *
from antlr3.tree import *
from antlr3.compat import set, frozenset


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
DOT=5
END=26
CITATION=19
PUNCT=13
WORK=20
SCOPE_R=24
R_C_BR=15

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INT", "DOT", "PUNTO", "COMMA", "VIRGOLA", "HYPHEN_fr", "HYPHEN", "SEMICOL", 
    "CHAR", "PUNCT", "WS", "R_C_BR", "BRACKETS", "LITERAL", "REF", "CITATION", 
    "WORK", "EDITOR", "SCOPE", "SCOPE_S", "SCOPE_R", "START", "END", "LEVEL"
]




class cp_treeparser(TreeParser):
    grammarFileName = "cp_treeparser.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"
    tokenNames = tokenNames

    def __init__(self, input, state=None):
        if state is None:
            state = RecognizerSharedState()

        TreeParser.__init__(self, input, state)




              
        import logging
        self.logger = logging.getLogger("Main.cp_treeparser")
        self.refs=[]
        self.prev_ref={}
        self.curr_ref=None
        self.count=0
        self.levels=[]




                


        



    # $ANTLR start "doc"
    # cp_treeparser.g:24:1: doc : ( citation )+ ;
    def doc(self, ):

        try:
            try:
                # cp_treeparser.g:24:5: ( ( citation )+ )
                # cp_treeparser.g:24:7: ( citation )+
                pass 
                # cp_treeparser.g:24:7: ( citation )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CITATION) :
                        alt1 = 1


                    if alt1 == 1:
                        # cp_treeparser.g:24:7: citation
                        pass 
                        self._state.following.append(self.FOLLOW_citation_in_doc56)
                        self.citation()

                        self._state.following.pop()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "doc"


    # $ANTLR start "citation"
    # cp_treeparser.g:27:1: citation : ^( CITATION ref ( ref )* ) ;
    def citation(self, ):

        try:
            try:
                # cp_treeparser.g:31:2: ( ^( CITATION ref ( ref )* ) )
                # cp_treeparser.g:32:1: ^( CITATION ref ( ref )* )
                pass 
                self.match(self.input, CITATION, self.FOLLOW_CITATION_in_citation70)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_ref_in_citation72)
                self.ref()

                self._state.following.pop()
                # cp_treeparser.g:32:16: ( ref )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == REF) :
                        alt2 = 1


                    if alt2 == 1:
                        # cp_treeparser.g:32:16: ref
                        pass 
                        self._state.following.append(self.FOLLOW_ref_in_citation74)
                        self.ref()

                        self._state.following.pop()


                    else:
                        break #loop2



                self.match(self.input, UP, None)



                #action start
                       
                result = {}
                result["refs"]=self.refs

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "citation"


    # $ANTLR start "ref"
    # cp_treeparser.g:35:1: ref : ^( REF ( work )* scp ( editor )* ) ;
    def ref(self, ):

              
        if(self.curr_ref is None):
        	self.curr_ref = {}
        else:
        	self.prev_ref=dict(self.curr_ref)
        	self.curr_ref={}

        try:
            try:
                # cp_treeparser.g:51:1: ( ^( REF ( work )* scp ( editor )* ) )
                # cp_treeparser.g:52:1: ^( REF ( work )* scp ( editor )* )
                pass 
                self.match(self.input, REF, self.FOLLOW_REF_in_ref97)

                self.match(self.input, DOWN, None)
                # cp_treeparser.g:52:7: ( work )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == WORK) :
                        alt3 = 1


                    if alt3 == 1:
                        # cp_treeparser.g:52:7: work
                        pass 
                        self._state.following.append(self.FOLLOW_work_in_ref99)
                        self.work()

                        self._state.following.pop()


                    else:
                        break #loop3


                self._state.following.append(self.FOLLOW_scp_in_ref102)
                self.scp()

                self._state.following.pop()
                # cp_treeparser.g:52:17: ( editor )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == EDITOR) :
                        alt4 = 1


                    if alt4 == 1:
                        # cp_treeparser.g:52:17: editor
                        pass 
                        self._state.following.append(self.FOLLOW_editor_in_ref104)
                        self.editor()

                        self._state.following.pop()


                    else:
                        break #loop4



                self.match(self.input, UP, None)



                #action start
                       
                if(not self.curr_ref.has_key('work') and self.prev_ref.has_key('work')):
                	self.curr_ref["work"]=self.prev_ref["work"]
                elif(not self.curr_ref.has_key('work')):
                	self.curr_ref["work"]=None
                self.refs.append(dict(self.curr_ref))

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "ref"


    # $ANTLR start "work"
    # cp_treeparser.g:55:1: work : ^( WORK (x+= LITERAL )+ ) ;
    def work(self, ):

        x = None
        list_x = None

        try:
            try:
                # cp_treeparser.g:55:5: ( ^( WORK (x+= LITERAL )+ ) )
                # cp_treeparser.g:56:1: ^( WORK (x+= LITERAL )+ )
                pass 
                self.match(self.input, WORK, self.FOLLOW_WORK_in_work115)

                self.match(self.input, DOWN, None)
                # cp_treeparser.g:56:9: (x+= LITERAL )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == LITERAL) :
                        alt5 = 1


                    if alt5 == 1:
                        # cp_treeparser.g:56:9: x+= LITERAL
                        pass 
                        x=self.match(self.input, LITERAL, self.FOLLOW_LITERAL_in_work119)
                        if list_x is None:
                            list_x = []
                        list_x.append(x)



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1



                self.match(self.input, UP, None)
                #action start
                 
                y=[n.toString() for n in list_x]
                self.curr_ref["work"]=" ".join(y)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "work"


    # $ANTLR start "editor"
    # cp_treeparser.g:63:1: editor : ^( EDITOR LITERAL ) ;
    def editor(self, ):

        try:
            try:
                # cp_treeparser.g:63:7: ( ^( EDITOR LITERAL ) )
                # cp_treeparser.g:64:1: ^( EDITOR LITERAL )
                pass 
                self.match(self.input, EDITOR, self.FOLLOW_EDITOR_in_editor132)

                self.match(self.input, DOWN, None)
                self.match(self.input, LITERAL, self.FOLLOW_LITERAL_in_editor134)

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "editor"


    # $ANTLR start "level"
    # cp_treeparser.g:67:1: level[typ] returns [List levs] : ^( LEVEL lev+= INT ) ( ^( LEVEL lev1+= INT ) )* ;
    def level(self, typ):

        levs = None

        lev = None
        lev1 = None
        list_lev = None
        list_lev1 = None

              
        if(typ=="end"):
        	self.levels=[]

        try:
            try:
                # cp_treeparser.g:78:1: ( ^( LEVEL lev+= INT ) ( ^( LEVEL lev1+= INT ) )* )
                # cp_treeparser.g:79:1: ^( LEVEL lev+= INT ) ( ^( LEVEL lev1+= INT ) )*
                pass 
                self.match(self.input, LEVEL, self.FOLLOW_LEVEL_in_level158)

                self.match(self.input, DOWN, None)
                lev=self.match(self.input, INT, self.FOLLOW_INT_in_level162)
                if list_lev is None:
                    list_lev = []
                list_lev.append(lev)


                self.match(self.input, UP, None)
                # cp_treeparser.g:79:19: ( ^( LEVEL lev1+= INT ) )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == LEVEL) :
                        alt6 = 1


                    if alt6 == 1:
                        # cp_treeparser.g:79:20: ^( LEVEL lev1+= INT )
                        pass 
                        self.match(self.input, LEVEL, self.FOLLOW_LEVEL_in_level167)

                        self.match(self.input, DOWN, None)
                        lev1=self.match(self.input, INT, self.FOLLOW_INT_in_level171)
                        if list_lev1 is None:
                            list_lev1 = []
                        list_lev1.append(lev1)

                        #action start
                                                              
                        self.count+=1
                        self.levels.append(str(lev1))

                        #action end

                        self.match(self.input, UP, None)


                    else:
                        break #loop6


                #action start
                 
                if(not typ=="end"):
                	self.count+=1
                temp=[]
                temp = self.levels
                self.levels=[]
                self.levels.append(str(lev))
                self.levels+=temp

                #action end



                #action start
                       
                if(typ=="single"):
                	self.curr_ref["scp"]["start"]=self.levels
                else:
                	self.curr_ref["scp"][typ]=self.levels

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return levs

    # $ANTLR end "level"


    # $ANTLR start "scp"
    # cp_treeparser.g:94:1: scp : ( scp_single | scp_range ) ;
    def scp(self, ):

              
        self.count=0
        self.levels=[]

        try:
            try:
                # cp_treeparser.g:100:1: ( ( scp_single | scp_range ) )
                # cp_treeparser.g:100:3: ( scp_single | scp_range )
                pass 
                # cp_treeparser.g:100:3: ( scp_single | scp_range )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == SCOPE_S) :
                    alt7 = 1
                elif (LA7_0 == SCOPE_R) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # cp_treeparser.g:100:4: scp_single
                    pass 
                    self._state.following.append(self.FOLLOW_scp_single_in_scp193)
                    self.scp_single()

                    self._state.following.pop()


                elif alt7 == 2:
                    # cp_treeparser.g:100:15: scp_range
                    pass 
                    self._state.following.append(self.FOLLOW_scp_range_in_scp195)
                    self.scp_range()

                    self._state.following.pop()







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "scp"


    # $ANTLR start "scp_single"
    # cp_treeparser.g:103:1: scp_single : ^( SCOPE_S level[\"single\"] ) ;
    def scp_single(self, ):

              
        self.curr_ref["scp"]={}

        try:
            try:
                # cp_treeparser.g:107:1: ( ^( SCOPE_S level[\"single\"] ) )
                # cp_treeparser.g:108:1: ^( SCOPE_S level[\"single\"] )
                pass 
                self.match(self.input, SCOPE_S, self.FOLLOW_SCOPE_S_in_scp_single210)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_level_in_scp_single212)
                self.level("single")

                self._state.following.pop()

                self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "scp_single"


    # $ANTLR start "scp_range"
    # cp_treeparser.g:111:1: scp_range : ^( SCOPE_R ^( START level[\"start\"] ) ^( END level[\"end\"] ) ) ;
    def scp_range(self, ):

              
        self.curr_ref["scp"]={}
        self.curr_ref["scp"]["start"]=[]
        self.curr_ref["scp"]["end"]=[]

        try:
            try:
                # cp_treeparser.g:133:1: ( ^( SCOPE_R ^( START level[\"start\"] ) ^( END level[\"end\"] ) ) )
                # cp_treeparser.g:134:1: ^( SCOPE_R ^( START level[\"start\"] ) ^( END level[\"end\"] ) )
                pass 
                self.match(self.input, SCOPE_R, self.FOLLOW_SCOPE_R_in_scp_range232)

                self.match(self.input, DOWN, None)
                self.match(self.input, START, self.FOLLOW_START_in_scp_range235)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_level_in_scp_range237)
                self.level("start")

                self._state.following.pop()

                self.match(self.input, UP, None)
                self.match(self.input, END, self.FOLLOW_END_in_scp_range242)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_level_in_scp_range244)
                self.level("end")

                self._state.following.pop()

                self.match(self.input, UP, None)

                self.match(self.input, UP, None)



                #action start
                       
                sl=len(self.curr_ref["scp"]["start"])
                el=len(self.curr_ref["scp"]["end"])
                if(el!=sl):
                  count = 0
                  self.curr_ref["scp"]["start"].reverse()
                  while(len(self.curr_ref["scp"]["start"])>len(self.curr_ref["scp"]["end"])):
                    self.curr_ref["scp"]["end"].append(None)
                    count+=1
                  for n,l in enumerate(self.curr_ref["scp"]["end"]):
                    if(l is None):
                      self.curr_ref["scp"]["end"][n]=self.curr_ref["scp"]["start"][n]
                  self.curr_ref["scp"]["start"].reverse()
                  self.curr_ref["scp"]["end"].reverse()
                  

                #action end

            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass

        return 

    # $ANTLR end "scp_range"


    # Delegated rules


 

    FOLLOW_citation_in_doc56 = frozenset([1, 19])
    FOLLOW_CITATION_in_citation70 = frozenset([2])
    FOLLOW_ref_in_citation72 = frozenset([3, 18])
    FOLLOW_ref_in_citation74 = frozenset([3, 18])
    FOLLOW_REF_in_ref97 = frozenset([2])
    FOLLOW_work_in_ref99 = frozenset([20, 23, 24])
    FOLLOW_scp_in_ref102 = frozenset([3, 21])
    FOLLOW_editor_in_ref104 = frozenset([3, 21])
    FOLLOW_WORK_in_work115 = frozenset([2])
    FOLLOW_LITERAL_in_work119 = frozenset([3, 17])
    FOLLOW_EDITOR_in_editor132 = frozenset([2])
    FOLLOW_LITERAL_in_editor134 = frozenset([3])
    FOLLOW_LEVEL_in_level158 = frozenset([2])
    FOLLOW_INT_in_level162 = frozenset([3])
    FOLLOW_LEVEL_in_level167 = frozenset([2])
    FOLLOW_INT_in_level171 = frozenset([3])
    FOLLOW_scp_single_in_scp193 = frozenset([1])
    FOLLOW_scp_range_in_scp195 = frozenset([1])
    FOLLOW_SCOPE_S_in_scp_single210 = frozenset([2])
    FOLLOW_level_in_scp_single212 = frozenset([3])
    FOLLOW_SCOPE_R_in_scp_range232 = frozenset([2])
    FOLLOW_START_in_scp_range235 = frozenset([2])
    FOLLOW_level_in_scp_range237 = frozenset([3])
    FOLLOW_END_in_scp_range242 = frozenset([2])
    FOLLOW_level_in_scp_range244 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(cp_treeparser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
