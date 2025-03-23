install.packages(jsonlite)
install.packages(glue)
install.packages(dplyr)
install.packages("httr")
library(jsonlite)
library(dplyr)
library(glue)
library("httr")

#Input do caminho dos dados salvos
path <- readline(prompt = "Insira o destino onde o arquivo foi salvo: ")

#Trazendo dados JSON para o formato DATA FRAME
dados <- data.frame(fromJSON(path))

print(dados)

#API - Configurações iniciais
cidade <- "São Paulo"
API_KEY <- "7621dd8760f87d562a4e5a21bffbdc36"
API_ID <- paste0("https://api.openweathermap.org/data/2.5/weather?q=",cidade,"&appid=",API_KEY)
API_ID <- URLencode(API_ID)
request <- httr::GET(API_ID)
#print(content(request,"text"))

database_weather <- fromJSON(content(request, "text"))
print(database_weather)

#Calculo de média de insumos
media_insumos_milho <- mean((dados %>% filter(dados$CULTURA == "MILHO"))$INSUMOS)
media_insumos_soja <- mean((dados %>% filter(dados$CULTURA == "SOJA"))$INSUMOS)

desvio_insumos_milho <- sd((dados %>% filter(dados$CULTURA == "MILHO"))$INSUMOS)
desvio_insumos_soja <- sd((dados %>% filter(dados$CULTURA == "SOJA"))$INSUMOS)

#Impressão de dados de insumos
print(glue("Media de defensivos de soja: {media_insumos_soja}\nMedia de fertilizantes utilizados na cultura de milho: {media_insumos_milho}"))
print(glue("Media de desvio de insumos de defensivo de soja: {desvio_insumos_soja}\nMedia de desvio insumos de fertilizante de milho: {desvio_insumos_milho}"))

#Impressão dos dados meteorológicos
print(glue("CIDADE: {database_weather$name}\nTEMPO: {database_weather$weather$description}\nTEMPERATURA: {database_weather$main$temp - 273.15}\nSENSAÇÃO TERMICA: {database_weather$main$feels_like - 273.15}\nUMIDADE: {database_weather$main$humidity}%"))
