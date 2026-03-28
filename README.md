#  Paw Match

**Paw Match** is a web service that helps users find the most suitable dog breed based on their lifestyle and preferences.

The application analyzes user parameters (living space, activity level, presence of kids, etc.) and matches them with dog breed characteristics stored in the database.

---

##  Features

-  Dog breeds database
-  Smart breed recommendation algorithm
-  Quiz-based matching system
-  Favorites list for authenticated users
-  Quiz results history
-  JWT Authentication
-  REST API for frontend integration

---

##  Matching System

The project includes an **advanced matching system** that recommends the most suitable dog breeds based on user preferences.

###  Input Parameters

User provides:

- `size` (1–3)
- `energy` (1–5)
- `kids` (1–5)
- `housing_type` ("Apartment", "House", "Apartment/House")

---

###  Algorithm Logic

Each breed is evaluated using a **weighted scoring system**.

#### Weights:

| Parameter | Weight |
|----------|--------|
| size     | 1.0    |
| energy   | 1.5    |
| kids     | 2.0    |
| housing  | 2.5    |

- Lower score → better match
- Final result is converted into **match percentage (0–100%)**

---

##  API Overview

###  Authentication

- `POST /api/v1/auth/register/`
- `POST /api/v1/auth/login/`
- `POST /api/v1/auth/logout/`
- `GET /api/v1/auth/me/`

---

###  Breeds

- `GET /api/v1/breeds/`
- `GET /api/v1/breeds/{id}/`

---

###  Matching

- `POST /api/v1/match/`

➡ Returns best matching breeds  
➡ Automatically saves quiz result (if user is authenticated)

---

###  Favorites

- `POST /api/v1/breeds/{id}/favorite/`
- `DELETE /api/v1/breeds/{id}/unfavorite/`
- `GET /api/v1/favorites/`

---

###  Quiz Results

- `GET /api/v1/quiz-results/`
- `GET /api/v1/quiz-results/{id}/`
- `POST /api/v1/quiz-results/`

Update/delete operations are intentionally disabled (immutable history)

---

##  Database Models (Simplified)

### Breed

- `name`
- `description`
- `image_url`
- `size`
- `energy`
- `grooming`
- `kids_friendly`
- `housing_type`

---

### Favorite

- `user`
- `breed`

---

### QuizResult

- `user`
- `size`
- `energy`
- `kids`
- `housing_type`
- `created_at`

---

## Tech Stack

### Backend:

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Django ORM

---

## Infrastructure

- Docker
- Docker Compose
- JWT Authentication

---

## Tools

- Git / GitHub
- Postman

---

## Setup (Development)

### 1. Clone repository

```bash
git clone https://github.com/UrbanAstronaut88/paw-match
```

### 2. Run Project
```
cd paw-match
docker-compose up --build

docker compose exec web python manage.py createsuperuser
```


## Team Roles (Concept)
* Backend Developer – API, database, matching logic
* Frontend Developer – UI, quiz interface
* QA Engineer – testing & validation
* Designer – UX/UI
* Data Analyst – analytics & insights
* Project Manager – coordination