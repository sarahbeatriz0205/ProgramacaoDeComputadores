A = float(input())
B = float(input())
C = float(input())

area_trianguloretangulo = (A*C)/2

area_circulo = 3.14159 * (C * C)

area_trapezio = (A + B) * (C / 2)

area_quadrado = (B * B)

area_retangulo = (A * B)

print("TRIANGULO:", "{:.3f}".format(area_trianguloretangulo))
print("CIRCULO:", "{:.3f}".format(area_circulo))
print("TRAPEZIO:", "{:.3f}".format(area_trapezio))
print("QUADRADO:", "{:.3f}".format(area_quadrado))
print("RETANGULO:", "{:.3f}".format(area_retangulo))
