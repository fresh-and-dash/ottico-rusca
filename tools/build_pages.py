"""Generate the three service pages (Italian and English) and the sitemap.
Header, menu, footer and styles are taken from each language's home page, so the pages always match it.
The texts of the pages are in PAGES below, in Italian and English.
Run after build_en.py:  python3 tools/build_en.py && python3 tools/build_pages.py
"""
import datetime, json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.otticorusca.ch/'
TODAY = datetime.date.today().isoformat()

PAGES = [
    {
        'key': 'esame',
        'it': {
            'slug': 'esame-della-vista', 'name': 'Esame della vista',
            'title': 'Esame della vista a Lugano | Studio ottico Rusca, Savosa',
            'desc': 'Esame della vista completo a Savosa, alle porte di Lugano, eseguito da Marco Rusca, ottico diplomato federale (maestro ottico). Su appuntamento, con il tempo che serve.',
            'h1': 'Esame della vista a Lugano',
            'lead': 'Una refrazione completa, eseguita di persona da Marco Rusca, ottico diplomato federale (maestro ottico). A Savosa, su appuntamento, con il tempo che una misura seria richiede.',
            'teaser': 'Una refrazione completa, non un test rapido.',
            'sections': [
                ('Che cosa si misura', None, [
                    ('p', 'Un esame della vista serio non si ferma alla tabella delle lettere. Serve a stabilire la correzione esatta: quella con cui vedrà bene, senza fatica, per tutta la giornata.'),
                    ('ul', ['la correzione per lontano e per vicino;', 'l’astigmatismo, con il suo grado e il suo asse;',
                            'l’equilibrio tra i due occhi, perché lavorino insieme senza sforzo;', 'la distanza a cui legge e lavora davvero, schermo compreso.']),
                ]),
                ('Come si svolge', None, [
                    ('steps', [('Il colloquio', 'Come usa gli occhi durante la giornata, a che distanza lavora, se guida di sera, quali occhiali o lenti a contatto porta oggi.'),
                               ('La misura', 'La refrazione vera e propria, un occhio alla volta e poi insieme, con la calma necessaria per non lasciare nulla all’approssimazione.'),
                               ('Il risultato', 'La correzione viene spiegata in parole chiare. Solo dopo si parla di lenti e montatura.')]),
                    ('photo', {'src': '../img/studio-strumenti', 'alt': 'Refrattometro automatico in primo piano e, sullo sfondo, la poltrona e l’unità d’esame con forottero e lampada a fessura',
                               'cap': 'Gli strumenti di misura dello studio, a Savosa.'}),
                ]),
                ('Quando conviene farlo', None, [
                    ('p', 'In assenza di disturbi, un controllo ogni due anni circa è una buona abitudine. Conviene anticiparlo se nota uno di questi segnali:'),
                    ('ul', ['fatica a leggere, o bisogno di allontanare il testo;', 'mal di testa o occhi stanchi a fine giornata;',
                            'difficoltà alla guida di sera;', 'vista meno nitida davanti allo schermo.']),
                    ('p', 'Dopo i quarant’anni la messa a fuoco da vicino cambia per tutti: è la presbiopia, e si corregge bene quando viene misurata con precisione.'),
                ]),
                ('Ottico o oculista?', None, [
                    ('p', 'L’oculista è un medico: diagnostica e cura le malattie dell’occhio. Per misurare la vista e correggerla con occhiali o lenti a contatto ci si può rivolgere direttamente a un ottico diplomato federale.'),
                    ('p', 'Le due figure sono complementari. Se durante l’esame emerge qualcosa che richiede un accertamento medico, lo studio La indirizza all’oculista.'),
                ]),
            ],
            'cta_h': 'Per un esame della vista a Savosa, Lugano', 'cta_p': 'Lo studio riceve una persona alla volta, solo su appuntamento.',
        },
        'en': {
            'slug': 'eye-examination', 'name': 'Eye examination',
            'title': 'Eye examination in Lugano | Studio ottico Rusca, Savosa',
            'desc': 'A complete eye examination in Savosa, on the edge of Lugano, carried out by Marco Rusca, Swiss federally certified optician (master optician). By appointment, with the time it takes.',
            'h1': 'Eye examination in Lugano',
            'lead': 'A complete refraction, carried out personally by Marco Rusca, Swiss federally certified optician (master optician). In Savosa, by appointment, with the time a serious measurement requires.',
            'teaser': 'A complete refraction, not a quick test.',
            'sections': [
                ('What is measured', None, [
                    ('p', 'A serious eye examination does not stop at the letter chart. Its purpose is to establish the exact correction: the one that lets you see well, without strain, all day long.'),
                    ('ul', ['the correction for distance and for near;', 'astigmatism, with its power and axis;',
                            'the balance between the two eyes, so that they work together without effort;', 'the distance at which you really read and work, screens included.']),
                ]),
                ('How it works', None, [
                    ('steps', [('The conversation', 'How you use your eyes during the day, at what distance you work, whether you drive at night, which glasses or contact lenses you wear today.'),
                               ('The measurement', 'The refraction itself, one eye at a time and then together, calmly enough that nothing is left to approximation.'),
                               ('The result', 'The correction is explained in plain words. Only then do we talk about lenses and frames.')]),
                    ('photo', {'src': '../../img/studio-strumenti', 'alt': 'Automatic refractometer in the foreground, with the examination chair and unit, phoropter and slit lamp behind',
                               'cap': 'The practice’s measuring instruments, in Savosa.'}),
                ]),
                ('When to have one', None, [
                    ('p', 'If you have no complaints, a check about every two years is a good habit. It is worth bringing it forward if you notice any of these signs:'),
                    ('ul', ['difficulty reading, or the need to hold text further away;', 'headaches or tired eyes at the end of the day;',
                            'trouble driving at night;', 'less sharp vision in front of a screen.']),
                    ('p', 'After forty, near focus changes for everyone: this is presbyopia, and it is corrected well when it is measured precisely.'),
                ]),
                ('Optician or ophthalmologist?', None, [
                    ('p', 'An ophthalmologist is a medical doctor who diagnoses and treats eye diseases. To have your eyesight measured and corrected with glasses or contact lenses, you can go directly to a federally certified optician.'),
                    ('p', 'The two are complementary. If the examination reveals anything that calls for a medical check, the practice refers you to an ophthalmologist.'),
                ]),
            ],
            'cta_h': 'For an eye examination in Savosa, Lugano', 'cta_p': 'The practice sees one person at a time, by appointment only.',
        },
    },
    {
        'key': 'progressive',
        'it': {
            'slug': 'lenti-progressive', 'name': 'Lenti progressive',
            'title': 'Lenti progressive a Lugano | Studio ottico Rusca, Savosa',
            'desc': 'Lenti progressive e da ufficio a Savosa, Lugano: da cosa dipende il risultato e cosa fare se non ci si abitua. Marco Rusca, ottico diplomato federale (maestro ottico).',
            'h1': 'Lenti progressive a Lugano',
            'lead': 'Una lente progressiva funziona quando misura, lente e montatura sono giuste insieme. È il lavoro in cui precisione ed esperienza contano di più.',
            'teaser': 'Da cosa dipende il risultato, e cosa fare se non ci si abitua.',
            'sections': [
                ('Come funzionano', None, [
                    ('p', 'Una lente progressiva riunisce in un solo occhiale la visione da lontano, quella intermedia e quella da vicino, senza linee visibili. La parte alta serve per guardare lontano, quella centrale per le distanze intermedie, quella bassa per leggere.'),
                    ('p', 'Ai lati la visione è meno nitida: è una caratteristica di tutte le lenti progressive, più o meno marcata secondo la qualità e il disegno della lente.'),
                ]),
                ('Da cosa dipende il risultato', None, [
                    ('p', 'La lente progressiva migliore in assoluto non esiste. Esiste quella giusta per una persona, e dipende da quattro cose:'),
                    ('ul', ['<strong>La correzione esatta.</strong> Un piccolo errore nella misura si sente molto più che con una lente semplice.',
                            '<strong>La centratura.</strong> Bastano pochi millimetri di scarto perché le zone della lente non cadano dove servono.',
                            '<strong>Il disegno della lente.</strong> Si sceglie in base all’uso reale: guida, ufficio, lettura, sport.',
                            '<strong>La montatura.</strong> Deve avere l’altezza sufficiente per contenere tutte le zone, e va regolata sul viso prima di prendere le misure.']),
                    ('photo', {'src': '../img/studio-montature', 'alt': 'La parete illuminata delle montature e il banco per la scelta e la regolazione',
                               'cap': 'La scelta della montatura, nello studio.'}),
                ]),
                ('Se non ci si abitua', 'adattamento', [
                    ('p', 'Abituarsi a un nuovo paio di lenti progressive richiede di solito da qualche giorno a un paio di settimane. Se dopo questo periodo restano fastidi, senso di instabilità o zone sfocate, quasi sempre la causa è una di queste:'),
                    ('ul', ['una correzione non del tutto esatta;', 'una centratura imprecisa;', 'una lente o una montatura non adatte all’uso che ne fa.']),
                    ('p', 'Nella maggior parte dei casi il problema si può individuare e correggere. Se porta lenti progressive con cui non si trova bene, anche fatte altrove, può chiedere un appuntamento per farle verificare.'),
                ]),
                ('Lenti da ufficio', None, [
                    ('p', 'Chi lavora molte ore allo schermo spesso si trova meglio con una lente pensata per le distanze brevi e intermedie: la zona per lo schermo e la scrivania è molto più ampia che in una lente progressiva normale.'),
                    ('p', 'Non è adatta alla guida: è un secondo occhiale, da affiancare a quello di tutti i giorni.'),
                ]),
            ],
            'cta_h': 'Per le sue lenti progressive, a Savosa, Lugano', 'cta_p': 'Si parte sempre dall’esame della vista. Lo studio riceve solo su appuntamento.',
        },
        'en': {
            'slug': 'progressive-lenses', 'name': 'Progressive lenses',
            'title': 'Progressive lenses in Lugano | Studio ottico Rusca, Savosa',
            'desc': 'Progressive and office lenses in Savosa, Lugano: what the result depends on and what to do if you cannot get used to them. Marco Rusca, Swiss federally certified optician (master optician).',
            'h1': 'Progressive lenses in Lugano',
            'lead': 'A progressive lens works when the measurement, the lens and the frame are right together. It is the work where precision and experience matter most.',
            'teaser': 'What the result depends on, and what to do if you cannot get used to them.',
            'sections': [
                ('How they work', None, [
                    ('p', 'A progressive lens brings distance, intermediate and near vision together in a single pair of glasses, with no visible lines. The upper part is for looking into the distance, the middle for intermediate distances, the lower part for reading.'),
                    ('p', 'At the sides, vision is less sharp: this is true of all progressive lenses, more or less noticeably depending on the quality and design of the lens.'),
                ]),
                ('What the result depends on', None, [
                    ('p', 'There is no such thing as the best progressive lens in absolute terms. There is the right one for a particular person, and it depends on four things:'),
                    ('ul', ['<strong>The exact correction.</strong> A small error in the measurement is felt far more than with a simple lens.',
                            '<strong>The centring.</strong> A deviation of a few millimetres is enough for the zones of the lens to fall in the wrong place.',
                            '<strong>The lens design.</strong> It is chosen according to real use: driving, office work, reading, sport.',
                            '<strong>The frame.</strong> It must be tall enough to hold all the zones, and it is adjusted to the face before the measurements are taken.']),
                    ('photo', {'src': '../../img/studio-montature', 'alt': 'The illuminated wall of frames and the counter for choosing and adjusting them',
                               'cap': 'Choosing the frame, at the practice.'}),
                ]),
                ('If you cannot get used to them', 'adapting', [
                    ('p', 'Getting used to a new pair of progressive lenses usually takes from a few days to a couple of weeks. If discomfort, a sense of unsteadiness or blurred areas remain after that, the cause is almost always one of these:'),
                    ('ul', ['a correction that is not quite exact;', 'imprecise centring;', 'a lens or frame that does not suit the way you use them.']),
                    ('p', 'In most cases the problem can be identified and corrected. If you wear progressive lenses you are not comfortable with, even ones made elsewhere, you can request an appointment to have them checked.'),
                ]),
                ('Office lenses', None, [
                    ('p', 'People who spend many hours at a screen are often more comfortable with a lens designed for short and intermediate distances: the area for the screen and the desk is much wider than in a standard progressive lens.'),
                    ('p', 'It is not suitable for driving: it is a second pair of glasses, to use alongside your everyday pair.'),
                ]),
            ],
            'cta_h': 'For your progressive lenses, in Savosa, Lugano', 'cta_p': 'It always starts with the eye examination. The practice sees clients by appointment only.',
        },
    },
    {
        'key': 'contatto',
        'it': {
            'slug': 'lenti-a-contatto', 'name': 'Lenti a contatto',
            'title': 'Lenti a contatto a Lugano | Studio ottico Rusca, Savosa',
            'desc': 'Lenti a contatto a Savosa, Lugano, con Marco Rusca, maestro ottico e autore di una guida sulle lenti a contatto: dalla prima prova ai controlli.',
            'h1': 'Lenti a contatto a Lugano',
            'lead': 'Una lente a contatto si sceglie sull’occhio, non su una scatola. Lo studio segue l’applicazione dalla prima prova ai controlli periodici.',
            'teaser': 'Dalla prima prova ai controlli periodici.',
            'sections': [
                ('Perché serve un’applicazione', None, [
                    ('p', 'Ogni occhio ha una forma, una curvatura e una lacrimazione proprie. La stessa lente può essere perfetta per una persona e scomoda per un’altra.'),
                    ('p', 'Per questo la lente viene scelta e provata sull’occhio che la porterà, e adattata finché vista e comfort sono quelli giusti.'),
                ]),
                ('Come si svolge', None, [
                    ('steps', [('Il colloquio e l’esame', 'Quando e quanto vuole portare le lenti, per quali attività, e la misura della vista.'),
                               ('La prova', 'La lente scelta viene provata sull’occhio: si valutano la vista, la posizione e il comfort.'),
                               ('L’istruzione', 'Come mettere e togliere le lenti, come pulirle e conservarle, quante ore portarle.'),
                               ('I controlli', 'Fanno parte dell’applicazione e vengono programmati fin dall’inizio.')]),
                ]),
                ('Quale lente', None, [
                    ('p', 'Esistono lenti morbide e rigide, giornaliere o a ricambio periodico, per miopia, ipermetropia, astigmatismo e presbiopia. Quale sia adatta dipende dall’occhio e dall’uso che ne farà: si stabilisce durante l’applicazione, non prima.'),
                ]),
                ('Perché i controlli contano', None, [
                    ('p', 'L’occhio cambia nel tempo, e una lente che andava bene può non essere più la più adatta. I controlli periodici servono a verificare che la vista sia sempre corretta e che la lente continui a essere ben tollerata.'),
                ]),
                ('Un libro sulle lenti a contatto', 'libro', [
                    ('book', {'src': '../img/libro-copertina.jpg', 'alt': 'Copertina del libro «Lenti a contatto. Guida pratica per tutti» di Marco Rusca',
                              'p': 'Marco Rusca è l’autore di <cite>Lenti a contatto. Guida pratica per tutti</cite>, una guida che risponde con parole semplici alle domande più frequenti: se sono migliori degli occhiali, da che età si possono portare, se ogni difetto visivo si può correggere con le lenti a contatto.',
                              'href': '../#libro', 'link': 'Vedere il libro'}),
                ]),
            ],
            'cta_h': 'Per le sue lenti a contatto, a Savosa, Lugano', 'cta_p': 'Per chi le porta già e per chi comincia. Lo studio riceve solo su appuntamento.',
        },
        'en': {
            'slug': 'contact-lenses', 'name': 'Contact lenses',
            'title': 'Contact lenses in Lugano | Studio ottico Rusca, Savosa',
            'desc': 'Contact lenses in Savosa, Lugano, with Marco Rusca, master optician and author of a guide to contact lenses: from the first trial to check-ups.',
            'h1': 'Contact lenses in Lugano',
            'lead': 'A contact lens is chosen on the eye, not from a box. The practice looks after the fitting from the first trial to regular check-ups.',
            'teaser': 'From the first trial to regular check-ups.',
            'sections': [
                ('Why a fitting is needed', None, [
                    ('p', 'Every eye has its own shape, curvature and tear film. The same lens can be perfect for one person and uncomfortable for another.'),
                    ('p', 'That is why the lens is chosen and tried on the eye that will wear it, and adapted until vision and comfort are right.'),
                ]),
                ('How it works', None, [
                    ('steps', [('Conversation and examination', 'When and how long you want to wear lenses, for which activities, and the measurement of your eyesight.'),
                               ('The trial', 'The chosen lens is tried on the eye: vision, position and comfort are assessed.'),
                               ('Instruction', 'How to insert and remove the lenses, how to clean and store them, how many hours to wear them.'),
                               ('Check-ups', 'They are part of the fitting and are scheduled from the start.')]),
                ]),
                ('Which lens', None, [
                    ('p', 'There are soft and rigid lenses, daily or regular-replacement, for short-sightedness, long-sightedness, astigmatism and presbyopia. Which one is suitable depends on the eye and on how you will use it: this is established during the fitting, not before.'),
                ]),
                ('Why check-ups matter', None, [
                    ('p', 'Eyes change over time, and a lens that used to be right may no longer be the most suitable. Regular check-ups verify that your vision is still properly corrected and that the lens is still well tolerated.'),
                ]),
                ('A book on contact lenses', 'libro', [
                    ('book', {'src': '../../img/libro-copertina.jpg', 'alt': 'Cover of the book «Lenti a contatto. Guida pratica per tutti» by Marco Rusca',
                              'p': 'Marco Rusca is the author of <cite>Lenti a contatto. Guida pratica per tutti</cite> (Contact lenses: a practical guide for everyone), which answers the most common questions in plain words: whether they are better than glasses, from what age they can be worn, whether every vision problem can be corrected with contact lenses.',
                              'href': '../#libro', 'link': 'See the book'}),
                ]),
            ],
            'cta_h': 'For your contact lenses, in Savosa, Lugano', 'cta_p': 'For those who already wear them and for those starting out. The practice sees clients by appointment only.',
        },
    },
]

