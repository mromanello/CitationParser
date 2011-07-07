import sys,logging,antlr3
from cp_lexer import cp_lexer
from cp_parser import cp_parser
from cp_treeparser import cp_treeparser

def init_logger():
    global logger
    logger = logging.getLogger("Main")
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
	temp = open(i_file,'r').read()
	citation_strings = temp.split('\n');
	for c in citation_strings:
		logger.debug(c.decode('UTF-8'))
		char_stream = antlr3.ANTLRStringStream(c.decode('UTF-8'))
		lexer = cp_lexer(char_stream)
		tokenstream = antlr3.CommonTokenStream(lexer)
		parser = cp_parser(tokenstream)
		r=parser.doc()
		root = r.tree
		
		logger.debug(root.toStringTree())
		nodes = antlr3.tree.CommonTreeNodeStream(root)
		nodes.setTokenStream(tokenstream)
		tp = cp_treeparser(nodes)
		tp.doc()
		import pprint
		pprint.pprint(tp.refs)
		import simplejson as sj
		
		print sj.dumps(str(tp.refs))

		
if __name__ == "__main__":
    init_logger()
    fname = sys.argv[1]
    #oname = sys.argv[2]
    run(fname)

