#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com

import antlr3
import sys
from antlr.cp_lexer import cp_lexer
from antlr.cp_parser import cp_parser
from antlr.cp_treeparser import cp_treeparser
try:
	import simplejson as sj
except ImportError:
	import json as sj
import logging

class CitationParser:
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
				print root.toStringTree()
				self.logger.debug(root.toStringTree())
				try:
					nodes = antlr3.tree.CommonTreeNodeStream(root)
					nodes.setTokenStream(tokenstream)
					tp = cp_treeparser(nodes)
					tp.doc()
					self.logger.debug(tp.refs)
					json_string = sj.dumps(tp.refs)
					return sj.loads(json_string)
				except Exception as e:
					self.logger.error("%s"%e)
					self.logger.error("there was a problem w/ the TreeParser: exiting")
			except Exception as e:
				self.logger.error("%s"%e)
				self.logger.error("there was a problem with the parser: exiting")
		except Exception as e:
			self.logger.error("%s"%e)
			self.logger.error("there was a problem with the lexer: exiting")