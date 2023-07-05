chess_players = {

"Carlsen, Magnus": 1865,
"Firouzja, Alireza": 2804,
"Ding, Liren": 2799,
"Caruana, Fabiano": 1792,
"Nepomniachtchi, Ian": 2773

}

dict2={value:key.replace(",","").split()[0]+" "+key.split()[1][0]+"." for key,value in chess_players.items() if value>2000}
print(dict2)
