import sqlalchemy
import databases
import ormar


# 2. Initialization
DATABASE_URL = "sqlite:///db.sqlite"

base_ormar_config = ormar.OrmarConfig(
    database=databases.Database(DATABASE_URL),
    metadata=sqlalchemy.MetaData(),
    engine=sqlalchemy.create_engine(DATABASE_URL),
)


class Author(ormar.Model):
    ormar_config = base_ormar_config.copy(tablename="authors")

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)


base_ormar_config.metadata.create_all(base_ormar_config.engine)



