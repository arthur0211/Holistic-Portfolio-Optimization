import uuid
from datetime import date, datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, Text, Numeric, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class RISAQuadrant(PyEnum):
    CONSERVADOR_PRECAVIDO = "Conservador Precavido"
    CRESCIMENTO_MODERADO = "Crescimento Moderado"
    BUSCADOR_DE_OPORTUNIDADES = "Buscador de Oportunidades"
    ESPECIALISTA_EM_RISCO = "Especialista em Risco"
    NAO_DEFINIDO = "Não Definido"

class ClientProfile(Base):
    __tablename__ = "client_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Dados Demográficos (adaptado para Brasil)
    full_name = Column(String(255), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False) # Cadastro de Pessoas Físicas
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    # Considerar adicionar: Endereço, Estado Civil, Profissão, etc., conforme necessidade e LGPD.

    # Risk Number (a ser definido como será obtido/calculado)
    risk_number = Column(Integer, nullable=True) # Exemplo: 1-99

    # Perfil RISA (Risk, Income, Suitability, Aspiration)
    risa_quadrant = Column(Enum(RISAQuadrant), nullable=True, default=RISAQuadrant.NAO_DEFINIDO)
    # Poderíamos ter campos mais detalhados para cada componente do RISA se necessário:
    # risa_risk_score = Column(Numeric(5, 2), nullable=True)
    # risa_income_need = Column(Numeric(5, 2), nullable=True)
    # risa_suitability_knowledge = Column(Numeric(5, 2), nullable=True)
    # risa_aspiration_level = Column(Numeric(5, 2), nullable=True)

    # Pontuações de Vieses Comportamentais (JSON ou tabela separada poderia ser uma opção)
    # Para MVP, pode ser um campo de texto ou JSON simples.
    # Exemplo: {'aversao_perda': 7, 'excesso_confianca': 5}
    behavioral_biases_scores = Column(Text, nullable=True) # Armazenar como JSON string

    # Relacionamento com Assessor (se aplicável, pode ser uma FK para uma tabela de Assessores)
    # advisor_id = Column(UUID(as_uuid=True), ForeignKey('advisors.id'), nullable=True)
    # advisor = relationship("Advisor", back_populates="clients")

    # Outros campos relevantes para suitability podem ser adicionados aqui
    # Exemplo: objetivos_investimento, situacao_financeira, conhecimento_produtos (CVM)
    investment_objectives = Column(Text, nullable=True)
    financial_situation = Column(Text, nullable=True) # Poderia ser mais granular
    product_knowledge = Column(Text, nullable=True) # Poderia ser mais granular

    def __repr__(self):
        return f"<ClientProfile(id={self.id}, cpf='{self.cpf}', name='{self.full_name}')>"

# TODO: Considerar tabelas separadas para:
# - Endereços (se complexo)
# - Respostas detalhadas do questionário RISA
# - Detalhamento de Vieses Comportamentais (se não for JSON)
# - Histórico de Perfil (se o perfil muda ao longo do tempo)

# Exemplo de uma tabela de Assessores (se necessário)
# class Advisor(Base):
#     __tablename__ = "advisors"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String(255), nullable=False)
#     clients = relationship("ClientProfile", back_populates="advisor")


# Configuração da Base de Dados e Engine (será em um arquivo separado, e.g., src/db/session.py)
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# DATABASE_URL = "postgresql://user:password@host:port/database"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine) # Para criar as tabelas 