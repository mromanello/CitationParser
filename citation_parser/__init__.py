	#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com
__version__='0.4.0'

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
# imports needed for the KB bit
import rdflib
from rdflib import plugin
plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class DisambiguationNotFound(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

    def __str__(self):
        return repr(self.message)

class KnowledgeBase(object):
	"""
	docstring for KnowledgeBase

	TODO: 
	* test allegrordf to connect to an AG 3store via rdflib (hard to run AG3 locally)
	* test mysql as backend

	Example:

	>>> kb = KnowledgeBase("/Users/rromanello/Documents/APh_Corpus_GUI/cwkb/export_triples/kb-all-in-one.ttl", "turtle")

	"""
	def __init__(self,source_file=None, source_format=None, source_endpoint=None):
		super(KnowledgeBase, self).__init__()
		try:
			assert source_file is not None and source_format is not None
			self._graph = rdflib.Graph()
			if(type(source_file) == type("string")):
				self._graph.parse(source_file,format=source_format)
			elif(type(source_file) == type([])):
				for file in source_file:
					self._graph.parse(file,format=source_format)
			print >> sys.stderr, "Loaded %i triples"%len(self._graph)
			self._author_names = None
			self._author_abbreviations = None
			self._work_titles = None
			self._work_abbreviations = None
		except Exception, e:
			raise e

	@property
	def author_names(self):
		if(self._author_names is not None):
			return self._author_names
		else:
			self._author_names = self._fetch_author_names()
			return self._author_names

	@property
	def author_abbreviations(self):
		if(self._author_abbreviations is not None):
			return self._author_abbreviations
		else:
			self._author_abbreviations = self._fetch_author_abbreviations()
			return self._author_abbreviations

	@property
	def work_titles(self):
		if(self._work_titles is not None):
			return self._work_titles
		else:
			self._work_titles = self._fetch_work_titles()
			return self._work_titles

	@property
	def work_abbreviations(self):
		if(self._work_abbreviations is not None):
			return self._work_abbreviations
		else:
			self._work_abbreviations = self._fetch_work_abbreviations()
			return self.work_abbreviations

	def _fetch_author_names(self,to_lowercase=True):
		authors_query = """
		    PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT DISTINCT ?author ?label ?urnstring
			
			WHERE {
				?author crm:P1_is_identified_by ?name .
		        ?name a frbroo:F12_Name .
		        ?name rdfs:label ?label .

		        OPTIONAL {
		            ?author crm:P1_is_identified_by ?urn .
		            ?urn a crm:E42_Identifier .
		            ?urn rdfs:label ?urnstring .
		        }
		        }

		         
		    } ORDER BY (?author)
		"""
		author_names = {}
		flat_author_names = {}
		query_result = self._graph.query(authors_query)
		for uri, author_name, urn in query_result:
			if(to_lowercase):
				name = author_name.lower()
			if author_name.language is not None:
				language = author_name.language
			else:
				language = "def"
			if urn is None:
				if author_names.has_key(uri):
					author_names[uri][language] = name
				else:
					author_names[uri] = {}
					author_names[uri][language] = name
			else:
				if author_names.has_key(urn):
					author_names[urn][language] = name
				else:
					author_names[urn] = {}
					author_names[urn][language] = name
		for key in author_names:
			for n,lang in enumerate(author_names[key]):
				flat_author_names["%s$$%i"%(key,n+1)] = unicode(author_names[key][lang])
		return flat_author_names

	def _fetch_author_abbreviations(self, to_lowercase=True):
		author_abbreviations_query = """
		    PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT DISTINCT ?author ?label ?urnstring ?abbr
			
			WHERE {
		        ?author crm:P1_is_identified_by ?name .
		        ?name crm:P139_has_alternative_form ?abbrev .
		        ?abbrev rdfs:label ?abbr .
		        OPTIONAL {
		            ?author crm:P1_is_identified_by ?urn .
		            ?urn a crm:E42_Identifier .
		            ?urn rdfs:label ?urnstring .
		        }
		    } ORDER BY (?author)

		"""
		abbreviations = {}
		flat_abbreviations = {}
		query_result = self._graph.query(author_abbreviations_query)
		for uri, author_name, urn, abbreviation in query_result:
			if(to_lowercase):
				abbr = abbreviation.lower()
			if urn is None:
				if abbreviations.has_key(uri):
					abbreviations[uri] = abbreviations[uri].append(abbr)
				else:
					abbreviations[uri] = []
					abbreviations[uri].append(abbr)
			else:
				if abbreviations.has_key(urn):
					abbreviations[urn].append(abbr)
				else:
					abbreviations[urn] = []
					abbreviations[urn].append(abbr)
		for key in abbreviations:
			if(abbreviations[key] is not None):
				for n,item in enumerate(abbreviations[key]):
					flat_abbreviations["%s$$%i"%(key,n+1)] = unicode(abbreviations[key][n])
			else:
				print key, abbreviations[key]
		return flat_abbreviations

	def _fetch_work_titles(self, to_lowercase=True):
		works_query = """
		    PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT DISTINCT ?work ?title ?urnstring
			
			WHERE {
		        ?work a frbroo:F1_Work .
		        ?work frbroo:P102_has_title ?utitle .
		        ?utitle rdfs:label ?title
		        OPTIONAL {
		            ?work crm:P1_is_identified_by ?urn .
		            ?urn a crm:E42_Identifier .
		            ?urn rdfs:label ?urnstring .
		        }
		    } 
		    ORDER BY (?work)

		"""
		query_result = self._graph.query(works_query)
		work_titles = {}
		flat_work_titles = {}
		for uri,work_title,urn in query_result:
			if(to_lowercase):
				title = work_title.lower()
			if work_title.language is not None:
				language = work_title.language
			else:
				language = "def"
			# TODO remove articles according to language
			regexps = {
				"en" : r'^the '
				,"de" : r'^der |^die |^das '
				,"fr" : r'^le |^la |^l\' |^les '
				,"it" : r'^il | ^lo | ^la |^gli |^le '
				,"def" : r''
				,"la" : r''
			}
			if(language in regexps.keys()):
				title = re.sub(regexps[language],"",title)
			if urn is None:
				if(work_titles.has_key(uri)):
					work_titles[uri][language] = title
				else:
					work_titles[uri] = {}
					work_titles[uri][language] = title
			else:
				if(work_titles.has_key(urn)):
					work_titles[urn][language] = title
				else:
					work_titles[urn] = {}
					work_titles[urn][language] = title
		for key in work_titles:
			for n,lang in enumerate(work_titles[key]):
				flat_work_titles["%s$$%i"%(key,n+1)] = unicode(work_titles[key][lang])
		return flat_work_titles

	def _fetch_work_abbreviations(self, to_lowercase=True):
		work_abbreviations_query = """
		    PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT DISTINCT ?work ?label ?urnstring ?abbr
			
			WHERE {
		        ?work frbroo:P102_has_title ?title .
		        ?title crm:P139_has_alternative_form ?abbrev .
		        ?abbrev rdfs:label ?abbr .
		        OPTIONAL {
		            ?work crm:P1_is_identified_by ?urn .
		            ?urn a crm:E42_Identifier .
		            ?urn rdfs:label ?urnstring .
		        }
		    } ORDER BY (?work)
		"""
		work_abbreviations = {}
		flat_work_abbreviations = {}
		query_result = self._graph.query(work_abbreviations_query)
		for uri, work_title, urn, abbreviation in query_result:
			if(to_lowercase):
				abbr = abbreviation.lower()
			if urn is None:
				if work_abbreviations.has_key(uri):
					work_abbreviations[uri] = work_abbreviations[uri].append(abbr)
				else:
					work_abbreviations[uri] = []
					work_abbreviations[uri].append(abbr)
			else:
				if work_abbreviations.has_key(urn):
					work_abbreviations[urn].append(abbr)
				else:
					work_abbreviations[urn] = []
					work_abbreviations[urn].append(abbr)
		for key in work_abbreviations:
			if(work_abbreviations[key] is not None):
				for n,item in enumerate(work_abbreviations[key]):
					flat_work_abbreviations["%s$$%i"%(key,n+1)] = unicode(work_abbreviations[key][n])
			else:
				print key, work_abbreviations[key]
		return flat_work_abbreviations

	def get_URI_by_CTS_URN(self,input_urn):
		"""
		Takes a CTS URN as input and returns the matching URI
		"""
		search_query = """
		    PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT ?resource_URI
			
			WHERE {
				?resource_URI crm:P1_is_identified_by ?urn .
				?urn a crm:E42_Identifier .
		    	?urn rdfs:label "%s"
		    }
		"""%(input_urn)
		query_result = list(self._graph.query(search_query))
		# there must be only one URI match for a given URN
		assert len(query_result)==1
		return query_result[0][0]

	def get_author_of(self,work_cts_urn):
		search_query = """
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		PREFIX crm: <http://erlangen-crm.org/current/>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		
		SELECT ?author_urn_string	
		WHERE {
			?work crm:P1_is_identified_by ?urn .
			?urn a crm:E42_Identifier .
	    	?urn rdfs:label "%s" .
          	?creation frbroo:R16_initiated ?work .
          	?author frbroo:P14i_performed ?creation .
          	?author crm:P1_is_identified_by ?author_urn .
          	?author_urn a crm:E42_Identifier .
          	?author_urn rdfs:label  ?author_urn_string.
	    }
		"""%work_cts_urn
		query_result = list(self._graph.query(search_query))
		return query_result[0][0]

	def get_name_of(self,author_cts_urn):
		search_query = """
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		PREFIX crm: <http://erlangen-crm.org/current/>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		
		SELECT ?name
		WHERE {
	      	?author crm:P1_is_identified_by ?author_urn .
			?author_urn a crm:E42_Identifier .
	      	?author_urn rdfs:label "%s" .
	      	?author crm:P1_is_identified_by ?name_uri .
          	?name_uri a frbroo:F12_Name .
	      	?name_uri rdfs:label ?name .
	    }
		"""%author_cts_urn
		query_result = list(self._graph.query(search_query))
		return [name[0] for name in query_result]

	def get_title_of(self,work_cts_urn):
		search_query = """
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
			PREFIX crm: <http://erlangen-crm.org/current/>
			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
			
			SELECT DISTINCT ?title
			
			WHERE {
		        ?work a frbroo:F1_Work .
		        ?work frbroo:P102_has_title ?utitle .
		        ?utitle rdfs:label ?title .
		        ?work crm:P1_is_identified_by ?urn .
		        ?urn a crm:E42_Identifier .
		        ?urn rdfs:label "%s" .
		    }
		"""%work_cts_urn
		query_result = list(self._graph.query(search_query))
		return [title[0] for title in query_result]

	def get_opus_maximum_of(self,author_cts_urn):
		"""
		given the CTS URN of an author, this method returns the CTS URN of
		its opus maximum. If not available returns None.
		"""
		search_query = """
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		PREFIX crm: <http://erlangen-crm.org/current/>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
		PREFIX frbroo: <http://erlangen-crm.org/efrbroo/>
		PREFIX base: <http://127.0.0.1:8000/cwkb/types#>
		
		SELECT ?urn	
		WHERE {
			?work crm:P1_is_identified_by ?work_urn .
			?work crm:P2_has_type base:opusmaximum .
			?work_urn a crm:E42_Identifier .
	    	?work_urn rdfs:label ?urn .
          	?creation frbroo:R16_initiated ?work .
          	?author frbroo:P14i_performed ?creation .
          	?author crm:P1_is_identified_by ?author_urn .
          	?author_urn a crm:E42_Identifier .
          	?author_urn rdfs:label  "%s".
	    }
		"""%author_cts_urn
		query_result = list(self._graph.query(search_query))
		try:
			return query_result[0][0]
		except Exception, e:
			return None

	def validate():
		pass

	def describe(cts_urn, language="en"):
		"""
		TODO: given a CTS URN, return a description
		Return a tuple where:
			result[0] is the label
			result[1] is the language of the label
		"""
		pass
				
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
					json_string = json.dumps(tp.refs)
					return json.loads(json_string)
				except Exception as e:
					self.logger.error("%s"%e)
					self.logger.error("there was a problem w/ the TreeParser: exiting")
			except Exception as e:
				self.logger.error("%s"%e)
				self.logger.error("there was a problem with the parser: exiting")
		except Exception as e:
			self.logger.error("%s"%e)
			self.logger.error("there was a problem with the lexer: exiting")

class CitationMatcher(object):
	"""
	TODO
	docstring for CitationMatcher

	Example:

	>>> kb = KnowledgeBase("/Users/rromanello/Documents/APh_Corpus_GUI/cwkb/export_triples/kb-all-in-one.ttl", "turtle")
	>>> cm = CitationMatcher(kb)
	>>> citation_urn = cm.disambiguate("Hom. Il.","1.100")
	
	"""
	def __init__(self, knowledge_base):
		super(CitationMatcher, self).__init__()
		try:
			self._citation_parser = CitationParser()
			self._kb = knowledge_base
			self._author_names = knowledge_base.author_names
			self._work_titles = knowledge_base.work_titles
			self._author_abbreviations = knowledge_base.author_abbreviations
			self._work_abbreviations = knowledge_base.work_abbreviations
			self._author_idx, self._author_abbr_idx, self._work_idx, self._work_abbr_idx = self._initialise_indexes()
		except Exception, e:
			raise e

	def _initialise_indexes(self):
		from pysuffix import suffixIndexers
		from pysuffix.suffixIndexers import DictValuesIndexer
		try:
			author_idx = DictValuesIndexer(self._author_names)
			author_abbr_idx = DictValuesIndexer(self._author_abbreviations)
			work_idx = DictValuesIndexer(self._work_titles)
			work_abbr_idx = DictValuesIndexer(self._work_abbreviations)
			return author_idx, author_abbr_idx, work_idx, work_abbr_idx
		except Exception, e:
			raise e

	def _format_scope(self,scope_dictionary):
		"""
		Args:
			scope_dictionary:
				{u'start': [u'1', u'100']}
		returns:
			string
		"""
		if(scope_dictionary.has_key("end")):
			#is range
			return "%s-%s"%(".".join(scope_dictionary["start"]),".".join(scope_dictionary["end"]))
		else:
			#is not range
			return ".".join(scope_dictionary["start"])

	def matches_author(self, string, fuzzy=False, distance_threshold=3):
		"""
		This function retrieves from the KnowledgeBase possible authors that match the search string.
		None is returned if no matches are found.

		Args:
			string: the search string

		Returns:
			a list of tuples, ordered by distance between the seach and the matching string, where:
				tuple[0] contains the id (i.e. CTS URN) of the matching author
				tuple[1] contains a label of the matching author
				tuple[2] is the distance, measured in characters, between the search string and the matching string
		"""
		string = string.lower()
		author_matches, abbr_matches = [],[]
		if(not fuzzy):
			author_matches = [(id.split("$$")[0], self._author_names[id], len(self._author_names[id])-len(string)) for id in self._author_idx.searchAllWords(string)]
			abbr_matches = [(id.split("$$")[0], self._author_abbreviations[id], len(self._author_abbreviations[id])-len(string)) for id in self._author_abbr_idx.searchAllWords(string)]
		else:
			from nltk.metrics import edit_distance
			abbr_matches = [(id.split("$$")[0], self._author_abbreviations[id], edit_distance(string,self._author_abbreviations[id])) for id in self._author_abbreviations if edit_distance(string,self._author_abbreviations[id]) <= distance_threshold]
			abbr_matches = sorted(abbr_matches, key =itemgetter(2))
			author_matches = []
			for id in self._author_names:
				if(string.endswith(".")):
					if string.replace(".","") in self._author_names[id]:
						if(len(string)>(len(self._author_names[id])/2)):
							try:
								assert abbr_matches[0][2]==0
								distance = len(self._author_names[id])-len(string)
								if distance < 0:
									distance = 1
								author_matches.append((id.split("$$")[0], self._author_names[id],distance))
							except Exception, e:
								author_matches.append((id.split("$$")[0], self._author_names[id],0))
						else:
							if(edit_distance(string,self._author_names[id]) <= distance_threshold):
								author_matches.append((id.split("$$")[0], self._author_names[id], edit_distance(string,self._author_names[id])))
				else:
					if(edit_distance(string,self._author_names[id]) <= distance_threshold):
						author_matches.append((id.split("$$")[0], self._author_names[id], edit_distance(string,self._author_names[id])))
		if(len(author_matches)>0 or len(abbr_matches)>0):
			return sorted(author_matches + abbr_matches, key =itemgetter(2))
		else:
			return None

	def matches_work(self, string,fuzzy=False, distance_threshold=3):
		"""
		This function retrieves from the KnowledgeBase possible works that match the search string.
		None is returned if no matches are found.

		Args:
			string: the search string

		Returns:
			a list of tuples, ordered by distance between the seach and the matching string, where:
				tuple[0] contains the id (i.e. CTS URN) of the matching work
				tuple[1] contains a label of the matching work
				tuple[2] is the distance, measured in characters, between the search string and the matching string
		"""
		string = string.lower()
		work_matches, work_abbr_matches = [],[]
		if(not fuzzy):
			work_matches = [(id.split("$$")[0], self._work_titles[id], len(self._work_titles[id])-len(string)) for id in self._work_idx.searchAllWords(string)]
			work_abbr_matches = [(id.split("$$")[0], self._work_abbreviations[id], len(self._work_abbreviations[id])-len(string)) for id in self._work_abbr_idx.searchAllWords(string)]
		else:
			from nltk.metrics import edit_distance
			work_matches = [(id.split("$$")[0], self._work_titles[id], edit_distance(string,self._work_titles[id])) for id in self._work_titles if edit_distance(string,self._work_titles[id]) <= distance_threshold]
			work_abbr_matches = [(id.split("$$")[0], self._work_abbreviations[id], edit_distance(string,self._work_abbreviations[id])) for id in self._work_abbreviations if edit_distance(string,self._work_abbreviations[id]) <= distance_threshold]
		if(len(work_matches)>0 or len(work_abbr_matches)>0):
			return sorted(work_matches + work_abbr_matches, key=itemgetter(2))
		else:
			return None

	def disambiguate(self
					, citation_string
					, scope
					, n_guess=1
					, validate = False
					, fuzzy = False
					, distance_threshold=3
					, use_context = False
					, entities_before = None
					, entities_after = None
					, cleanup = False
					):
		"""
		Args:
			citation_string:
				e.g. "Hom. Il."
			scope:
				e.g. "10.1", "1.204", "X 345"
			n_guess:
				number of guesses that should be returned
				if n_guess > 1, they are returned as ordered list, with
				the most likely candidate first and the least likely last.
		Returns:
			a list of pyCTS.CTS_URN objects.

		Example:
			>>> cm.disambiguate("Hom. Il.","1.100")
		"""
		def longestSubstringFinder(string1, string2):
			"""
			solution taken from http://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
			"""
			answer = ""
			len1, len2 = len(string1), len(string2)
			for i in range(len1):
				match = ""
				for j in range(len2):
					if (i + j < len1 and string1[i + j] == string2[j]):
						match += string2[j]
					else:
						if (len(match) > len(answer)): answer = match
						match = ""
			return answer
		match = []
		try:
			normalized_scope = self._citation_parser.parse(scope)
		except Exception, e:
			print >> sys.stderr, "Got exception %s while parsing \"%s\""%(e,scope)
			normalized_scope = scope

		# citation string has one single token
		if(len(citation_string.split(" "))==1):
			match = self.matches_work(citation_string,fuzzy,distance_threshold)
			# TODO this is problematic
			# should be: match is None or match does not contain at least one entry with distance=0
			zero_distance_match = False
			if(match is not None):
				for m in match:
					if(m[2]==0):
						zero_distance_match = True
			print fuzzy
			print citation_string
			print "zero distance match is %s"%zero_distance_match
			if match is None or not zero_distance_match:
			#if match is None:
				try:
					match = self.matches_author(citation_string,fuzzy,distance_threshold)
				except Exception, e:
					raise e
			if match is not None:
				#match = [(id,name,diff) for id, name, diff in match if diff == 0][:n_guess] # this has to be removed
				pass
			else:
				# fuzzy matching as author
				# then fuzzy matching as work
				# ad the end take the matching with lowest score
				pass
		# citation string has two tokens
		elif(len(citation_string.split(" "))==2):
			tok1 = citation_string.split(" ")[0]
			tok2 = citation_string.split(" ")[1]
			# case 1: tok1 is author and tok2 is work
			match_tok1 = self.matches_author(tok1,fuzzy,distance_threshold)
			match_tok2 = self.matches_work(tok2,fuzzy,distance_threshold)
			#print >> sys.stderr, match_tok1
			#print >> sys.stderr, match_tok2
			if(match_tok1 is not None and match_tok2 is not None):
				# take this
				for id1,label1,score1 in match_tok1:
					for id2,label2,score2 in match_tok2:
						if(id1 in id2):
							match = [(id2,label2,score2)]
							break
			else:
				# case 2: tok1 and tok2 are author
				match = self.matches_author(citation_string,fuzzy,distance_threshold)
				if match is None:
					# case 3: tok1 and tok2 are work
					match = self.matches_work(citation_string,fuzzy,distance_threshold)
				else:
					# take this
					pass
		# citation string has more than two tokens
		elif(len(citation_string.split(" "))>2):
			match = self.matches_author(citation_string,fuzzy,distance_threshold)
		# TODO
		if(not use_context):
			pass
		else:
			pass
		# return only n_guess results
		if(match is None or len(match)==0):
			raise DisambiguationNotFound("For the string \'%s\' no candidates for disambiguation were found!"%citation_string)
		elif(len(match)<= n_guess):
			print >> sys.stderr, "There are %i results and `n_guess`==%i. Nothing to cut."%(len(match),n_guess)
		elif(len(match)> n_guess):
			# iterate and get what's the lowest ed_score
			# then keep only the matches with lowest (best) score
			# then keep the one with longest common string
			lowest_score = 1000
			for m in match:
			    score = m[2]
			    if(score < lowest_score):
			        lowest_score = score
			filtered_matches = [m for m in match if m[2]==lowest_score]
			best_match = ("",None)
			if(lowest_score > 0):
				for match in filtered_matches:
				    lcs = longestSubstringFinder(match[1],citation_string)
				    if(len(lcs)>len(best_match[0])):
				        best_match = (lcs,match)
				match = [best_match[1]]
				print match
			else:
				# TODO: use context here to disambiguate
				match = match[:n_guess]
		results = []
		for id, label, score in match:
			formatted_scope = self._format_scope(normalized_scope[0]['scp'])
			urn = CTS_URN("%s:%s"%(id, formatted_scope))
			# check: does the URN has a scope but is missing the work element (not possible)?
			if(urn.work is None):
				# if so, try to get the opus maximum from the KB
				opmax = self._kb.get_opus_maximum_of(urn.get_urn_without_passage())
				if(opmax is not None):
					print >> sys.stderr, "%s is opus maximum of %s"%(opmax,urn)
					urn = CTS_URN("%s:%s"%(opmax,formatted_scope))
			results.append(urn)
		print >> sys.stderr,results
		return results