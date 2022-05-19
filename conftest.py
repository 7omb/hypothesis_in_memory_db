from hypothesis import database
from hypothesis import settings

settings.register_profile('inmemory', database=database.InMemoryExampleDatabase())
settings.load_profile('inmemory')
