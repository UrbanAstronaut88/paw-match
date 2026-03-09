# Paw Match

Paw Match is a web service that helps users find the most suitable dog breed based on their lifestyle and preferences.

The application analyzes user parameters (living space, activity level, presence of kids, etc.) and matches them with dog breed characteristics stored in the database.

The goal of the project is to demonstrate a full-stack product workflow including backend API development, frontend UI, and recommendation logic.

## Features

Dog breeds database

Breed recommendation algorithm

Quiz-based matching system

REST API for frontend integration

Favorites list for users

Basic analytics for quiz results

## Tech Stack
* Backend

* Python 3.12

* Django

* Django REST Framework

* PostgreSQL

* Django ORM

## Infrastructure

* Docker
* Docker Compose
* Authentication
* JWT Authentication

## Tools

* Git / GitHub

* Postman (API testing)

* pytest (testing)


## Database Models (Simplified)
* Breeds

* Stores information about dog breeds.

### Fields:

* name

* description

* image_url

* size (1–3)

* energy_level (1–5)

* grooming_difficulty (1–5)

* kids_friendly

* housing_type

## Users

* Stores user accounts.

### Fields:

* email

* name

* password (hashed)

* favorites

## QuizResults

### Stores answers from the matching quiz.

#### Fields:

* user_id

* activity_level

* living_space

* kids

* created_at


## Setup (Development)

### Clone the repository:

```bash
git clone https://github.com/UrbanAstronaut88/paw-match
```
* Go to project directory:

```bash
cd paw-match
```

* Run with Docker:
```bash
docker-compose up --build
```

----------------------------------------------------------------------

# Team Roles

* ## Backend Developer
#### Responsible for API development, database architecture, and matching algorithm.

* ## Frontend Developer
#### Responsible for UI implementation and quiz interface.

* ## QA Engineer
#### Responsible for testing and validating matching logic.

* ## Scrum Master
#### Responsible for task management and sprint organization.