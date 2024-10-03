# TP 1+2

## Exercice 1 : Chiffre de Vigenère

### Test 1 :

- Input : texte: `Bonjour`, clé: `CLE`
- Output : `e<4.<;6`

### Test 2 :

- Input : texte: `Je suis un chat rouge`, clé: `FRAISE`
- Output : `p8A=I/:R78S)/46IF5<:'`

### Test 3 :

- Input : texte: `La clé n'existe pas`, clé: ``
- Output : `/!\ La clé ne peut pas être vide /!\`

## Exercice 2 : Déchiffrement du chiffre de Vigenère

### Test 1 :

- Input : texte: `e<4.<;6`,  clé: `CLE`
- Output : `Bonjour`

### Test 2 :

- Input : texte: `p8A=I/:R78S)/46IF5<:'`, clé: `FRAISE`
- Output : `Je suis un chat rouge`

### Test 3 :

- Input : texte: `p8A=I/:R78S)/46IF5<:'`, clé: ``
- Output : `/!\ La clé ne peut pas être vide /!\`

## Exercice 3 : L'attaque de Kasiski

### Test :

- Input : fichier: `kasiski.txt`
- Output : `La taille de la clé est de 7`