def exibir_voltar():
    #Função auxiliar para exibir a opção de voltar ao menu
    voltar = input("\nDeseja voltar ao menu anterior? (sim/não): ").strip().lower()
    if voltar != "sim":
        return False
    return True

def detalhes_projeto(razao_social, setor, localizacao, ano, descricao, beneficios):
    while True:
        #exibe os detalhes do projeto escolhido
        print(f"\n📝 Razão Social: {razao_social}")
        print(f"🏢 Setor de Atuação: {setor}")
        print(f"📍 Localização: {localizacao}")
        print(f"📅 Ano Fundado: {ano}")
        print(f"📜 Descrição: {descricao}")
        print(f"💡 Benefícios:\n{beneficios}")
        print("Opções:")
        print("1. 🌐 Visitar o site da empresa")
        print("2. 📝 Se inscrever no projeto")
        print("3. ↩️ Voltar")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            print("🌐 Visitando o site da empresa... (Funcionalidade em desenvolvimento)")
        elif escolha == "2":
            print("\n🔗 Link para o formulário de inscrição:")
            print("https://forms.gle/4m962qT2J1omNKVz7")  #link real do formulári de inscrição
        elif escolha == "3":
            return  #te retorna para o menu de projetos
        else:
            print("❌ Opção inválida. Tente novamente.")

        if not exibir_voltar():
            break  #se o usuário não quiser voltar, sai do loop

