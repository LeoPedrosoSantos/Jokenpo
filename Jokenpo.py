import random

Jokenpo = ["Pedra", "Papel", "Tesoura"]

Tu = input("Escolha entre 0(Pedra), 1(Papel), 2(Tesoura): ")

Tu = int(Tu)

if Tu == 0:
    Tu = Jokenpo[0]
elif Tu == 1:
    Tu = Jokenpo[1]
elif Tu == 2:
    Tu = Jokenpo[2]


IA = random.randint(0, 2)

if IA == 0:
    IA = Jokenpo[0]
elif IA == 1:
    IA = Jokenpo[1]
elif IA == 2:
    IA = Jokenpo[2]
    
print("\nA sua escolha foi:", Tu)
print("\nA escolha da IA foi:", IA)

if Tu == Jokenpo[0] and IA == Jokenpo[2]: 
    print("\nVocê venceu! :D")
elif Tu == Jokenpo[1] and IA == Jokenpo[0]: 
    print("\nVocê venceu! :D")
elif Tu == Jokenpo[2] and IA == Jokenpo[1]: 
    print("\nVocê venceu! :D")
elif Tu == IA:
    print("\nEmpate! '-'")
else:  
    print("\nVocê perdeu! :(")

Fechar = input("\nAperte enter para finalizar!")