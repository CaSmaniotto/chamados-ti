from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from aplicacao.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    remember = BooleanField("Continuar conectado")
    botao_confirmacao = SubmitField("Entrar")

class FormCriarConta(FlaskForm):
    matricula = StringField("ID Matrícula", validators=[DataRequired(), Length(6, 6)])

    departamento = SelectField("Departamento", validators=[DataRequired()],
                                choices=[(0, 'Selecione seu departamento'), 
                                    ('Marketing','Marketing'),
                                    ('Administração', 'Administração'), 
                                    ('Segurança', 'Segurança'), 
                                    ('Operações', 'Operações'), 
                                    ('Informática/TI', 'Informática/TI')], default=0)
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirme sua senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Registrar")

    def validate_email(self, email): 
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")
        
    def validate_matricula(self, matricula):
        usuario = Usuario.query.filter_by(matricula=matricula.data).first()
        if usuario:
            raise ValidationError("Matrícula já cadastrada, faça login para continuar")

class FormChamado(FlaskForm):
    problema = SelectField("Categoria", validators=[DataRequired()], 
                           choices=[(0, 'Selecione uma categoria'), 
                                    ('Suspeita de vírus no computador', 'Suspeita de vírus no computador'),
                                    ('Dúvidas em geral', 'Dúvidas em geral'), 
                                    ('Computador não liga','Computador não liga'), 
                                    ('Problemas no teclado e mouse','Problemas no teclado e mouse'), 
                                    ('Dúvidas em geral','Dúvidas em geral'), 
                                    ('Acesso a rede','Acesso a rede'), 
                                    ('Problema no email','Problema no email'), 
                                    ('Não consigo acessar', 'Não consigo acessar'), 
                                    ('Outro','Outro')], default=0)
    descricao = TextAreaField("Descrição", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
    
    def validate_problema(self, problema):
        if not int(problema.data):
            raise ValidationError("Selecione uma opção válida!")
