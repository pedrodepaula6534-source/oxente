# ==========================================
#         OXENTE NA COZINHA
# ==========================================

print("=" * 45)
print("     BEM-VINDO AO OXENTE NA COZINHA")
print("=" * 45)

receitas = []

receitas.append("Baião de Dois")
receitas.append("Acarajé")
receitas.append("Tapioca")
receitas.append("Carne de Sol")
receitas.append("Escondidinho")
receitas.append("Moqueca Baiana")
receitas.append("Cuscuz Nordestino")
receitas.append("Sarapatel")
receitas.append("Buchada de Bode")
receitas.append("Vatapá")

while True:

    print("\n========== MENU ==========")

    for i in range(len(receitas)):
        print(f"{i+1} - {receitas[i]}")

    print("0 - Sair")

    opcao = input("\nDigite uma opção: ")

    if opcao == "1":
        print("\n--- Baião de Dois ---")

        ingredientes = []
        ingredientes.append("2 xícaras de arroz")
        ingredientes.append("1 xícara de feijão")
        ingredientes.append("Queijo coalho")
        ingredientes.append("Carne seca")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "2":
        print("\n--- Acarajé ---")

        ingredientes = []
        ingredientes.append("Feijão fradinho")
        ingredientes.append("Cebola")
        ingredientes.append("Azeite de dendê")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "3":
        print("\n--- Tapioca ---")

        ingredientes = []
        ingredientes.append("Goma de tapioca")
        ingredientes.append("Coco ralado")
        ingredientes.append("Queijo")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "4":
        print("\n--- Carne de Sol ---")

        ingredientes = []
        ingredientes.append("Carne de sol")
        ingredientes.append("Mandioca")
        ingredientes.append("Manteiga")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "5":
        print("\n--- Escondidinho ---")

        ingredientes = []
        ingredientes.append("Purê de mandioca")
        ingredientes.append("Carne seca")
        ingredientes.append("Queijo")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "6":
        print("\n--- Moqueca Baiana ---")

        ingredientes = []
        ingredientes.append("Peixe")
        ingredientes.append("Leite de coco")
        ingredientes.append("Azeite de dendê")

        ingredientes.append("Pimentão")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "7":
        print("\n--- Cuscuz Nordestino ---")

        ingredientes = []
        ingredientes.append("Flocão de milho")
        ingredientes.append("Água")
        ingredientes.append("Sal")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "8":
        print("\n--- Sarapatel ---")

        ingredientes = []
        ingredientes.append("Miúdos")
        ingredientes.append("Temperos")
        ingredientes.append("Pimentão")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "9":
        print("\n--- Buchada de Bode ---")

        ingredientes = []
        ingredientes.append("Carne de bode")
        ingredientes.append("Temperos")
        ingredientes.append("Verduras")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "10":
        print("\n--- Vatapá ---")

        ingredientes = []
        ingredientes.append("Camarão")
        ingredientes.append("Pão")
        ingredientes.append("Leite de coco")
        ingredientes.append("Azeite de dendê")

        print("\nIngredientes:")
        for item in ingredientes:
            print("-", item)

    elif opcao == "0":
        print("\nObrigado por usar o OXENTE NA COZINHA!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
        break 