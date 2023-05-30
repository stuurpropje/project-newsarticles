# Uitwerking van code review

Sabrina, Thom

    Wat is het tegengekomen probleem?
    Hoe zou je dit beter kunnen maken?
    Wat voor afweging maak je? Vaak is een keuze voor iets ook een keuze tegen iets anders.
    Illustreer met enkele voorbeelden.

## 1. Herhalende call naar stopwords.words("english") binnen remove_stopwords() in de data_cleaning module

## 2. Waarom is finished een boolean die een functie verstopt? Hoe kan je dit verbeteren?

## 3. Waarom worden functies gedefiniëerd in topic_modeling.ipynb in plaats van deze te importeren uit een module voor de leesbaarheid?

## 4. Als persoon niet bekend met de code die wordt uitgevoerd, waarom heb je voor bepaalde keuzes gekozen?

## 5. Het is nog vrij onduidelijk wat er gebeurd in de vectorizer module. Wat gebeurd er bij een LDA?





Let bij de punten die je noemt wel op haalbaarheid en let ook op de details. Het mag best veel werk kosten om een verbetering door te zetten, maar het moet wel mogelijk zijn en kloppen.

2.	Datacleaning.py
Stop words is niet geheel duidelijk voor een leek
wat zijn stop words?
-	Is een lijst van ongeveer 1000 woorden

Remove_stopwords
-	Filler kan gecached worden zodat deze niet elke keer opnieuw geassigned hoeft te worden
Nog wel meer comments
Print statements + comments?

3.	Lemmatizer.py
-	Comment imports?
-	Niet duidelijk hoe CSVs worden geschreven naar een bestand
-	Verklaar de print functie
o	Wat doet hij
o	Waar is hij
o	Hoe ver is hij
o	Hoe lang is hij bezig?
Ieder jaar heeft een los csv bestand

Waarom die ik iets?
-	Waarom heb gebruik i de file_pointer functie?
o	Zodat bij storing het programma door kan gaan waar het was gebleven
-	Waarom doe ik df_slice_gen?

5.	Vectorizer.py
Wat doet threading?
Geen docstring loading_animation
Wat doet lda?
Waarom is data_vectorized eerst een lege string?
Comment eventjes thread = threading
Wat doet joblib.dump?
-	Schrijven van dataframe naar bestand
Waarom finished = bool?
Finished kan niet expliciet worden meegegeven
-	Finished is een functie waar je dat ding mee laat lopen
-	Het ziet er nu uit als een variabele dus het is niet duidelijk wat hij doet

6.	Topic_modelling.ipynb
Picking related articles
-	Wat doet hij nou eigenlijk?
-	Schrijf een summary
Load_all_years
-	Spelling
Compare_topic

Waarom importeer ik niet mijn functies?
-	Lol ja lol goede vraag

Geef labels aan x en y as voor recommendation()
Voeg een .md toe onder welke ID gaat over welk onderwerp?
-	Deze plot gaat over x, wat is x?
-	Of zeggen waar ze de topic lijst kunnen vinden
-	Of allebei
-	Of voeg een dict toe van id = topic
Voeg toe hoe ze recommendation_widget() kunnen gebruiken
Wat zegt similarity(0.60)?

7.	Results.ipynb
Func defs in andere code
Uitleg bij vergelijking van df.main en de kleine
Wat haal je hieruit?
Wat kan je concluderen?
Meer uitleg bij:
-	Processed and unprocessed data
-	Welke paren horen bij elkaar?
Kopje erbij van proof of concept afgelopen: hier staat de echte data
Vectorization and applying a lda on the actual dataset
-	Kopje bij topic wat je doet en wat je ermee kan
-	Interpreteer recommendation() en recommendation_widget()

ìk mis een rode draad door je project. je hebt duidelijk heel veel gedaan aan coderen en je project ziet er indrukwekkend uit. het probleem is dat ik totaal niet kan volgen wat je doet. het toevoegen van een introductie en conclusie zouden erg helpen.

in results.ipynb ga je over al je andere files heen en geef je steeds een korte uitleg. ik mis hier echter waarom je bepaalde dingen doet. het lees meer als een technische handleiding dan een datascience project.