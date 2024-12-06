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





SELECT program_clients.client_id, program_clients.program_id, program_clients.price, program_clients.status, program_clients.contract_status, program_clients.created_at, program_clients.id, program_1.title, program_1.start_date, program_1.end_date, program_1.place, program_1."desc", program_1.price AS price_1, program_1.status AS status_1, program_1.slug, program_1.id AS id_1 
FROM program_clients JOIN client ON program_clients.client_id = client.id LEFT OUTER JOIN program AS program_1 ON program_1.id = program_clients.program_id 
WHERE client.slug = $1::VARCHAR 

AND (EXISTS (SELECT 1 
FROM program 
WHERE program.id = program_clients.program_id AND program.status = $2::programstatus))
2024-12-06 14:19:15,835 INFO sqlalchemy.engine.Engine [generated in 0.00152s] ('smirnoviurii', 'AC')
2024-12-06 14:19:15,884 INFO sqlalchemy.engine.Engine SELECT client.id AS client_id, client.phone AS client_phone, client.email AS client_email, client.slug AS client_slug, client.updated_at AS client_updated_at, client.created_at AS client_created_at, client.name AS client_name, client.last_name AS client_last_name, client.second_name AS client_second_name 
FROM client 
WHERE client.id IN ($1::INTEGER)

SELECT client_document.client_id AS client_document_client_id, client_document.doc_type AS client_document_doc_type, client_document.series AS client_document_series, client_document.number AS client_document_number, client_document.date_of_issue AS client_document_date_of_issue, client_document.issued_by AS client_document_issued_by, client_document.id AS client_document_id 
FROM client_document 
WHERE client_document.client_id IN ($1::INTEGER)

SELECT client_profile.client_id AS client_profile_client_id, client_profile.shirt_size AS client_profile_shirt_size, client_profile.status AS client_profile_status, client_profile.nutrition_features AS client_profile_nutrition_features, client_profile.comment AS client_profile_comment, client_profile.city AS client_profile_city, client_profile.date_of_birth AS client_profile_date_of_birth, client_profile.id AS client_profile_id 
FROM client_profile 
WHERE client_profile.client_id IN ($1::INTEGER)



SELECT program_clients.client_id, program_clients.program_id, program_clients.price, program_clients.status, program_clients.contract_status, program_clients.created_at, program_clients.id, program_1.title, program_1.start_date, program_1.end_date, program_1.place, program_1."desc", program_1.price AS price_1, program_1.status AS status_1, program_1.slug, program_1.id AS id_1, client_document_1.doc_type, client_document_1.series, client_document_1.number, client_document_1.date_of_issue, client_document_1.issued_by, client_document_1.client_id AS client_id_1, client_document_1.id AS id_2, client_profile_1.shirt_size, client_profile_1.status AS status_2, client_profile_1.nutrition_features, client_profile_1.comment, client_profile_1.city, client_profile_1.date_of_birth, client_profile_1.client_id AS client_id_2, client_profile_1.id AS id_3, client_1.phone, client_1.email, client_1.slug AS slug_1, client_1.updated_at, client_1.created_at AS created_at_1, client_1.name, client_1.last_name, client_1.second_name, client_1.id AS id_4 
FROM program_clients JOIN client ON program_clients.client_id = client.id LEFT OUTER JOIN program AS program_1 ON program_1.id = program_clients.program_id LEFT OUTER JOIN client AS client_1 ON client_1.id = program_clients.client_id LEFT OUTER JOIN client_document AS client_document_1 ON client_1.id = client_document_1.client_id LEFT OUTER JOIN client_profile AS client_profile_1 ON client_1.id = client_profile_1.client_id 
WHERE client.slug = $1::VARCHAR 

AND (EXISTS (SELECT 1 
FROM program 
WHERE program.id = program_clients.program_id AND program.status = $2::programstatus))