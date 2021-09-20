from django.http import HttpResponse

from .models import Tuote

ETUSIVU_HTML = """
<html>
<body>
<h1>Kauppa</h1>
Osta täältä:<br>
{}
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
    tuotelinkit = []
    for tuote in Tuote.objects.all():
        linkki = '<a href="/tuote/{id}/">{nimi}</a>'.format(
            id=tuote.id,
            nimi=tuote.nimi,
        )
        # linkki = f'<a href="/tuote/{tuote.id}/">{tuote.nimi}</a>'
        tuotelinkit.append(linkki)
    linkkiteksti = '<br>'.join(tuotelinkit)
    return HttpResponse(ETUSIVU_HTML.format(linkkiteksti))


def tuotesivu(request, tuote_id):
    return HttpResponse(TUOTESIVU_HTML.format(tuote_id))
