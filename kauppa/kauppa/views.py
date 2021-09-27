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


def tietokantakyselyn_esimerkki():
    # Kaikkiin tietokantariveihin pääsee
    #  Luokka.objects.all() -kutsulla, joka palauttaa QuerySetin
    kaikki_tuotteet = Tuote.objects.all()

    # QuerySettiä voi suodattaa (=filtteröidä)
    tuotteet_jolla_id_3 = kaikki_tuotteet.filter(id=3)
    filtteroidut_tuotteet = kaikki_tuotteet.filter(hinta__lt=30)
    monimutkainen_kysely = (
        Tuote.objects
        .filter(hinta__lt=30)
        .filter(nimi__contains='u')
        .exclude(id=3)
    )

    # QuerySetillä on esim count(),
    # joka kertoo montako objektia QS sisältää
    print('QuerySet 1:', kaikki_tuotteet)
    print(kaikki_tuotteet.count())
    print('QuerySet 2:', tuotteet_jolla_id_3)
    print(tuotteet_jolla_id_3.count())

    # Jos QuerySetissä on vain yksi objekti, sen voi
    # hakea QuerySetistä get-metodilla:
    tuote = tuotteet_jolla_id_3.get()
    print('objekti:', tuote)
    print('hinta:', tuote.hinta)

    # QuerySetin sisältämiä objekteja voi käydä läpi
    # for-loopilla
    for tuote in filtteroidut_tuotteet:
        print(tuote, tuote.hinta)
