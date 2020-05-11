from decimal import Decimal
from pydantic import BaseModel


class Assessment(BaseModel):
    assessmentId: Decimal
    internalTaxonId: Decimal
    scientificName: str
    redlistCategory: str
    redlistCriteria: str
    yearPublished: Decimal
    assessmentDate: str
    criteriaVersion: Decimal
    language: str
    rationale: str
    habitat: str
    threats: str
    population: str
    populationTrend: str
    range: str
    useTrade: str
    systems: str
    conservationActions: str
    realm: str
    yearLastSeen: str
    possiblyExtinct: bool
    possiblyExtinctInTheWild: bool
    scopes: str

    class Config:
        orm_mode = True


class Habitat(BaseModel):
    index: Decimal
    assessmentId: Decimal
    internalTaxonId: Decimal
    scientificName: str
    code: str
    name: str
    majorImportance: str
    season: str
    suitability: str

    class Config:
        orm_mode = True


class Country(BaseModel):
    index: Decimal
    assessmentId: Decimal
    internalTaxonId: Decimal
    scientificName: str
    code: str
    name: str
    presence: str
    origin: str
    seasonality: str
    formerlyBred: str

    class Config:
        orm_mode = True


class Threat(BaseModel):
    index: Decimal
    assessmentId: Decimal
    internalTaxonId: Decimal
    scientificName: str
    code: str
    name: str
    stressCode: str
    stressName: str
    ancestry: str
    ias: str
    internationalTrade: str
    scope: str
    severity: str
    text: str
    timing: str
    virus: str

    class Config:
        orm_mode = True
