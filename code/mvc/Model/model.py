from mysql import connector

class Model:
    """
    ********************************************
    * A data model with mysql for a cine DB *
    ********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file 
        self.config_db = self.read_config_db() 
        self.connect_to_db() 

    def read_config_db(self):
         d = {}
         with open ( self.config_db_file) as f_r:
             for line in f_r:
                (key, val) = line.strip().split(':')
                d[key]=val
         return d
    
    def connect_to_db(self):
          self.cnx = connector.connect(**self.config_db)
          self.cursor = self.cnx.cursor()
    
    def close_db(self):
          self.cnx.close()

    """
    ************************************
    *        Metodos para admin      *
    ************************************
    """
    def crear_admin(self, Nombre, Email, password,Num):
        try:
            sql ='INSERT INTO administrador(`Nombre`,`Email`,`password`,`Num`) values (%s, %s, %s, %s)'
            vals = (Nombre,Email,password,Num)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_admin(self,Id_Administrador):
        try:
            sql = 'SELECT * FROM administrador WHERE Id_Administrador = %s'
            vals = (Id_Administrador,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def leer_admins(self):
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_admin(self, fields, vals):
        try:
            sql = 'UPDATE administrador SET ' + ','.join(fields)+'WHERE Id_Administrador = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_admin(self, Id_Administrador):
        try:
            sql = 'DELETE FROM administrador WHERE Id_Administrador = %s'
            vals = (Id_Administrador,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def inicio_admin(self, Email):
        try:
            sql = 'select * from administrador where Email = %s'
            vals = (Email,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return (err)

    """
    ************************************
    *        Metodos para usuario      *
    ************************************
    """
    def crear_usuario(self, Nombre, Email, password,Num):
        try:
            sql ='INSERT INTO usuario(`Nombre`,`Email`,`password`,`Num`) values (%s, %s, %s, %s)'
            vals = (Nombre,Email,password,Num)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_usuario(self,Id_Usuario):
        try:
            sql = 'SELECT * FROM usuario WHERE Id_Usuario = %s'
            vals = (Id_Usuario,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def leer_usuarios(self):
        try:
            sql = 'SELECT * FROM usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_usuario(self, fields, vals):
        try:
            sql = 'UPDATE usuario SET ' + ','.join(fields)+'WHERE Id_Usuario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_usuario(self, Id_Usuario):
        try:
            sql = 'DELETE FROM usuario WHERE Id_Usuario = %s'
            vals = (Id_Usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def inicio_usuario(self, Email):
        try:
            sql = 'select * from Usuario where Email = %s'
            vals = (Email,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return (err)

    def leer_usuario_email_password(self, Email, password):
        try:
            sql = 'SELECT * FROM usuario WHERE Email = %s and password = %s'
            vals = (Email, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_administrador_email_password(self, Email, password):
        try:
            sql = 'SELECT * FROM administrador WHERE Email = %s and password = %s'
            vals = (Email, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)
    """
    ************************************
    *     Metodos para peliculas       *
    ************************************
    """
    def crear_pelicula(self, Titulo, Genero, Duracion, Idioma):
            try:
                sql = 'INSERT INTO pelicula (`Titulo`, `Genero`, `Duracion`, `Idioma`) VALUES (%s, %s, %s, %s)'
                vals = (Titulo, Genero, Duracion, Idioma)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_pelicula(self, Id_Pelicula):
        try:
            sql = 'SELECT * FROM pelicula WHERE Id_Pelicula = %s'
            vals = (Id_Pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_peliculas(self):
        try:
            sql = 'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+'WHERE Id_Pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_pelicula(self, Id_Pelicula):
        try:
            sql = 'DELETE FROM Pelicula WHERE Id_Pelicula = %s'
            vals = (Id_Pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    """
    ************************************
    *     Metodos para Sala       *
    ************************************
    """
    def crear_Sala(self, Asientos, Tipo):
            try:
                sql = 'INSERT INTO sala (`Asientos`,`Tipo`) VALUES (%s,%s)'
                vals = (Asientos,Tipo,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_Sala(self, Id_Sala):
        try:
            sql = 'SELECT * FROM sala WHERE Id_Sala = %s'
            vals = (Id_Sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_Salas(self):
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_Sala(self, fields, vals):
        try:
            sql = 'UPDATE sala SET ' + ','.join(fields)+'WHERE Id_Sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_Sala(self, Id_Sala):
        try:
            sql = 'DELETE FROM Sala WHERE Id_Sala = %s'
            vals = (Id_Sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    """
    ************************************
    *     Metodos para butacas        *
    ************************************
    """
    def crear_butaca(self, Id_Butaca, Estado):
            try:
                sql = 'INSERT INTO butaca (`Id_Butaca`, `Estado`) VALUES (%s, %s)'
                vals = (Id_Butaca, Estado,)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_butaca(self, Id_Butaca):
        try:
            sql = 'SELECT * FROM butaca WHERE Id_Butaca = %s'
            vals = (Id_Butaca,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_butacas(self):
        try:
            sql = 'SELECT * FROM butaca'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_butaca(self, fields, vals):
        try:
            sql = 'UPDATE butaca SET '+','.join(fields)+'WHERE Id_Butaca = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_butaca(self, Id_Butaca):
        try:
            sql = 'DELETE FROM butaca WHERE Id_Butaca = %s'
            vals = (Id_Butaca,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)
    
    """
    ************************************
    *     Metodos para Funcion       *
    ************************************
    """
    def crear_funcion(self, Id_Pelicula, Id_Sala, fecha, horario):
            try:
                sql = 'INSERT INTO funcion (`Id_Pelicula`,`Id_Sala`,`fecha`,`horario`) VALUES (%s,%s,%s,%s)'
                vals = (Id_Pelicula, Id_Sala, fecha, horario)
                self.cursor.execute(sql, vals)
                self.cnx.commit()
                return True
            except connector.Error as err:
                self.cnx.rollback()
                return(err)

    def leer_funcion(self, Id_Funcion):
        try:
            sql = 'SELECT * FROM funcion WHERE Id_Funcion = %s'
            vals = (Id_Funcion,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_funciones(self):
        try:
            sql = 'SELECT funcion.*, pelicula.Titulo FROM funcion JOIN pelicula ON funcion.Id_Pelicula = pelicula.Id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_funcion(self, fields, vals):
        try:
            sql = 'UPDATE funcion SET ' + ','.join(fields)+'WHERE Id_Funcion = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_funcion(self, Id_Funcion):
        try:
            sql = 'DELETE FROM funcion WHERE Id_Funcion = %s'
            vals = (Id_Funcion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)    

    def horario_funcion(self,horario):
        try:
            sql = 'SELECT funcion.*, pelicula.Titulo FROM funcion JOIN pelicula ON funcion.Id_Pelicula = pelicula.Id_Pelicula AND funcion.horario = %s'
            vals = (horario,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def fecha_funcion(self,fecha):
        try:
            sql = 'SELECT funcion.*, pelicula.Titulo FROM funcion JOIN pelicula ON funcion.Id_Pelicula = pelicula.Id_Pelicula AND funcion.fecha = %s'
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def pelicula_funcion(self,Id_Pelicula):
        try:
            sql = 'SELECT funcion.*, pelicula.Titulo FROM funcion JOIN pelicula ON funcion.Id_Pelicula = pelicula.Id_Pelicula AND funcion.Id_Pelicula = %s'
            vals = (Id_Pelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    """
    ************************************
    *        Metodos para Ticket       *
    ************************************
    """
    def crear_Ticket(self, Id_Funcion, Id_Usuario, Id_Butaca):
        try:
            sql = 'INSERT INTO ticket (`Id_Funcion`,`Id_Usuario`, `Id_Butaca`) values (%s, %s, %s)'
            vals = (Id_Funcion, Id_Usuario, Id_Butaca)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
        except connector.Error as err:
            self.cnx.rollback()
            return (err)

    def leer_Ticket(self, Id_Ticket):
        try:
            sql = 'SELECT * FROM Ticket WHERE Id_Ticket = %s'
            vals = (Id_Ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return(err)

    def leer_Tickets(self):
        try:
            sql = 'SELECT * FROM ticket'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return(err)

    def actualizar_Ticket(self, fields, vals):
        try:
            sql = 'UPDATE Ticket SET ' + ','.join(fields)+'WHERE Id_Ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def eliminar_Ticket(self, Id_Ticket):
        try:
            sql = 'DELETE FROM Ticket WHERE Id_Ticket = %s'
            vals = (Id_Ticket,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def leer_Tickets_usuario(self,Id_Usuario):
        try:
            sql = 'SELECT ticket.*, usuario.Nombre FROM ticket JOIN usuario ON ticket.Id_usuario = usuario.Id_usuario AND ticket.Id_Usuario = %s'
            vals = (Id_Usuario,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err