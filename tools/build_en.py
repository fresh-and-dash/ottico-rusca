"""Generate the English home page (en/index.html) from the Italian one (index.html).

The list T holds every Italian text with its English translation: when a text changes in index.html,
change it here too, then run:  python3 tools/build_en.py && python3 tools/build_pages.py
"""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IT = os.path.join(REPO, 'index.html')
SITE = 'https://www.otticorusca.ch/'

it = open(IT, encoding='utf-8').read()


def rep(s, a, b, count=None):
    n = s.count(a)
    assert n >= 1, ('missing', a[:90])
    if count is not None:
        assert n == count, (n, a[:90])
    return s.replace(a, b)


# ---------------------------------------------------------------- shared additions
LANG_CSS = '''  .lang { display: flex; align-items: center; gap: .1rem; font-family: var(--sans); font-size: .8rem; letter-spacing: .05em; }
  .lang a { text-decoration: none; color: rgba(244,247,250,.6); padding: .35rem .5rem; border-radius: 999px; transition: color .3s, box-shadow .3s; }
  .lang a:hover { color: var(--paper); }
  .lang a[aria-current] { color: var(--paper); box-shadow: inset 0 0 0 1px rgba(244,247,250,.35); }
'''
if '.lang {' not in it:
    it = rep(it, '  .head-actions { display: flex; align-items: center; gap: 1.1rem; }\n',
             '  .head-actions { display: flex; align-items: center; gap: 1.1rem; }\n' + LANG_CSS, 1)


def lang_nav(current, it_href, en_href, label):
    a_it = f'<a href="{it_href}" lang="it" hreflang="it"' + (' aria-current="page"' if current == 'it' else '') + '>IT</a>'
    a_en = f'<a href="{en_href}" lang="en" hreflang="en"' + (' aria-current="page"' if current == 'en' else '') + '>EN</a>'
    return f'<nav class="lang" aria-label="{label}">{a_it}{a_en}</nav>'


ALTERNATES = (f'<link rel="alternate" hreflang="it" href="{SITE}">\n'
              f'<link rel="alternate" hreflang="en" href="{SITE}en/">\n'
              f'<link rel="alternate" hreflang="x-default" href="{SITE}">')

if 'hreflang="en"' not in it:
    it = rep(it, f'<link rel="canonical" href="{SITE}">', f'<link rel="canonical" href="{SITE}">\n' + ALTERNATES, 1)
    it = rep(it, '    <div class="head-actions">\n',
             '    <div class="head-actions">\n      ' + lang_nav('it', './', 'en/', 'Lingua') + '\n', 1)
    it = rep(it, '<a href="mailto:eye-marcorusca@hotmail.com">eye-marcorusca@hotmail.com</a></p>\n</div>',
             '<a href="mailto:eye-marcorusca@hotmail.com">eye-marcorusca@hotmail.com</a><br><a href="en/" lang="en" hreflang="en">English version</a></p>\n</div>', 1)
open(IT, 'w', encoding='utf-8').write(it)

