### Processus de réconciliation avec OpenRefine

-Télécharger Openrefine et ouvrir via le terminal. On peut ajouter son CSV mais prend également d'autres formats. 
-Bonne pratique : dupliquer la colonne qu'on veut réconcilier avant de lancer le processus. Documenter toutes les décisions.

## Wikidata 
-Réconciliation Wikidata simple mais on valide à la main : possibilité de valider une réconciliation pour l'ensemble 
des cellules similaires.
-Possibilité d'ajouter des colonnes à partir de la colonne enrichie : permet d'ajouter automatiquement une colonne pour les
coordonnées géographiques par ex. 
-Proposition : on créé une table de relation entre les 55 thèmes de recherche et les entités wikidata (cf.sujet_TRHAA.csv) grâce à un identifiant.

## OpenAlex
-OpenAlex ne fournit pas d'endpoint pour Openrefine (seulement une API rest classique).
-Option 1 : reconciliation via wikidata
-Option 2 : transformer l'API OpenAlex en endpoint compatible (cf. Chatgpt)
    On peut utiliser Python + Flask par exemple. Le script permet de recevoir une requête de OpenRefine (/reconcile) 
    avec le nom à chercher, d'interroger OpenAlex (https://api.openalex.org/authors?search=...), de transformer le JSON reçu en format compatible OpenRefine et de retourner ce JSON à OpenRefine
    
Faire tourner test_OpenAlex.py

Lancer dans Bash : python3 openalex_reconcile.py

Dans Openrefine : reconcile/add custom service/url/http://localhost:5000/reconcile puis tester avec un nom d'auteur 

## Potentialités 
-D'autres enrichissements possibles en fonction du projet : 
    -Pleiade geocollider (sites historiques) - en fait il est plus ou moins déjà intégré dans Wikidata donc pas besoin
    -PeriodO (périodes historiques) - pas encore testé
-Python : il existe un module python (https://perma.cc/5UBV-J8RS) qui permet d'intégrer l'API wikidata et son SPARQL endpoint = ça vaut le coup d'essayer mais à mon avis c'est pas utile dans notre cas. 

## Question à poser : 
-est-ce qu'on souhaite ajouter une colonne avec les QID ? 
-attention pas de mise à jour possible si l'élément est modifié dans wikidata il faut supprimer la colonne et refaire
-est-ce qu'on cherche une précision plus grande sur les sujets en ajoutant un alignement Pleiade ou Periodo par ex ? 

## Thèmes de recherche : 

Archéologie et ethnologie du monde moderne et contemporain
Archéologie : méthodes et histoire
Architecture
Art (généralités)
Art de la civilisation japonaise
Art de la péninsule indienne et de l'Asie du Sud-Est
Art des jardins
Art du moyen âge occidental
Art du XIXe siècle
Art du XXe et XXIe siècle
Art et archéologie de l'Italie et de Rome
Art et archéologie de la Gaule préromaine et romaine
Art et archéologie de la Grèce
Art et archéologie Orient
Art paléochrétien, Art byzantin
Art de la renaissance et des temps modernes (XVe - XVIIIe siècles)
Arts de la scène
Arts décoratifs, objets mobilier, textiles
Arts et objets d'Afrique
Arts et objets d'Asie
Arts et objets d'Océanie
Arts et objets de la civilisation islamique
Arts et objets des Amériques
Arts graphiques
Chine-Corée (art de la civilisation chinoise)
Cinéma
Conservation, restauration
Culture matérielle
Décoration intérieure, design
Enluminure / Codicologie
Esthétique, Théorie de l'art
Ethnologie, anthropologie
Etudes du milieu, éco-système
Gender Studies
Géographie de l'art
Histoire culturelle / Transfert culturel
Histoire de l'histoire de l'art et de la critique d'art
Histoire des institutions artistiques, de l'enseignement artistique
Iconographie
Littérature artistique, sources, récits de voyage, guides
Marché de l'art, Provenance des oeuvres d'art
Médailles, monnaies
Mode et vêtement
Mosaïques
Muséologie et étude des collections (publiques et privées)
Musique
Nouveaux médias XX - XXIe siècles
Patrimoine monumental, sauvegarde et transformations
Peinture
Photographie
Préhistoire - Protohistoire
Science de l’image, Visual Studies
Sculpture
Sociologie de l'art, Histoire sociale de l'art
Techniques artistiques
Urbanisme

