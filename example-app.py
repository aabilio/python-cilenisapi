#!/usr/bin/env python
# -*- coding: utf-8 -*-


from cilenisapi.client import Cilenis

CILENIS_APP_ID  = u"XXXXXXXX"
CILENIS_APP_KEY = u"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

example_texts = {
	"example_url"   : u"http://internacional.elpais.com/internacional/2015/03/11/actualidad/1426093551_815019.html",
	"text_neutral"  : u"Hola qué tal estamos",
	"text_positive" : u"Hola qué tal estamos, yo bien!",
	"text_negative" : u"Hola qué tal estamos, yo bastante mal!",
	"text_lorem"    : u'''Al contrario del pensamiento popular, el texto de Lorem Ipsum no es simplemente texto aleatorio. Tiene sus raices en una pieza cl´sica de la literatura del Latin, que data del año 45 antes de Cristo, haciendo que este adquiera mas de 2000 años de antiguedad. Richard McClintock, un profesor de Latin de la Universidad de Hampden-Sydney en Virginia, encontró una de las palabras más oscuras de la lengua del latín, "consecteur", en un pasaje de Lorem Ipsum, y al seguir leyendo distintos textos del latín, descubrió la fuente indudable. Lorem Ipsum viene de las secciones 1.10.32 y 1.10.33 de "de Finnibus Bonorum et Malorum" (Los Extremos del Bien y El Mal) por Cicero, escrito en el año 45 antes de Cristo. Este libro es un tratado de teoría de éticas, muy popular durante el Renacimiento. La primera linea del Lorem Ipsum, "Lorem ipsum dolor sit amet..", viene de una linea en la sección 1.10.32''',
	"text_entities" : u"Hola me llamo Pedro y vivo en Ourense, Galicia. Me gustaría trabajar en la ONU.",
	"infinitive"    : u"beber",
	"no_infinitive" : u"sardina",
}



if __name__ == "__main__":

	cilenisApi = Cilenis(CILENIS_APP_ID, CILENIS_APP_KEY)

	print "[ TEST ] get_language_identifier: %s" % example_texts['text_neutral']
	lang = cilenisApi.get_language_identifier(text=example_texts['text_neutral'])
	print "\t\_ %s" % lang

	print "[ TEST ] get_sentiment: %s" % example_texts['text_positive']
	sentiment_name, sentiment_weight = cilenisApi.get_sentiment(text=example_texts['text_positive'])
	print "\t\_ %s (%s)" % (sentiment_name, sentiment_weight)

	print "[ TEST ] get_sentiment: %s" % example_texts['text_negative']
	sentiment_name, sentiment_weight = cilenisApi.get_sentiment(text=example_texts['text_negative'], lang="es")
	print "\t\_ %s (%s)" % (sentiment_name, sentiment_weight)

	print "[ TEST ] get_keywords: %s..." % example_texts['text_lorem'][0:20]
	keywords, html = cilenisApi.get_keywords(text=example_texts['text_lorem'], lang="es")
	print "\t\_ %s ..." % (keywords[0])

	print "[ TEST ] get_multiwords: %s..." % example_texts['text_lorem'][0:20]
	multiwords = cilenisApi.get_multiwords(text=example_texts['text_lorem'], lang="es")
	print "\t\_ %s ..." % (multiwords[0]) if multiwords else "\t\_ No multiwords in text"

	print "[ TEST ] get_entities: %s" % example_texts['text_entities']
	entities, html = cilenisApi.get_entities(text=example_texts['text_entities'], lang="es", entity="all")
	print "\t\_ %s" % entities if entities else "\t\_ No entities in text"
	
	print "[ TEST ] get_people: %s" % example_texts['text_entities']
	people = cilenisApi.get_people(text=example_texts['text_entities'], lang="es")
	print "\t\_ %s" % people if people else "\t\_ No people in text"
	
	print "[ TEST ] get_organizations: %s" % example_texts['text_entities']
	organizations = cilenisApi.get_organizations(text=example_texts['text_entities'], lang="es")
	print "\t\_ %s" % organizations if organizations else "\t\_ No organizations in text"
	
	print "[ TEST ] get_places: %s" % example_texts['text_entities']
	places = cilenisApi.get_places(text=example_texts['text_entities'], lang="es")
	print "\t\_ %s" % places if places else "\t\_ No places in text"

	print "[ TEST ] split: %s" % example_texts['text_entities']
	splitted_text = cilenisApi.split(text=example_texts['text_entities'], lang="es")
	print "\t\_ %s" % splitted_text

	print "[ TEST ] get_keyword_context: %s" % example_texts['example_url']
	contexts = cilenisApi.get_keyword_context(keyword="aprobada", url=example_texts['example_url'], lang="es")
	print "\t\_ %s" % contexts

	print "[ TEST ] conjugate: %s" % example_texts['infinitive']
	conjugations, lang = cilenisApi.conjugate(text=example_texts['infinitive'], lang="es")
	print "\t\_ %s" % conjugations

	print "[ TEST ] is_infinitive: %s" % example_texts['infinitive']
	isInfinitive = cilenisApi.is_infinitive(text=example_texts['infinitive'], lang="es")
	print "\t\_ %s" % isInfinitive

	print "[ TEST ] is_infinitive: %s" % example_texts['no_infinitive']
	isInfinitive = cilenisApi.is_infinitive(text=example_texts['no_infinitive'], lang="es")
	print "\t\_ %s" % isInfinitive

	print "[ TEST ] get_text_from_web: %s" % example_texts['example_url']
	text = cilenisApi.get_text_from_web(url=example_texts['example_url'], lang="es")
	print "\t\_ %s" % text

	print "[ TEST ] raw_endpoint: %s" % example_texts['text_positive']
	raw_response = cilenisApi.raw_endpoint( endpoint=u"language_identifier", params={
		"text": example_texts['text_positive'],
		"format": "xml",
		"app_id": CILENIS_APP_ID,
		"app_key": CILENIS_APP_KEY
	})
	print "\t\_ %s" % raw_response
	


	



	