# ---------------------------------------------------------------- English page
en = it
EN_JSONLD = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@graph": [\n    {\n      "@type": "Optician",\n      "@id": "https://www.otticorusca.ch/#studio",\n      "name": "Studio ottico Rusca",\n      "alternateName": [\n        "Ottico Rusca",\n        "Rusca Marco, ottico"\n      ],\n      "description": "Optical practice in Savosa, on the edge of Lugano, by appointment: eye examinations, prescription glasses, progressive lenses and contact lenses. Marco Rusca, Swiss federally certified optician (master optician), more than forty years of practice.",\n      "url": "https://www.otticorusca.ch/",\n      "image": [\n        "https://www.otticorusca.ch/img/studio-strumenti-1600.jpg",\n        "https://www.otticorusca.ch/img/studio-sala-esame-1200.jpg",\n        "https://www.otticorusca.ch/img/studio-montature-1600.jpg",\n        "https://www.otticorusca.ch/img/studio-attesa-1600.jpg",\n        "https://www.otticorusca.ch/og-image-en.png"\n      ],\n      "telephone": "+41919663268",\n      "email": "eye-marcorusca@hotmail.com",\n      "address": {\n        "@type": "PostalAddress",\n        "streetAddress": "Via Emilio Maraini 27",\n        "postalCode": "6942",\n        "addressLocality": "Savosa",\n        "addressRegion": "TI",\n        "addressCountry": "CH"\n      },\n      "geo": {\n        "@type": "GeoCoordinates",\n        "latitude": 46.01683,\n        "longitude": 8.94424\n      },\n      "hasMap": "https://www.google.com/maps/search/?api=1&query=Studio+ottico+Rusca%2C+Via+Emilio+Maraini+27%2C+6942+Savosa&query_place_id=ChIJw0RDq34yhEcRZd4bjoxRZnE",\n      "areaServed": [\n        {\n          "@type": "City",\n          "name": "Savosa"\n        },\n        {\n          "@type": "City",\n          "name": "Lugano"\n        },\n        {\n          "@type": "AdministrativeArea",\n          "name": "Luganese"\n        },\n        {\n          "@type": "AdministrativeArea",\n          "name": "Canton of Ticino"\n        }\n      ],\n      "knowsAbout": [\n        "Eye examination",\n        "Refraction",\n        "Progressive lenses",\n        "Occupational lenses",\n        "Contact lenses",\n        "Astigmatism",\n        "Presbyopia"\n      ],\n      "hasOfferCatalog": {\n        "@type": "OfferCatalog",\n        "name": "Services",\n        "itemListElement": [\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Eye examination"\n            }\n          },\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Prescription glasses"\n            }\n          },\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Progressive lenses"\n            }\n          },\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Occupational (office) lenses"\n            }\n          },\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Contact lens fitting"\n            }\n          },\n          {\n            "@type": "Offer",\n            "itemOffered": {\n              "@type": "Service",\n              "name": "Adjustment and repair of glasses"\n            }\n          }\n        ]\n      },\n      "founder": {\n        "@id": "https://www.otticorusca.ch/#marco-rusca"\n      },\n      "sameAs": [\n        "https://www.local.ch/it/d/savosa/6942/ottico/rusca-marco-NcHW8Whr9MO1ePPfZew7Yw"\n      ],\n      "brand": [\n        {\n          "@type": "Brand",\n          "name": "Silhouette"\n        },\n        {\n          "@type": "Brand",\n          "name": "Porsche Design"\n        },\n        {\n          "@type": "Brand",\n          "name": "Furla"\n        },\n        {\n          "@type": "Brand",\n          "name": "Lamarca"\n        },\n        {\n          "@type": "Brand",\n          "name": "Titanflex"\n        },\n        {\n          "@type": "Brand",\n          "name": "Airlight"\n        },\n        {\n          "@type": "Brand",\n          "name": "Clark"\n        },\n        {\n          "@type": "Brand",\n          "name": "Trevi 1971"\n        },\n        {\n          "@type": "Brand",\n          "name": "Chopard"\n        },\n        {\n          "@type": "Brand",\n          "name": "ic! berlin"\n        },\n        {\n          "@type": "Brand",\n          "name": "Police"\n        },\n        {\n          "@type": "Brand",\n          "name": "Humphrey’s"\n        },\n        {\n          "@type": "Brand",\n          "name": "Ray-Ban"\n        },\n        {\n          "@type": "Brand",\n          "name": "Marius Morel"\n        },\n        {\n          "@type": "Brand",\n          "name": "Gambini"\n        },\n        {\n          "@type": "Brand",\n          "name": "Dolce&Gabbana"\n        },\n        {\n          "@type": "Brand",\n          "name": "Alberto Puccini"\n        }\n      ]\n    },\n    {\n      "@type": "Person",\n      "@id": "https://www.otticorusca.ch/#marco-rusca",\n      "name": "Marco Rusca",\n      "image": "https://www.otticorusca.ch/img/marco-rusca-960.jpg",\n      "jobTitle": "Swiss federally certified optician (master optician)",\n      "birthPlace": {\n        "@type": "Place",\n        "name": "Lugano"\n      },\n      "alumniOf": {\n        "@type": "EducationalOrganization",\n        "name": "Swiss Higher School of Optics (Scuola superiore svizzera d’ottica)",\n        "address": {\n          "@type": "PostalAddress",\n          "addressLocality": "Olten",\n          "addressCountry": "CH"\n        }\n      },\n      "hasCredential": [\n        {\n          "@type": "EducationalOccupationalCredential",\n          "credentialCategory": "diploma",\n          "name": "Swiss federal optician’s diploma (master optician)",\n          "dateCreated": "1986"\n        },\n        {\n          "@type": "EducationalOccupationalCredential",\n          "credentialCategory": "diploma",\n          "name": "Ticino cantonal optician’s diploma"\n        }\n      ],\n      "knowsAbout": [\n        "Contact lenses",\n        "Eye examination",\n        "Progressive lenses"\n      ],\n      "worksFor": {\n        "@id": "https://www.otticorusca.ch/#studio"\n      }\n    },\n    {\n      "@type": "Book",\n      "@id": "https://www.otticorusca.ch/#libro",\n      "name": "Lenti a contatto. Guida pratica per tutti",\n      "author": {\n        "@id": "https://www.otticorusca.ch/#marco-rusca"\n      },\n      "inLanguage": "it",\n      "about": {\n        "@type": "Thing",\n        "name": "Contact lenses"\n      },\n      "image": "https://www.otticorusca.ch/img/libro-copertina.jpg",\n      "url": "https://www.otticorusca.ch/en/#libro"\n    },\n    {\n      "@type": "WebSite",\n      "@id": "https://www.otticorusca.ch/#website",\n      "url": "https://www.otticorusca.ch/",\n      "name": "Studio ottico Rusca",\n      "inLanguage": [\n        "it-CH",\n        "en"\n      ],\n      "publisher": {\n        "@id": "https://www.otticorusca.ch/#studio"\n      }\n    },\n    {\n      "@type": "FAQPage",\n      "@id": "https://www.otticorusca.ch/#domande",\n      "mainEntity": [\n        {\n          "@type": "Question",\n          "name": "What is the difference between an optician, an optometrist and an ophthalmologist?",\n          "acceptedAnswer": {\n            "@type": "Answer",\n            "text": "An ophthalmologist is a medical doctor who diagnoses and treats eye diseases. An optician makes glasses and fits contact lenses; an optometrist is an optician with higher training, specialised in eye examinations. To have your eyesight measured you can go directly to a federally certified optician; if anything calls for a medical check, the practice refers you to an ophthalmologist."\n          }\n        },\n        {\n          "@type": "Question",\n          "name": "What does “Swiss federally certified optician (master optician)” mean?",\n          "acceptedAnswer": {\n            "@type": "Answer",\n            "text": "It is the higher federal diploma of the optician’s profession in Switzerland. Beyond basic training it covers eye examinations and contact lens fitting. Marco Rusca obtained it in 1986 at the Swiss Higher School of Optics in Olten and has practised the profession for more than forty years."\n          }\n        },\n        {\n          "@type": "Question",\n          "name": "How often should I have my eyes tested?",\n          "acceptedAnswer": {\n            "@type": "Answer",\n            "text": "If you have no complaints, about every two years. Sooner if you notice changes: difficulty reading, headaches, trouble driving at night, tiredness in front of a screen."\n          }\n        },\n        {\n          "@type": "Question",\n          "name": "Why can’t I get used to my progressive lenses?",\n          "acceptedAnswer": {\n            "@type": "Answer",\n            "text": "The three most common causes are a correction that is not quite exact, imprecise centring, or a lens or frame that does not suit how the glasses are really used. It is worth having the measurements and the fitting checked before giving up."\n          }\n        },\n        {\n          "@type": "Question",\n          "name": "Where is the practice and how do I make an appointment?",\n          "acceptedAnswer": {\n            "@type": "Answer",\n            "text": "In Savosa, at Via Emilio Maraini 27, in the Crocifisso area, on the edge of Lugano. The practice sees clients by appointment only: by phone on +41 91 966 32 68 or with the form below."\n          }\n        }\n      ]\n    }\n  ]\n}\n</script>'

# paths one level down
for a, b in [('url("fonts/', 'url("../fonts/'), ('href="fonts/', 'href="../fonts/'),
             ('href="favicon.svg"', 'href="../favicon.svg"'), ('href="apple-touch-icon.png"', 'href="../apple-touch-icon.png"')]:
    en = rep(en, a, b)

en = rep(en, lang_nav('it', './', 'en/', 'Lingua'), lang_nav('en', '../', './', 'Language'), 1)
en = rep(en, '<a href="en/" lang="en" hreflang="en">English version</a>', '<a href="../" lang="it" hreflang="it">Versione italiana</a>', 1)

# structured data (English block generated by seo_edits.jsonld)
_ld_a = en.index('<script type="application/ld+json">'); _ld_b = en.index('</script>', _ld_a) + len('</script>')
en = en[:_ld_a] + EN_JSONLD + en[_ld_b:]

