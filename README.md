# <p align="center"> AI do gry planszowej "Wsiąść do pociągu" </p>
<p align="center"> <b><i><u>Wykonali:</u></i></b> <br> Jakub Kujawiński 147510 <br> Krzysztof Chmielewski 147443 </p>

## 1. Opis rzeczywistego problemu
Projekt polega na stworzeniu AI do gry planszowej "Wsiąść do pociągu", którego zadaniem jest symulacja gracza.
W stworzonym przez nas środowisku w grze uczestniczy dwóch zawodników, gracz oraz bot z zaprogramowanym przez nas AI.
W grę może grać 5 uczestników, więc w bardziej rozbudowanym środowisku można by zagrać w więcej osób oraz z większą liczbą botów.
Tak zaprogramowany bot może być użyty jako zawodnik typu CPU w grze, w celu rozrywki lub/i nauki.
Zagadnienie opiera się na optymalnym znajdowaniu ścieżek w grafie oraz zarządzaniu zasobami.

## 2. State of art
Znane koncepcje rozwiązania:

Do znajdowania najkrótszej ścieżki między punktami został użyty <b>algorytm Dijkstry</b>, ponieważ połączenia między sąsiednimi punktami nie są jednostkowe.
Algorytm ten jest wystarczający, ale nie jest optymalny, ponieważ rozpatruje każde docelowe połączenie indywidualnie zamiast sprawdzać optymalne połączenia dla wielu punktów, które mogą mieć części wspólne. \
Innym rozwiązaniem tego zagadnienia jest <b>zmodyfikowany algorytm TSP</b>, który łączy wszystkie rozpatrywane punkty (tworzy on niedomknięty pierścień). Jest to algorytm NP-trudny, co oznacza, że trudność rozwiązania rośnie wykładniczo, w naszym przypadku może się okazać zbyt złożony. \
Trzecim rozwiązaniem jest <b>algorytm komiwojażera</b>. Jest to algorytm heurystyczny, czyli pozwala znaleźć rozwiązanie zbliżone do optymalnego, które niekoniecznie będzie najlepsze.\
Stworzone AI bierze również pod uwagę priorytety tworzenia połączeń, tj. najpierw skupia się na tworzeniu tych, które są trudniejsze do stworzenia.
Oprócz tego jest jeszcze element losowości; bot ma szansę wykonać bardziej ryzykowny lub bezpieczniejszy ruch przy przygotowaniach do stworzenia połączenia.
Większość algorytmów bota, stworzona jest za pomocą znajomości teorii grafów. Możliwe jest rozszerzenie inteligencji bota, poprzez skorzystanie z typowych dla grafów stopni centralności, bliskości, pośrednictwa. \
Degree Centrality (DC) czyli stopień centralności danego punktu jest iloczynem sumy wartości połączeń przez liczbę miast. 
Im mniejsza liczba połączeń, tym dane miasto powinno mieć wyższą wartość priorytetu budowy drogi z uwzględnieniem ilości celów do danego połączenia miasta. 
Na przykład dla Edynburgu, który ma tylko jedno bezpośrenie połaczenie, a liczba celów przechodząca przez to miasto wynosi 2, priorytet szybszego wybudowania trasy przez to miasto powinien być wyższy niż np. dla Kadyksu, który ma 2 połączenia, a przez którego przechodzi tylko 1 cel. \
Closeness Centrality (CC), czyli stopień bliskości miar jak łatwo dotrzeć do innych węzłów z danego miasta, jak blisko centrum znajduje się miasto.
Liczony jest przez odwrotność sumy liczby najkrótszych ścieżek (stosujemy algorytm Dijkstry) podzieloną przez liczbę wszystkich miast z wyłączeniem jednego. 
Większy priorytet mają miasta z wyższą wartością tego współczynnika.\
Betweenness Centrality (BC) - stopień pośrednictwa mówi jak często dane miasto jest na trasie między innymi miastami w grafie. 
Tu używa się algorytmu Brandesa. Większy priorytet mają miasta z wyższą wartością tego współczynnika.\
Clustering Coefficient - współczynnik skupienia się powiązanych węzłów w grafie (sąsiedztwa). 
Większy priorytet mają miasta z niższą wartością tego współczynnika.\
Należałoby każdej z tych wartości dobrać odpowiednią wagę i stworzyć przypisany współczynnik priorytetu dla bota. 
Przykładowe wartości można zobaczyć w pliku <b>examples.png</b>. 

## 3. Opis wybranej koncepcji
Nasz bot istnieje w stworzonym przez nas środowisku, które składa się z punktów (miast), dróg między nimi, ich kosztów zbudowania, oraz celów, które po zrealizowaniu dodają dodatkowe punkty.\
Zaprogramowany przez nas bot skupia się w pierwszej kolejności na połączeniach, które są warte najwięcej punktów.
Mając wybrane dwa punkty do połączenia, bot używa algorytmu Dijkstry, żeby znaleźć najkrótsze połączenie między nimi.
Następnie bot analizuje każdy segment otrzymanego połączenia i najpierw skupia się na tych odcinkach, które są najtrudniejsze do zbudowania.
Spośród tych segmentów bot wylicza do zbudowania którego z nich jest mu najbliżej.\
Potrzebne dane to istniejące połączenia w środowisku, posiadane przez bota cele i karty, oraz karty widoczne na stole.
Po ewaluacji danych bot zwraca do środowiska informacje o ruchu, jaki chce wykonać.

## 4. Proof of concept
Po uruchomieniu pliku main.py pojawi się okno gry, po lewej stronie jest mapa, po prawej są przyciski do interakcji ze środowiskiem oraz karty i cele.\
W lewym dolnym rogu prawej sekcji okna pojawi się konsola, w której wyświetlane jest ostatnie 5 informacji o stanie gry.\
Po rozpoczęciu gry gracz może porozumiewać się ze środowiskiem przy pomocy kliknięć myszy (input) oraz konsoli (output).\
Zasady gry są opisane w pliku <b>ZASADY.md</b>.
