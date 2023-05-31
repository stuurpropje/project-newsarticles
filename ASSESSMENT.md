# Assessment

## Opmerkelijke projectonderdelen

### 1. Een hele grote dataset toepassen

Een van de eerste struikelblokken binnen mijn project was het verwerken van all-the-news-2-1.csv.
Dit was omdat deze dusdanig groot is dat Jupyter Notebook het bestand niet in wilt laden bijvoorbeeld. Maar het heeft wel geresulteerd in andere problemen die ik heb kunnen oplossen.

### 3. Multithreading van een functie

Het eerste probleem bij een grote dataset was dat het allemaal *heel erg* lang duurt om functies toe te passen.
Dit heb ik opgelost binnen de lemmatizer module door gebruik te maken van de ProcessPoolExecutor module.

Origineel had ik een module genaamd modin geimporteerd die multithreading inherent zou toepassen op dataframe modificaties. Ik was er echter achter gekomen dat deze module vrij waardeloos was. Een [issue gepost op GitHub](https://github.com/modin-project/modin/issues/98) geeft aan dat het inladen van een .csv bestand van 3 GB waar een modificatie op wordt toegepast al snel 110 GB aan RAM vereist.
De ontwikkelaars van de module zeggen dat dit 'gewoon is zoals het ongeveer hoort te werken'.

Door zelf binnen de lemmatization module de dataframe modificaties zelfstandig te verdelen over de cores heb ik ervoor gezorgd dat mijn modificatie ook parallel uitgevoerd kon worden, zonder 110 GB aan RAM nodig te hebben. Het was hiermee mogelijk om lemmatizatie toe te passen op de gehele dataset in 55 uur in plaats van ~260 uur.

### 2. Timer tijdens een functie in de terminal

Naast het multithreading van hetzelfde proces, heb ik ook uitgezocht hoe ik twee verschillende processen kon multithreaden. 
Hiermee was het mogelijk om een opdracht die lang duurt (vectorisatie) te klokken.
Zo kon een functie en een timer tegelijkertijd worden getoond.

### 4. De mogelijkheid tot het onderbroken uitvoeren van de lemmatizer

Alle code die we tot nu hebben geschreven zou niet onderbroken uitgevoerd kunnen worden.
De lemmatizer module is hier uniek in dat naast multitheading het ook mogelijk is om de module te stoppen (door de gebruiker of door een crash) en weer te runnen waar het weer doorgaat waar het was gebleven. De module onthoudt namelijk waar het was gebleven.

### 5. Het maken van een functionele widget

Het eindresultaat van dit project is de implementatie van een widget die een primitieve zoekmachine nabootst. Ik ben erg trots op de recommendation_widget omdat het gebruik maakt libraries en andere implementatie om een 'front end'.

## Keuzes

### 1. Het enkel houden bij topic modeling

Aanvankelijk was mijn projectontwerp om topic modeling te doen, en vervolgens een sentiment analyse toe te passen.
Door topic modeling wilde ik alle artikelen selecteren die over bepaalde bedrijven gingen om een sentiment analyse uit te voeren over deze bedrijven.
Op het resultaat hiervan wilde ik een meervoudige lineare regressie toepassen om een rangschikking te maken en deze vergelijken met hun beurskoers.

Echter heb ik de sentiment analyse niet uitgevoerd. De implementatie van de bovenstaande opmerkelijke projectonderdelen hebben veel tijd gekost waardoor het niet mogelijk was om nog een nieuw onderdeel te maken.
Het was misschien niet zo handig om te veel hooi op de vork te nemen, maar door de opbouw van mijn project is het niet een probleem geweest omdat het in feite drie opzichzelfstaande onderdelen zijn.

Het is beter om dit project enkel bij topic modeling te houden omdat het hiermee mogelijk was om de code hiervan netter en beter te maken.
Wanneer ik ook een sentiment analyse zou hebben uitgevoerd, zouden allebei de onderdelen waarschijnlijk slordig zijn door een tekort aan tijd. 

### 2. Het nemen van een steekproef in plaats van het gebruik van de gehele dataset

Het toepassen van een steekproef in plaats van het modificeren van alle data zou heel erg veel tijd hebben gekost. Zelfs met de multithreading zou lemmitizatie bijna 60 uur hebben gekost. Vectorisatie, lda fitting en distributienormalisatie zouden rond de 15 uur kosten op de gehele dataset.

Dit is allemaal veel tijd die niet veel bieden. Een steekproef toont namelijk nog steeds de implementatie, en zorgt ervoor dat correcties gemakkelijk gemaakt kunnen worden in plaats van dat meerdere uren nodig zijn om een enkele functie te draaien.

De nieuwe oplossing is beter omdat de schaal van het project in weze hetzelfde is gebleven, maar gemakkelijker te debuggen.
Per ongeluk verwijderen van bestanden zoals de gevectoriseerde data kost hierdoor enkel één uur, in plaats van 10.
Het heeft meer flexibiliteit toegestaan in het verbeteren van mijn eigen code.
Wanneer ik een 'final' implementatie zou maken waar alle bugs zijn opgelost, was het prima om de volledige dataset uit all-the-news-2-1.csv te gebruiken.
