-- Create all extensions
\ir extensions/test.sql

BEGIN;

SELECT plan(13);

\ir fixtures.sql
\ir database/test.sql
\ir storage/test.sql

SELECT * FROM finish();

ROLLBACK;
