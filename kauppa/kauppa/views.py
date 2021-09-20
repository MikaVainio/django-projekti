from django.http import HttpResponse

from .models import Tuote

ETUSIVU_HTML = """
<html>
<body>
<h1>Kauppa</h1>
Osta täältä 
<a href="/tuote/1/">tuotetta 1</a>
tai
<a href="/tuote/2/">tuotetta 2</a>.
</body>
</html>
"""

TUOTESIVU_HTML = """
<html>
<body>
<h1>Kauppa</h1>
<h2>Tuote {}</h2>
<p>
Nyt tarjouksessa. Osta heti!
</p>
<p>
<a href="/">[etusivu]</a>
</p>
</body>
</html>
"""


def etusivu(request):
    for tuote in Tuote.objects.all():
        print(tuote)
    return HttpResponse(ETUSIVU_HTML)


def tuotesivu(request, tuote_id):
    return HttpResponse(TUOTESIVU_HTML.format(tuote_id))
