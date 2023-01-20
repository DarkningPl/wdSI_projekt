# <p align="center"> <b>Zasady gry:</b> </p>
## Karty
W talii jest 110 kart, 12 kart każdego z podstawowych kolorów, oraz 14 kart srebrnych, które mogą przyjmować dowolny kolor.
Na stole jest 5 widocznych kart, karty gracza, karty bota (niewidoczne) oraz stosik kart.
Karty służą do budowania połączenia na mapie.
## Połączenia
Połączenia między sąsiednimi miastami są wyświetlane w postaci cegiełek (ilość cegiełek jest równa kosztowi ich zbudowania).\
Cegiełki jednokolorowe (z wyjątkiem szarych) wymagają kart odpowiadającego im koloru do zbudowania połączenia.\
Połączenia z cegiełek dwukolorowych mogą być zbudowane przy użyciu kart jednego lub drugiego koloru (lecz nie ich kombinacji).\
Cegiełki szare mogą być zbudowane przy użyciu kart dowolnego koloru, trzeba tylko wybrać, jakiego.\
Cegiełki, które mają ciemnoszarą kropkę wymagają użycia srebrnej karty (oznaczającą lokomotywę).\
Połączenia jedno- lub dwukolorowe mogą być tunelem, co objawia się ciemnoszarymi prostokątami na końcach cegiełki.
Przy próbie zbudowania takiego tunelu, ze stosu są brane 3 karty i każda karta, która ma taki sam kolor, jakiego koloru karty chcieliśmy użyć, zwiększa nam ilość kart potrzebnych na jego zbudowanie.\
Przykładowo, jeżeli tunel jest koloru zielonego i ma długość 2, a spośród trzech kart wybranych ze stosu jest jedna zielona, koszt zbudowania tego połączenia wyniesie 3 karty zamiast 2.
## Cele
W grze jest 6 długich celów oraz 40 krótkich.
Na początku gry przyznawany jest 1 cel długi i 3 krótkie, z których 2 mogą zostać odrzucone.
Cele są wyświetlane jako prostokąty, które zawierają nazwę miast, które chcemy połączyć oraz punkty do zdobycia za połączenie ich.
Cele wyświetlane między kartami gracza i kartami odsłoniętymi są tymczasowe, jeżeli nie są wygodne, można je wybrać do odrzucenia.
Cele po prawej stronie ekranu są na stałe i nie można ich odrzucić.
Można mieć maksymalnie 8 celów.
## Punktacja
Za zbudowanie pojedynczego połączenia dostajemy punkty w zależności od jego długości:\
1 - 1pkt<br>2 - 2pkt<br>3 - 4pkt <br>4 - 7pkt<br>6 - 15pkt<br>8 - 21pkt\
Oprócz tego, za zrealizowanie celu przyznawane są punkty równe liczbie na karcie.
W przypadku, gdy nie udało się go zrealizować, punkty są odbierane.
## Ruchy
Zabranie kart ze stosu - gracz w ciemno bierze 2 karty z kupki.\
Zabranie kart ze stołu - gracz może zabrać 2 karty koloru lub 1 kartę srebrną z kart widocznych na stole.\
Zabranie celów - gracz dobiera 3 karty celów, może odrzucić maksymalnie 2 z nich, wymaga zatwierdzenia przyciskiem kontynuuj, wtedy nieodrzucone cele zostają dodane na stałe.\
Zbudowanie połączenia - gracz wybiera połączenie kliknięciem myszki, następnie postępuje zgodnie z poleceniami konsoli.
Gdy zapytany, czy zbudować połączenie przy użyciu <i>m</i> kart koloru i <i>n</i> kart srebrnych, należy kliknąć przycisk jeszcze raz, aby zatwierdzić budowę.\
Pas - gracz nie wykonuje żadnego ruchu, można kliknąć w dowolnym momencie (poza odrzucaniem celów).\
Kontynuuj - kliknięcie tego przycisku po wybraniu celów do odrzucenia spowoduje zatwierdzenie niewybranych i odrzucenie wybranych. (Można kliknąć tylko, gdy gracz ma cele tymczasowe.)
## Budowanie połączeń
Budowanie połączenia wymaga użycia wystarczającej ilości kart odpowiedniego koloru oraz zużycie tylu wagonów, ile cegiełek zawiera połączenie.\
Zbudowane połączenie wyświetla wagonik gracza (kolor jasnoniebieski) lub wagonik bota (kolor ceglasty).
Nie można zbudować połączenia, które już zostało zbudowane.
## Koniec gry
Gdy gracz lub bot ma tylko 2 lub mniej wagonów, gra wchodzi w ostateczną fazę, gdzie każdy ma tylko 1 ruch.
Po wykonaniu tego ruchu następuje koniec gry i podsumowanie punktów.