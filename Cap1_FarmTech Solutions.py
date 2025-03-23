import os #importando a biblioteca os do python
import json #importando a biblioteca json do python
from time import sleep #<- Importando a função sleep da biblioteca time do python
from math import pi #<- importando o valor de 'pi' com biblioteca de math do python


dados = {'CULTURA':[],
        'AREA':[],
        'INSUMOS':[]}#<- "Tabela de dados" do tipo dict (dictionary) onde são definidas chaves com valores. Explicando de outra forma, é como se as chaves fossem colunas e os valores fossem os dados inseridos na coluna exemplo 

# MENU
try: #<- try é um comando built in do Python cujo ele vai iniciar um bloco de tentantiva de execução do código (caso o arquivo não exista)
    with open(r'C:\Users\Davi\Documents\Projetos\FIAP\FASE 1\FIAP_atividade_cap1\vetor_farmtech_solutions.json', 'x') as arquivo: #<- Atribui uma variavel chamada arquivo com a função open para criar um arquivo novo (método = "x")
        arquivo.write('') #<- Escreve um arquivo vazio
except FileExistsError: #<- except faz parte do bloco "try". Aqui é onde indicamos a excessão (erro) que pode iniciar o codigo dentro desse bloco (caso o arquivo exista)
    print('O arquivo já existe.') #<- Imprime uma mensagem para meu bloco de excessão

#FUNÇÃO DESTINADA A EXIBIÇÃO DE DADOS
def exibir_dados(dicionario): #<- Declarando uma função nova (bloco que executará um conjundo de códigos caso seja chamado em outros pontos da script) / defina exibir_dados(dicionario / dado_externo_necessário) / O nome dicionário é apenas "ficticio", pois qualquer variavel aque atenda as condições necessárias pode ser adicionado nesse espaço

    # Montando cabeçario
    print('\n|INDEX|CULTURA|-----AREA-----|-----INSUMOS-----|')

    # Montando extrutura de pseudotabela
    for idx in range(0, len(dicionario['CULTURA'])): #<- Laço que identificara a quantidade de index presentes na tabela
        print(f"|{idx:<4} | {dicionario['CULTURA'][idx]:<5} | {dicionario['AREA'][idx]:<12} | {dicionario['INSUMOS'][idx]:<15} |") #<- Impressão de dados em formato de tabela

#FUNÇÃO DESTINADA CALCULAR A CULTURA
def inserir_dados(insert: bool = False): #<- Declarando uma nova função (bloco que executará um conjundo de códigos caso seja chamado em outros pontos da script) / defina inserir_dados

    # Declarando variaveis globais (variaveis definidas internamente que podem ser trazidas para fora da função)
    global area, insumo, manejo_insumo, cultura

    # Tentativa
    try: #<- try é um comando built in do Python cujo ele vai iniciar um bloco de tentantiva de execução do código

        # Input da cultura a ser utilizada
        cultura = input('DIGITE A CULTURA QUE DESEJA INCLUIR:\nMILHO\nSOJA\nR:').upper() #<- input de dados de cultura / .upper() coloca os dados inseridos em uppercase(maiusculo)

        # MILHO
        if cultura == 'MILHO': #<- Condição para inicio do bloco (se cultura for igual a MILHO)
            
            # Aviso
            print('\nA cultura escolhida foi o milho.\nA cultura de milho tem a caracteristica de ser cultivada em uma area quadrada com fertilizante.\nA cada m² serão aplicados 100g de fertilizante.')

            # CALCULE A AREA PLANTADA 
            m = int(input('DIGITE EM METROS O TAMANHO DE UM DOS LADOS DA AREA PARA CALCULAR A AREA EM M²: ')) #<-input de dados para calculo de area
            area = round(m ** 2, 2) #<- Calculo da area "quadrado"

            # CALCULE O MANEJO DE INSUMOS
            insumo = 100 #<- Definindo quantidade de insumos baseado no tipo de cultura
            manejo_insumo = round(area * insumo,2) #<- Calculo de insumos

        # SOJA
        elif cultura == 'SOJA': #<- Condição para inicio do bloco (se cultura for igual a SOJA)

            # Aviso
            print('\nA cultura escolhida foi o soja.\nA cultura de soja tem a caracteristica de ser cultivada em uma area redonda com defensivos de soja.\nA cada m² serão pulverizados 500ml de defensivo de soja.')

            # CALCULE A AREA PLANTADA
            r = int(input('DIGITE EM METROS O RAIO DA AREA: ')) #<-input de dados para calculo de area
            area = round(pi * r ** 2,2) #<- Calculo da area "quadrado"

            # CALCULE O MANEJO DE INSUMOS
            insumo = 500 #<- Definindo quantidade de insumos baseado no tipo de cultura
            manejo_insumo = round(area * insumo,2) #<- Calculo de insumos
        else:
            raise(ValueError)
        # ARMAZENE TUDO EM LISTAS
        if insert == True:
            dados['CULTURA'].append(cultura) #<- Inserção dos dados da variavel global "cultura" (definida na função "inserir_dados) na tabela
            dados['AREA'].append(area) #<- Inserção dos dados da variavel global "area" (definida na função "inserir_dados) na tabela
            dados['INSUMOS'].append(manejo_insumo) #<- Inserção dos dados da variavel global "manejo_insumo" (definida na função "inserir_dados) na tabela
    # Excessao
    except ValueError as error: #<- except faz parte do bloco "try". Aqui é onde indicamos a excessão (erro) que pode iniciar o codigo dentro desse bloco
        print('Algum valor foi digitado incorretamente.\nTente novamente') #<- Comando que será executado caso a excessão seja verdadeira
        sleep(3)

