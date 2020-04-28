from sqlalchemy import and_, func
from sqlalchemy.orm import Session
# from sqlalchemy.dialects import postgresql

from . import models


def get_hotspot_habitats(db: Session):
    code_list = ('1.5', '1.6', '1.7', '1.8', '1.9', '5.1', '5.2',
                 '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '14.6')
    category_list = ('Critically Endangered', 'Endangered', 'Vulnerable')

    threatened_list = db.query(
        models.Assessment.scientificName
    ).filter(
        models.Assessment.redlistCategory.in_(
            category_list
        )
    ).subquery()

    query = db.query(
        models.Habitat.name,
        func.count('*')
    ).filter(
        and_(
            models.Habitat.code.in_(
                code_list
            ), models.Habitat.scientificName.in_(
                threatened_list
            )
        )
    ).group_by(
        models.Habitat.name
    ).order_by(
        func.count('*').desc()
    ).all()
    # Debug SQLAlchemy query:
    # str(query.statement.compile(dialect=postgresql.dialect()))
    return [{"habitat": row[0], "count": row[1]} for row in query]


def get_hotspot_habitat_by_country(db: Session, country: str):
    code_list = ('1.5', '1.6', '1.7', '1.8', '1.9', '5.1', '5.2',
                 '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '14.6')
    category_list = ('Critically Endangered', 'Endangered', 'Vulnerable')

    species_in_country = db.query(
        models.Country.scientificName
    ).filter(
        models.Country.name == country
    ).subquery()

    threatened_list = db.query(
        models.Assessment.scientificName
    ).filter(
        models.Assessment.redlistCategory.in_(
            category_list
        )
    ).subquery()

    query = db.query(
        models.Habitat.name,
        func.count('*')
    ).filter(
        and_(
            models.Habitat.code.in_(
                code_list
            ), and_(
                models.Habitat.scientificName.in_(
                    threatened_list
                ), models.Habitat.scientificName.in_(
                    species_in_country
                )
            )
        )
    ).group_by(
        models.Habitat.name
    ).order_by(
        func.count('*').desc()
    ).all()

    return [{"habitat": row[0], "count": row[1]} for row in query]


def get_threats(db: Session):
    query = db.query(
        models.Threat.name,
        func.count('*')
    ).group_by(
        models.Threat.name
    ).order_by(
        func.count('*').desc()
    ).all()

    return [{"name": row[0], "count": row[1]} for row in query]


def get_threats_by_habitat(db: Session, habitat_code: str):
    species_in_habitat = db.query(
        models.Habitat.scientificName
    ).filter(
        models.Habitat.code == habitat_code
    ).subquery()

    query = db.query(
        models.Threat.name,
        func.count('*')
    ).filter(
        models.Threat.scientificName.in_(
            species_in_habitat
        )
    ).group_by(
        models.Threat.name
    ).order_by(
        func.count('*').desc()
    ).all()

    return [{"name": row[0], "count": row[1]} for row in query]


def get_threats_by_country(db: Session, country: str):
    species_in_country = db.query(
        models.Country.scientificName
    ).filter(
        models.Country.name == country
    ).subquery()

    query = db.query(
        models.Threat.name,
        func.count('*')
    ).filter(
        models.Threat.scientificName.in_(
            species_in_country
        )
    ).group_by(
        models.Threat.name
    ).order_by(
        func.count('*').desc()
    ).all()

    return [{"name": row[0], "count": row[1]} for row in query]
