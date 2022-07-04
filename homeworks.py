if6
a = int(input('1-son:'))
b = int(input('2-son:'))
if a>b:
  print(f'{a} katta')
else:
  print(f'{b} katta')
if7
a = int(input('1-son:'))
b = int(input('2-son:'))
if a>b:
  print(f'{b} kichik')
else:
  print(f'{a} kichik')
if8
a = int(input('1-son:'))
b = int(input('2-son:'))
if a>b:
  print(f'{a} katta')
  print(f'{b} kichik')
else:
  print(f'{b} katta')
  print(f'{a} kichik')
if11
a = int(input('1-son:'))
b = int(input('2-son:'))
if a < b:
  print(f'{b} katta')
elif a == b:
  print(f'{0} teng ')
elif a > b:
  print(f'{a} katta ')
if12
son=[]
for sons in range(0,3):
  son.append(int(input(f'{sons+1}-sonni kiriting')))
son.remove(min(son))
print(son)
if13
son=[]
for sons in range(0,3):
  son.append(int(input(f'{sons+1}-sonni kiriting')))
print(min(son))
if14
son=[]
for sons in range(0,3):
  son.append(int(input(f'{sons+1}-sonni kiriting')))
print(max(son))
print(min(son))
if15
son=[]
for sons in range(0,3):
  son.append(int(input(f'{sons+1}-sonni kiriting')))
son.remove(min(son))
print(son)
if16
a = int(input('1-son:'))
b = int(input('2-son:'))
c = int(input('3-son:'))
if a < b < c:
  print(a,a,b,b,c,c)
else:
  print(-a,-b,-c)
if17
a = int(input('1-son:'))
b = int(input('2-son:'))
c = int(input('3-son:'))
if a < b < c or a < b < c:
  print(a,a,b,b,c,c)
else:
  print(-a,-b,-c)