# head
T = [
    ('<html lang="it-CH">', '<html lang="en">'),
    # frames gallery
    ('<p class="fg-kicker">Alcune delle montature in studio</p>', '<p class="fg-kicker">Some of the frames at the practice</p>'),
    ('aria-label="Filtra per marca"', 'aria-label="Filter by brand"'),
    ('data-brand="*">Tutte</button>', 'data-brand="*">All</button>'),
    ('data-more="Mostra tutte le 27 montature" data-less="Mostra meno">Mostra tutte le 27 montature</button>', 'data-more="Show all 27 frames" data-less="Show fewer">Show all 27 frames</button>'),
    ('aria-label="Foto"', 'aria-label="Photos"'),
    ('alt="Montatura Silhouette: senza cerchio, color bronzo"', 'alt="Silhouette frame: rimless, bronze"'),
    ('<span class="fg-d">Senza cerchio, color bronzo</span>', '<span class="fg-d">Rimless, bronze</span>'),
    ('alt="Montatura Silhouette: ovale, ambra trasparente"', 'alt="Silhouette frame: oval, transparent amber"'),
    ('<span class="fg-d">Ovale, ambra trasparente</span>', '<span class="fg-d">Oval, transparent amber</span>'),
    ('alt="Montatura Silhouette: ovale, verde acqua trasparente"', 'alt="Silhouette frame: oval, transparent aqua green"'),
    ('<span class="fg-d">Ovale, verde acqua trasparente</span>', '<span class="fg-d">Oval, transparent aqua green</span>'),
    ('alt="Montatura Porsche Design: titanio nero, aste rosse"', 'alt="Porsche Design frame: black titanium, red temples"'),
    ('<span class="fg-d">Titanio nero, aste rosse</span>', '<span class="fg-d">Black titanium, red temples</span>'),
    ('alt="Montatura Porsche Design: senza cerchio, nera"', 'alt="Porsche Design frame: rimless, black"'),
    ('<span class="fg-d">Senza cerchio, nera</span>', '<span class="fg-d">Rimless, black</span>'),
    ('alt="Montatura Porsche Design: ovale in titanio, nera"', 'alt="Porsche Design frame: oval titanium, black"'),
    ('<span class="fg-d">Ovale in titanio, nera</span>', '<span class="fg-d">Oval titanium, black</span>'),
    ('alt="Montatura Furla: squadrata, acetato nero"', 'alt="Furla frame: square, black acetate"'),
    ('<span class="fg-d">Squadrata, acetato nero</span>', '<span class="fg-d">Square, black acetate</span>'),
    ('alt="Montatura Furla: tonda, acetato nero"', 'alt="Furla frame: round, black acetate"'),
    ('<span class="fg-d">Tonda, acetato nero</span>', '<span class="fg-d">Round, black acetate</span>'),
    ('alt="Montatura Furla: squadrata, tartarugata"', 'alt="Furla frame: square, tortoiseshell"'),
    ('<span class="fg-d">Squadrata, tartarugata</span>', '<span class="fg-d">Square, tortoiseshell</span>'),
    ('alt="Montatura Lamarca: a farfalla, nera con verde e rosso"', 'alt="Lamarca frame: cat-eye, black with green and red"'),
    ('<span class="fg-d">A farfalla, nera con verde e rosso</span>', '<span class="fg-d">Cat-eye, black with green and red</span>'),
    ('alt="Montatura Lamarca: tonda, mosaico blu e arancio"', 'alt="Lamarca frame: round, blue and orange mosaic"'),
    ('<span class="fg-d">Tonda, mosaico blu e arancio</span>', '<span class="fg-d">Round, blue and orange mosaic</span>'),
    ('alt="Montatura Lamarca: a rombo, blu e ocra"', 'alt="Lamarca frame: diamond-shaped, blue and ochre"'),
    ('<span class="fg-d">A rombo, blu e ocra</span>', '<span class="fg-d">Diamond-shaped, blue and ochre</span>'),
    ('alt="Montatura Titanflex: rettangolare, metallo grafite"', 'alt="Titanflex frame: rectangular, graphite metal"'),
    ('<span class="fg-d">Rettangolare, metallo grafite</span>', '<span class="fg-d">Rectangular, graphite metal</span>'),
    ('alt="Montatura Titanflex: tonda, metallo color bronzo"', 'alt="Titanflex frame: round, bronze metal"'),
    ('<span class="fg-d">Tonda, metallo color bronzo</span>', '<span class="fg-d">Round, bronze metal</span>'),
    ('alt="Montatura Airlight: ovale, acciaio rosso"', 'alt="Airlight frame: oval, red steel"'),
    ('<span class="fg-d">Ovale, acciaio rosso</span>', '<span class="fg-d">Oval, red steel</span>'),
    ('alt="Montatura Airlight: tonda, metallo blu"', 'alt="Airlight frame: round, blue metal"'),
    ('<span class="fg-d">Tonda, metallo blu</span>', '<span class="fg-d">Round, blue metal</span>'),
    ('alt="Montatura Clark: tartarugata con blu"', 'alt="Clark frame: tortoiseshell with blue"'),
    ('<span class="fg-d">Tartarugata con blu</span>', '<span class="fg-d">Tortoiseshell with blue</span>'),
    ('alt="Montatura Trevi 1971: a farfalla, rosso e lilla"', 'alt="Trevi 1971 frame: cat-eye, red and lilac"'),
    ('<span class="fg-d">A farfalla, rosso e lilla</span>', '<span class="fg-d">Cat-eye, red and lilac</span>'),
    ('alt="Montatura Chopard: senza cerchio, color oro rosa"', 'alt="Chopard frame: rimless, rose gold colour"'),
    ('<span class="fg-d">Senza cerchio, color oro rosa</span>', '<span class="fg-d">Rimless, rose gold colour</span>'),
    ('alt="Montatura ic! berlin: tonda, metallo sottile"', 'alt="ic! berlin frame: round, thin metal"'),
    ('<span class="fg-d">Tonda, metallo sottile</span>', '<span class="fg-d">Round, thin metal</span>'),
    ('alt="Montatura Police: tonda, verde trasparente"', 'alt="Police frame: round, transparent green"'),
    ('<span class="fg-d">Tonda, verde trasparente</span>', '<span class="fg-d">Round, transparent green</span>'),
    ('alt="Montatura Humphrey’s: tonda, sfumata blu e verde"', 'alt="Humphrey’s frame: round, blue-to-green gradient"'),
    ('<span class="fg-d">Tonda, sfumata blu e verde</span>', '<span class="fg-d">Round, blue-to-green gradient</span>'),
    ('alt="Montatura Ray-Ban: rettangolare, nera"', 'alt="Ray-Ban frame: rectangular, black"'),
    ('<span class="fg-d">Rettangolare, nera</span>', '<span class="fg-d">Rectangular, black</span>'),
    ('alt="Montatura Marius Morel 1880: tonda, acetato color corno"', 'alt="Marius Morel 1880 frame: round, horn-coloured acetate"'),
    ('<span class="fg-d">Tonda, acetato color corno</span>', '<span class="fg-d">Round, horn-coloured acetate</span>'),
    ('alt="Montatura Gambini: tonda, blu trasparente"', 'alt="Gambini frame: round, transparent blue"'),
    ('<span class="fg-d">Tonda, blu trasparente</span>', '<span class="fg-d">Round, transparent blue</span>'),
    ('alt="Montatura Dolce&amp;Gabbana: squadrata, nera e oro"', 'alt="Dolce&amp;Gabbana frame: square, black and gold"'),
    ('<span class="fg-d">Squadrata, nera e oro</span>', '<span class="fg-d">Square, black and gold</span>'),
    ('alt="Montatura Alberto Puccini: squadrata, nera con strass"', 'alt="Alberto Puccini frame: square, black with rhinestones"'),
    ('<span class="fg-d">Squadrata, nera con strass</span>', '<span class="fg-d">Square, black with rhinestones</span>'),
    ('<span class="fv">Ospite</span><span class="fl">alla Radio svizzera italiana e Televisione svizzera italiana</span>', '<span class="fv">Guest</span><span class="fl">on Swiss Italian-language public radio and television</span>'),
    # portrait of Marco Rusca
    ('alt="Ritratto di Marco Rusca, ottico diplomato federale (maestro ottico)"', 'alt="Portrait of Marco Rusca, Swiss federally certified optician (master optician)"'),
    ('<span class="portrait-badge"><b>Diploma federale</b><span>Olten, 1986</span></span>', '<span class="portrait-badge"><b>Federal diploma</b><span>Olten, 1986</span></span>'),
    ('<figcaption>Ottico diplomato federale (maestro ottico), titolare dello studio.</figcaption>', '<figcaption>Swiss federally certified optician (master optician), owner of the practice.</figcaption>'),
    ('<p><b>La riceve Marco Rusca</b><span>di persona, su appuntamento</span></p>', '<p><b>Marco Rusca will see you</b><span>in person, by appointment</span></p>'),
    # the practice in photographs (#lo-studio)
    ('srcset="img/', 'srcset="../img/'),
    (', img/', ', ../img/'),
    ('href="img/', 'href="../img/'),
    ('<p class="tour-kicker">Lo studio</p>', '<p class="tour-kicker">The practice</p>'),
    ('Uno sguardo dentro lo studio.', 'A look inside the practice.'),
    ('alt="La sala d’esame dello studio, con gli strumenti per l’esame della vista"', 'alt="The practice’s examination room, with the instruments for eye examinations"'),
    ('<p class="tour-cap-t">Gli strumenti di misura</p><p class="tour-cap-d">Dalla misura automatica alla prova soggettiva: ogni valore viene verificato prima di ordinare una lente.</p>', '<p class="tour-cap-t">The measuring instruments</p><p class="tour-cap-d">From automatic measurement to the subjective test: every value is checked before a lens is ordered.</p>'),
    ('<p class="tour-cap-t">La sala d’esame</p><p class="tour-cap-d">Una stanza dedicata all’esame della vista, attrezzata per ogni fase.</p>', '<p class="tour-cap-t">The examination room</p><p class="tour-cap-d">A room dedicated to eye examinations, equipped for every stage.</p>'),
    ('Una sala d’esame attrezzata, una scelta di montature selezionate, una sala d’attesa tranquilla. Lo studio si trova in Via Emilio Maraini 27 a Savosa, zona Crocifisso, e riceve solo su appuntamento.', 'A fully equipped examination room, a selection of carefully chosen frames, a quiet waiting room. The practice is at Via Emilio Maraini 27 in Savosa, in the Crocifisso area, and sees clients by appointment only.'),
    ('alt="La sala d’esame: poltrona e unità d’esame con forottero, lampada a fessura e proiettore di ottotipi"', 'alt="The examination room: examination chair and unit with phoropter, slit lamp and chart projector"'),
    ('<span class="tg-t">La sala d’esame</span><span class="tg-d">Forottero, lampada a fessura e proiettore di ottotipi, in una stanza dedicata.</span>', '<span class="tg-t">The examination room</span><span class="tg-d">Phoropter, slit lamp and chart projector, in a dedicated room.</span>'),
    ('alt="Refrattometro automatico in primo piano e, sullo sfondo, la poltrona e l’unità d’esame"', 'alt="Automatic refractometer in the foreground, with the examination chair and unit behind"'),
    ('<span class="tg-t">Gli strumenti di misura</span><span class="tg-d">Dalla misura automatica alla prova soggettiva, ogni valore viene verificato.</span>', '<span class="tg-t">The measuring instruments</span><span class="tg-d">From automatic measurement to the subjective test, every value is checked.</span>'),
    ('alt="La parete illuminata delle montature e il banco per la scelta e la regolazione"', 'alt="The illuminated wall of frames and the counter for choosing and adjusting them"'),
    ('<span class="tg-t">Le montature</span><span class="tg-d">Una selezione, non un catalogo: si provano con calma e si regolano sul viso.</span>', '<span class="tg-t">The frames</span><span class="tg-d">A selection, not a catalogue: tried on at leisure and adjusted to your face.</span>'),
    ('alt="La sala d’attesa dello studio, luminosa e tranquilla"', 'alt="The practice’s waiting room, bright and quiet"'),
    ('<span class="tg-t">La sala d’attesa</span><span class="tg-d">Si riceve su appuntamento, una persona alla volta.</span>', '<span class="tg-t">The waiting room</span><span class="tg-d">By appointment only, one person at a time.</span>'),
    ('aria-label="Chiudi"', 'aria-label="Close"'),
    ('aria-label="Foto precedente"', 'aria-label="Previous photo"'),
    ('aria-label="Foto successiva"', 'aria-label="Next photo"'),
    # the book (#libro)
    ('src="img/', 'src="../img/'),
    ('<span class="fv">Autore</span><span class="fl">di <a href="#libro"><cite>Lenti a contatto. Guida pratica per tutti</cite></a></span>', '<span class="fv">Author</span><span class="fl">of <a href="#libro">a practical guide to contact lenses</a></span>'),
    ('Nato a Lugano, ha conseguito prima il diploma cantonale ticinese e poi, nel 1986, il diploma federale di ottico (maestria) alla Scuola superiore svizzera d’ottica di Olten. Da allora è titolare del proprio studio a Lugano-Crocifisso. Per anni ha affiancato alla pratica l’insegnamento dell’ottica al Centro Professionale Tecnico, ed è stato chiamato come esperto federale agli esami di maestria: chi forma e valuta i futuri maestri ottici conosce la professione fino in fondo.', 'Born in Lugano, he first obtained the Ticino cantonal diploma and then, in 1986, the Swiss federal optician’s diploma (master optician) at the Swiss Higher School of Optics in Olten. He has run his own practice in Lugano-Crocifisso ever since. For many years he combined practice with teaching optics at the Centro Professionale Tecnico, and he has served as a federal expert at the master optician examinations: those who train and assess future master opticians know the profession inside out.'),
    ('Lo studio nasce da una convinzione semplice, maturata in decenni di pratica: la vista si misura con pazienza e si corregge con precisione, e nessuna delle due cose si fa bene di fretta.', 'The practice grew from a simple conviction, formed over decades of practice: eyesight is measured with patience and corrected with precision, and neither can be done well in a hurry.'),
    ('Maestria federale conseguita nel 1986 alla Scuola superiore svizzera d’ottica di Olten', 'Federal master’s diploma obtained in 1986 at the Swiss Higher School of Optics in Olten'),
    ('<span class="t">Autore di <cite>Lenti a contatto. Guida pratica per tutti</cite></span><span class="small">Una guida per chi porta, o vorrebbe portare, le lenti a contatto. <a href="#libro">Vedere il libro</a></span>', '<span class="t">Author of <cite>Lenti a contatto. Guida pratica per tutti</cite></span><span class="small">A guide for people who wear, or would like to wear, contact lenses. <a href="#libro">See the book</a></span>'),
    ('alt="Copertina del libro «Lenti a contatto. Guida pratica per tutti» di Marco Rusca"', 'alt="Cover of the book «Lenti a contatto. Guida pratica per tutti» by Marco Rusca"'),
    ('alt="Quarta di copertina: le domande a cui risponde il libro e una breve biografia di Marco Rusca"', 'alt="Back cover: the questions the book answers and a short biography of Marco Rusca"'),
    ('data-front="Gira il libro" data-back="Torna alla copertina"', 'data-front="Turn the book over" data-back="Back to the cover"'),
    ('<span>Gira il libro</span>', '<span>Turn the book over</span>'),
    ('Un libro sulle lenti a contatto, scritto da chi le applica.', 'A book on contact lenses, written by someone who fits them.'),
    ('Marco Rusca è l’autore di <cite>Lenti a contatto. Guida pratica per tutti</cite>: una guida scritta per rispondere con chiarezza, e con parole semplici, alle domande di chi porta le lenti a contatto o pensa di cominciare.', 'Marco Rusca is the author of <cite>Lenti a contatto. Guida pratica per tutti</cite> (Contact lenses: a practical guide for everyone), written to answer clearly, and in plain words, the questions of people who wear contact lenses or are thinking of starting.'),
    ('<li>Sono migliori degli occhiali?</li>', '<li>Are they better than glasses?</li>'),
    ('<li>È vero che impediscono il progredire della miopia?</li>', '<li>Is it true that they stop short-sightedness from progressing?</li>'),
    ('<li>Da che età e fino a quando si possono portare?</li>', '<li>From what age, and until when, can they be worn?</li>'),
    ('<li>Si possono portare per mesi ininterrottamente?</li>', '<li>Can they be worn for months without a break?</li>'),
    ('<li>Il vostro difetto visivo può essere corretto con le lenti a contatto?</li>', '<li>Can your vision problem be corrected with contact lenses?</li>'),
    ('Sono domande che non hanno una risposta valida per tutti. Per questo, in studio, la risposta arriva dopo l’esame dei suoi occhi e una prova delle lenti.', 'None of these questions has an answer that applies to everyone. That is why, at the practice, the answer comes after an examination of your eyes and a trial of the lenses.'),
    # facts row, reviews heading
    ('<span class="fv">Diploma federale</span>', '<span class="fv">Federal diploma</span>'),
    ('<span class="fv">Oltre 40 anni</span>', '<span class="fv">Over 40 years</span>'),
    ('<span class="fl">di pratica professionale</span>', '<span class="fl">of professional practice</span>'),
    ('<span class="fv">Già docente</span>', '<span class="fv">Former lecturer</span>'),
    ('<span class="fl">al Centro Professionale Tecnico</span>', '<span class="fl">at the Centro Professionale Tecnico</span>'),
    ('<h2>Cosa dicono i clienti</h2>', '<h2>What clients say</h2>'),
    # FAQ, links to the service pages, footer links
    ('<h3>Che differenza c’è tra ottico, optometrista e oculista?</h3>', '<h3>What is the difference between an optician, an optometrist and an ophthalmologist?</h3>'),
    ('<p>L’oculista è un medico: diagnostica e cura le malattie dell’occhio. L’ottico realizza occhiali e lenti a contatto; l’optometrista è l’ottico con formazione superiore, specializzato nell’esame della vista. Per misurare la vista ci si può rivolgere direttamente a un ottico diplomato federale; se emergono segni che richiedono un accertamento medico, lo studio indirizza all’oculista.', '<p>An ophthalmologist is a medical doctor who diagnoses and treats eye diseases. An optician makes glasses and fits contact lenses; an optometrist is an optician with higher training, specialised in eye examinations. To have your eyesight measured you can go directly to a federally certified optician; if anything calls for a medical check, the practice refers you to an ophthalmologist.'),
    ('<h3>Che cosa significa «ottico diplomato federale (maestro ottico)»?</h3>', '<h3>What does “Swiss federally certified optician (master optician)” mean?</h3>'),
    ('<p>È il diploma federale superiore della professione di ottico in Svizzera. Oltre alla formazione di base comprende l’esame della vista e l’applicazione di lenti a contatto. Marco Rusca lo ha conseguito nel 1986 alla Scuola superiore svizzera d’ottica di Olten ed esercita la professione da oltre quarant’anni.', '<p>It is the higher federal diploma of the optician’s profession in Switzerland. Beyond basic training it covers eye examinations and contact lens fitting. Marco Rusca obtained it in 1986 at the Swiss Higher School of Optics in Olten and has practised the profession for more than forty years.'),
    ('<h3>Ogni quanto conviene controllare la vista?</h3>', '<h3>How often should I have my eyes tested?</h3>'),
    ('<p>In assenza di disturbi, ogni due anni circa. Prima, se nota cambiamenti: fatica a leggere, mal di testa, difficoltà alla guida di sera, stanchezza davanti allo schermo.', '<p>If you have no complaints, about every two years. Sooner if you notice changes: difficulty reading, headaches, trouble driving at night, tiredness in front of a screen.'),
    ('<h3>Perché non riesco ad abituarmi alle lenti progressive?</h3>', '<h3>Why can’t I get used to my progressive lenses?</h3>'),
    ('<p>Le cause più frequenti sono tre: una correzione non del tutto esatta, una centratura imprecisa, una lente o una montatura non adatte all’uso reale. Conviene far verificare misure e montaggio prima di rinunciare.', '<p>The three most common causes are a correction that is not quite exact, imprecise centring, or a lens or frame that does not suit how the glasses are really used. It is worth having the measurements and the fitting checked before giving up.'),
    ('<h3>Dove si trova lo studio e come si prende appuntamento?</h3>', '<h3>Where is the practice and how do I make an appointment?</h3>'),
    ('<p>A Savosa, in Via Emilio Maraini 27, zona Crocifisso, alle porte di Lugano. Lo studio riceve solo su appuntamento: per telefono allo 091 966 32 68 oppure con il modulo qui sotto.', '<p>In Savosa, at Via Emilio Maraini 27, in the Crocifisso area, on the edge of Lugano. The practice sees clients by appointment only: by phone on +41 91 966 32 68 or with the form below.'),
    ('>Come si svolge l’esame della vista</a>', '>How the eye examination works</a>'),
    ('>Lenti progressive: come si scelgono</a>', '>Progressive lenses: how they are chosen</a>'),
    ('>Lenti a contatto: come avviene l’applicazione</a>', '>Contact lenses: how the fitting works</a>'),
    ('>Se non ci si abitua alle progressive</a>', '>If you cannot get used to progressives</a>'),
    ('>Lenti progressive: da cosa dipende il risultato</a>', '>Progressive lenses: what the result depends on</a>'),
    ('<h2 class="reveal">Domande frequenti</h2>', '<h2 class="reveal">Frequently asked questions</h2>'),
    ('/">Esame della vista</a>', '/">Eye examination</a>'),
    ('/">Lenti progressive</a>', '/">Progressive lenses</a>'),
    ('/">Lenti a contatto</a>', '/">Contact lenses</a>'),
    ('href="esame-della-vista/', 'href="eye-examination/'),
    ('href="lenti-progressive/', 'href="progressive-lenses/'),
    ('href="lenti-a-contatto/', 'href="contact-lenses/'),
    ('#adattamento"', '#adapting"'),
    ('<title>Ottico a Savosa, Lugano | Studio ottico Rusca</title>', '<title>Optician in Lugano (Savosa) | Studio ottico Rusca</title>'),
    ('content="Studio ottico Rusca a Savosa, alle porte di Lugano: esame della vista, occhiali, lenti progressive e lenti a contatto. Ottico diplomato federale (maestro ottico), oltre quarant\'anni di pratica. Su appuntamento."',
     'content="Rusca optical practice in Savosa, on the edge of Lugano: eye examinations, glasses, progressive lenses and contact lenses. Swiss federally certified optician (master optician), more than forty years of practice. By appointment."'),
    ('content="Studio ottico Rusca – Ottico a Savosa, Lugano"', 'content="Studio ottico Rusca – Optician in Savosa, Lugano"'),
    ('content="Uno studio, non un negozio. Ottico diplomato federale (maestro ottico), riceve su appuntamento a Savosa."',
     'content="A practice, not a shop. Swiss federally certified optician (master optician), seeing clients by appointment in Savosa."'),
    ('<meta property="og:image" content="https://www.otticorusca.ch/og-image.png">', '<meta property="og:image" content="https://www.otticorusca.ch/og-image-en.png">'),
    ('Lo studio ottico Rusca si trova a Savosa, in zona Crocifisso, alle porte di Lugano. Riceve su appuntamento chi arriva da Lugano, dal Luganese e dal resto del Ticino. ',
     'The Rusca optical practice is in Savosa, in the Crocifisso area, on the edge of Lugano. It sees clients by appointment from Lugano, the surrounding area and the rest of Ticino. '),
    ('>Indicazioni stradali</a>', '>Directions</a>'),
    ('<meta property="og:locale" content="it_CH">', '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="it_CH">'),
    (f'<meta property="og:url" content="{SITE}">', f'<meta property="og:url" content="{SITE}en/">'),
    (f'<link rel="canonical" href="{SITE}">', f'<link rel="canonical" href="{SITE}en/">'),

    # header, menu
    ('>Vai al contenuto<', '>Skip to content<'),
    ('aria-label="Rusca, studio ottico – inizio pagina"', 'aria-label="Rusca, optician – back to top"'),
    ('<span class="role">Studio ottico, Lugano – Crocifisso</span>', '<span class="role">Optical practice, Lugano – Crocifisso</span>'),
    ('aria-label="Sezioni"', 'aria-label="Sections"'),
    ('>Lo studio</a>', '>The practice</a>'),
    ('>Il metodo<', '>The method<'),
    ('<a href="#montature">Montature</a>', '<a href="#montature">Frames</a>'),
    ('>Competenze</a>', '>Expertise</a>'),
    ('>Appuntamento</a>', '>Appointment</a>'),
    ('>Richiedere un appuntamento<', '>Request an appointment<'),
    ('aria-label="Apri il menu"', 'aria-label="Open menu"'),
    ("open ? 'Chiudi il menu' : 'Apri il menu'", "open ? 'Close menu' : 'Open menu'"),

    # hero
    ('Prima degli occhiali, l’ottico.', 'Before the glasses, the optician.'),
    ('aria-label="In breve"', 'aria-label="At a glance"'),
    ('Studio di ottica e contattologia, su appuntamento', 'Optics and contact lens practice, by appointment'),
    ('<span>Studio di ottica e contattologia</span>', '<span>Optics and contact lens practice</span>'),
    ('Si riceve esclusivamente su appuntamento.', 'Strictly by appointment.'),
    ('Si riceve su appuntamento', 'By appointment only'),
    ('Marco Rusca, ottico diplomato federale (maestro ottico), mette oltre quarant’anni di pratica al servizio di una cosa sola: la vista di chi si affida a lui. Una persona alla volta, con il tempo che una misurazione seria richiede.',
     'Marco Rusca, Swiss federally certified optician (master optician), puts more than forty years of practice at the service of one thing only: the eyesight of those who place their trust in him. One person at a time, with the time a serious measurement requires.'),
    ('<span class="also">oppure </span>', '<span class="also">or </span>'),

    # credentials strip
    ('Ottico diplomato federale (maestro ottico)</span>', 'Swiss federally certified optician (master optician)</span>'),
    ('Già docente al Centro Professionale Tecnico</span>', 'Former lecturer at the Centro Professionale Tecnico</span>'),
    ('Oltre quarant’anni di pratica</span>', 'More than forty years of practice</span>'),

    # the practice
    ('Uno studio, non un negozio.', 'A practice, not a shop.'),
    ('<b>anni di pratica</b>Una persona alla volta, su appuntamento, con il tempo che serve.',
     '<b>years of practice</b>One person at a time, by appointment, with all the time it takes.'),
    ('Qui non troverà scaffali di montature da provare in fretta, né il cartello con l’offerta del mese. Troverà uno studio che considera la vista una cosa troppo seria per essere trattata di corsa.',
     'Here you will not find shelves of frames to try on in a hurry, nor a sign announcing this month’s offer. You will find a practice that considers eyesight far too serious a matter to be rushed.'),
    ('La differenza tra un occhiale qualunque e un occhiale giusto non sta nella montatura. Sta nella precisione con cui la vista è stata misurata, nella scelta delle lenti in base a come vengono usate davvero, e nella cura con cui sono state centrate, montate e regolate. È un lavoro da ottico. Qui lo fa un maestro ottico, personalmente, dall’inizio alla fine.',
     'The difference between any pair of glasses and the right pair is not in the frame. It lies in how precisely the eyes were measured, in choosing lenses for how they will actually be used, and in the care with which they were centred, fitted and adjusted. That is an optician’s work. Here it is done by a master optician, personally, from start to finish.'),
    ('Schema di una lente che porta a fuoco un fascio di raggi paralleli', 'Diagram of a lens bringing a beam of parallel rays to a focus'),
    ('>fuoco</text>', '>focus</text>'),
    ('>distanza focale</text>', '>focal length</text>'),
    ('>raggi paralleli</text>', '>parallel rays</text>'),
    ('Una lente corregge solo se è calcolata e centrata per l’occhio che la porta. Pochi millimetri di errore nel montaggio bastano a vanificare un’ottima lente.',
     'A lens only corrects properly if it is calculated and centred for the eye that wears it. An error of a few millimetres in fitting is enough to undo an excellent lens.'),

    # comparison
    ('La differenza si vede.', 'You can see the difference.'),
    ('Trascini il cursore. A sinistra, come si vede con una correzione approssimativa; a destra, con una correzione misurata come si deve. Fino all’ultima riga.',
     'Drag the slider. On the left, how you see with an approximate correction; on the right, with a correction measured properly. Right down to the last line.'),
    ('Vedere bene non è questione di fortuna. È una misura fatta bene.', 'Seeing well is not a matter of luck. It is a measurement done well.'),
    ('>correzione approssimativa<', '>approximate correction<'),
    ('>correzione misurata<', '>measured correction<'),
    ('aria-label="Confronto: trascini per passare dalla visione sfocata a quella nitida"', 'aria-label="Comparison: drag to move from blurred to sharp vision"'),
    ('La tavola è una semplificazione. In studio la misura si fa con la strumentazione e il tempo che servono, non con un cursore.',
     'The chart is a simplification. In the practice, the measurement is made with the proper instruments and all the time it takes, not with a slider.'),

    # method
    ('Ogni visita segue lo stesso percorso, che si tratti di un primo paio di occhiali, di una correzione complessa o di lenti a contatto.',
     'Every visit follows the same path, whether it is a first pair of glasses, a complex prescription or contact lenses.'),
    ('<h3>Il colloquio</h3>', '<h3>The conversation</h3>'),
    ('Prima di qualsiasi misura, una conversazione: come usa gli occhi durante la giornata, a che distanza lavora, quanto tempo passa davanti a uno schermo, se guida di notte, se ha già portato lenti progressive o lenti a contatto. La correzione giusta dipende da queste risposte, e da altre ancora.',
     'Before any measurement, a conversation: how you use your eyes during the day, at what distance you work, how much time you spend in front of a screen, whether you drive at night, whether you have worn progressive lenses or contact lenses before. The right correction depends on these answers, and on others besides.'),
    ('<h3>L’esame della vista</h3>', '<h3>The eye examination</h3>'),
    ('Una refrazione completa, non un test rapido. Si misura tutto ciò che serve a definire la correzione esatta, con la calma necessaria per non lasciare nulla all’approssimazione.',
     'A complete refraction, not a quick test. Everything needed to define the exact correction is measured, calmly enough that nothing is left to approximation.'),
    ('<h3>La scelta di lenti e montatura</h3>', '<h3>Choosing lenses and frame</h3>'),
    ('Le lenti si scelgono in base alla correzione e all’uso reale; la montatura in base al viso e alla correzione che dovrà portare. È la regola opposta a quella di molti negozi: prima la vista, poi l’estetica. Fatte nell’ordine giusto, le due cose vanno d’accordo.',
     'Lenses are chosen according to the prescription and to real use; the frame according to the face and to the correction it will have to carry. It is the opposite of the rule in many shops: eyesight first, then looks. Done in the right order, the two go together.'),
    ('<h3>Il montaggio e la regolazione</h3>', '<h3>Fitting and adjustment</h3>'),
    ('Il maestro ottico esegue personalmente centratura, montaggio e regolazione finale. Un’ottima lente montata con qualche millimetro di errore smette di essere un’ottima lente.',
     'The master optician personally carries out centring, fitting and final adjustment. An excellent lens fitted a few millimetres off stops being an excellent lens.'),
    ('<h3>Il controllo</h3>', '<h3>The follow-up</h3>'),
    ('Dopo alcune settimane si verifica che l’adattamento sia completo e che tutto funzioni come previsto. Per le lenti a contatto i controlli fanno parte dell’applicazione e vengono programmati fin dall’inizio.',
     'After a few weeks we check that you have fully adapted and that everything works as it should. For contact lenses, check-ups are part of the fitting and are scheduled from the very start.'),

    # frames
    ('La montatura giusta esiste. Ma si sceglie dopo la misura.', 'The right frame exists. But it is chosen after the measurement.'),
    ('Ogni montatura impone dei vincoli alle lenti: dimensione, curvatura, distanza dagli occhi. Con una correzione forte, una lente grande diventa spessa e pesante; con una progressiva, un’altezza insufficiente compromette la zona di lettura. Per questo qui la montatura si sceglie insieme all’ottico, dopo l’esame e non prima.',
     'Every frame places constraints on the lenses: size, curvature, distance from the eyes. With a strong prescription, a large lens becomes thick and heavy; with a progressive, too little height compromises the reading area. That is why, here, the frame is chosen together with the optician, after the examination and not before.'),
    ('Le montature in studio sono una selezione, non un catalogo: si provano con calma, con la correzione già definita, e si regolano sul viso prima di ordinare le lenti.',
     'The frames in the practice are a selection, not a catalogue: they are tried on calmly, with the correction already defined, and adjusted to the face before the lenses are ordered.'),

    # Marco Rusca
    ('Ci sono ottici che vendono occhiali e ottici che si occupano di vista. Marco Rusca appartiene alla seconda categoria da oltre quarant’anni.',
     'There are opticians who sell glasses and opticians who take care of eyesight. Marco Rusca has belonged to the second kind for more than forty years.'),
    ('<span class="t">Segue ogni cliente in prima persona</span>', '<span class="t">Looks after every client personally</span>'),
    ('Esame, scelta, montaggio e regolazione: dall’inizio alla fine, senza passaggi di mano', 'Examination, choice, fitting and adjustment: from start to finish, never handed on to someone else'),
    ('Per anni ha insegnato il mestiere, oltre a esercitarlo', 'For many years he taught the craft as well as practising it'),
    ('Un’esperienza che non si improvvisa, soprattutto nei casi difficili', 'Experience that cannot be improvised, especially in difficult cases'),

    # expertise
    ('Di cosa si occupa lo studio', 'What the practice does'),
    ('Occhiali e lenti a contatto sono le due specializzazioni dello studio. In entrambi i casi l’obiettivo è lo stesso: una correzione esatta, portata con comfort, che duri nel tempo.',
     'Glasses and contact lenses are the practice’s two specialities. In both cases the aim is the same: an exact correction, worn in comfort, that lasts.'),
    ('<h3>Occhiali e lenti progressive</h3>', '<h3>Glasses and progressive lenses</h3>'),
    ('Lenti monofocali, progressive e da lavoro, calcolate sui suoi parametri e sull’uso che ne farà. Montature scelte per la correzione che devono portare, oltre che per il viso. Regolazioni e piccole riparazioni curate nello studio.',
     'Single-vision, progressive and occupational lenses, calculated on your measurements and on how you will use them. Frames chosen for the correction they must carry as well as for the face. Adjustments and small repairs handled in the practice.'),
    ('<h3>Lenti a contatto</h3>', '<h3>Contact lenses</h3>'),
    ('Applicazione di lenti a contatto dalla prima prova ai controlli periodici. Ogni lente viene scelta e adattata all’occhio che la porta, con l’istruzione necessaria per usarla bene e in sicurezza.',
     'Contact lens fitting from the first trial to regular check-ups. Every lens is chosen and adapted to the eye that wears it, with the guidance needed to use it well and safely.'),
    ('<h3>Correzioni difficili</h3>', '<h3>Complex prescriptions</h3>'),
    ('Astigmatismi elevati, differenze marcate tra i due occhi, presbiopie complesse, difficoltà di adattamento alle lenti progressive: i casi in cui l’esperienza fa la differenza, e che uno studio su appuntamento può seguire con il tempo necessario.',
     'High astigmatism, marked differences between the two eyes, complex presbyopia, difficulty adapting to progressive lenses: the cases where experience makes the difference, and which a practice working by appointment can follow with the time they need.'),

    # manifesto
    ('La scelta di chi tiene alla propria vista.', 'The choice for those who care about their eyesight.'),
    ('Questo studio è per chi porta gli occhiali dalla mattina alla sera e non si accontenta di vedere «abbastanza bene». Per chi ha una correzione difficile. Per chi ha già provato altrove senza trovarsi bene. Per chi preferisce affidarsi a una persona, non a un’insegna.',
     'This practice is for people who wear glasses from morning to night and are not content to see “well enough”. For those with a difficult prescription. For those who have tried elsewhere without success. For those who would rather trust a person than a shop sign.'),
    ('Non è lo studio adatto a chi cerca l’occhiale più economico o la promozione del momento: per quello esistono catene ben organizzate. Qui si viene per un’altra ragione.',
     'It is not the right practice for those looking for the cheapest glasses or the latest promotion: well-organised chains exist for that. People come here for a different reason.'),

    # appointment
    ('<dt>Telefono</dt>', '<dt>Phone</dt>'),
    ('<dt>Studio</dt>', '<dt>Practice</dt>'),
    ('<dt>Orari</dt>', '<dt>Opening hours</dt>'),
    ('Il modo più semplice è una telefonata. In alternativa, lasci i suoi recapiti: riceverà una chiamata per concordare data e ora.',
     'The simplest way is a phone call. Alternatively, leave your details and you will be called back to arrange a date and time.'),
    ('<label>Nome e cognome<', '<label>Full name<'),
    ('<label>Telefono<', '<label>Phone<'),
    ('<label>Email (facoltativa)<', '<label>Email (optional)<'),
    ('<label>Prima visita o già cliente<', '<label>First visit or existing client<'),
    ('<option>Prima visita</option>', '<option>First visit</option>'),
    ('<option>Già cliente</option>', '<option>Existing client</option>'),
    ('<label>Motivo della visita<', '<label>Reason for the visit<'),
    ('<option>Esame della vista e nuovi occhiali</option>', '<option>Eye examination and new glasses</option>'),
    ('<option>Lenti a contatto</option>', '<option>Contact lenses</option>'),
    ('<option>Controllo, regolazione o riparazione</option>', '<option>Check-up, adjustment or repair</option>'),
    ('<option>Una correzione che finora non ha funzionato</option>', '<option>A correction that has not worked so far</option>'),
    ('<option>Altro</option>', '<option>Other</option>'),
    ('<label>Note (facoltative)<', '<label>Notes (optional)<'),
    ('placeholder="Giorni e orari preferiti, o qualsiasi cosa sia utile sapere prima della visita"',
     'placeholder="Preferred days and times, or anything useful to know before the visit"'),
    ('>Inviare la richiesta<', '>Send request<'),
    ('La richiesta arriva per email allo studio tramite il servizio FormSubmit e serve solo a ricontattarla.', 'Your request reaches the practice by email via the FormSubmit service and is used only to contact you.'),

    # script messages and the email it composes
    ("'Per poterla richiamare servono nome e numero di telefono.'", "'To be called back, please give your name and phone number.'"),
    ("'Invio in corso…'", "'Sending…'"),
    ("'Grazie, la richiesta è stata inviata. Riceverà una chiamata al più presto per fissare l’appuntamento.'", "'Thank you, your request has been sent. You will receive a call shortly to arrange your appointment.'"),
    ("'Non è stato possibile inviare la richiesta da qui: si sta aprendo il suo programma di posta con il messaggio già compilato. In alternativa può chiamare lo 091 966 32 68.'", "'The request could not be sent from here: your email app is opening with the message already filled in. Alternatively, please call +41 91 966 32 68.'"),

    # footer
    ('Marco Rusca, ottico diplomato federale SHFA (maestro ottico)', 'Marco Rusca, Swiss federally certified optician, SHFA (master optician)'),
    ('Titolare e responsabile del sito:', 'Owner and person responsible for this website:'),

    # international phone format for visitors from abroad
    ('>091 966 32 68<', '>+41 91 966 32 68<'),
]
for a, b in T:
    en = rep(en, a, b)

os.makedirs(os.path.join(REPO, 'en'), exist_ok=True)
open(os.path.join(REPO, 'en', 'index.html'), 'w', encoding='utf-8').write(en)

# ---------------------------------------------------------------- robots (the sitemap is written by build_pages.py)
open(os.path.join(REPO, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
print('ok', len(it), len(en))
