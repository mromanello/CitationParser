import sys,logging,antlr3
from core import citation_parser
from cp_lexer import cp_lexer
from cp_parser import cp_parser
from cp_treeparser import cp_treeparser

def init_logger():
    global logger
    logger = logging.getLogger("crex")
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    logger.info("Logger Initialised.")
    
def run(i_file):
	cipa = citation_parser()
	temp = open(i_file,'r').read()
	citation_strings = temp.split('\n');
	for c in citation_strings:
		r = cipa.parse(c)
		logger.info("Result: %s"%r)
		
if __name__ == "__main__":
    init_logger()
    fname = sys.argv[1]
    #oname = sys.argv[2]
    run(fname)

