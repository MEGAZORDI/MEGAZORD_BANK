Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from time import sleep
... print('=' * 30)
... print('{:^30}'.format('MEGAZORD BANK'))
... print('=' * 30)
... value = int(input('Dollar bills 1$, 10$, 20$, 50$ \nHow much do you want to withdraw? '))
... total = value
... bills = 50
... totbills = 0
... print('-' * 30)
... print('Counting bills...')
... sleep(2.0)
... print(' ' * 30)
... while True:
...     if total >= bills:
...         total -= bills
...         totbills += 1
...     else:
...         if totbills > 0:
...             print(f'Withdrawing a total of {totbills} dollar bills of {bills}$')
...         if bills == 50:
...             bills = 20
...         elif bills == 20:
...             bills = 10
...         elif bills == 10:
...             bills = 1
...         totbills = 0
...         if total == 0:
...             break
... print('=' * 30)
