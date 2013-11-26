import sys
import logging
from core import citation_parser

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
	"""
	Args:
		i_file:
			the path to a text file containing one citation per line
	"""
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

