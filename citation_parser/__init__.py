#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com
#__version__='0.4.1'

from pyCTS import CTS_URN
from operator import itemgetter
import antlr3
import sys
import re
from antlr.cp_lexer import cp_lexer
from antlr.cp_parser import cp_parser
from antlr.cp_treeparser import cp_treeparser
try:
	import simplejson as json
except ImportError:
	import json as json
import logging

import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
				
class CitationParser:
	"""
	This class is a wrapper for the different components of the CitationParser, i.e. lexer, parser and tree parser.
	
	"""
	def __init__(self):
		logger.debug("citation_parser instance initialised")
	def parse(self,text):
		if(type(text) is not type("ü".decode('UTF-8'))):
			logger.info("converting input string to utf-8")
			text = text.decode('UTF-8')
		logger.debug(text)
		char_stream = antlr3.ANTLRStringStream(text)
		try:
			lexer = cp_lexer(char_stream)
			tokenstream = antlr3.CommonTokenStream(lexer)
			parser = cp_parser(tokenstream)
			try:
				r=parser.doc()
				root = r.tree
				print root.toStringTree()
				logger.debug(root.toStringTree())
				try:
					nodes = antlr3.tree.CommonTreeNodeStream(root)
					nodes.setTokenStream(tokenstream)
					tp = cp_treeparser(nodes)
					tp.doc()
					logger.debug(tp.refs)
					json_string = json.dumps(tp.refs)
					return json.loads(json_string)
				except Exception as e:
					logger.error("%s"%e)
					logger.error("there was a problem w/ the TreeParser: exiting")
			except Exception as e:
				logger.error("%s"%e)
				logger.error("there was a problem with the parser: exiting")
		except Exception as e:
			logger.error("%s"%e)
			logger.error("there was a problem with the lexer: exiting")