while True: #<- Bloco de looping
# LIMPEZA DO TERMINAL
    
    # Apresentação do menu
    print(' '*8,'MENU',' '*8,'\n','-'*22,'\n 1 - Inserir dados\n 2 - Exibir dados\n 3 - Atualizar dados\n 4 - Deletar dados\n 5 - Carregar dados salvos\n 6 - Salvar dados\n 7 - Sair\n','-'*22)#<- Impressão do Menu / a expressão "\n" pula uma linha no print)

    try: #<- try é um comando built in do Python cujo ele vai iniciar um bloco de tentantiva de execução do código
        menu_select = int(input('Qual ação gostaria de executar?\n ')) #<- Input da opção do menu a ser executada

        if menu_select > 7 or menu_select < 1: #< Valida se a opção digitada pelo usuaria está entra 5 e 1 (opções de menu)
            os.system('cls') #<- Realiza limpeza do terminalos.system('cls') #<- Realiza limpeza do terminal
            print('O valor escolhido pelo usuário não corresponde a um indice valido.') #<- Imprime um erro caso a condição proposta acima seja verdadeira
            sleep(1) #<- o código fica parado por 1 segundo 

        else:
        # INSERÇÃO DE DADOS

            # Aqui será trabalhado uma das opções de execução do MENU
            if menu_select == 1: #<- Bloco condicional (se a variavel menu_select for igual a 1, então execute o bloco abaixo)
                
                # Declarando variavel de loop
                resp_menu_1 = True #<- Variavel referencia para looping (variavel booleana)
                
                while resp_menu_1 == True: #<- Bloco de looping (enquanto resp_menu_1 for verdadeiro, o este bloco será executado)
                    inserir_dados(True) #<- Chama a função "inserir_dados" que definimos anteriormente
                    
                    os.system('cls') #<- Realiza limpeza do terminal

                    resp_menu_1 = int(input('\nDESEJA INSERIR DADOS\n1-SIM\n2-NAO\nR: ')) #<- Input da variavel de referencia do looping para determinar se haverá continuidade da execução
                
                
            # EXIBIÇÃO DE DADOS
            elif menu_select == 2: #<- Bloco condicional (se a variavel menu_select for igual a 2, então execute o bloco abaixo)
                os.system('cls') #<- Realiza limpeza do terminal
                exibir_dados(dados) #<- Chama a função "exibir_dados" que definimos anteriormente

                
                input('Para voltar ao MENU pressiona ENTER.') #<- Input que não armazena nenhum dado em variavel. Utilizado apenas para manter a visão da tabela na opção do menu "Exibir dados"
                os.system('cls')#<- Realiza limpeza do terminal

            # ATUALIZAÇÃO DE DADOS
            elif menu_select == 3: #<- Bloco condicional (se a variavel menu_select for igual a 3, então execute o bloco abaixo)
                os.system('cls') #<- Realiza limpeza do terminal

                # Definindo variavel de LOOP
                resp_menu_3 = 1 #<- Variavel referencia para looping (variavel booleana)

                # Looping de atualização de dados
                while resp_menu_3 == True: #<- Bloco de looping (enquanto resp_menu_3 for verdadeiro, o este bloco será executado)
                    exibir_dados(dados) #<- Chama a função "exibir_dados" que definimos anteriormente

                    # Definindo index que será alterado
                    idx = int(input('\nEscolha os dados que deseja alterar: ')) #<- Input de dados para definir qual indice será alterado

                    # Condição para validação de index existente
                    if idx > len(dados)+1 or idx < 0: #< Condicional que verifica se o indice indicado pelo usuário é do que o maior indice apresentado na tabela (len(dados) exibe a quantidade de linhas (indices) presentes na tabela) / ATENÇÃO: Essa não é uma boa forma de executar a proposta, pois pode gerar erros em casos onde o programa tenha que ser mais trabalhado, entretanto, para esse casso funcionará.
                        os.system('cls') #<- Realiza limpeza do terminal
                        print('O valor escolhido pelo usuário não corresponde a um indice valido.') #<- Imprime um erro caso a condição proposta acima seja verdadeira
                        sleep(1) #<- o código fica parado por 1 segundo 

                    else:
                        # Definido novos dados
                        inserir_dados() #<- Chama a função "inserir_dados" que definimos anteriormente

                        # Atualização dos dados da lista
                        dados['CULTURA'][idx] = cultura #<- Utiliza a variavel "idx" para acessar um indice da tabela "dados" e aplicar o valor da variavel global "cultura" utilizando o operador de atribuição "="
                        dados['AREA'][idx] = area #<- Utiliza a variavel "idx" para acessar um indice da tabela "dados" e aplicar outro valor utilizando o operador de atribuição "="
                        dados['INSUMOS'][idx] = manejo_insumo #<- Utiliza a variavel "idx" para acessar um indice da tabela "dados" e aplicar outro valor utilizando o operador de atribuição "="

                    resp_menu_3 = int(input('Desja atualizar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: ')) #<- Input da variavel de referencia do looping para determinar se haverá continuidade da execução

                os.system('cls') #<- Chama a função "exibir_dados" que definimos anteriormente


            # EXCLUSÃO DE DADOS
            elif menu_select == 4: #<- Bloco condicional (se a variavel menu_select for igual a 4, então execute o bloco abaixo)
                
                resp_menu_4 = True #<- Variavel referencia para looping (variavel booleana)
                while resp_menu_4 == True: #<- Bloco de looping (enquanto resp_menu_4 for verdadeiro, o este bloco será executado)
                    exibir_dados(dados) #<- Chama a função "exibir_dados" que definimos anteriormente

                    # Definindo index que será alterado
                    idx = int(input('\nEscolha os dados que deseja excluir da tabela: ')) #<- Input de dados para definir qual indice será alterado

                    # Condição para validação de index existente
                    if idx > len(dados)+1 or idx < 0: #< Condicional que verifica se o indice indicado pelo usuário é do que o maior indice apresentado na tabela (len(dados) exibe a quantidade de linhas (indices) presentes na tabela) / ATENÇÃO: Essa não é uma boa forma de executar a proposta, pois pode gerar erros em casos onde o programa tenha que ser mais trabalhado, entretanto, para esse casso funcionará.
                        os.system('cls') #<- Realiza limpeza do terminal
                        print('O valor escolhido pelo usuário não corresponde a um indice valido.') #<- Imprime um erro caso a condição proposta acima seja verdadeira
                        sleep(1) #<- o código fica parado por 1 segundo 
                    else:#<- Condicional de retorno de valor falso

                    # Atualização dos dados da lista
                        dados['CULTURA'].pop(idx) #<- Utiliza o "pop" para deletar os dados com base na variavel "idx" para acessar um indice da tabela "dados"
                        dados['AREA'].pop(idx) #<- Utiliza o "pop" para deletar os dados com base na variavel "idx" para acessar um indice da tabela "dados"
                        dados['INSUMOS'].pop(idx) #<- Utiliza o "pop" para deletar os dados com base na variavel "idx" para acessar um indice da tabela "dados"

                    # Atualização variavel de loop (utilizado para determinar se devemos continuar)
                    resp_menu_4 = int(input('Desja deletar mais algum dado da tabela?\n1-SIM\n2-NAO\nR: ')) #<- Input da variavel de referencia do looping para determinar se haverá continuidade da execução
                    
                os.system('cls') #<- Realiza limpeza do terminal
            elif menu_select == 5:
                os.system('cls')
                path = input('INSIRA O CAMINHO ONDE OS DADOS QUE DESEJA CARREGAR ESTÃO SALVOS:\n') #<- Input do caminho onde o arquivo foi salvo
                with open(rf'{path}', 'r') as arquivo: #<- Cria uma variavel com o nome "arquvio" e salva e cria um bloco de atividades relacionadas a variavel
                    dados = json.load(arquivo) #<- Carrega arquivo JSON
                os.system('cls')

            elif menu_select == 6:
                os.system('cls') #<- Realiza limpeza do terminal
                path = input('INSIRA UM CAMINHO ONDE DESEJA SALVAR OS DADOS:\n') #<- Input do caminho onde o arquivo foi salvo
                with open(rf'{path}\vetor_farmtech_solutions.json', 'w') as arquivo: #<- Cria uma variavel com o nome "arquvio" e salva e cria um bloco de atividades relacionadas a variavel
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4) #<- Carrega arquivo JSON
                os.system('cls')
                
            # # EXIT
            elif menu_select == 7: #<- Bloco condicional (se a variavel menu_select for igual a 5, então execute o bloco abaixo)
                os.system('cls') #<- Realiza limpeza do terminal
                q = int(input('VOCÊ FECHARÁ A EXECUÇÃO DO PROGRAMA E TODOS OS DADOS UTILIZADOS SERÃO PERDIDO\nDESEJA SALVAR?\n1-SIM\n2-NAO\nR:'))
                if q == 1: #<- Condicional de verificação de dados boleanos
                    path = input('INSIRA O CAMINHO ONDE OS DADOS QUE DESEJA CARREGAR ESTÃO SALVOS:\n') #<- Input do caminho onde o arquivo foi salvo
                    with open(rf'{path}\vetor_farmtech_solutions.json', 'r') as arquivo: #<- Cria uma variavel com o nome "arquvio" e salva e cria um bloco de atividades relacionadas a variavel
                        dados = json.load(arquivo) #<- Carrega arquivo JSON
                    os.system('cls')#<- Realiza limpeza do terminal
                    print('Dados salvos com sucesso!. O programa sera desligado em 5 segundos.')
                    sleep(6)
                elif q > 2: #<- Verifica se a variavel q é maior do que as opções fornecidas
                    continue #<- Para o bloco condicional, entretanto continua a execução do código
                else: #<- Condicional de retorno de valor falso
                    pass #< não realiza nenhuma ação
                exit() #<- Termina a execução
                
    except ValueError:#<- except faz parte do bloco "try". Aqui é onde indicamos a excessão (erro) que pode iniciar o codigo dentro desse bloco
        os.system('cls') #<- Realiza limpeza do terminal
        print('O valor escolhido pelo usuário não corresponde a um indice valido.')
        sleep(2) #<- o código fica parado por 2 segundo
        os.system('cls') #<- Realiza limpeza do terminal

