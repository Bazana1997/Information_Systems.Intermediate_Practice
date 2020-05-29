class View:
    def start(self):
        print('______________________________')
        print('|         CLONOPOLIS         |')       
        print('------------------------------')

    def end(self):
        print('****************************')
        print('*    ¡Hasta la proxima!    *')
        print('****************************')
    
    def menu_principal(self):
        print('*************************')
        print('* -- Menu principal --  *')
        print('*************************')
        print('1. Inicio de sesion usuario')
        print('2. Inicio de sesion administrador')
        print('3. Registrar usuario nuevo')
        print('4. Salir')

    def menu_admin(self):
        print('****************************')
        print('*        MENU ADMIN        *')
        print('****************************\n')
        print(' 1. Funciones')
        print(' 2. Peliculas')
        print(' 3. Sala')
        print(' 4. Butaca')
        print(' 5. Entrada')
        print(' 6. Usuarios')
        print(' 7. Salir')

    def menu_funciones(self):
        print('****************************')
        print('*        MENU Funciones    *')
        print('****************************\n')
        print(' 1. Crear funciones')
        print(' 2. Ver funciones')
        print(' 3. Editar funciones')
        print(' 4. Eliminar funciones')
        print(' 5. Salir')

    def menu_peliculas(self):
        print('****************************')
        print('*        MENU PELICULAS    *')
        print('****************************\n')
        print(' 1. Crear pelicula')
        print(' 2. Ver peliculas')
        print(' 3. Editar pelicula')
        print(' 4. Eliminar pelicula')
        print(' 5. Salir')

    def menu_salas(self):
        print('****************************')
        print('*        MENU SALAS      *')
        print('****************************\n')
        print(' 1. Crear sala')
        print(' 2. Ver salas')
        print(' 3. Editar sala')
        print(' 4. Eliminar sala')
        print(' 5. Salir')

    def menu_butaca(self):
        print('****************************')
        print('*        MENU BUTACAS      *')
        print('****************************\n')
        print(' 1. Crear butaca')
        print(' 2. Ver butacas')
        print(' 3. Editar butaca')
        print(' 4. Eliminar butaca')
        print(' 5. Salir')

    def menu_usuario(self):
        print('****************************')
        print('*        MENU USUARIO      *')
        print('****************************\n')
        print(' 1. Crear usuario')
        print(' 2. Ver usuarios')
        print(' 3. Editar usuario')
        print(' 4. Eliminar usuario')
        print(' 5. Crear administrador')
        print(' 6. Ver administrador')
        print(' 7. Editar administrador')
        print(' 8. Eliminar administrador')
        print(' 9. Salir')
    
    def menu_Ticket(self):
        print('****************************')
        print('*        MENU TICKET      *')
        print('****************************\n')
        print(' 1. Crear Ticket')
        print(' 2. Ver Tickets')
        print(' 3. Editar Ticket')
        print(' 4. Eliminar Ticket')
        print(' 5. Salir')

    def menu_user(self):
        print('****************************')
        print('*        MENU ClIENTE      *')
        print('****************************\n')
        print(' 1. Ver funciones')
        print(' 2. Ver funciones por hora')
        print(' 3. Ver funciones por fecha')
        print(' 4. ver funciones por pelicula')
        print(' 5. Ver pelicula')
        print(' 6. Comprar entrada')
        print(' 7. Ver entrada')
        print(' 8. Salir')


    def input(self, campo):
        print('> Ingrese '+ campo+': ', end='')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')
     
    def not_valid_option(self):
        print('¡Opcion no valida!/n Intenta de nuevo')
     
    def ask(self, output):
        print(output, end = '')   

    def msg(self, output):
        print(output)     

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +') 
        print('+'*(len(str(id))+len(op)+24))     

    def err(self, output):
        print('\nERROR - ', output,'\n')

    def mostrar_pelicula(self, record):
        print('ID:', record[0])
        print('Titulo:', record[1])
        print('Genero:', record[2])
        print('Duracion:', record[3])
        print('Idioma:', record[4])

    def mostrar_pelicula_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_pelicula_midder(self):
        print('-'*48)
    
    def mostrar_pelicula_footer(self):
        print('*'*48)

    def mostrar_usuario(self, record):
        print('ID:', record[0])
        print('Nomnre:', record[1])
        print('Email:', record[2])
        print('Num:', record[3])
        print('password:', record[4])

    def mostrar_usuario_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_usuario_midder(self):
        print('-'*48)
    
    def mostrar_usuario_footer(self):
        print('*'*48)

    def mostrar_admin(self, record):
        print('ID:', record[0])
        print('Nomnre:', record[1])
        print('Email:', record[2])
        print('Num:', record[3])
        print('password:', record[4])

    def mostrar_admin_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_admin_midder(self):
        print('-'*48)
    
    def mostrar_admin_footer(self):
        print('*'*48)

    def mostrar_sala(self, record):
        print('ID:', record[0])
        print('Asientos:', record[1])
        print('Tipo',record[2])

    def mostrar_sala_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_sala_midder(self):
        print('-'*48)
    
    def mostrar_sala_footer(self):
        print('*'*48)

    def mostrar_butaca(self, record):
        print('ID:', record[0])
        print('Estado:', record[1])

    def mostrar_butaca_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_butaca_midder(self):
        print('-'*48)
    
    def mostrar_butaca_footer(self):
        print('*'*48)
    
    def mostrar_funcion(self, record):
        print('Id_Funcion: ', record[0])
        print('Id_Pelicula: ', record[1])
        print('Id_Sala: ', record[2])
        print('fecha: ', record[3])
        print('horario: ', record[4])
        print('Titulo de la pelicula: ', record[5])

    def mostrar_funcion_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_funcion_midder(self):
        print('-'*48)
    
    def mostrar_funcion_footer(self):
        print('*'*48)

    def mostrar_Ticket(self, record):
        print('Id_Ticket: ', record[0])
        print('Id_Pelicula: ', record[1])
        print('Id_Sala: ', record[2])
        print('horario: ', record[3])

    def mostrar_Ticket_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_Ticket_midder(self):
        print('-'*48)
    
    def mostrar_Ticket_footer(self):
        print('*'*48)

    def mostrar_tickets(self, record):
        print('Id_tickets: ', record[0])
        print('Id_Pelicula: ', record[1])
        print('Id_Sala: ', record[2])
        print('butaca: ', record[3])

    def mostrar_tickets_header(self, header):
          print(header.center(48,'*'))
          print('-'*48)

    def mostrar_tickets_midder(self):
        print('-'*48)
    
    def mostrar_tickets_footer(self):
        print('*'*48)

    