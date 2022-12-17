total_cidades = int(input())
distancias = []
rota = []
distancia_rota = 0
valor_diesel = 0
for i in range(1, total_cidades, 1):
    for j in range(i+1, total_cidades+1,1):
        valor_distancia = int(input())
        distancias.append( {"c1":i, "c2":j, "d": valor_distancia} )

cidades_rota = int(input())
for i in range(cidades_rota):
    rota.append(int(input()))

valor_diesel = float(input())

for i in range(len(rota)-1):
    cidade1 = rota[i]
    cidade2 = rota[i+1]
    dist = 0
    for item in distancias:
        if (item["c1"] == cidade1 and item["c2"] == cidade2) or (item["c1"] == cidade2 and item["c2"] == cidade1):
            dist = item["d"]
            break
    distancia_rota += dist

cidade1 = rota[len(rota)-1]
cidade2 = rota[0]
dist = 0
for item in distancias:
    if (item["c1"] == cidade1 and item["c2"] == cidade2) or (item["c1"] == cidade2 and item["c2"] == cidade1):
        dist = item["d"]
        break

distancia_rota += dist

combustivel = distancia_rota / 3

valor_total = combustivel * valor_diesel

print('R$ {:.2f}'.format(valor_total))