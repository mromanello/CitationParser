# $ANTLR 3.1.2 cp_lexer.g 2012-04-06 11:54:45

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
PUNTO=6
BRACKETS=16
WS=14
HYPHEN=10
COMMA=7
CHAR=12
SEMICOL=11
LITERAL=17
HYPHEN_fr=9
INT=4
DOT=5
PUNCT=13
EOF=-1
VIRGOLA=8
R_C_BR=15


class cp_lexer(Lexer):

    grammarFileName = "cp_lexer.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)






    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:13:5: ( ( '0' .. '9' )+ )
            # cp_lexer.g:13:7: ( '0' .. '9' )+
            pass 
            # cp_lexer.g:13:7: ( '0' .. '9' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57)) :
                    alt1 = 1


                if alt1 == 1:
                    # cp_lexer.g:0:0: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "PUNTO"
    def mPUNTO(self, ):

        try:
            _type = PUNTO
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:15:7: ( DOT )
            # cp_lexer.g:15:9: DOT
            pass 
            self.mDOT()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PUNTO"



    # $ANTLR start "VIRGOLA"
    def mVIRGOLA(self, ):

        try:
            _type = VIRGOLA
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:16:9: ( COMMA )
            # cp_lexer.g:16:11: COMMA
            pass 
            self.mCOMMA()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VIRGOLA"



    # $ANTLR start "HYPHEN"
    def mHYPHEN(self, ):

        try:
            _type = HYPHEN
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:17:7: ( HYPHEN_fr )
            # cp_lexer.g:17:9: HYPHEN_fr
            pass 
            self.mHYPHEN_fr()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HYPHEN"



    # $ANTLR start "SEMICOL"
    def mSEMICOL(self, ):

        try:
            _type = SEMICOL
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:18:8: ( ';' )
            # cp_lexer.g:18:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMICOL"



    # $ANTLR start "HYPHEN_fr"
    def mHYPHEN_fr(self, ):

        try:
            # cp_lexer.g:19:20: ( '-' )
            # cp_lexer.g:19:22: '-'
            pass 
            self.match(45)




        finally:

            pass

    # $ANTLR end "HYPHEN_fr"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            # cp_lexer.g:20:14: ( '.' )
            # cp_lexer.g:20:16: '.'
            pass 
            self.match(46)




        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            # cp_lexer.g:21:16: ( ',' )
            # cp_lexer.g:21:18: ','
            pass 
            self.match(44)




        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "CHAR"
    def mCHAR(self, ):

        try:
            # cp_lexer.g:22:15: ( ( 'A' .. 'Z' | 'a' .. 'z' | '\\u00E0' .. '\\u00FF' ) )
            # cp_lexer.g:22:17: ( 'A' .. 'Z' | 'a' .. 'z' | '\\u00E0' .. '\\u00FF' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122) or (224 <= self.input.LA(1) <= 255):
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "CHAR"



    # $ANTLR start "PUNCT"
    def mPUNCT(self, ):

        try:
            # cp_lexer.g:23:16: ( ( DOT | COMMA | HYPHEN_fr )+ )
            # cp_lexer.g:23:18: ( DOT | COMMA | HYPHEN_fr )+
            pass 
            # cp_lexer.g:23:18: ( DOT | COMMA | HYPHEN_fr )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((44 <= LA2_0 <= 46)) :
                    alt2 = 1


                if alt2 == 1:
                    # cp_lexer.g:
                    pass 
                    if (44 <= self.input.LA(1) <= 46):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt2 >= 1:
                        break #loop2

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1






        finally:

            pass

    # $ANTLR end "PUNCT"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:26:3: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # cp_lexer.g:26:5: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # cp_lexer.g:26:5: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((9 <= LA3_0 <= 10) or LA3_0 == 13 or LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # cp_lexer.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            if self._state.backtracking == 0:
                _channel=HIDDEN;




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "R_C_BR"
    def mR_C_BR(self, ):

        try:
            # cp_lexer.g:27:16: ( ( ')' | ')' COMMA ) )
            # cp_lexer.g:27:17: ( ')' | ')' COMMA )
            pass 
            # cp_lexer.g:27:17: ( ')' | ')' COMMA )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 41) :
                LA4_1 = self.input.LA(2)

                if (LA4_1 == 44) :
                    alt4 = 2
                else:
                    alt4 = 1
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # cp_lexer.g:27:18: ')'
                pass 
                self.match(41)


            elif alt4 == 2:
                # cp_lexer.g:27:22: ')' COMMA
                pass 
                self.match(41)
                self.mCOMMA()







        finally:

            pass

    # $ANTLR end "R_C_BR"



    # $ANTLR start "BRACKETS"
    def mBRACKETS(self, ):

        try:
            _type = BRACKETS
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:28:9: ( ( '(' | R_C_BR )+ )
            # cp_lexer.g:28:11: ( '(' | R_C_BR )+
            pass 
            # cp_lexer.g:28:11: ( '(' | R_C_BR )+
            cnt5 = 0
            while True: #loop5
                alt5 = 3
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 40) :
                    alt5 = 1
                elif (LA5_0 == 41) :
                    alt5 = 2


                if alt5 == 1:
                    # cp_lexer.g:28:13: '('
                    pass 
                    self.match(40)


                elif alt5 == 2:
                    # cp_lexer.g:28:19: R_C_BR
                    pass 
                    self.mR_C_BR()


                else:
                    if cnt5 >= 1:
                        break #loop5

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1


            if self._state.backtracking == 0:
                self.skip();




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BRACKETS"



    # $ANTLR start "LITERAL"
    def mLITERAL(self, ):

        try:
            _type = LITERAL
            _channel = DEFAULT_CHANNEL

            # cp_lexer.g:29:9: ( ( ( CHAR )+ ( PUNCT )* ( CHAR )* ) )
            # cp_lexer.g:29:11: ( ( CHAR )+ ( PUNCT )* ( CHAR )* )
            pass 
            # cp_lexer.g:29:11: ( ( CHAR )+ ( PUNCT )* ( CHAR )* )
            # cp_lexer.g:29:12: ( CHAR )+ ( PUNCT )* ( CHAR )*
            pass 
            # cp_lexer.g:29:12: ( CHAR )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122) or (224 <= LA6_0 <= 255)) :
                    LA6_2 = self.input.LA(2)

                    if (self.synpred14_cp_lexer()) :
                        alt6 = 1




                if alt6 == 1:
                    # cp_lexer.g:0:0: CHAR
                    pass 
                    self.mCHAR()


                else:
                    if cnt6 >= 1:
                        break #loop6

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1


            # cp_lexer.g:29:18: ( PUNCT )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((44 <= LA7_0 <= 46)) :
                    alt7 = 1


                if alt7 == 1:
                    # cp_lexer.g:0:0: PUNCT
                    pass 
                    self.mPUNCT()


                else:
                    break #loop7


            # cp_lexer.g:29:25: ( CHAR )*
            while True: #loop8
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((65 <= LA8_0 <= 90) or (97 <= LA8_0 <= 122) or (224 <= LA8_0 <= 255)) :
                    alt8 = 1


                if alt8 == 1:
                    # cp_lexer.g:0:0: CHAR
                    pass 
                    self.mCHAR()


                else:
                    break #loop8








            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LITERAL"



    def mTokens(self):
        # cp_lexer.g:1:8: ( INT | PUNTO | VIRGOLA | HYPHEN | SEMICOL | WS | BRACKETS | LITERAL )
        alt9 = 8
        LA9 = self.input.LA(1)
        if LA9 == 48 or LA9 == 49 or LA9 == 50 or LA9 == 51 or LA9 == 52 or LA9 == 53 or LA9 == 54 or LA9 == 55 or LA9 == 56 or LA9 == 57:
            alt9 = 1
        elif LA9 == 46:
            alt9 = 2
        elif LA9 == 44:
            alt9 = 3
        elif LA9 == 45:
            alt9 = 4
        elif LA9 == 59:
            alt9 = 5
        elif LA9 == 9 or LA9 == 10 or LA9 == 13 or LA9 == 32:
            alt9 = 6
        elif LA9 == 40 or LA9 == 41:
            alt9 = 7
        elif LA9 == 65 or LA9 == 66 or LA9 == 67 or LA9 == 68 or LA9 == 69 or LA9 == 70 or LA9 == 71 or LA9 == 72 or LA9 == 73 or LA9 == 74 or LA9 == 75 or LA9 == 76 or LA9 == 77 or LA9 == 78 or LA9 == 79 or LA9 == 80 or LA9 == 81 or LA9 == 82 or LA9 == 83 or LA9 == 84 or LA9 == 85 or LA9 == 86 or LA9 == 87 or LA9 == 88 or LA9 == 89 or LA9 == 90 or LA9 == 97 or LA9 == 98 or LA9 == 99 or LA9 == 100 or LA9 == 101 or LA9 == 102 or LA9 == 103 or LA9 == 104 or LA9 == 105 or LA9 == 106 or LA9 == 107 or LA9 == 108 or LA9 == 109 or LA9 == 110 or LA9 == 111 or LA9 == 112 or LA9 == 113 or LA9 == 114 or LA9 == 115 or LA9 == 116 or LA9 == 117 or LA9 == 118 or LA9 == 119 or LA9 == 120 or LA9 == 121 or LA9 == 122 or LA9 == 224 or LA9 == 225 or LA9 == 226 or LA9 == 227 or LA9 == 228 or LA9 == 229 or LA9 == 230 or LA9 == 231 or LA9 == 232 or LA9 == 233 or LA9 == 234 or LA9 == 235 or LA9 == 236 or LA9 == 237 or LA9 == 238 or LA9 == 239 or LA9 == 240 or LA9 == 241 or LA9 == 242 or LA9 == 243 or LA9 == 244 or LA9 == 245 or LA9 == 246 or LA9 == 247 or LA9 == 248 or LA9 == 249 or LA9 == 250 or LA9 == 251 or LA9 == 252 or LA9 == 253 or LA9 == 254 or LA9 == 255:
            alt9 = 8
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 9, 0, self.input)

            raise nvae

        if alt9 == 1:
            # cp_lexer.g:1:10: INT
            pass 
            self.mINT()


        elif alt9 == 2:
            # cp_lexer.g:1:14: PUNTO
            pass 
            self.mPUNTO()


        elif alt9 == 3:
            # cp_lexer.g:1:20: VIRGOLA
            pass 
            self.mVIRGOLA()


        elif alt9 == 4:
            # cp_lexer.g:1:28: HYPHEN
            pass 
            self.mHYPHEN()


        elif alt9 == 5:
            # cp_lexer.g:1:35: SEMICOL
            pass 
            self.mSEMICOL()


        elif alt9 == 6:
            # cp_lexer.g:1:43: WS
            pass 
            self.mWS()


        elif alt9 == 7:
            # cp_lexer.g:1:46: BRACKETS
            pass 
            self.mBRACKETS()


        elif alt9 == 8:
            # cp_lexer.g:1:55: LITERAL
            pass 
            self.mLITERAL()






    # $ANTLR start "synpred14_cp_lexer"
    def synpred14_cp_lexer_fragment(self, ):
        # cp_lexer.g:29:12: ( CHAR )
        # cp_lexer.g:29:12: CHAR
        pass 
        self.mCHAR()


    # $ANTLR end "synpred14_cp_lexer"



    def synpred14_cp_lexer(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred14_cp_lexer_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(cp_lexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
