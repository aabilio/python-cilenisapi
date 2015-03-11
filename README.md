
python-instagram
======
A Python 2 client for the Cilenisapi REST APIs

Installation
-----
pip install python-cilenisapi

Requires
-----
  * None


Cilenisapi API REST
------------------------------
Cilenis [developer site](https://cilenisapi.3scale.net/developers) documents all the Cilenis REST APIs.
   

Data Retrieval:
-----

Init Module


``` python
from cilenisapi.client import Cilenis

CILENIS_APP_ID  = u"XXXXXXXX"
CILENIS_APP_KEY = u"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

cilenisApi = Cilenis(CILENIS_APP_ID, CILENIS_APP_KEY)
```

See the endpoints docs for more on these methods: https://cilenisapi.3scale.net/developers

get_language_identifier from text or url
``` python
lang = cilenisApi.get_language_identifier(text=u"some text")
lang = cilenisApi.get_language_identifier(url=u"http://google.es")
```            

get_sentiment from text or url (with optional lang parameter)
``` python
sentiment_name, sentiment_weight = cilenisApi.get_sentiment(text=u"some text")
sentiment_name, sentiment_weight = cilenisApi.get_sentiment(url=u"http://google.es")
sentiment_name, sentiment_weight = cilenisApi.get_sentiment(text=u"some text", lang="es")
```  

get_keywords from text or url (with optional lang parameter)
``` python
keywords, html = cilenisApi.get_keywords(text=u"some text", lang="es")
keywords, html = cilenisApi.get_keywords(url=u"http://google.es")
```  

get_multiwords from text or url (with optional lang parameter)
``` python
keywords, html = cilenisApi.get_multiwords(text=u"some text", lang="es")
keywords, html = cilenisApi.get_multiwords(url=u"http://google.es")
```  

get_entities (people, organizations, places) from text or url (with optional lang and entity parameters)
``` python
entities, html = cilenisApi.get_entities(text=u"some text", lang="es", entity="all")
entities, html = cilenisApi.get_entities(text=u"some text")
entities, html = cilenisApi.get_entities(text=u"some text", entity="people")
entities, html = cilenisApi.get_entities(text=u"some text", entity="organizations")
entities, html = cilenisApi.get_entities(text=u"some text", entity="places")
```  

get_people from text or url (with optional lang parameter)
``` python
people = cilenisApi.get_people(text=u"some text", lang="es")
people = cilenisApi.get_people(url="http://google.es")
```  

get_organizations from text or url (with optional lang parameter)
``` python
organizations = cilenisApi.get_organizations(text=u"some text", lang="es")
organizations = cilenisApi.get_organizations(url="http://google.es")
```  

get_places from text or url (with optional lang parameter)
``` python
places = cilenisApi.get_places(text=u"some text", lang="es")
places = cilenisApi.get_places(url="http://google.es")
```  

split text or text from url (with optional lang parameter)
``` python
splitted_text = cilenisApi.split(text=u"some text", lang="es")
splitted_text = cilenisApi.split(url="http://google.es")
```  

get_keyword_context url (with optional lang parameter)
``` python
contexts = cilenisApi.get_keyword_context(keyword="aprobada", url="http://google.es")
contexts = cilenisApi.get_keyword_context(keyword="aprobada", url="http://google.es", lang="es")
```  

conjugate verb from infinitive (with optional lang parameter)
``` python
conjugations, lang = cilenisApi.conjugate(text="comer", lang="es")
conjugations, lang = cilenisApi.conjugate(text="comer")
```

is_infinitive (a word) (with optional lang parameter)
``` python
isInfinitive = cilenisApi.is_infinitive(text=u"comer", lang="es")
isInfinitive = cilenisApi.is_infinitive(text=u"palabra")
```

get_text_from_web (url) (with optional lang parameter)
``` python
text = cilenisApi.get_text_from_web(url=u"http://google.es", lang="es")
text = cilenisApi.get_text_from_web(url=u"http://google.es")
```

raw_endpoint (call api with raw endpoint and params and get raw response)
``` python
raw_response = cilenisApi.raw_endpoint( endpoint=u"language_identifier", params={
  "text": u"texto de ejemplo",
  "format": "xml",
  "app_id": CILENIS_APP_ID,
  "app_key": CILENIS_APP_KEY
})
```



Error handling
------
Importing the bind module allows handling of specific error status codes. An example is provided below:
``` python
from cilenisapi.exceptions import CilenisApiException, CilenisValidationException

try:
  # your code goes here
except CilenisValidationException as e:
  print "Validation error %s" % unicode(e)

try:
  # your code goes here
except CilenisApiException as e:
  print "API error %s" % unicode(e)
```


Example:
```python
>>> conjugations, lang = cilenisApi.conjugate(text=u"palabra", lang="es")

Traceback (most recent call last):
  File "example-app.py", line 28, in <module>
    conjugations, lang = cilenisApi.conjugate(text=u"palabra", lang="es")
  File ".../python-cilenisapi/cilenisapi/client.py", line 97, in wrapped_f
    return f(self, *args, **kwargs)
  File ".../python-cilenisapi/cilenisapi/client.py", line 147, in conjugate
    raise CilenisApiException(msg=unicode(result_json['conjugations'][0]['conjugation'][0]['code_tense']))
cilenisapi.exceptions.CilenisApiException: palabra no es un verbo en infinitivo
```

Sample app
------
This repository includes a one-file sample app.

``` bash
python example-app.py
```

