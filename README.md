<h1 align="center">Filmová aplikace</h1>

<ol>
  <li>Slovník</li>
  <li>Output</li>
  <li>Část kódu</li>
</ol>

<ul>
  <li><h2>Slovník</h2>
    <p>V programu je založený slovník, ve kterém jsou 3 hlavní klíče (Filmy, Seriály, Plán) Ke každému je přiřazena <br>
       hodnota v podobě dalšího slovníku, ve kterém ,u Filmů a seriálů, jsou 4 klíče (žánry), k nimž je přiřazena hodnota dalšího slovníku,<br>
       v němž se nachází itemy v podobě označení filmu/seriálu a názvu filmu/seriálu.<br>
       Poté je tu již zmiňovaný Plán, ke kterému je přiřazena hodnota pouze jednoho slovníku, ve kterém <br>
       se nachází 3 itemy (jednotlivé plány - Standart, Pro, Ultra)</p></li>
        
  <li><h2>Output</h2>
    <p>Nejprve se vás program zeptá na jméno a příjmení. Poté se vás zeptá na službu, kterou chcet aby program udělal.<br>
       Po zvolení služby se vás program zeptá na žánr filmu/seriálu (neplatí pro Plán) a nakonec už jen pomocí for cyklu vypíše filmy/seriály<br>
       pod daným žánrem.</p></li>
       
  <li><h2>Část kódu</h2>
    <p>Následující kód kontroluje zda byl vybrán film. Pokud Ano tento kód se spustí. Nejprve se na 2. řádku program zeptá<br>
       jaký žánr chcete a poté na 3. řádku kontrolujeme zda se zadaný input nachází ve slovníku, který je jako hodnota<br>
       ke klíči "Filmy". Pokud ano tak se spustí poslední část kódu a to již zmíněný for cyklus, který prochází klíče a hodnoty<br>
       v itemech zvoleného žánru a ty poté vypíše.</p></li>
      <img src = "https://github.com/HellusJ/filmy_osss/blob/main/Filmkod.img.png?raw=true" height = "140" width = "720">
</ul>
