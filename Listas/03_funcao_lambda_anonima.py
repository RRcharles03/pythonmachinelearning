#  Funcao padrao em Python

def somaQuadrado(a, b):
  somaQ = a**2 + b**2
  return somaQ

print(somaQuadrado(4, 5))

# Funcao lambda em Python

somaQuadrado2 = lambda a, b: a**2 + b**2
print(somaQuadrado2(2,2))