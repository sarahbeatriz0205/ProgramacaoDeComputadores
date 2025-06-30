Ca, Ba, Pa = map(int, input().split()) #números disponíveis de refeições
Cr, Br, Pr = map(int, input().split()) #número de refeições requisitadas, em ordem
falta = 0

if Cr > Ca:
    falta = falta + Cr - Ca

if Br > Ba:
    falta = falta + Br - Ba

if Pr > Pa:
    falta = falta + Pr - Pa

print(falta)