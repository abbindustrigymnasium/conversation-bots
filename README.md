# conversation-bots
En bot som har konversation med en annan person genom Discord.

Original planen är att skapa 2 botar som pratar med varandra men det är inte möjligt att köra 2 Discord botar samtidigt i ett system. Så jag minskade antal botarna istället. 

## Vad jag har gjort
Jag har gjort en bot som man kan ha en konversation med. Den är inte perfekt och det är mycket svårt att få den att hålla en lång och djup konversation. Den största orsaken till den är att library:n som jag använder krävs en ganska specifik format på tränings data, och det skulle ta jättelänge för att skapa en träningsdata. Och chattbotar behöver relativt mycket data för att den ska bli bra. Dock så kan boten lära sig av att prata med människor, på så sätt så lär man boten, men det tar väldigt lång tid.

Jag har även använt Discord library för att få in boten som en Discord bot. Trots att jag inte kan ha den öppen 24/7 så kommer den fortfarande vara publikt. Det vill säga att andra människor kan chatta med boten för att hjälpa mig träna den också.

## Hur ha du gjort
Jag använder mig av en chat bot library kallas chatterbot. Den har redan ganska mycket i jättefå linjer av kod. Så kod mässigt ser den inte alls så komplicerad, och det är den inte. Jag har även använt mig av chatterbot-corpus, vilket är chatterbots egna tränings dataset. Vilket är bra nog eftersom chatterbot kan lära sig av konversationer den har med användaren också. 

Jag har även testat och använda mig av Ubuntu dialog corpus. Vilket är ett gigantiskt dataset för att träna chatterboten. Den blir väldigt bra om man tränar boten med den dataset men den stora nackdelen är att det tar ungefär 8 timmar för att träna den, och minst 10 minuter för att svara, vilket är allt för lång tid. Så den är oanvändbar. 

## Reflektion
Min original plan var att få två bottar att prata med varandra. Men för att den ska vara intressant så krävs det att botarna ska ha olika personligheter, vilket är omöjligt med den metoden jag använder. Tyvärr finns det inte många bra alternativer för chatbot libraries. Så jag ändrade till denna idéen istället. 

Det svåraste med denna projekt är då inte att skapa AI:n, eftersom den finns redan en färdig i en library. Utan att få in den i Discord. 

Jag tror att det skulle har varit lättare om jag hade spenderat mer tid på att hitta andra chatbot libraries. Eller kanske spenderad mer tid på att undersöka chatterbot samt något sätt för att automatisera träningsdata. Hade jag gjort nån av de tror jag att det skulle ha varit lite mer intressant att jobba med AI:n. 

## Vad jag har lärt mig
Jag har lärt mig hur en chattbot fungerar. Inte på djupare nivå men tillräckligt. Jag hade redan erfarenhet med att jobba med en Discord bot. Dock så var det ganska länge sedan så det är lite kul att komma tillbaka till den igen. 