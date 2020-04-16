from sqlalchemy import Boolean, Column, Numeric, String
# from sqlalchemy.orm import relationship

from .database import Base


class Assessment(Base):
    __tablename__ = "assessments"

    assessmentId = Column(Numeric(12, 0), nullable=False)
    internalTaxonId = Column(Numeric(12, 0), nullable=False)
    scientificName = Column(String, nullable=False, primary_key=True)
    redlistCategory = Column(String, nullable=False)
    redlistCriteria = Column(String)
    yearPublished = Column(Numeric(4, 0), nullable=False)
    assessmentDate = Column(String, nullable=False)
    criteriaVersion = Column(Numeric(4, 0), nullable=False)
    language = Column(String)
    rationale = Column(String)
    habitat = Column(String)
    threats = Column(String)
    population = Column(String)
    populationTrend = Column(String)
    range = Column(String)
    useTrade = Column(String)
    systems = Column(String)
    conservationActions = Column(String)
    realm = Column(String)
    yearLastSeen = Column(String)
    possiblyExtinct = Column(Boolean)
    possiblyExtinctInTheWild = Column(Boolean)
    scopes = Column(String)

    def __repr__(self):
        return f'<Assessment for {self.scientificName}>'


class Habitat(Base):
    __tablename__ = "habitats"

    index = Column(Numeric, primary_key=True)
    assessmentId = Column(Numeric(12, 0), nullable=False)
    internalTaxonId = Column(Numeric(12, 0), nullable=False)
    scientificName = Column(String, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    majorImportance = Column(String)
    season = Column(String)
    suitability = Column(String)

    def __repr__(self):
        return f'<Habitats that {self.scientificName} can be found in>'


class Country(Base):
    __tablename__ = "countries"

    index = Column(Numeric, primary_key=True)
    assessmentId = Column(Numeric(12, 0), nullable=False)
    internalTaxonId = Column(Numeric(12, 0), nullable=False)
    scientificName = Column(String, nullable=False)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    presence = Column(String)
    origin = Column(String)
    seasonality = Column(String)
    formerlyBred = Column(String)

    def __repr__(self):
        return f'<Countries that {self.scientificName} can be found in>'
