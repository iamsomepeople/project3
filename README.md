# This is Joe Tam's portfolio project 3

## Description
In previous module, I developed a flask application of a restaurant which provided some simple functions like create an order, assigning staff to handle an order, etc.

In this project, I have re-written it using django framework, here are the criterias I have achieved in this project:

- Data query using ORM
- Leverage AWS ECS (Elastic Container Services) to deploy my project
- Apply JWT (Json Web Tokens) as authentication of api calls

## Setup
*  Prerequisites
    - ECS cluster
    - RDS Postgresql instance with a database named "proj3"
    - Security group for RDS instance above allows TCP 5432 connections from ECS EC2 instances
* DB Initialize procedure (Needed only for first time startup)
    1. Access the ECS EC2 instance using SSH
        > ssh -i \<your keypair> ec2-user@\<your ec2 instance>
    2. Make a migration for django base tables
        > python manage.py makemigrations
    3. Apply the migration to RDS    
        > python manage.py migrate
    4. Make a migration for Staffs app
        > python manage.py makemigrations staffs
    5. Apply the migration for Staffs app to RDS 
        > python manage.py migrate staffs
    6. Make a migration for Customers app
        > python manage.py makemigrations customers
    7. Apply the migration for Customers app to RDS 
        > python manage.py migrate customers
    8. Make a migration for Orders app
        > python manage.py makemigrations orders
    7. Apply the migration for Orders app to RDS 
        > python manage.py migrate orders
* (Optional) Load sample data into RDS
    1.  Load Staffs data
        > python sample_data.py
    2.  Load Customers data
        > python sample_data_customers.py
    3.  Load Orders data
        > python sample_data_orders.py
    
