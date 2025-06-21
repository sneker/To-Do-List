
def mostrar_menu():
    print("\n--- To-Do List ---")
    print("1. Ver tarefas")
    print("2. Adicionar tarefa")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Sair")


lista =[]
dici ={}
def Adicionar_tarefas():
     dici['texto']=str(input('Descrição da tarefa: '))
     dici['concluido'] = '❌'
     lista.append(dici.copy())
     
def Concluido():
    ver_tarefa()
    con = int(input('Qual deseja marcar como concluido:'))
    lista[con]['concluido']='✅'

def ver_tarefa():
    for c,v in enumerate(lista):
        print(f'{c}. {v['concluido']} {v['texto']} ')

while True :
    mostrar_menu()
    resposta = int(input('Qual opção Voce deseja: '))

    if resposta == 2:
        Adicionar_tarefas()
    elif resposta ==1:
        ver_tarefa()
    elif resposta ==3:
        Concluido()
    elif resposta ==5:
        break





