# API - Application Programming Interface - программный интерфейс приложения
# HTTP/HTTPS (Hypertext Transfer Protocol/Secure Hypertext Transfer Protocol, протокол передачи гипертекста/протокол защищенной передачи гипертекста)
#  — основа веб-коммуникации и передачи данных в Интернете.
# REST (Representational State Transfer, передача состояния представления) строго говоря, не протокол, а архитектурный стиль, построенный поверх 
# HTTP. API, созданные в этом стиле, называются RESTful. Они не сохраняют состояние (не хранят информацию о предыдущих запросах) 
# и позволяют эффективно кэшировать данные.
# RPC (Remote Procedure Call, удаленный вызов процедуры) — позволяет выполнять код на сервере, удаленно вызывая процедуры (по имени). 
# Такие API обычно тесно связаны с реализацией на серверной стороне и редко публикуются в открытом доступе.
# CRUD - CREATE, READ, UPDATE, DELETE
'''
entity - relationship schema (ER схема)
user:
- id
- email
- full_name
- password
- role

ticket:
- id
- car_class
- created_at
- price
- train_id
- user_id

train:
- id
- arrives_at
- departs_at
- first_class
- name
- seats_per_car
- second_class
- station_from_id
- station_to_id

station:
- id
- city
- code
- country
'''