UI = {
    'it': {'lang': 'it-CH', 'home': SITE, 'skip': 'Vai al contenuto', 'cta': 'Richiedere un appuntamento', 'phone': '091 966 32 68',
           'related': 'Altri servizi dello studio', 'open': 'Apri il menu', 'close': 'Chiudi il menu', 'og': 'og-image.png', 'locale': 'it_CH',
           'area': 'Canton Ticino', 'crumb_label': 'Percorso', 'host_t': 'La riceve Marco Rusca',
           'host_d': 'ottico diplomato federale (maestro ottico), di persona'},
    'en': {'lang': 'en', 'home': SITE + 'en/', 'skip': 'Skip to content', 'cta': 'Request an appointment', 'phone': '+41 91 966 32 68',
           'related': 'Other services', 'open': 'Open menu', 'close': 'Close menu', 'og': 'og-image-en.png', 'locale': 'en_GB',
           'area': 'Canton of Ticino', 'crumb_label': 'Breadcrumb', 'host_t': 'Marco Rusca will see you',
           'host_d': 'Swiss federally certified optician (master optician), in person'},
}

PAGE_CSS = '''
  /* ---------- Service pages ---------- */
  .page-hero { position: relative; background: var(--ink); color: var(--paper); padding: clamp(8.5rem, 17vw, 11.5rem) 0 clamp(3.2rem, 7vw, 5.5rem); overflow: hidden; isolation: isolate; }
  .page-hero::before { content: ""; position: absolute; inset: 0; z-index: -2; background: linear-gradient(180deg, #08182D 0%, var(--ink) 60%, var(--ink-2) 100%); }
  .page-hero .glow { position: absolute; z-index: -1; right: -10vw; top: -16vw; width: 48vw; height: 48vw; border-radius: 50%; filter: blur(60px); opacity: .5; pointer-events: none; background: radial-gradient(circle, rgba(127,182,234,.3), transparent 62%); }
  .page-hero .deco { position: absolute; z-index: -1; right: max(1.25rem, calc((100% - 74rem) / 2)); bottom: clamp(2rem, 6vw, 4.5rem); width: min(30vw, 24rem); opacity: .5; pointer-events: none; }
  @media (max-width: 60em) { .page-hero .deco { display: none; } }
  .crumb { font-family: var(--sans); font-size: .85rem; color: var(--mist-2); }
  .crumb a { color: inherit; text-decoration: none; }
  .crumb a:hover { color: var(--paper); }
  .crumb span { margin-inline: .5rem; opacity: .6; }
  .page-hero h1 { margin-top: 1.2rem; font-size: clamp(2.6rem, 1.5rem + 4.6vw, 5.2rem); line-height: 1.02; font-weight: 400; letter-spacing: -.02em; font-variation-settings: "opsz" 72; max-width: 14ch; text-wrap: balance; }
  .page-hero .lead { margin-top: 1.6rem; font-size: var(--step-1); line-height: 1.45; max-width: 50ch; color: rgba(244,247,250,.88); font-variation-settings: "opsz" 20; }
  .page-hero .actions { margin-top: 2rem; display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.75rem; }
  .page-hero .actions .phone, .cta-band .phone { font-family: var(--sans); text-decoration: none; }
  .page-hero .actions .phone { color: rgba(244,247,250,.88); }
  .page-hero .actions .phone:hover, .cta-band .phone:hover { text-decoration: underline; text-underline-offset: .18em; }
  .page-body .section { padding-block: clamp(3.2rem, 7vw, 5.5rem) 0; }
  .page-body .section:last-child { padding-bottom: clamp(4.5rem, 10vw, 8rem); }
  .page-body .prose ul { margin: 1.1em 0 0; padding-left: 1.15rem; max-width: 58ch; }
  .page-body .prose ul + p { margin-top: 1.1em; }
  .page-body .prose li + li { margin-top: .45rem; }
  .page-body .prose li::marker { color: var(--blue); }
  .page-body .steps { margin-top: 0; }
  .page-body .steps li { padding-block: 1.5rem; }
  .page-body .prose ul.titles { margin-top: 0; padding-left: 0; max-width: 60ch; }
  .page-body .titles a { text-decoration: none; }
  .page-body .titles a:hover { text-decoration: underline; text-underline-offset: .18em; }
  .page-photo { margin: 2rem 0 0; max-width: 62ch; }
  .page-photo img { display: block; width: 100%; height: auto; border-radius: 18px; box-shadow: 0 30px 60px -45px rgba(10,28,51,.65); }
  .page-photo figcaption { margin-top: .8rem; }
  .page-book { display: grid; grid-template-columns: 6.5rem 1fr; gap: 1.4rem; align-items: center; max-width: 62ch; }
  @media (min-width: 40em) { .page-book { grid-template-columns: 8.5rem 1fr; gap: 2.2rem; } }
  .page-book img { display: block; width: 100%; height: auto; border-radius: 2px 4px 4px 2px; transform: perspective(700px) rotateY(-14deg); transform-origin: left center; box-shadow: 0 24px 36px -22px rgba(10,28,51,.65), 0 0 0 1px rgba(10,28,51,.08); }
  .page-book cite { font-style: italic; }
  .page-body .prose .page-book p { margin: 0; }
  .page-book .more { margin-top: .8rem; }
  .cta-band { background: var(--paper-2); padding-block: clamp(4rem, 8vw, 6.5rem); }
  .cta-band h2 { font-size: var(--step-3); line-height: 1.08; font-weight: 400; letter-spacing: -0.015em; font-variation-settings: "opsz" 48; max-width: 18ch; text-wrap: balance; }
  .cta-band .actions { margin-top: 1.6rem; display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.75rem; }
  .cta-band .phone { color: var(--ink-2); }
'''

