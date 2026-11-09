class Management:
    def __init__(self):
        self.tasks = []
        self.translate_priority = {
            "1": "baixa",
            "2": "média",
            "3": "alta"
        }
    def add_tasks(self):
                task = input('Write your task: ').lower().strip()
                if not isinstance(task, str) or task == '':
                    raise ValueError('Task must be a string.')
                elif task == '':
                    return('Tasks can not be empty.')
                else:
                    print(f' Task {task} added to the list')
                situation = input('Write the situation of your task [ completed / pending ]').strip().lower()
                if situation not in ('pending', 'completed'):
                    return('Situation must be "pending" or "completed".')
                    
                priority_option = input('Write the priority of your task [ 1 -  low | 2 - medium | 3 - high ]')
                priority =  self.translate_priority[priority_option]
                new_task = {'title': task,
                            'situation': situation,
                            'priority': priority}
                self.tasks.append(new_task)
                

    def delete_tasks(self):
                task_to_delete = input('Write the task to delete: ').strip()
                for t in self.tasks:
                    if t['title'] == task_to_delete:
                        self.new_tasks.remove(t)  
                        print(f'Task "{task_to_delete}" has been deleted!')
                    else:
                         return('Task not found')
              
                 

    def show_priorities(self):
                print('---ALL TASKS---')
                if not self.tasks:
                    return 'Tasks not found.'
                else:
                    for t in self.tasks:
                        print(f' title: {t['title']} | situation: {t['situation']} | priority: {t['priority']} ')
                        

    def uptade(self):
                    
        while True:
            print('---UPTADE TASKS---')
            task = input('Which task you want to uptade? ').lower().strip()
            
            task_found = False
            for t in self.tasks:
                if t['title'] == task:
                    task_found = True
                    new_situation = input('Which situation you want to update? [ completed / pending ]: ').strip().lower()
                    
                    if new_situation not in ('completed', 'pending'):
                        print('❌ Write "completed" or "pending"')
                    else:
                        t['situation'] = new_situation
                        print(f'🔄 Situation of "{task}" updated to "{new_situation}"!')
                    break  # Sai do loop for após processar a tarefa encontrada
            
            if not task_found:
                print('⚠ Task not found.')
                
            # Pergunta se quer continuar e controla o while True principal corretamente
            option = input('Do you want to uptade more tasks? [Y/N]: ').strip().upper()
            if option != 'Y':
                print("Exiting update screen...")
                break  # Sai do while True se o usuário digitar N (ou qualquer coisa diferente de Y)

                        

a = Management()
a.add_tasks()
a.uptade()
a.add_tasks()
a.add_tasks()
a.delete_tasks()
a.show_priorities()
                        