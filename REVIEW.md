# Uitwerking van code review

Sabrina, Duco

    Wat is het tegengekomen probleem?
    Hoe zou je dit beter kunnen maken?
    Wat voor afweging maak je? Vaak is een keuze voor iets ook een keuze tegen iets anders.
    Illustreer met enkele voorbeelden.

## 1. Herhalend stopwords.words("english") binnen remove_stopwords() in de data_cleaning module aanroepen

De functie remove_stopwords() haalt meerdere keren de lijst met Engelse stopwoorden op door stopwords.words("english") aan te roepen. 
Dit is overbodig en onnodig, omdat deze functie elke keer hetzelfde zal teruggeven.

De afweging is dat de "main" beter leesbaar is, en ook geimporteerd kan worden in andere NLP projecten voor teksten met andere talen. 
Er zal er niet heel veel procesvermogen en tijd worden gewonnen omdat de functie maar 5 keer wordt aangeroepen. 
Enkel de leesbaarheid van de main code wordt een beetje verslechterd omdat meer informatie in het argument van remove_stopwords moet worden doorgegeven.

Dit is dus een betere implementatie van de remove_stopwords functie dan huidig.

Een voorbeeld zou kunnen zijn dat in een nieuw project over Nederlandse nieuwsartikelen het volgende wordt aangeroepen:

```python3
>>> from data_cleaning.py import remove_stopwords
>>> remove_stopwords("Ik heb mijn fiets altijd hier neergezet.", stopwords.words("dutch"))
>>> "fiets neergezet"
```

## 2. Wat is nou eigenlijk de daadwerkelijke functie van finished in de vectorizer module?

Finished (en meer specifiek de twee regels na finished) starten en stoppen een klokje op een nieuwe thread welke de huidig lopende tijd laat zien sinds de aanvang van het programma.
```python3
>>> thread = threading.Thread(target=running_time)
>>> thread.start()
```
Het probleem hier is dat het niet duidelijk is dat finished een variabele is die invloed heeft op de running_time functie. 
Finished wordt gebruikt als stopconditie, maar wordt doorgegeven als globale variabele. 
De reden dat dit gebeurd is omdat het niet mogelijk is om informatie door te geven aan running_time als argument.
Duidelijker zou zijn om finished, running_time en thread te combineren in een wrapper functie.
Hieruit kan de relatie tussen de drie beter worden bepaald. 
Het doel van de variabele duidelijker en is de code gemakkelijker begrijpbaar.

De afweging is dat het al vrij complex was om de functie aan te roepen en te stoppen omdat geen argumenten meegegeven kunnen worden aan running_time. Een wrapper functie die het bundelt maakt het misschien wel duidelijker binnen zichzelf door finished te compartimenteren, maar in de main wordt het juist minder duidelijk omdat deze wrapper functie veel takenop zich neemt. 

In plaats van de de code in de main op deze manier:
![screenshot of implementation](/screenshots/running_time%20threading%20function.png)

Kan ook het volgende worden gedaan:
```python3
def lda_fitting_and_normalizing(lda, data_vectorized):
    content of 
```

## 3. Waarom worden functies gedefiniëerd in topic_modeling.ipynb in plaats van deze te importeren?

Het probleem hier is dat functies direct worden gedefinieerd in het Jupyter Notebook-bestand topic_modeling.ipynb, in plaats van deze uit een aparte module te importeren.
Dit kan de leesbaarheid van de code verminderen en het moeilijker maken om functies te hergebruiken.

Om dit beter te maken, was het ook mogelijk om het gros van de functies te definiëren in een aparte module en binnen topic_modeling.ipynb enkel de visualisatiefuncties te definiëren.
Hierdoor wordt de code overzichtelijker en bevordert het de herbruikbaarheid van functies in andere delen van het project.

Door de andere functies in een losse module te plaatsen, wordt de code overzichtelijker en wordt de herbruikbaarheid van functies bevorderd.
Hierdoor wordt het makkelijker voor bijvoorbeeld results.ipyb om dezelfde functies importeren en gebruiken.
Dit kan consistentie in de code kan bevorderen door de manier hoe functies worden geimporteerd uit Jupyter Notebooks.
Bovendien wordt de leesbaarheid van topic_modeling.ipynb verbeterd omdat de focus ligt op enkel de specifieke visualisatiefuncties in plaats van het definiëren van alle functies.

De afweging hier is dat het creëren van weer een aparte module en het importeren van deze functies een extra stap toevoegd met de benodigde organisatie.
Wanneer er veel functies beheert moeten worden zoals het geval is binnen dit project wordt het dan al snel lastig om consistentie te waarborgen door de toenemende complexiteit. Desalniettemin kan deze extra inspanning kan de moeite waard zijn vanwege de verbeterde leesbaarheid en herbruikbaarheid van de code wanneer importeren kan worden gedaan uit een module in plaats van een Jupyter Notebook.

## 4. Voor iemand die niet bekend is met threading, is het heel onduidelijk wat er precies gebeurd. Wat doe je precies?

## 5. Het is nog vrij onduidelijk wat er gebeurd in de vectorizer module. Wat gebeurd er bij een LDA?


Load.py:
TimeSeries
Extra print tussen load en write?
Je kan proberen een inschatting maken van hoe lang het laden duurt

Define main ipv if name == main
Je zie dan meteen het allerbelangrijkste
Ipv naar beneden te moeten scrollen
Data_cleaning.py
Je kan 1 functie maken van voor elke set van data_cleaning.py manipulatie zodat het in 1x duidelijk
is wat elk blok van df_apply doet
Random_sample.py
Elk van de 3 blokjes kan weer in elke losse functies voor de duidelijk
Waarom hele tijd _01 etc?
Je kan ze beter direct een naam geven
Raw, processed, sampled, lemmatized, vectorized

Lemmatization.py
Meer info bij de funcdef
Wat is filler eigenlijk? Licht dit toe

Finished starts a runtime clock on a separate thread
Waarom 50 topics voor LDA?

Topic_modeling.ipynb
- Seeding article
- Recommended article