DECO = ('<svg class="deco" viewBox="0 0 640 240" fill="none" stroke="url(#brass)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<ellipse cx="160" cy="120" rx="118" ry="84" fill="url(#lensfill)"/><ellipse cx="480" cy="120" rx="118" ry="84" fill="url(#lensfill)"/>'
        '<path d="M275 100 C 298 66, 342 66, 365 100"/><path d="M43 108 C 26 96, 8 100, 5 126"/><path d="M597 108 C 614 96, 632 100, 635 126"/></svg>')


def deeper(html):
    """Rewrite relative URLs for a page one directory below the language home."""
    def attr(m):
        name, url = m.group(1), m.group(2)
        if re.match(r'(https?:|mailto:|tel:|data:|/)', url):
            return m.group(0)
        if url.startswith('#'):
            return f'{name}="../{url}"'
        if url == './':
            return f'{name}="../"'
        return f'{name}="../{url}"'
    html = re.sub(r'\b(href|src)="([^"]*)"', attr, html)
    return re.sub(r'url\("(?!data:|https?:|/)([^"]+)"\)', lambda m: f'url("../{m.group(1)}")', html)


def grab(html, pattern, what):
    m = re.search(pattern, html, re.S)
    assert m, what
    return m.group(0)


def body_html(blocks):
    out = []
    for kind, val in blocks:
        if kind == 'p':
            out.append(f'        <p class="reveal">{val}</p>')
        elif kind == 'ul':
            out.append('        <ul class="reveal">' + ''.join(f'<li>{x}</li>' for x in val) + '</ul>')
        elif kind == 'photo':
            out.append(f'        <figure class="page-photo reveal"><img src="{val["src"]}-960.jpg" srcset="{val["src"]}-960.jpg 960w, {val["src"]}-1600.jpg 1600w" '
                       f'sizes="(min-width: 60em) 52vw, 100vw" width="1600" height="1200" loading="lazy" decoding="async" alt="{val["alt"]}">'
                       f'<figcaption class="small">{val["cap"]}</figcaption></figure>')
        elif kind == 'book':
            out.append(f'        <div class="page-book reveal"><img src="{val["src"]}" width="800" height="1137" loading="lazy" decoding="async" alt="{val["alt"]}">'
                       f'<div><p>{val["p"]}</p><a class="more" href="{val["href"]}">{val["link"]}</a></div></div>')
        elif kind == 'steps':
            out.append('        <ol class="steps">' + ''.join(
                f'<li class="reveal"><span class="n">{i}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(val, 1)) + '</ol>')
    return '\n'.join(out)


def build(lang, page):
    ui, c = UI[lang], page[lang]
    other = 'en' if lang == 'it' else 'it'
    home = open(os.path.join(REPO, 'index.html' if lang == 'it' else 'en/index.html'), encoding='utf-8').read()
    url = ui['home'] + c['slug'] + '/'
    alt = {l: UI[l]['home'] + page[l]['slug'] + '/' for l in ('it', 'en')}

    styles = deeper(''.join(re.findall(r'<style>.*?</style>', home, re.S)))
    cut = styles.rindex('</style>')
    styles = styles[:cut] + PAGE_CSS + styles[cut:]
    defs = grab(home, r'<svg width="0" height="0" style="position:absolute" aria-hidden="true">.*?</svg>', 'defs')
    header = deeper(grab(home, r'<header class="site-head" id="top">.*?</header>', 'header'))
    menu = deeper(grab(home, r'<div class="menu" id="menu">.*?</div>', 'menu'))
    footer = deeper(grab(home, r'<footer class="site-foot">.*?</footer>', 'footer'))

    # language switch points at the same page in the other language
    for block_name in ('header', 'menu'):
        block = header if block_name == 'header' else menu
        if lang == 'it':
            block = block.replace('href="../" lang="it"', 'href="./" lang="it"')
            assert 'href="../en/" lang="en"' in block
            block = block.replace('href="../en/" lang="en"', f'href="../en/{page["en"]["slug"]}/" lang="en"')
        else:
            block = block.replace('href="../" lang="en"', 'href="./" lang="en"')
            assert 'href="../../" lang="it"' in block
            block = block.replace('href="../../" lang="it"', f'href="../../{page["it"]["slug"]}/" lang="it"')
        if block_name == 'header':
            header = block
        else:
            menu = block

    sections = []
    for title, anchor, blocks in c['sections']:
        ident = f' id="{anchor}"' if anchor else ''
        sections.append(f'  <section class="section"{ident}>\n    <div class="wrap split">\n      <h2 class="reveal">{title}</h2>\n      <div class="prose">\n{body_html(blocks)}\n      </div>\n    </div>\n  </section>')
    others = [p for p in PAGES if p is not page]
    related = ''.join(f'<li class="reveal" style="--i:{i}"><a class="t" href="../{o[lang]["slug"]}/">{o[lang]["name"]}</a><span class="small">{o[lang]["teaser"]}</span></li>' for i, o in enumerate(others))
    sections.append(f'  <section class="section">\n    <div class="wrap split">\n      <h2 class="reveal">{ui["related"]}</h2>\n      <div class="prose">\n        <ul class="titles">{related}</ul>\n      </div>\n    </div>\n  </section>')

    studio = {'@type': 'Optician', '@id': SITE + '#studio', 'name': 'Studio ottico Rusca', 'url': SITE, 'telephone': '+41919663268',
              'address': {'@type': 'PostalAddress', 'streetAddress': 'Via Emilio Maraini 27', 'postalCode': '6942', 'addressLocality': 'Savosa', 'addressRegion': 'TI', 'addressCountry': 'CH'}}
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': url, 'url': url, 'name': c['title'], 'description': c['desc'], 'inLanguage': ui['lang'],
         'isPartOf': {'@id': SITE + '#website'}, 'about': {'@id': SITE + '#studio'}},
        {'@type': 'Service', 'name': c['name'], 'serviceType': c['name'], 'description': c['desc'], 'provider': studio,
         'areaServed': [{'@type': 'City', 'name': 'Savosa'}, {'@type': 'City', 'name': 'Lugano'}, {'@type': 'AdministrativeArea', 'name': ui['area']}]},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Studio ottico Rusca', 'item': ui['home']},
            {'@type': 'ListItem', 'position': 2, 'name': c['name'], 'item': url}]},
    ]}

    html = f'''<!DOCTYPE html>
<html lang="{ui['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['title']}</title>
<meta name="description" content="{c['desc']}">
<meta name="theme-color" content="#0A1C33">
<meta property="og:title" content="{c['title']}">
<meta property="og:description" content="{c['desc']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Studio ottico Rusca">
<meta property="og:image" content="{SITE}{ui['og']}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="{ui['locale']}">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="it" href="{alt['it']}">
<link rel="alternate" hreflang="en" href="{alt['en']}">
<link rel="alternate" hreflang="x-default" href="{alt['it']}">
<link rel="icon" href="{'../' if lang == 'it' else '../../'}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{'../' if lang == 'it' else '../../'}apple-touch-icon.png">
<link rel="preload" href="{'../' if lang == 'it' else '../../'}fonts/newsreader.woff2" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.className += ' js';</script>

<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>

{styles}
</head>
<body class="page">
<a class="skip" href="#contenuto">{ui['skip']}</a>

{defs}

{header}

{menu}

<main id="contenuto">

  <section class="page-hero">
    <div class="glow" aria-hidden="true"></div>
    {DECO}
    <div class="wrap">
      <nav class="crumb" aria-label="{ui['crumb_label']}"><a href="../">Studio ottico Rusca</a><span aria-hidden="true">/</span>{c['name']}</nav>
      <h1>{c['h1']}</h1>
      <p class="lead">{c['lead']}</p>
      <div class="actions">
        <a class="btn" href="../#appuntamento">{ui['cta']}</a>
        <a class="phone" href="tel:+41919663268">{ui['phone']}</a>
      </div>
    </div>
  </section>

  <div class="page-body">
{chr(10).join(sections)}
  </div>

  <section class="cta-band">
    <div class="wrap split">
      <div>
        <h2 class="reveal">{c['cta_h']}</h2>
        <div class="host reveal"><img class="host-img" src="{'../' if lang == 'it' else '../../'}img/marco-rusca-avatar-240.jpg" width="240" height="240" alt="" loading="lazy" decoding="async"><p><b>{ui['host_t']}</b><span>{ui['host_d']}</span></p></div>
      </div>
      <div class="prose">
        <p class="lead reveal">{c['cta_p']}</p>
        <div class="actions reveal">
          <a class="btn" href="../#appuntamento">{ui['cta']}</a>
          <a class="phone" href="tel:+41919663268">{ui['phone']}</a>
        </div>
      </div>
    </div>
  </section>

</main>

{footer}

<script>
(function () {{
  var head = document.querySelector('.site-head');
  var onScrollHead = function () {{ head.classList.toggle('is-scrolled', window.scrollY > 24); }};
  onScrollHead(); window.addEventListener('scroll', onScrollHead, {{ passive: true }});
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  var setMenu = function (open) {{ document.body.classList.toggle('menu-open', open); burger.setAttribute('aria-expanded', open ? 'true' : 'false'); burger.setAttribute('aria-label', open ? '{ui['close']}' : '{ui['open']}'); }};
  burger.addEventListener('click', function () {{ setMenu(!document.body.classList.contains('menu-open')); }});
  menu.querySelectorAll('a').forEach(function (a) {{ a.addEventListener('click', function () {{ setMenu(false); }}); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') setMenu(false); }});
  document.getElementById('anno').textContent = new Date().getFullYear();
  var io = new IntersectionObserver(function (entries) {{ entries.forEach(function (en) {{ if (en.isIntersecting) {{ en.target.classList.add('is-in'); io.unobserve(en.target); }} }}); }}, {{ threshold: 0.12, rootMargin: '0px 0px -6% 0px' }});
  document.querySelectorAll('.reveal').forEach(function (el) {{ io.observe(el); }});
}})();
</script>
</body>
</html>
'''
    out_dir = os.path.join(REPO, c['slug'] if lang == 'it' else os.path.join('en', c['slug']))
    os.makedirs(out_dir, exist_ok=True)
    open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(html)
    return url


