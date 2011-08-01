#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com

import logging, antlr3,sys
from cp_lexer import cp_lexer
from cp_parser import cp_parser
from cp_treeparser import cp_treeparser

class citation_parser:
	"""
	This class is a wrapper for the different components of the CitationParser, i.e. lexer, parser and tree parser.
	
	"""
	def __init__(self):
		self.logger = logger = logging.getLogger("crex.citation_parser")
		self.logger.debug("citation_parser instance initialised")
	
	def parse(self,text):
		if(type(text) is not type("ü".decode('UTF-8'))):
			self.logger.info("converting input string to utf-8")
			text = text.decode('UTF-8')
		self.logger.debug(text)
		char_stream = antlr3.ANTLRStringStream(text)
		try:
			lexer = cp_lexer(char_stream)
			tokenstream = antlr3.CommonTokenStream(lexer)
			parser = cp_parser(tokenstream)
			try:
				r=parser.doc()
				root = r.tree
				self.logger.debug(root.toStringTree())
				try:
					nodes = antlr3.tree.CommonTreeNodeStream(root)
					nodes.setTokenStream(tokenstream)
					tp = cp_treeparser(nodes)
					tp.doc()
					import simplejson as sj
					result = sj.dumps(str(tp.refs))
					return result
				except Exception as e:
					self.logger.error("%s"%Error)
					self.logger.error("there was a problem w/ the TreeParser: exiting")
			except Exception as e:
				self.logger.error("%s"%Error)
				self.logger.error("there was a problem with the parser: exiting")
		except Exception as e:
			self.logger.error("%s"%e)
			self.logger.error("there was a problem with the lexer: exiting")