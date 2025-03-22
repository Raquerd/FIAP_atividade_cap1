install.packages(jsonlite)
install.packages(glue)
install.packages(jsonlite)
library(jsonlite)
library(dplyr)
library(glue)

#Input do caminho dos dados salvos
path <- readline(prompt = "Insira o destino onde o arquivo foi salvo: ")

#Trazendo dados JSON para o formato DATA FRAME
dados <- data.frame(fromJSON(path))

print(dados)

#Calculo de média de insumos
media_insumos_milho <- mean((dados %>% filter(dados$CULTURA == "MILHO"))$INSUMOS)
media_insumos_soja <- mean((dados %>% filter(dados$CULTURA == "SOJA"))$INSUMOS)

desvio_insumos_milho <- sd((dados %>% filter(dados$CULTURA == "MILHO"))$INSUMOS)
desvio_insumos_soja <- sd((dados %>% filter(dados$CULTURA == "SOJA"))$INSUMOS)

#Calculo de desvio de insumos
print(glue("Media de defensivos de soja: {media_insumos_soja}\nMedia de fertilizantes utilizados na cultura de milho: {media_insumos_milho}"))
print(glue("Media de desvio de insumos de defensivo de soja: {desvio_insumos_soja}\nMedia de desvio insumos de fertilizante de milho: {desvio_insumos_milho}"))
