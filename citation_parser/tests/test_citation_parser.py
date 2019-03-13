from citation_parser import CitationParser


def test_citation_parser():
    """Bare minimum test for a citation_parser."""
    cipa = CitationParser()
    res = cipa.parse("Hom. Il. 1,12-20; Verg. Aen., 2.240")
    assert len(res) == 2


def test_scope2urn():
    """Test static method `CitationParser.scope2urn`."""
    urn = "urn:cts:greekLit:tlg0012.tlg001"
    cipa = CitationParser()
    norm_scope = cipa.parse("Hom. Il. 1,12-20; 2.240")
    urns = CitationParser.scope2urn(urn, norm_scope)
    assert urns == [
        "urn:cts:greekLit:tlg0012.tlg001:1.12-1.20",
        "urn:cts:greekLit:tlg0012.tlg001:2.240"
    ]
