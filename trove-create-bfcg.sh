#!/bin/bash

for DB in p2 p4 p6 p8 sigma tau
do
  echo ${DB}:
  trove database-create BCG-DB $DB
  trove user-grant-access BCG-DB ubuntu $DB
done
