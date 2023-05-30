# Uitwerking van code review

Sabrina, Thom

    Wat is het tegengekomen probleem?
    Hoe zou je dit beter kunnen maken?
    Wat voor afweging maak je? Vaak is een keuze voor iets ook een keuze tegen iets anders.
    Illustreer met enkele voorbeelden.

## 1. Herhalende call naar stopwords.words("english") binnen remove_stopwords() in de data_cleaning module

Het probleem hier is dat de functie remove_stopwords() meerdere keren de lijst met Engelse stopwoorden ophaalt, wat onnodig is en de prestaties kan beïnvloeden.
Het zorgt er ook voor dat het minder duidelijk is voor een leek wat de stopwords.words("english") functie eigenlijk doet.

Om dit probleem op te lossen, kan je de lijst met Engelse stopwoorden slechts één keer ophalen buiten de functie en deze als een argument aan remove_stopwords() doorgeven. Op deze manier wordt de lijst niet herhaaldelijk opgehaald en verbetert de prestatie van de code.

De prestatie van de functie wordt enigszins verbeterd, maar het ophalen van de lijst buiten de functie kan enige extra complexiteit introduceren in de code.
De afweging hier is een marginale prestatieverbetering, maar een extra argument die moet worden meegegeven.
Het is een afweging van prestatieverbetering tegenover complexiteit.

## 2. Waarom is finished in de vectorizer module een boolean die een functie verstopt? Dit is nu heel onduidelijk

Finished wordt gebruikt als stopconditie voor een functie die wordt aangeroepen door middel van thread.start().
Finished wordt echter doorgegeven als global variabele in plaats van dat deze als functie de threading functie start of stopt. Dit is onduidelijk en verhult het doel van de variabele.

Om dit beter te maken is het mogelijk om finished dus te vervangen door een functie die de threading functie start of stopt.
Hierdoor wordt het doel van de variabele duidelijker en is de code gemakkelijker begrijpbaar.

De afweging is echter dat het al vrij complex was om de functie aan te roepen en te stoppen omdat de threading.Thread(target=functie) geen argumenten meegeeft aan de functie.
Het zou dan dus nodig zijn om een volledige wrapper te schrijven die dit beter specificeert. Dit maakt de code wel complexer, en daarmee misschien minder gemakkelijk begrijpbaar.

Een ander alternatief zijn zorgvuldig geschreven comments die toelichten wat de rol van de finished variabele is.

## 3. Waarom worden functies gedefiniëerd in topic_modeling.ipynb in plaats van deze te importeren uit een module voor de leesbaarheid?

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
