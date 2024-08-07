from flask import Flask,render_template,request,url_for,flash,redirect
from flask_bootstrap import Bootstrap
from formularios.registroQuejas import RegistroQuejaForm
import psycopg2 

app = Flask(__name__,static_folder="./static")
app.config['BOOTSTRAP_SERVE_LOCAL'] = False
app.config['SECRET_KEY'] = "xnsjkaxnsaihxyuq@#dq"
Bootstrap(app)

class Conexion:
    _DATABASE = 'quejasSAT'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None 
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion == None:
            # si el objeto conexione s none no se ha creado un objeto de conexion
            # se crea
            try:
                cls._conexion = psycopg2.connect(user=cls._USERNAME,password=cls._PASSWORD,host=cls._HOST,port=int(cls._DB_PORT),database=cls._DATABASE)
                return cls._conexion
            except Exception as e:
                exit()
        else: return cls._conexion
    @classmethod
    def obtenerCursor(cls):
        ''' esta clase creara un cursor '''
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                raise flash(f'Error en el sistema! {e}')
        return cls._cursor
    @classmethod
    def close(cls):
        if not(cls._conexion is None):
            cls._conexion.close()
            

@app.route('/')
def index():
    ''' este metodo retornara un formulario de logeo '''
    return render_template('index.html')
@app.route('/registro',methods=["GET","POST"])
def registrar():
    formulary = RegistroQuejaForm()
    if request.method == "POST" and formulary.validate_on_submit():
        try:
            conn = Conexion.obtenerConexion()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO registro_de_quejas.quejas(texto_queja,email_quejoso,nombres_personal_corrupto) VALUES ('{formulary.descirpcion.data}','{formulary.email.data}','{formulary.personal.data}');")
            cursor.close()
            conn.commit()
            flash("Queja registrada correctamente!",'flash-succress')
            
        except Exception as e:
            print(e)
            print(f"INSERT INTO registro_de_quejas.quejas(texto_queja,email_quejoso,nombres_personal_corrupto) VALUES ('{formulary.descirpcion.data}','{formulary.email.data}','{formulary.personal.data}');")
            flash(f"Error al intentar regustrar la queja",'flash-error')
            
        return redirect(url_for('index'))
    return render_template('registro.html', form=formulary)
@app.route('/eventos')
def eventos():
    ''' metodo usado para ver informacion sobre el turnado de las quejas'''
    
    return render_template('estado.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)