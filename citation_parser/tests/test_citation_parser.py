from citation_parser import CitationParser

def test_citation_parser():
	cipa = CitationParser()
	res = cipa.parse("Hom. Il. 1,12-20; Verg. Aen., 2.240")
	assert len(res)==2