def menu_projetos():
    print("\n🚀 Bem-vindo à seção PROJETOS!")
    projetos = [
        {"nome": "SolarTech Energia", "setor": "Energia Solar", "localizacao": "São Paulo, SP", "ano": 2012,
         "descricao": "A SolarTech é uma empresa líder no setor de energia renovável, especializada em soluções de energia solar.\n"
                      "Nosso compromisso é com a sustentabilidade e inovação, proporcionando sistemas eficientes para um futuro mais verde.",
         "beneficios": "1. 💰 Economia de Energia: Reduza sua conta em até 95%.\n"
                       "2. 🌱 Sustentabilidade: Contribua para o meio ambiente com fontes renováveis.\n"
                       "3. 📈 Investimento de Longo Prazo: Retorno rápido e baixo custo de manutenção."},
        {"nome": "Ventus Energia", "setor": "Energia Eólica", "localizacao": "Porto Alegre, RS", "ano": 2018,
         "descricao": "A Ventus Energia foca no desenvolvimento de soluções de energia eólica, utilizando o vento para gerar eletricidade limpa e renovável.\n"
                      "Com tecnologia de ponta, buscamos eficiência e inovação para proporcionar energia limpa e economia.",
         "beneficios": "1. 💰 Economia de Energia: Reduza seus custos com energia elétrica.\n"
                       "2. 🌍 Sustentabilidade: Aumente sua responsabilidade ambiental.\n"
                       "3. 🛠️ Instalação Rápida: Baixo custo e instalação simplificada."}
    ]

    while True:
        #exibe os projetos disponíveis
        for i, projeto in enumerate(projetos, start=1):
            print(f"{i}. {projeto['nome']} - {projeto['setor']}")

        print("3. ↩️ Voltar ao menu principal")

        escolha = input("Escolha um projeto para saber mais: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= 2:
            projeto = projetos[int(escolha) - 1]
            detalhes_projeto(projeto["nome"], projeto["setor"], projeto["localizacao"], projeto["ano"],
                             projeto["descricao"], projeto["beneficios"])
        elif escolha == "3":
            return  #te retorna ao menu principal
        else:
            print("❌ Opção inválida. Tente novamente.")

        if not exibir_voltar():
            break  #sai se o usuário não quiser voltar

def menu_principal():
    print("🌞🌱Olá, seja bem-vindo(a) ao projeto EcoEnergy!")
    print("Estamos muito felizes em ter você aqui. Aproveite o conteúdo e sinta-se à vontade para\n"
          "    explorar todas as novidades. Se precisar de algo, estamos à disposição!\n")

    while True:
        #exibe as seções principais
        secao = input("Escolha a seção que você deseja acessar:\n"
                      "INICIO - PROJETOS - EQUIPE - SUGESTÕES\n").strip().upper()

        #te redireciona para a seção escolhida
        if secao == "INICIO":
            menu_inicio()
        elif secao == "PROJETOS":
            menu_projetos()
        elif secao == "EQUIPE":
            menu_equipe()
        elif secao == "SUGESTÕES":
            menu_sugestoes()
        else:
            print("❌ Opção inválida. Tente novamente.")

        #opção para retornar ou sair
        if not exibir_voltar():
            print("Obrigado por visitar a EcoEnergy! Até mais! 👋")
            break

def menu_inicio():
    print("\n🚀 Bem-vindo à seção INÍCIO!")
    while True:
        escolha = input("Escolha uma subseção:\n"
                        "1. 🌞Vantagens de usar energia solar\n"
                        "2. 🔢Cálculo Solar\n"
                        "3. 💸Reduzir Custos com Energia Sustentável\n"
                        "4. 📝Sua opinião Importa!\n"
                        "5. Voltar ao menu principal ↩️\n").strip()

        if escolha == "1":
            #exibindo as vantagens de usar energia solar
            mostrar_vantagens()
        elif escolha == "2":
            #chamando a função para cálculo solar
            calculo_solar()
        elif escolha == "3":
            print("\n💸 Reduza custos com energia sustentável:")
            print("Visite a seção PROJETOS para saber mais! 🌱")
        elif escolha == "4":
            print("\nSua opinião é importante para nós! 📝")
            print("Visite a seção SUGESTÕES para compartilhar suas ideias.")
        elif escolha == "5":
            return  #volta direto ao menu principal
        else:
            print("❌ Opção inválida. Tente novamente.")

        voltar = input("Deseja voltar ao menu INÍCIO? (sim/não): ").strip().lower()
        if voltar != "sim":
            break


def mostrar_vantagens():
    #Mostra as vantagens de usar energia solar
    print("\n🌞 Vantagens de usar energia solar:")
    print("1. 💸Economia: Com a energia solar, você pode reduzir sua conta de energia mensal")
    print("2. 🌱Sustentabilidade: Contribui para o meio ambiente usando uma energia limpa e renovável")
    print("3. 🔋Autossuficiência: Com a energia solar, você pode se tornar menos dependente da rede elétrica")


def calculo_solar():
    #Função para cálculo solar com base nas informações do usuário
    print("\n📊 Bem-vindo à ferramenta de Cálculo Solar!")
    print("Forneça informações principais para personalizar os resultados! 🌞")

    try:
        #solicita informações do usuário
        capacidade_sistema = float(input("⚡ Capacidade do Sistema Solar (kW): "))
        horas_sol_por_dia = float(input("☀️ Horas de Sol por Dia: "))
        consumo_mensal = float(input("🔌 Consumo Mensal (kWh): "))
        custo_por_kwh = float(input("💰 Custo por kWh (R$): "))

        #verifica se os valores são válidos
        if capacidade_sistema <= 0 or horas_sol_por_dia <= 0 or consumo_mensal <= 0 or custo_por_kwh <= 0:
            print("❌ Por favor, insira valores positivos para todos os campos.")
            return

        #calculando a produção anual do sistema solar
        producao_anual = capacidade_sistema * horas_sol_por_dia * 365

        #calculando o consumo anual
        consumo_anual = consumo_mensal * 12

        #calculando a economia potencial
        diferenca = producao_anual - consumo_anual
        economia_potencial = diferenca * custo_por_kwh if diferenca > 0 else 0

        #mostrando os resultados
        print("\n💰Resultados do Cálculo Solar:")
        print(f"Produção Anual do Sistema Solar: {producao_anual:.2f} kWh")
        print(f"Consumo Anual: {consumo_anual:.2f} kWh")
        print(f"Diferença (Economia Potencial): {diferenca:.2f} kWh")
        print(f"Economia Potencial: R${economia_potencial:.2f}")

    except ValueError:
        print("❌ Erro: Por favor, insira valores numéricos válidos.")

def menu_equipe():
    print("\n👥 Bem-vindo à seção EQUIPE! 👥")  #Mostrando informações da equipe
    equipe = [
        {"nome": "Sulamita Viegas dos Santos", "email": "rm561089@fiap.com.br",
         "github": "https://github.com/Sulamita020905",
         "linkedin": "https://br.linkedin.com/in/sulamita-viegas-dos-santos-280210223?trk=people-guest_people_search-card"},
        {"nome": "Matteus Viegas dos Santos", "email": "rm561090@fiap.com.br",
         "github": "https://github.com/matteusviegas",
         "linkedin": "https://br.linkedin.com/in/matteus-viegas-533437294?trk=public_profile_samename-profile"}
    ]
    for membro in equipe:
        print(f"\n👤 Nome: {membro['nome']}")
        print(f"📧 Email: {membro['email']}")
        print(f"💻 GitHub: {membro['github']}")
        print(f"🔗 LinkedIn: {membro['linkedin']}")
    input("\nPressione Enter para voltar ao menu principal...")

def menu_sugestoes():
    print("\n💡 Seção de SUGESTÕES 💡")
    print("Queremos ouvir sua opinião! Se você tem ideias para projetos ou melhorias, compartilhe conosco! ✨")
    print("📝 Formulário: [https://forms.gle/ZykhLviAh3RsY4xq8]")  #Link do formulário de sugestões
    input("\nPressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    menu_principal()