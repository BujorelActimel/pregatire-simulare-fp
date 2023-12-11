## Aplicație pentru Confectționarea de Mobilă

### Descriere
Aplicația a fost creată pentru o firmă specializată în confecționarea mobilei. Acest program, cu o interfață tip consolă, dispune de următoarele funcționalități:

1. **Cautarea de Mobilier pe Baza Tipului**
   - Utilizatorul introduce un șir de caractere, iar aplicația afișează toate obiectele de mobilier din stoc care au tipul introdus de utilizator. (2p)

2. **Cumpărarea Pieselor de Mobilier**
   - Utilizatorul introduce codul obiectului și numărul de piese dorite.
   - Aplicația afișează numele obiectului, prețul total și stocul rămas.
   - Stocul este actualizat și în fișierul de date. (3p)

### Structura Fișierului de Date
Obiectele de mobilier sunt stocate într-un fișier .txt, fiecare obiect pe o linie separată, iar atributele sunt separate prin punct.

Formatul obiectelor:
`<cod: string>, <tip obiect: string>, <nume obiect: string>, <stock disponibil: int>, <pret: float>`

Exemplu: CI10, corp iluminat, Lampa Venetia, 12, 500


### Observații și Punctaje

- **Punctaje**:
  - 1p: Implementare de bază
  - 1p: Arhitectură, proporțional cu funcționalitățile implementate corect.
  - 1p: Stil - Nume de variabile/metode sugestive, convenții de denumire consecvente, ascunderea atributelor, getter/setter, comentarii
  - 2p: Specificații și teste, proporțional cu funcționalitățile implementate.

- **Observații**:
  - Nu se acceptă aplicații care nu folosesc clase/obiecte.
  - În cazul în care datele nu sunt citite/scrise din fișier, punctajul se reduce la jumătate pentru fiecare funcționalitate.
  - Nu se pot folosi proiecte existente fără ajutor exterior.
