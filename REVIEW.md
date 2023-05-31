# Uitwerking van code review

Studenten die de code review hebben uitgevoerd: Sabrina, Duco

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

![screenshot van huidige implementatie](/screenshots/running_time%20threading%20function.png)

Kan ook het volgende worden gedaan:
```python3
def lda_fitting_and_normalizing(lda: pd.Dataframe, data_vectorized: pd.Dataframe) -> None:
    inhoud van screenshot
```

## 3. Waarom worden functies gedefiniëerd in topic_modeling.ipynb in plaats van deze te importeren?

Functies worden direct gedefiniëerd in het Jupyter Notebook-bestand topic_modeling.ipynb, in plaats van deze uit een aparte module te importeren.
Dit vermindert de leesbaarheid van de de notebook en maakt het moeilijker om functies hieruit te importeren.
```
from ipynb.fs.def.notebook_name import x, y
```
De bovenstaande regel importeert namelijk wel de functies, maar geeft maar een partiële import zoals hieronder is te zien.

![notebook function import](/screenshots/notebook_function_import.png)

Om dit beter te maken is het beter om het gros van de functies te definiëren in een aparte module en binnen topic_modeling.ipynb enkel de visualisatiefuncties te definiëren.
Hierdoor wordt de code overzichtelijker en bevordert het de herbruikbaarheid van functies in andere delen van het project.

Door de andere functies in een losse module te plaatsen, wordt de code overzichtelijker en wordt de herbruikbaarheid van functies bevorderd.
Ook de functies die worden definiëerd in results.ipynb kunnen dan gemakkelijk worden geplaatst in deze nieuwe module.  Results.ipynb wordt hierdoor aanzienlijk leesbaarder. Ook is hergebruik van functies gemakkelijker, omdat de link tussen een module en een geimporteerde module in een oopslag duidelijk kan zijn.

![proper function import](/screenshots/proper_func_import.png)

Een bijkomend positief effect is dat dee leesbaarheid van topic_modeling.ipynb wordt verbeterd omdat de focus ligt op enkel de specifieke visualisatiefuncties in plaats van het definiëren van alle functies.

De afweging hier is dat het creëren van weer een aparte module en het importeren van deze functies een extra stap toevoegd met de benodigde organisatie van alle functies en de folderstructuren.
Wanneer er veel functies beheert moeten worden zoals het geval is binnen dit project wordt het dan al snel lastig om consistentie te waarborgen door de toenemende complexiteit. 
Een kleine aanpassing (zoals het hernoemen van een folder) kan dan al snel veel imports laten crashen. Desalniettemin kan deze extra inspanning kan de moeite waard zijn vanwege de verbeterde leesbaarheid en herbruikbaarheid van de code wanneer importeren kan worden gedaan uit een module in plaats van een Jupyter Notebook.

## 4. Waarom worden csv bestanden 2016, 2016_01, 2016_02, etc. genoemd?

Het probleem hierbij is dat het niet duidelijk is wat de verschillen tussen deze bestanden eigenlijk zijn.
Een mogelijke oplossing zou zijn om ze een meer descriptieve suffix te geven. 
Zo kan 2016 2016_raw worden genoemd, 2016_01 worden hernoemd naar 2016_cleaned, 2016_02 naar 2016_sampled, 2016_03 naar 2016_lemmatized, etc. 
De extra folderstructuur binnen /topicmodeling/csv is dan ook overbodig, omdat deze dan op dezelfde manier benoemd kunnen worden.

Een grote afweging hierbij is dat de hierarchie van stappen niet meer in een oogopslag duidelijk is. 
Waar het eerst logisch is dat 2016_03 voortkomt uit het verwerken van 2016_02, is dit nu niet meer het geval. Wanneer nieuwe tussenstappen genomen moeten geworden (zoals een extra stap tussen data_cleaning en lemmatization waar emojis worden geconverteerd naar tekst bijvoorbeeld) is niet meer te zien dat 2016_emojified tussen 2016_cleaned en 2016_sampled hoort te staan. 

In het geval van numerieke identificators kunnen de opvolgende getallen eenvoudig worden opgehoogd. 2016_01 (cleaned), 2016_02 (emojified), 2016_03 (sampled) geven dan nog steeds een duidelijke hierarchie aan.

Een mogelijkheid is om binnen deze folder een README.md toe te voegen de kort elke achtervoegsel toelicht.

Een andere optie is het combineren van een descriptieve toelichting met het identificatiegetal.
Dit zou 2016_cleaned_01 opleveren maar resulteert ook weer in andere onduidelijkheid. 
Als er een 2016_cleaned_01, en daarna een 2016_sampled_02 lijkt het alsof  2016_sampled_01 ontbreekt.

## 5. Het hoofddoel van elke module is het runnen van de functies binnen de modules.

Opvallend is dat het nodig is binnen elke module om omlaag te scrollen om te kijken wat de module eigenlijk doet.
De andere functie definities staan dan eigenlijk 'in de weg'.
Dit kan worden opgelost door alle code in een een eigen functie bovenaan te zetten, en deze in de main aan te roepen. Dit zou er dan als volgt uitzien

```python3
def main():
    code in main

...

if __name__ == "__main__":
    main()
```

Voor een lezer van de module is het dan direct mogelijk om te zien wat de module precies uitvoert wanneer ze deze openen.

Een afweging hier is dat sommige modules veel functies bevatten die worden gebruikt in andere modules, zoals de Time class in de load module, of de load_years functie.
In deze gevallen zijn deze interessanter dan de main omdat men vaker hiernaar zal kijken, maar vaak maar een maal naar de main.
Voor de load module zou dit dus niet heel logisch zijn om te doen, maar de lemmatizer module bijvoorbeeld wel.
Men kan dan simpelweg omlaag scrollen om te kijken wat elke functie specifiek uitvoert.
