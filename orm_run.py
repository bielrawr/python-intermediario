import pandas as pd
df = pd.read_csv('modulo3/salaries.csv')
print(df.head())

from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

class SexoEnum(enum.Enum):
    F = 'F'
    M = 'M'

class CargoEnum(enum.Enum):
    ANALYST = 'ANALYST'
    ASSOCIATE = 'ASSOCIATE'
    SENIOR_ANALYST = 'SENIOR_ANALYST'
    SENIOR_MANAGER = 'SENIOR_MANAGER'
    MANAGER = 'MANAGER'
    DIRECTOR = 'DIRECTOR'

class UnidadeEnum(enum.Enum):
    FINANCE = 'FINANCE'
    WEB = 'WEB'
    IT = 'IT'
    OPERATIONS = 'OPERATIONS'
    MARKETING = 'MARKETING'
    MANAGEMENT = 'MANAGEMENT'

Base = declarative_base()

class Empregado(Base):
    __tablename__ = 'salarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    primeiro_nome = Column(String)
    sobrenome = Column(String)
    sexo = Column(Enum(SexoEnum))
    data_contratacao = Column(Date)
    data_atual = Column(Date)
    cargo = Column(Enum(CargoEnum))
    idade = Column(Integer)
    salario = Column(Float)
    unidade = Column(Enum(UnidadeEnum))
    ferias_usadas = Column(Integer)
    ferias_restantes = Column(Integer)
    avaliacoes = Column(Float)
    experiencia_anterior = Column(Float)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///salarios.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

df.rename(columns={
    'FIRST NAME': 'primeiro_nome',
    'LAST NAME': 'sobrenome',
    'SEX': 'sexo',
    'DOJ': 'data_contratacao',
    'CURRENT DATE': 'data_atual',
    'DESIGNATION': 'cargo',
    'AGE': 'idade',
    'SALARY': 'salario',
    'UNIT': 'unidade',
    'LEAVES USED': 'ferias_usadas',
    'LEAVES REMAINING': 'ferias_restantes',
    'RATINGS': 'avaliacoes',
    'PAST EXP': 'experiencia_anterior'
}, inplace=True)

# Transform enum values to match the Enum definitions
df['cargo'] = df['cargo'].str.replace(' ', '_').str.upper()
df['unidade'] = df['unidade'].str.upper()

df.to_sql('salarios', engine, if_exists='append', index=False)

from sqlalchemy import text
with engine.connect() as conn:
    resultado = conn.execute(text("SELECT CARGO, MIN(SALARIO/12) as salario_min, MAX(SALARIO/12) as salario_max, AVG(SALARIO/12) as salario_med FROM salarios GROUP BY CARGO"))
    print(resultado.fetchall())

sql = "SELECT CARGO, MIN(SALARIO/12) as salario_min, MAX(SALARIO/12) as salario_max, AVG(SALARIO/12) as salario_med FROM salarios GROUP BY CARGO"
df_resultado = pd.read_sql_query(sql, engine.connect())
print(df_resultado)

from sqlalchemy.orm import Session
from sqlalchemy import select, func

with Session(engine) as session:
    stmt = select(
        Empregado.cargo,
        func.min(Empregado.salario / 12).label('salario_min'),
        func.max(Empregado.salario / 12).label('salario_max'),
        func.avg(Empregado.salario / 12).label('salario_med')
    ).group_by(Empregado.cargo)
    resultados = session.execute(stmt).all()
    for linha in resultados:
        print(linha)
