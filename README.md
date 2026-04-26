#  Paw Match

**Paw Match** is a web service that helps users find the most suitable dog breed based on their lifestyle and preferences.

The application analyzes user parameters (living space, activity level, presence of kids, etc.) and matches them with dog breed characteristics stored in the database.

---

##  Features

-  Dog breeds database (15 breeds)
-  Smart breed recommendation algorithm
-  Quiz-based matching system
-  Favorites list for authenticated users
-  Quiz results history
-  JWT Authentication
-  User profile (name, city, age, avatar)
-  Password change
-  Breed comparison system (NEW)
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

### ️ Algorithm Logic

Each breed is evaluated using a **weighted scoring system**.

#### Weights:

| Parameter | Weight |
|----------|--------|
| size     | 1.0    |
| energy   | 1.5    |
| kids     | 2.0    |
| housing  | 2.5    |

###  Formula
**score = Σ (weight × normalized_difference)**
- Lower score → better match
- Result converted to **match percentage (0–100%)**

---

## Breed Comparison (NEW)

Compare two dog breeds side-by-side with UI-ready data.

---

# Features
* Progress bar ready (value / max)
* Labels for UI
* Housing chips
* Custom comparison text from DB (via matrix)

---

# Authentication
* POST /api/v1/auth/register/
* POST /api/v1/auth/login/
* POST /api/v1/auth/logout/
* POST /api/v1/auth/refresh/


# User Profile
* GET /api/v1/auth/me/
* PATCH /api/v1/auth/me/ (update profile + avatar upload)
* PATCH /api/v1/auth/change-password/


# Breeds
* GET /api/v1/breeds/
* GET /api/v1/breeds/{id}/

# Matching
* POST /api/v1/match/


# Favorites
* POST /api/v1/breeds/{id}/favorite/
* DELETE /api/v1/breeds/{id}/unfavorite/
* GET /api/v1/favorites/

---

# Tech Stack
### Backend
- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Django ORM

### Frontend
- Vue 3 (Composition API)
- Pinia
- Vite
- Tailwind CSS
- Axios

# Infrastructure
- Docker
- Docker Compose
- JWT Authentication

---

# Setup (Development)
1) Clone the repository
```
git clone https://github.com/UrbanAstronaut88/paw-match
```

2) Run project
```
cd paw-match/backend
docker-compose up --build
```

3) Create Superuser
```
docker-compose exec web python manage.py createsuperuser
```

# API docs
### Swagger UI
http://127.0.0.1:8000/api/docs/

---


# Team Roles
* Backend Developer – API, database, matching logic 
* Frontend Developer – UI, quiz interface
* QA Engineer – testing & validation
* Designer – UX/UI
* Data Analyst – analytics, content
* Project Manager – coordination


