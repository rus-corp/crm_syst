SELECT client.phone, client.email, client.slug, client.updated_at, client.created_at, client.name, client.last_name, client.second_name, client.id 
FROM client 
WHERE client.slug = $1::VARCHAR

sys:1: SAWarning: 
SELECT statement has a cartesian product between FROM element(s) "program" and FROM element "program_clients".  Apply join condition(s) between each element to resolve.
2024-11-30 19:23:51,108 INFO sqlalchemy.engine.Engine 


SELECT program_clients.client_id, program_clients.program_id, program_clients.price, program_clients.status, program_clients.contract_status, program_clients.created_at, program_clients.id, program_1.title, program_1.start_date, program_1.end_date, program_1.place, program_1."desc", program_1.price AS price_1, program_1.status AS status_1, program_1.slug, program_1.id AS id_1 
FROM program_clients LEFT OUTER JOIN program AS program_1 ON program_1.id = program_clients.program_id, program 
WHERE program_clients.client_id = $1::INTEGER AND program.status = $2::programstatus



SELECT program_clients.client_id, program_clients.program_id, program_clients.price, program_clients.status, program_clients.contract_status, program_clients.created_at, program_clients.id, program_1.title, program_1.start_date, program_1.end_date, program_1.place, program_1."desc", program_1.price AS price_1, program_1.status AS status_1, program_1.slug, program_1.id AS id_1 
FROM program_clients JOIN client ON program_clients.client_id = client.id LEFT OUTER JOIN program AS program_1 ON program_1.id = program_clients.program_id 
WHERE client.slug = $1::VARCHAR AND (EXISTS (SELECT 1 
FROM program 
WHERE program.id = program_clients.program_id AND program.status = $2::programstatus))