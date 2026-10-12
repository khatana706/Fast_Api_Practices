Welcome to the **FastAPI & Pydantic Practices** repository! This project serves as a step-by-step practical guide to mastering modern data validation using **Pydantic (v2)** and building performance-driven asynchronous REST APIs using **FastAPI**.
>> 
>> ---
>> 
>> ## Repository Roadmap & File Structure
>> 
>> This repository contains standalone training scripts mapping out essential backend validation paradigms, culminating in a complete CRUD patient management system:
>> 
>>  **`main.py`** - A fully-functional, persistent RESTful Patient Management System API supporting complete CRUD operations, automated BMI calculators, and clinical health verdict generation.
>> -  **`patients.json`** - The flat-file JSON database layer storing patient dictionaries.
>> -  **`Whypandantic.py` & `whypandantic.py`** - Demonstration blueprints contrasting standard Python dictionaries against Pydantic structural schemas.
>> -  **`Field_validator.py`** - Implements field-specific constraints using Pydantic's `@field_validator` decorators.
>> -  **`computed_field.py`** - Demonstrates runtime structural modifications using `@computed_field` properties.
>> -  **`model_validator.py`** - Implements complex, multi-field cross-validation architectures using `@model_validator`.
>> -  **`nested_model.py`** - Practices complex object structures, embedding schemas within other schemas.
>> -  **`serialization.py`** - Practices converting Pydantic instances into standard Python dictionaries and raw string JSON encodings.
>> 
>> ---
>> 
>> ##  Features (Patient Management API)
>> 
>> -  **Create Patient:** Add validated logs with strict data checkpoints (Age range controls, specific Gender literals, positive physical dimensions).
>> -  **View Profiles:** Access a complete inventory of stored patient medical records.
>> -  **Targeted Lookup:** Instantly retrieve precise matching diagnostic records utilizing dynamic path parameters (`patient_id`).
>>    **Data Delta Modification (PUT):** Update specific parameters of a patient profile without breaking unchanged fields.
>> -  **Record Purging (DELETE):** Securely remove patient details from the persistent database state.
>> -  **Calculated BMI Matrix:** Embedded real-time computations adjusting BMI metrics to 2 decimal points.
>> -  **Automated Triage Logic:** Evaluates patient data instantly to label statuses (`Underweight`, `Normal`, `Overweight`, `Obese`).
>> 
>> ---
>> 
>> ##  Tech Stack & Requirements
>> 
>> - **FastAPI:** Modern Python web framework for highly efficient API development.
>> - **Pydantic (v2):** Core data parsing, structure enforcement, and automatic schema generators.
>> - **Uvicorn:** Ultra-fast ASGI server for launching local applications.
>> - **Python 3.10+**
>> 
>> ---
>> 
>> ## How to Run the Project Locally
>> 
>> ### Prerequisites
>> Ensure your local environment is running **Python 3.10** or higher.
>> 
>> ### Step 1: Clone the Repository
>> ```bash
>> git clone https://github.com
>> cd Fast_Api_Practices
>> ```
>> 
>> ### Step 2: Install Dependencies
>> ```bash
>> pip install fastapi uvicorn pydantic watchfiles
>> ```
>> 
>> ### Step 3: Spin Up the Application
>> ```bash
>> uvicorn main:app --reload
>> ```
>> 
>> ---
>> 
>> ## ?? Live API Testing Dashboard
>> 
>> FastAPI auto-generates highly functional user dashboards to run testing operations instantly without installing external tools like Postman. Launch your local instance and navigate to:
>> 
>> - **Interactive Swagger UI Documentations:** ?? [http://127.0.0](http://127.0.0)
>> - **Alternative Redoc Manual Layouts:** ?? [http://127.0.0](http://127.0.0)
>> 
