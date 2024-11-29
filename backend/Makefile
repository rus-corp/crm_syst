run:
	uvicorn main:app --reload

mm:
	alembic revision --autogenerate -m "$(c)"

up:
	alembic upgrade head

test-info:
	pytest --cov=apps tests/


drop:
	dropdb -U postgres astro_fast


create:
	createdb -U postgres astro_fast