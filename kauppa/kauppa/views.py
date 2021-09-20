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
    tuotteet = Tuote.objects.filter(id=tuote_id)
    tuote = tuotteet.get()
    return HttpResponse(TUOTESIVU_HTML.format(
        nimi=tuote.nimi, hinta=tuote.hinta))

TUOTESIVU_HTML = """
<html>
<body>
<h1>Kauppa</h1>
<h2>{nimi}</h2>
<p>
<b>{hinta} €</b>
Nyt tarjouksessa. Osta heti!
</p>
<p>
<a href="/">[etusivu]</a>
</p>
</body>
</html>
"""
