# narrative-csv-upload-backend

-- Download Docker Desktop and configure\
-- open terminal and go to project path\
-- Run docker-compose build (if see unauthorised error. Run "docker login" cmd on terminal and provide username/email and possword and build agian)\
-- Run docker-compose up




# Backend Possible Optimisations:
-- Authentication and Authorization\
-- Complete CRUD operations on data (Create, Read, Update, Delete)\
-- Upload multiple files in one go using multi threading.\
-- Better DB Design.\
-- Bulk operation to update, create data in batches to reduce db calls.\
-- Robust Error handing\
-- Efficiently handle CSV files with mixed data types and multiple sheets using robust libraries like pandas for parsing, cleaning, and formatting.\
-- Ensure data consistency and readability by correcting text grammar and properly processing non-text data.\
-- Supporting multiple types of document extensions like .DOC, .DOCX, .TXT, PDF etc\
-- Geocoding API to get a State from location, city, address etc\
-- Proper commenting for easy understanding\
-- S3 buckets for storing files\
-- Better code structure with OOPs for Modularity, Reusability, Maintainability and Scalabilit\
-- Google Map API key is directly passed to the Googlemaps SDK\
-- Use of environment variables for secret API Keys


# Optimisations:
-- Google maps geocoding API integrated\
-- S3 AWS Bucket integrated

