"""
The idea is to parse a corpus where NEs have been annotated.
The goal is to resolve the tagged NEs.

Which NEs:
	* AAUTHOR << ancient author
	* AWORK << ancient work title
	* REFAUWORK + REFSCOPE+ << canonical citation
	* AUTHOR + AWORK + REFSCOPE << discoursive citation
	
The best way is to use the chunking function of nltk.corpus.

core.citation_parser >> to parse scope element

from nltk.metrics.distance import edit_distance >> to compare strings against APh dictionary

"""