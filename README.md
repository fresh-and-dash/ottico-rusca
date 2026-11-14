# Studio ottico Rusca — sito web

Sito dello Studio ottico Rusca: Marco Rusca, ottico diplomato federale (maestro ottico), Via Emilio Maraini 27, 6942 Savosa.

Indirizzo: **https://www.otticorusca.ch** (dominio registrato su GoDaddy).

Sito statico di una sola pagina: tutto il codice è in `index.html`. Non servono server, database né installazioni, e il sito non usa cookie né servizi esterni (anche i caratteri tipografici sono inclusi nel repository).

| File | A cosa serve |
| --- | --- |
| `index.html` | Il sito |
| `fonts/` | Caratteri Newsreader e Hanken Grotesk, con la loro licenza (SIL Open Font License) |
| `favicon.svg`, `apple-touch-icon.png` | Icona nella scheda del browser e sulla schermata Home del telefono |
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

## Modifiche frequenti (in `index.html`)

- **Email che riceve le richieste del modulo**: attributo `data-email` del modulo con `id="richiesta"`.
- **Telefono, email, indirizzo**: cercare `091 966 32 68`, `eye-marcorusca@hotmail.com`, `Via Emilio Maraini` (compaiono in più punti).
- **Ritratto di Marco Rusca**: sostituire il monogramma "MR" seguendo il commento nella sezione con `id="marco-rusca"`.