urls = []
for page in PAGES:
    urls.append((build('it', page), build('en', page)))

pairs = [(SITE, SITE + 'en/')] + urls
HOME_IMAGES = ['img/studio-strumenti-1600.jpg', 'img/studio-sala-esame-1200.jpg', 'img/studio-montature-1600.jpg',
               'img/studio-attesa-1600.jpg', 'img/libro-copertina.jpg',
               'img/montature/silhouette-1-1200.jpg', 'img/montature/porsche-design-1-1200.jpg', 'img/montature/furla-1-1200.jpg', 'img/montature/lamarca-1-1200.jpg', 'img/montature/titanflex-1-1200.jpg', 'img/montature/airlight-1-1200.jpg', 'img/montature/trevi-coliseum-1-1200.jpg', 'img/montature/chopard-1-1200.jpg', 'img/montature/ic-berlin-1-1200.jpg', 'img/montature/police-1-1200.jpg', 'img/montature/humphreys-1-1200.jpg', 'img/montature/ray-ban-1-1200.jpg', 'img/montature/marius-morel-1-1200.jpg', 'img/montature/gambini-1-1200.jpg', 'img/montature/dolce-gabbana-1-1200.jpg', 'img/montature/alberto-puccini-1-1200.jpg']
PAGE_IMAGES = {'esame-della-vista': ['img/studio-strumenti-1600.jpg'], 'eye-examination': ['img/studio-strumenti-1600.jpg'],
               'lenti-progressive': ['img/studio-montature-1600.jpg'], 'progressive-lenses': ['img/studio-montature-1600.jpg'],
               'lenti-a-contatto': ['img/libro-copertina.jpg'], 'contact-lenses': ['img/libro-copertina.jpg']}
entries = []
for it_url, en_url in pairs:
    for loc in (it_url, en_url):
        slug = loc.rstrip('/').rsplit('/', 1)[-1]
        imgs = HOME_IMAGES if loc in (SITE, SITE + 'en/') else PAGE_IMAGES.get(slug, [])
        img_xml = ''.join(f'    <image:image><image:loc>{SITE}{i}</image:loc></image:image>\n' for i in imgs)
        entries.append(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n'
                       f'    <xhtml:link rel="alternate" hreflang="it" href="{it_url}"/>\n    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>\n'
                       f'{img_xml}  </url>')
open(os.path.join(REPO, 'sitemap.xml'), 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
    + '\n'.join(entries) + '\n</urlset>\n')
print('pages built:', len(urls) * 2, '| sitemap urls:', len(entries))
