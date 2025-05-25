from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database setup
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship("Freebie", back_populates="company")
    devs = relationship("Dev", secondary="freebies", viewonly=True)

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(
            item_name=item_name,
            value=value,
            dev=dev,
            company=self
        )
        session.add(freebie)
        session.commit()
        return freebie

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship("Freebie", back_populates="dev")
    companies = relationship("Company", secondary="freebies", viewonly=True)

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie.dev_id == self.id:
            freebie.dev = dev
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

# Create tables
Base.metadata.create_all(engine)