import math
import eng, hun
from eng import english
from hun import hungarian

chooselanguage = input("Choose the language/Válaszd ki a nyelvet (eng/hun): ")
if chooselanguage == 'eng':
    english.calc_eng()

elif chooselanguage == 'hun':
    hungarian.calc_hun()

else:
    print("Wrong input!/Helytelen használat!")