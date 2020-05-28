from Model.model import Model
from View.view import View
from datetime import date
import os

class Controller:
    
    """
    ************************************
    *  Controlador para cine Db        *
    ************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
     
    def start(self):
        self.view.start()
        self.menu_principal()

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f, v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals


    clear = lambda: os.system('cls') #on Windows System

    """
    ************************************
    *   Controladores inicio/registro  *
    ************************************
    """
    def menu_principal(self):
        os.system ("cls") 
        o = '0'
        while o != '4':
            self.view.menu_principal()
            self.view.option('4')
            o = input()
            if o == '1':
                self.inicio_sesion_usuario()
            elif o == '2':
                self.inicio_sesion_administrador()
            elif o == '3':
                self.registro_usuario()
            elif o == '4':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_inicio(self):
        self.view.ask('Email: ')
        Email = input()
        self.view.ask('Password: ')
        password = input()
        return [Email, password]


    def inicio_sesion_usuario(self):
        Email, password = self.ask_inicio()
        usuario = self.model.leer_usuario_email_password(Email, password)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header('Datos de tu usuario')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
            self.menu_user()
        else:
            if usuario == None:
                self.view.err('El EMAIL O EL PASSWORD SON INCORRECTOS')
            else: 
                self.view.err('PROBLEMA AL LEER EL USUARIO. REVISA.')
            return

    def inicio_sesion_administrador(self):
        Email, password = self.ask_inicio()
        administrador = self.model.leer_administrador_email_password(Email, password)
        if type(administrador) == tuple:
            self.view.mostrar_admin_header('Datos de tu administrador')
            self.view.mostrar_admin(administrador)
            self.view.mostrar_admin_midder()
            self.view.mostrar_admin_footer()
            self.menu_admin()
        else:
            if administrador == None:
                self.view.err('El EMAIL O EL PASSWORD SON INCORRECTOS')
            else: 
                self.view.err('PROBLEMA AL LEER EL administrador. REVISA.')
            return          

    def registro_usuario(self):
        print('registo de usuarios')
        self.view.input('Nombre')
        Nombre = input()
        self.view.input('Email')
        Email = input()
        self.view.input('Contraseña')
        password = input()
        self.view.input('Telefono')
        Num = input()

        result = self.model.crear_usuario(Nombre, Email, password, Num)
        if result == True:
            self.view.msg('Usuario creado')
        else:
            self.view.err(result)

    def registro_admin(self):
        print('registo de administradores')
        self.view.input('Nombre')
        Nombre = input()
        self.view.input('Email')
        Email = input()
        self.view.input('Contraseña')
        password = input()
        self.view.input('Telefono')
        Num = input()

        result = self.model.crear_admin(Nombre, Email, password, Num)
        if result == True:
            self.view.msg('Administrador creado')
        else:
            self.view.err(result)
    
    """
    ************************************
    *       Controladores usuario      *
    ************************************
    """

    def menu_user(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_user()
            self.view.option('5')
            o = input()
            if o == '1':
                self.leer_funciones()
            elif o == '2':
                self.leer_peliculas()
            elif o == '3':
                self.actualizar_Ticket()
            elif o == '4':
                self.leer_Ticket()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    
    """
    ************************************
    *   Controladores administradores  *
    ************************************||
    """

    def menu_admin(self):
        os.system ("cls") 
        o = '0'
        while o != '7':
            self.view.menu_admin()
            self.view.option('7')
            o = input()
            if o == '1':
                self.CtrlFunciones()
                pass
            elif o == '2':
                self.CtrlPeliculas()
            elif o == '3':
                self.Ctrlsalas()
            elif o == '4':
                self.CtrlButaca()
            elif o == '5':
                self.CtrlTicket()
            elif o == '6':
                self.CtrlUsuario()
            elif o == '7':
                self.view.end()
            else:
                self.view.not_valid_option()
        return


    """
    ************************************
    *   Controladores funciones  *
    ************************************
    """
    def CtrlFunciones(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_funciones()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_funcion()
            elif o == '2':
                self.leer_funciones()
            elif o == '3':
                self.actualizar_funcion()
            elif o == '4':
                self.eliminar_funcion()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.view.ask('Id_Pelicula  : ')
        Id_Pelicula = input()
        self.view.ask('Id_Sala: ')
        Id_Sala = input()
        self.view.ask('horario: ')
        horario = input()
        return[Id_Pelicula,Id_Sala,horario]

    def crear_funcion(self):
        print('Aregar funcion')
        self.view.ask('Id_Pelicula: ')
        Id_Pelicula = input()
        self.view.ask('Id_Sala: ')
        Id_Sala = input()
        self.view.ask('horario: ')
        horario = input()


        result = self.model.crear_funcion(Id_Pelicula, Id_Sala, horario)
        if result == True:
            self.view.msg('funcion creada')
        else:
            self.view.err(result)

    def leer_funcion(self):
        self.view.ask('ID funcion: ')
        Id_Funcion = input()
        funcion = self.model.leer_funcion(Id_Funcion)
        if type(funcion) == tuple:
            self.view.mostrar_funcion_header('Datos de la funcion'+Id_Funcion+' ')
            self.view.mostrar_funcion(funcion)
            self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            if funcion == None:
                self.view.err('LA FUNCION NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return   

    def leer_funciones(self):
        funcions = self.model.leer_funciones()
        if type(funcions) == list:
            self.view.mostrar_funcion_header(' Todos las funciones ')
            for funcion in funcions:
                self.view.mostrar_funcion(funcion)
                self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS funcions. REVISA')
        return

    def actualizar_funcion(self):
        self.view.ask('ID de la funcion: ')
        Id_Funcion = input()
        funcion = self.model.leer_funcion(Id_Funcion)
        if type(funcion) == tuple:
            self.view.mostrar_funcion_header(' identificador de la funcion '+Id_Funcion+' ')
            self.view.mostrar_funcion(funcion)
            self.view.mostrar_funcion_midder()
            self.view.mostrar_funcion_footer()
        else:
            if funcion == None:
                self.view.err('LA funcion NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA funcion. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['Id_Pelicula','Id_Sala','horario'], whole_vals)
        vals.append(Id_Funcion)
        vals = tuple(vals)
        out = self.model.actualizar_funcion(fields, vals)
        if out == True:
            self.view.ok(Id_Funcion, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR LA funcion. REVISA.')
        return

    def eliminar_funcion(self):
        self.view.ask('ID plicula: ')
        Id_Funcion = input()
        count = self.model.eliminar_funcion(Id_Funcion)
        if count != 0:
               self.view.ok(Id_Funcion, 'borro')
        else: 
            if count == 0:
                self.view.err('LA funcion NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR LA funcion. REVISA.')
        return

    """
    ************************************
    *   Controladores peliculas  *
    ************************************
    """

    def CtrlPeliculas(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_peliculas()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_pelicula()
            elif o == '2':
                self.leer_peliculas()
            elif o == '3':
                self.actualizar_pelicula()
            elif o == '4':
                self.eliminar_pelicula()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_pelicula(self):
        self.view.ask('Titulo: ')
        Titulo = input()
        self.view.ask('Genero: ')
        Genero = input()
        self.view.ask('Duracion: ')
        Duracion = input()
        self.view.ask('Idioma: ')
        Idioma = input()
        return[Titulo,Genero,Duracion,Idioma]

    def crear_pelicula(self):
        print('Aregar pelicula')
        self.view.ask('Titulo: ')
        Titulo = input()
        self.view.ask('Genero: ')
        Genero = input()
        self.view.ask('Duracion: ')
        Duracion = input()
        self.view.ask('Idioma: ')
        Idioma = input()

        result = self.model.crear_pelicula(Titulo, Genero, Duracion, Idioma)
        if result == True:
            self.view.msg('pelicula creada')
        else:
            self.view.err(result)

    def leer_pelicula(self):
        self.view.ask('ID pelicula: ')
        Id_Pelicula = input()
        pelicula = self.model.leer_pelicula(Id_Pelicula)
        if type(pelicula) == tuple:
            self.view.mostrar_pelicula_header('Datos de la pelicula'+Id_Pelicula+' ')
            self.view.mostrar_pelicula(pelicula)
            self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            if pelicula == None:
                self.view.err('LA PELICULA NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return   

    def leer_peliculas(self):
        peliculas = self.model.leer_peliculas()
        if type(peliculas) == list:
            self.view.mostrar_pelicula_header(' Todos las peliculas ')
            for pelicula in peliculas:
                self.view.mostrar_pelicula(pelicula)
                self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS peliculas. REVISA')
        return

    def actualizar_pelicula(self):
        self.view.ask('ID de la pelicula: ')
        Id_Pelicula = input()
        pelicula = self.model.leer_pelicula(Id_Pelicula)
        if type(pelicula) == tuple:
            self.view.mostrar_pelicula_header(' identificador de la pelicula '+Id_Pelicula+' ')
            self.view.mostrar_pelicula(pelicula)
            self.view.mostrar_pelicula_midder()
            self.view.mostrar_pelicula_footer()
        else:
            if pelicula == None:
                self.view.err('LA PELICULA NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA PELICULA. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['Titulo','Genero','Duracion','Idioma'], whole_vals)
        vals.append(Id_Pelicula)
        vals = tuple(vals)
        out = self.model.actualizar_pelicula(fields, vals)
        if out == True:
            self.view.ok(Id_Pelicula, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA.')
        return

    def eliminar_pelicula(self):
        self.view.ask('ID plicula: ')
        Id_Pelicula = input()
        count = self.model.eliminar_pelicula(Id_Pelicula)
        if count != 0:
               self.view.ok(Id_Pelicula, 'borro')
        else: 
            if count == 0:
                self.view.err('LA PELICULA NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return

    """
    ************************************
    *   Controladores Butaca  *
    ************************************
    """

    def CtrlButaca(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_butaca()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_butaca()
            elif o == '2':
                self.leer_butacas()
            elif o == '3':
                self.actualizar_butaca()
            elif o == '4':
                self.eliminar_butaca()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_butaca(self):
        self.view.ask('ID: (ingrese el numero del asiento ) ')
        Id_Butaca = input()
        self.view.ask('Estado: (0 = disponible, 1 = ocupado) ')
        Estado = input()
        return[Id_Butaca,Estado]

    def crear_butaca(self):
        print('Aregar butaca')
        self.view.ask('Id_Butaca: (ingrese el numero del asiento) ')
        Id_Butaca = input()
        self.view.ask('Estado: (0 = disponible, 1 = ocupado) ')
        Estado = input()

        result = self.model.crear_butaca(Id_Butaca, Estado)
        if result == True:
            self.view.msg('butaca creada')
        else:
            self.view.err('Butaca ya creada.')

    def leer_butaca(self):
        self.view.ask('ID butaca: ')
        Id_butaca = input()
        butaca = self.model.leer_butaca(Id_butaca)
        if type(butaca) == tuple:
            self.view.mostrar_butaca_header('Datos de la butaca'+Id_butaca+' ')
            self.view.mostrar_butaca(butaca)
            self.view.mostrar_butaca_midder()
            self.view.mostrar_butaca_footer()
        else:
            if butaca == None:
                self.view.err('LA butaca NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER LA butaca. REVISA.')
        return   

    def leer_butacas(self):
        butacas = self.model.leer_butacas()
        if type(butacas) == list:
            self.view.mostrar_butaca_header(' Todos las butacas ')
            for butaca in butacas:
                self.view.mostrar_butaca(butaca)
                self.view.mostrar_butaca_midder()
            self.view.mostrar_butaca_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS butacas. REVISA')
        return

    def actualizar_butaca(self):
        self.view.ask('ID de la butaca: ')
        Id_butaca = input()
        butaca = self.model.leer_butaca(Id_butaca)
        if type(butaca) == tuple:
            self.view.mostrar_butaca_header(' identificador de la butaca '+Id_butaca+' ')
            self.view.mostrar_butaca(butaca)
            self.view.mostrar_butaca_midder()
            self.view.mostrar_butaca_footer()
        else:
            if butaca == None:
                self.view.err('LA butaca NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA butaca. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_butaca()
        fields, vals = self.update_lists(['Id_Butaca','Estado','Duracion','Idioma'], whole_vals)
        vals.append(Id_butaca)
        vals = tuple(vals)
        out = self.model.actualizar_butaca(fields, vals)
        if out == True:
            self.view.ok(Id_butaca, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR LA butaca. REVISA.')
        return

    def eliminar_butaca(self):
        self.view.ask('ID plicula: ')
        Id_butaca = input()
        count = self.model.eliminar_butaca(Id_butaca)
        if count != 0:
               self.view.ok(Id_butaca, 'borro')
        else: 
            if count == 0:
                self.view.err('LA butaca NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR LA butaca. REVISA.')
        return

    """
    ************************************
    *        Controladores salas       *
    ************************************
    """

    def Ctrlsalas(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_salas()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_sala()
            elif o == '2':
                self.leer_salas()
            elif o == '3':
                self.actualizar_Sala()
            elif o == '4':
                self.eliminar_Sala()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_Sala(self):
        self.view.ask('Asientos: ')
        Asientos = input()
        self.view.ask('Tipo: ')
        Tipo = input()
        return[Asientos,Tipo]

    def crear_sala(self):
        print('Asientos en la sala')
        self.view.ask('Asientos: ')
        Asientos = input()
        print('Tipo  de la sala')
        self.view.ask('Tipo: ')
        Tipo = input()

        result = self.model.crear_Sala(Asientos, Tipo)
        if result == True:
            self.view.msg('sala creada')
        else:
            self.view.err(result)

    def leer_Sala(self):
        self.view.ask('ID sala: ')
        Id_Sala = input()
        sala = self.model.leer_Sala(Id_Sala)
        if type(sala) == tuple:
            self.view.mostrar_sala_header('Datos de la sala'+Id_Sala+' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            if sala == None:
                self.view.err('LA SALA NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER LA SALA. REVISA.')
        return   

    def leer_salas(self):
        salas = self.model.leer_Salas()
        if type(salas) == list:
            self.view.mostrar_sala_header(' Todos las salas ')
            for sala in salas:
                self.view.mostrar_sala(sala)
                self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS salas. REVISA')
        return

    def actualizar_Sala(self):
        self.view.ask('ID de la sala: ')
        Id_Sala = input()
        sala = self.model.leer_Sala(Id_Sala)
        if type(sala) == tuple:
            self.view.mostrar_sala_header(' identificador de la sala '+Id_Sala+' ')
            self.view.mostrar_sala(sala)
            self.view.mostrar_sala_midder()
            self.view.mostrar_sala_footer()
        else:
            if sala == None:
                self.view.err('LA SALA NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA SALA. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_Sala()
        fields, vals = self.update_lists(['Butaca','Tipo'], whole_vals)
        vals.append(Id_Sala)
        vals = tuple(vals)
        out = self.model.actualizar_Sala(fields, vals)
        if out == True:
            self.view.ok(Id_Sala, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR LA SALA. REVISA.')
        return

    def eliminar_Sala(self):
        self.view.ask('ID plicula: ')
        Id_Sala = input()
        count = self.model.eliminar_Sala(Id_Sala)
        if count != 0:
               self.view.ok(Id_Sala, 'borro')
        else: 
            if count == 0:
                self.view.err('LA SALA NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR LA SALA. REVISA.')
        return


    """
    ************************************
    *   Controladores usuario/admin  *
    ************************************
    """

    def CtrlUsuario(self):
        os.system ("cls") 
        o = '0'
        while o != '9':
            self.view.menu_usuario()
            self.view.option('9')
            o = input()
            if o == '1':
                self.registro_usuario()
            elif o == '2':
                self.leer_usuarios()
            elif o == '3':
                self.actualizar_usuario()
            elif o == '4':
                self.eliminar_usuario()
            elif o == '5':
                self.registro_admin()
            elif o == '6':
                self.leer_admins()
            elif o == '7':
                self.actualizar_admin()
            elif o == '8':
                self.eliminar_admin()
            elif o == '9':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    '''USER'''
    def ask_usuario(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Email: ')
        Email = input()
        self.view.ask('Num: ')
        Num = input()
        self.view.ask('password: ')
        password = input()
        return[Nombre,Email,Num,password]
            
    def leer_usuario(self):
        self.view.ask('ID usuario: ')
        Id_Usuario = input()
        usuario = self.model.leer_usuario(Id_Usuario)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header('Datos del usuario'+Id_Usuario+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.err('El USUARIO NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return   

    def leer_usuarios(self):
        usuarios = self.model.leer_usuarios()
        if type(usuarios) == list:
            self.view.mostrar_usuario_header(' Todos lOs usuarios ')
            for usuario in usuarios:
                self.view.mostrar_usuario(usuario)
                self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS USUARIOS. REVISA')
        return

    def actualizar_usuario(self):
        self.view.ask('ID de la usuario: ')
        Id_Usuario = input()
        usuario = self.model.leer_usuario(Id_Usuario)
        if type(usuario) == tuple:
            self.view.mostrar_usuario_header(' identificador de la usuario '+Id_Usuario+' ')
            self.view.mostrar_usuario(usuario)
            self.view.mostrar_usuario_midder()
            self.view.mostrar_usuario_footer()
        else:
            if usuario == None:
                self.view.err('LA usuario NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA usuario. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_usuario()
        fields, vals = self.update_lists(['Nombre','Email','Num','password'], whole_vals)
        vals.append(Id_Usuario)
        vals = tuple(vals)
        out = self.model.actualizar_usuario(fields, vals)
        if out == True:
            self.view.ok(Id_Usuario, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA.')
        return

    def eliminar_usuario(self):
        self.view.ask('ID usuario: ')
        Id_Usuario = input()
        count = self.model.eliminar_usuario(Id_Usuario)
        if count != 0:
               self.view.ok(Id_Usuario, 'borro')
        else: 
            if count == 0:
                self.view.err('EL USUARIO NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR AL USUARIO. REVISA.')
        return


    '''ADMIN'''

    def ask_admin(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Email: ')
        Email = input()
        self.view.ask('Num: ')
        Num = input()
        self.view.ask('password: ')
        password = input()
        return[Nombre,Email,Num,password]
            
    def leer_admin(self):
        self.view.ask('ID admin: ')
        Id_Administrador = input()
        admin = self.model.leer_admin(Id_Administrador)
        if type(admin) == tuple:
            self.view.mostrar_admin_header('Datos del admin'+Id_Administrador+' ')
            self.view.mostrar_admin(admin)
            self.view.mostrar_admin_midder()
            self.view.mostrar_admin_footer()
        else:
            if admin == None:
                self.view.err('El ADMINISTRADOR NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA.')
        return   

    def leer_admins(self):
        admins = self.model.leer_admins()
        if type(admins) == list:
            self.view.mostrar_admin_header(' Todos los admins ')
            for admin in admins:
                self.view.mostrar_admin(admin)
                self.view.mostrar_admin_midder()
            self.view.mostrar_admin_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS ADMINISTRADOR. REVISA')
        return

    def actualizar_admin(self):
        self.view.ask('ID del admin: ')
        Id_Administrador = input()
        admin = self.model.leer_admin(Id_Administrador)
        if type(admin) == tuple:
            self.view.mostrar_admin_header(' identificador de la admin '+Id_Administrador+' ')
            self.view.mostrar_admin(admin)
            self.view.mostrar_admin_midder()
            self.view.mostrar_admin_footer()
        else:
            if admin == None:
                self.view.err('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['Nombre','Email','Num','password'], whole_vals)
        vals.append(Id_Administrador)
        vals = tuple(vals)
        out = self.model.actualizar_admin(fields, vals)
        if out == True:
            self.view.ok(Id_Administrador, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA.')
        return

    def eliminar_admin(self):
        self.view.ask('ID admin: ')
        Id_Administrador = input()
        count = self.model.eliminar_admin(Id_Administrador)
        if count != 0:
               self.view.ok(Id_Administrador, 'borro')
        else: 
            if count == 0:
                self.view.err('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR AL ADMINISTRADOR. REVISA.')
        return

    
    """
    ************************************
    *   Controladores Tikets  *
    ************************************
    """

    def CtrlTicket(self):
        os.system ("cls") 
        o = '0'
        while o != '5':
            self.view.menu_Ticket()
            self.view.option('5')
            o = input()
            if o == '1':
                self.crear_Ticket()
            elif o == '2':
                self.leer_Tickets()
            elif o == '3':
                self.actualizar_Ticket()
            elif o == '4':
                self.eliminar_Ticket()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_Ticket(self):
        self.view.ask('Id_Funcion  : ')
        Id_Funcion = input()
        self.view.ask('Id_Usuario: ')
        Id_Usuario = input()
        self.view.ask('Id_Butaca: ')
        Id_Butaca = input()
        return[Id_Funcion,Id_Usuario,Id_Butaca]

    def crear_Ticket(self):
        print('Aregar Ticket')
        self.view.ask('Id_Funcion: ')
        Id_Funcion = input()
        self.view.ask('Id_Usuario: ')
        Id_Usuario = input()
        self.view.ask('Id_Butaca: ')
        Id_Butaca = input()

        result = self.model.crear_Ticket(Id_Funcion, Id_Usuario, Id_Butaca)
        if result == True:
            self.view.msg('Ticket creado')
            print("creado")
        else:
            self.view.err(result)

    def leer_Ticket(self):
        self.view.ask('ID Ticket: ')
        Id_Ticket = input()
        Ticket = self.model.leer_Ticket(Id_Ticket)
        if type(Ticket) == tuple:
            self.view.mostrar_Ticket_header('Datos de la Ticket'+Id_Ticket+' ')
            self.view.mostrar_Ticket(Ticket)
            self.view.mostrar_Ticket_midder()
            self.view.mostrar_Ticket_footer()
        else:
            if Ticket == None:
                self.view.err('LA Ticket NO EXISTE')
            else: 
                self.view.err('PROBLEMA AL LEER LA Ticket. REVISA.')
        return   

    def leer_Tickets(self):
        Tickets = self.model.leer_Tickets()
        if type(Tickets) == list:
            self.view.mostrar_Ticket_header(' Todos las Ticketes ')
            for Ticket in Tickets:
                self.view.mostrar_Ticket(Ticket)
                self.view.mostrar_Ticket_midder()
            self.view.mostrar_Ticket_footer()
        else:
            self.view.err('PROBLEMA AL LEER LOS Tickets. REVISA')
        return

    def actualizar_Ticket(self):
        self.view.ask('ID de la Ticket: ')
        Id_Ticket = input()
        Ticket = self.model.leer_Ticket(Id_Ticket)
        if type(Ticket) == tuple:
            self.view.mostrar_Ticket_header(' identificador de la Ticket '+Id_Ticket+' ')
            self.view.mostrar_Ticket(Ticket)
            self.view.mostrar_Ticket_midder()
            self.view.mostrar_Ticket_footer()
        else:
            if Ticket == None:
                self.view.err('LA Ticket NO EXISTE')
            else:
                self.view.err('PROBLEMA AL LEER LA Ticket. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_Ticket()
        fields, vals = self.update_lists(['Id_Funcion','Id_Usuario','Id_Butaca'], whole_vals)
        vals.append(Id_Ticket)
        vals = tuple(vals)
        out = self.model.actualizar_Ticket(fields, vals)
        if out == True:
            self.view.ok(Id_Ticket, 'actualizo')
        else:
            self.view.err('NO SE PUDO ACTUALIZAR LA Ticket. REVISA.')
        return

    def eliminar_Ticket(self):
        self.view.ask('ID plicula: ')
        Id_Ticket = input()
        count = self.model.eliminar_Ticket(Id_Ticket)
        if count != 0:
               self.view.ok(Id_Ticket, 'borro')
        else: 
            if count == 0:
                self.view.err('LA Ticket NO EXISTE')
            else:
                self.view.err('PROBLEMA AL BORRAR LA Ticket. REVISA.')
        return
