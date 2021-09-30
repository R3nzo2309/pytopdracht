Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Renzo Reemer')
Mijn naam is Renzo Reemer
>>> naam = '<JOUW NAAM HIER>'
>>> naam = 'Renzo Reemer'
>>> print(naam)
Renzo Reemer
>>> print(naam.upper())
RENZO REEMER
>>> print(naam[0:2])
Re
>>> print(naam[::-1])
remeeR ozneR
>>> leeftijd = 18
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Renzo Reemer ben je al 18 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
19
>>> leeftijd-=1
>>> leeftijd
18
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	elif leeftijd > 18:
		
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Je bent precies 18 jaar
>>> from random import randint
>>> randint(0,1000)
732
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
785
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 785
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-16 13:02:49.006614
>>> datum.strftime('%A %d %B %Y')
'Thursday 16 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    locale.setlocale(locale.LC_TIME, 'nl_NL')
  File "C:\Users\Student\AppData\Local\Programs\Python\Python39\lib\locale.py", line 610, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
>>> datum.strftime('%A %d %B %Y')
'Thursday 16 September 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    locale.setlocale(locale.LC_TIME, 'it_IT')
  File "C:\Users\Student\AppData\Local\Programs\Python\Python39\lib\locale.py", line 610, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
>>> datum.strftime('%A %d %B %Y')
'Thursday 16 September 2021'
>>> 