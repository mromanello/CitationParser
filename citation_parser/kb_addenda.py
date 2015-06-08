#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Matteo Romanello, matteo.romanello@gmail.com

"""
Rationale:

using `surf`+rdflib create a file (e.g. `kb_addenda.ttl`) which contains
the triples to be added to RDF export of the CWKB db. This way I can avoid
modifying directly the CWKB data (modifies are overwritten every time they
give me a new dump of the db).


"""

import surf
from surf import *
import rdflib
import codecs
from citation_parser import KnowledgeBase

abbreviations = [
	("urn:cts:cwkb:431.904","Orat.")
	,("urn:cts:latinLit:phi0474.phi005","Verr.")
	,("urn:cts:latinLit:phi0474.phi010","Cluent.")
	,("urn:cts:cwkb:998", "Nicand.")
	,("urn:cts:cwkb:998.3421" ,"Ther.")
	,("urn:cts:cwkb:1322.4345", "Hier. Epist.")
	,("urn:cts:greekLit:tlg0019.tlg009", "Ra.")
	,("urn:cts:greekLit:tlg0062.tlg031", "Philops.")
	,("urn:cts:cwkb:2386.8494" ,"Gest. Pelag.")
	,("urn:cts:cwkb:2388.8677", "Malch.")
	,("urn:cts:latinLit:phi0972.phi001", "Satyr.")
	,("urn:cts:latinLit:phi0972", "Petr.")
	,("urn:cts:cwkb:1351.4377","[ Verg. ] catal.")
	,("urn:cts:cwkb:664","Val. Flac.")
	,("urn:cts:greekLit:tlg0019.tlg008","Thesm.")
	,("urn:cts:greekLit:tlg0086.tlg003","Ath.")
	,("urn:cts:cwkb:766.1654","Meteor.")
	,("urn:cts:greekLit:tlg0003.tlg001","Thuc.")
]

names = [
	("urn:cts:cwkb:1322","Innocenzo I","it")
	,("urn:cts:cwkb:1358.4386" ,"Octavia","")
	,("urn:cts:cwkb:585","Pliny","en")
	,("urn:cts:cwkb:2796","Fulgence de Ruspe","fr")
	,("urn:cts:cwkb:2796","Fulgenzio di Ruspe","it")
	,("urn:cts:cwkb:2796","Fulgenzio","it")
	,("urn:cts:cwkb:2785","Beda","")
	,("urn:cts:cwkb:408","César","")
	,("urn:cts:cwkb:2392","Dracontius","")
]

titles = [
	("urn:cts:greekLit:tlg0020.tlg002", "Trabajos","es")
	,("urn:cts:cwkb:943.4531","Chronique","fr")
	,("urn:cts:cwkb:1075.3866","Life of Euripidis","en")
	,("urn:cts:cwkb:1398.4477","Contest of Homer and Hesiod","en")
	,("urn:cts:greekLit:tlg0019.tlg009","Grenouilles","fr")
	,("urn:cts:greekLit:tlg0019.tlg001","Acharnians","en")
	,("urn:cts:greekLit:tlg0020.tlg002","Erga","la")
	,("urn:cts:greekLit:tlg0059.tlg012","Phaidros","")
]

is_opus_maximum = [
	"urn:cts:latinLit:phi0550.phi001" #Lucr. De rerum natura
	,"urn:cts:latinLit:phi0472.phi001" # Catullus carmina
	,"urn:cts:greekLit:tlg0016.tlg001" # Herodotus' Historiae
	,"urn:cts:cwkb:2447.8028" # Avienus' Aratea
	,"urn:cts:cwkb:664.1367" # Valerius Flaccus Argonautica
	,"urn:cts:latinLit:stoa0023.stoa001" # Ammianus, Res Gestae
	,"urn:cts:cwkb:539.1115" # Martial's Epigrammata
	,"urn:cts:greekLit:tlg0003.tlg001" # Thuc. Hist.
]

knowledge_base_rdf_file = "/Users/rromanello/Documents/APh_Corpus_GUI/cwkb/export_triples/kb-all-in-one.ttl"
kb_addenda_file = "/Users/rromanello/Documents/APh_Corpus_GUI/cwkb/export_triples/kb-addenda.ttl"
knowlegde_base = KnowledgeBase(knowledge_base_rdf_file, "turtle")

store = Store(  reader='rdflib', writer='rdflib', rdflib_store = 'IOMemory')
session = Session(store)
# declare namespaces
surf.ns.register(crm='http://erlangen-crm.org/current/')
surf.ns.register(frbroo='http://erlangen-crm.org/efrbroo/')
# the graph to suck in all the rdf bits
g = rdflib.Graph()

E55_Type = session.get_class(surf.ns.CRM["E55_Type"])
F1_Work = session.get_class(surf.ns.FRBROO["F1_Work"])

opMax = E55_Type("http://127.0.0.1:8000/cwkb/types#opusmaximum")
opMax.rdfs_label = """The opux maximum of a given author:
					hat is, the only preserved work by that
					author or the most known one"""
g.parse(data=opMax.serialize('xml'))

for urn in is_opus_maximum:
	uri = knowlegde_base.get_URI_by_CTS_URN(urn)
	work = F1_Work(uri)
	work.crm_P2_has_type = opMax
	g.parse(data=work.serialize('xml'))

ofile = codecs.open(kb_addenda_file,'w','utf-8')
ofile.write(g.serialize(format="turtle"))
ofile.close()


