# **Wine Quality Predictor**

**DAT158 – Innlevering 2: Prosjektarbeid**

Erlend Gildberg Røstøen, Artin Bahrampour, Andreas Borgenvik<span style="text-decoration:underline;"> </span>

27.11.2026


## **1: BESKRIV PROBLEMET**


### **OMFANG / SCOPE**

Målet med prosjektet er å utvikle en nettside som bruker maskinlæring til å predikere kvaliteten på rødvin basert på vinens kjemiske egenskaper.

Prosjektet er rettet mot personer som er interessert i vin, 

Maskinlæring passer til oppgaven fordi forholdet mellom vinens kjemiske egenskaper og kvalitet ikke nødvendigvis er lineært eller enkelt å beskrive med faste regler.

Det finnes allerede datasett og maskinlæringsprosjekter som undersøker vinkvalitet. Vårt prosjekt skiller seg først og fremst ut ved å gjøre en slik prediksjon tilgjengelig gjennom en enkel nettside.

Prosjektet krever en vanlig datamaskin, Python og relevante programvarebiblioteker. Gradio brukes til å lage nettsiden, mens Pandas og Scikit-learn brukes til databehandling og maskinlæring.


### **METRIKKER**

Modellen evalueres ved hjelp av accuracy (treffsikkerhet). Dette måler andelen observasjoner i testdatasettet der modellen predikerer riktig kvalitetsscore.

Datasettet inneholder flere ulike kvalitetsscorer. Noen scorer forekommer oftere enn andre, og dette kan påvirke hvor godt modellen presterer. Derfor bør accuracy tolkes sammen med fordelingen av kvalitetsscorene og hvilke feil modellen gjør.

Prosjektet regnes som teknisk vellykket dersom modellen kan trenes, evalueres og brukes til prediksjoner gjennom nettsiden.


## **2: DATA**

Prosjektet bruker Wine Quality-datasettet fra UCI Machine Learning Repository. Datasettet inneholder kjemiske målinger av rødvin og tilhørende kvalitetsscorer.

Datasettet består av 1599 observasjoner av rødvin. Hver observasjon har elleve numeriske inputvariabler og én målvariabel.

Inputvariablene er:



* Fixed acidity
* Volatile acidity
* Citric acid
* Residual sugar
* Chlorides
* Free sulfur dioxide
* Total sulfur dioxide
* Density
* pH
* Sulphates
* Alcohol

Dataene er allerede samlet inn og gjort tilgjengelige gjennom UCI Machine Learning Repository. Vi trenger derfor ikke å samle inn egne data.

Vi bruker Pandas til å lese datasettet og organisere variablene. Inputvariablene skilles fra målvariabelen før treningen. Deretter deles dataene i et treningssett på 80 prosent og et testsett på 20 prosent. Vi bruker en fast random seed for å gjøre eksperimentet reproduserbart, og stratified splitting for å bevare omtrent samme fordeling av kvalitetsscorene i begge settene.

Modellen benytter numeriske variabler direkte. Random Forest krever ikke standardisering av variablene, så skalering er ikke nødvendig i denne løsningen. Datasettet kontrolleres ved innlasting for å sikre at det har forventede kolonner og kan leses korrekt.

Prosjektet bruker ikke personopplysninger. Dataene beskriver kjemiske egenskaper ved vin og tilhørende kvalitetsscorer

. 


## **3: MODELLERING**

Vi bruker Random Forest Classifier fra Scikit-learn for å predikere kvalitetsscoren.

Vi valgte Random Forest fordi modellen er relativt enkel å implementere, fungerer godt med numeriske tabulære data og krever lite forhåndsbehandling..

Som en enkel baseline kan vi bruke den vanligste kvalitetsscoren i treningsdatasettet som prediksjon for alle observasjoner i testdatasettet. Dette gir et referansepunkt for å vurdere om Random Forest lærer nyttige mønstre sammenlignet med en enkel løsning.

Dataene deles i trenings- og testsett før modelltreningen. Modellen trenes bare på treningssettet, mens testsettet brukes til å måle ytelsen på data som ikke ble brukt under treningen.

Vi bruker accuracy som hovedmetrikk.

**Resultater fra eksperimentene:**


<table>
  <tr>
   <td><strong>Måling</strong>
   </td>
   <td><strong>Resultat</strong>
   </td>
  </tr>
  <tr>
   <td>Antall observasjoner
   </td>
   <td>1599
   </td>
  </tr>
  <tr>
   <td>Treningsdata
   </td>
   <td>80 %
   </td>
  </tr>
  <tr>
   <td>Testdata
   </td>
   <td>20 %
   </td>
  </tr>
  <tr>
   <td>Modell
   </td>
   <td>Random Forest Classifier
   </td>
  </tr>
  <tr>
   <td>Antall beslutningstrær
   </td>
   <td>100
   </td>
  </tr>
  <tr>
   <td>Baseline accuracy
   </td>
   <td>42.5%
   </td>
  </tr>
  <tr>
   <td>Random Forest test accuracy
   </td>
   <td>65.31%
   </td>
  </tr>
</table>


Feilprediksjoner kan undersøkes ved å sammenligne modellens prediksjoner med de faktiske kvalitetsscoreene. En prediksjon på kvalitetsscore 6 når den faktiske scoren er 7, er en annen type feil enn en prediksjon på 3 når den faktiske scoren er 8. Dette er relevant fordi kvalitetsscorene har en naturlig rekkefølge, selv om modellen behandler dem som separate klasser.


## **4: DEPLOYMENT**

Modellen og nettsiden implementeres i Python. Gradio brukes til å lage et brukergrensesnitt der brukeren kan fylle inn de elleve kjemiske målingene. Når brukeren sender inn verdiene, opprettes en observasjon med samme variabelstruktur som treningsdataene. Den trente modellen returnerer deretter en predikert kvalitetsscore.

Nettsiden viser kvalitetsscoren og en enkel beskrivelse av resultatet. Applikasjonen viser også modellens målte test-accuracy som informasjon om modellens generelle ytelse. Denne verdien beskriver ytelsen på testdatasettet, ikke sikkerheten i en enkelt prediksjon.

Løsningen kan kjøres lokalt med Python.

**GitHub-repository: **[https://github.com/h571605/wine-quality-predictor](https://github.com/h571605/wine-quality-predictor)

**5: REFERANSER**



1. Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems, 47*(4), 547–553.[ https://doi.org/10.1016/j.dss.2009.05.016](https://doi.org/10.1016/j.dss.2009.05.016)
2. UCI Machine Learning Repository. *Wine Quality Dataset*.[ https://archive.ics.uci.edu/dataset/186/wine+quality](https://archive.ics.uci.edu/dataset/186/wine+quality)
3. Scikit-learn. *RandomForestClassifier documentation*.[ https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
4. Scikit-learn. *Model evaluation documentation*.[ https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html)
5. Gradio. *Documentation*.[ https://www.gradio.app/docs](https://www.gradio.app/docs)
6. Pandas. *Documentation*.[ https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
