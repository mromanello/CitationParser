"""
Rationale:

using `surf`+rdflib create a file (e.g. `kb_addenda.ttl`) which contains
the triples to be added to RDF export of the CWKB db. This way I can avoid
modifying directly the CWKB data (modifies are overwritten every time they
give me a new dump of the db).


"""

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