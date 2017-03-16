# -*- coding: utf-8 -*-
from arango import create

# create connection to database
conn = create(db="test")

# create database itself
conn.database.create()

# create collection with name `test_collection`
conn.test_collection.create()
# create document
conn.test_collection.documents.create({"sample_key": "sample_value"})
# get first document
doc = conn.test_collection.documents().first
# get document body
doc.body

# get all documents in collection
for doc in conn.test_collection.query.execute():
  print doc.id

# work with AQL
conn.test_range.create()

for n in range(10):
  conn.test_range.documents.create({
    "n": n,
    "mult": n * n})

conn.test_range.query.filter(
  filter("n == 1 || n == 5")).execute()

# delete database
conn.database.delete()
