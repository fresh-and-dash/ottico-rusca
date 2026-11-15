# Studio ottico Rusca — sito web

Sito dello Studio ottico Rusca: Marco Rusca, ottico diplomato federale (maestro ottico), Via Emilio Maraini 27, 6942 Savosa.

Indirizzo: **https://www.otticorusca.ch** (dominio registrato su GoDaddy). Versione inglese: **https://www.otticorusca.ch/en/**.

Sito statico in italiano e in inglese: la pagina principale e tre pagine dedicate a esame della vista, lenti progressive e lenti a contatto. Non servono server, database né installazioni, e il sito non usa cookie né servizi esterni (anche i caratteri tipografici sono inclusi nel repository).

| File | A cosa serve |
| --- | --- |
| `index.html` | Il sito in italiano (lingua principale) |
| `en/index.html` | Il sito in inglese |
| `esame-della-vista/`, `lenti-progressive/`, `lenti-a-contatto/` | Pagine dedicate ai servizi (in inglese sotto `en/`) |
| `tools/` | Programmi che generano la versione inglese e le pagine dei servizi |
| `fonts/` | Caratteri Newsreader e Hanken Grotesk, con la loro licenza (SIL Open Font License) |
| `favicon.svg`, `apple-touch-icon.png` | Icona nella scheda del browser e sulla schermata Home del telefono |
| `og-image.png`, `og-image-en.png` | Anteprima mostrata quando il link viene condiviso (WhatsApp, social) |
| `sitemap.xml`, `robots.txt` | Aiutano Google a trovare e collegare le due lingue |
| `.nojekyll` | Dice a GitHub Pages di pubblicare i file così come sono |

## Pubblicazione con GitHub Pages

**Settings → Pages** → *Build and deployment* → **Deploy from a branch** → `main` e `/ (root)` → **Save**. Dopo qualche minuto l'indirizzo del sito compare in cima alla stessa pagina.

Per aggiornare il sito: aprire `index.html` qui su GitHub, icona della matita, modificare, **Commit changes**. Il sito si aggiorna da solo.

### Dominio `www.otticorusca.ch`

1. Il dominio è indicato nel file `CNAME` (`www.otticorusca.ch`) e compare in **Settings → Pages → Custom domain**.
2. Nel DNS di GoDaddy:
   - `www` → record **CNAME** verso `fresh-and-dash.github.io`
   - dominio senza `www` → quattro record **A**: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Quando GitHub conferma il dominio, attivare **Enforce HTTPS**. Le modifiche DNS possono richiedere fino a 24 ore.

## Portarlo in Lovable

Scaricare il repository come ZIP (**Code → Download ZIP**), poi nella dashboard di Lovable: **+** nel campo del prompt → **Import project to Lovable** → **Upload code** → caricare lo ZIP → **Start import**. Lovable ricostruisce il sito con la propria tecnologia: confrontare il risultato con l'originale, soprattutto gli effetti, e chiedere a Lovable di correggere le differenze.

## Modifiche frequenti

Solo `index.html` (la pagina italiana) si modifica a mano. La pagina inglese e le pagine dei servizi vengono generate, quindi una modifica fatta direttamente lì va persa alla generazione successiva.

1. Modificare il testo in `index.html`.
2. Se il testo esiste anche in inglese, aggiornare la coppia italiano/inglese nell'elenco `T` di `tools/build_en.py`.
3. I testi delle pagine dei servizi sono in `PAGES`, dentro `tools/build_pages.py`, in italiano e in inglese.
4. Rigenerare: `python3 tools/build_en.py && python3 tools/build_pages.py`, poi pubblicare le modifiche.

Dove si trovano le cose in `index.html`:

- **Email che riceve le richieste del modulo**: attributo `data-email` del modulo con `id="richiesta"`.
- **Telefono, email, indirizzo**: cercare `091 966 32 68`, `eye-marcorusca@hotmail.com`, `Via Emilio Maraini` (compaiono in più punti).
- **Ritratto di Marco Rusca**: sostituire il monogramma "MR" seguendo il commento nella sezione con `id="marco-rusca"`.
- **Recensioni Google**: la sezione con `id="recensioni"` si riempie da sola con i dati di Google (media, numero di recensioni e fino a tre recensioni da 4 o 5 stelle). Resta nascosta finché nell'attributo `data-key` non c'è una chiave API di Google Places (New), limitata al sito www.otticorusca.ch; la stessa chiave va messa anche in `en/index.html`, oppure basta rigenerare la pagina inglese.
- **Domande frequenti**: sezione con `id="domande"`; le stesse domande sono ripetute nei dati strutturati in cima alla pagina.
