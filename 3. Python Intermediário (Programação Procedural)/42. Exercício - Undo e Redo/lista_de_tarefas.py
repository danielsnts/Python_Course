def listar_tarefas(tasks):
    print()
    for i, item in enumerate(tasks):
        print(f'{i+1} {item}')
    print()


def adicionar_tarefas(lista, tarefa):
    lista.append(tarefa)


def desfazer_tarefa(task_list, aux_list):
    if not task_list:  # Verifica se a lista etá vazia
        print('Não há o o que desfazer:\t')
    else:
        ultima_tarefa = task_list.pop()  # Remove a ultima tarefa da lista principal e guarda
        aux_list.append(ultima_tarefa)


def refazer_tarefa(task_list, aux_list):
    if not aux_list:  # Verifica se a lista etá vazia
        print('Não há o o que refazer:\t')
    else:
        ultima_tarefa = aux_list.pop()  # Remove a ultima tarefa da lista auxiliar e guarda
        task_list.append(ultima_tarefa)


lista_tarefas = [1, 11, 111, 222]  # Lista de tarefas
lista_reserva = []  # Lista auxiliar

while True:
    print(f'lista_tarefas = {lista_tarefas}')
    print(f'lista_reserva = {lista_reserva}')
    comando = input('Insira uma tarefa cou comando [undo, redo, ls]\n')

    if comando == 'undo':  # Defazer
        desfazer_tarefa(lista_tarefas, lista_reserva)
        continue  # O loop volta daqui
    elif comando == 'redo':  # Refazer
        refazer_tarefa(lista_tarefas, lista_reserva)
        continue
    elif comando == 'ls':
        listar_tarefas(lista_tarefas)
        continue

    adicionar_tarefas(lista_tarefas, comando)
