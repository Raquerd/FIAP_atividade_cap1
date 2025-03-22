library(jsonlite, dplyr)

#Input do caminho dos dados salvos
path <- readline(prompt = "Insira o destino onde o arquivo foi salvo: ")

#Trazendo dados JSON para o formato DATA FRAME
dados <- data.frame(fromJSON(path))

print(dados)

# Input de cultura a ser calculada
cultura <- readline(prompt="Possuimos dois tipos de cultura do qual podemos realizar os calculos estatisticos\nMILHO\nSOJA\nDigite a cultura que deseja utilizar: ")


media_insumos = mean(dados %>% filter(dados$INSUMOS == cultura))
media_insumos = mean(dados %>% filter(dados$INSUMOS == cultura))

print("Media de defensivos de soja")