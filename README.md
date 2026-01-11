# AI Wiki Quiz Generator

## Project Description
AI Wiki Quiz Generator is a full-stack web application that allows users to generate quizzes automatically from Wikipedia articles. By simply providing a Wikipedia URL, the system scrapes the article content, uses an AI language model to generate quiz questions, stores the results in a database, and displays them through an interactive web interface.

The application also maintains a history of previously generated quizzes, avoids duplicate processing of the same URL, and allows users to revisit earlier quizzes instantly.


## Objectives
- Automatically generate quizzes from Wikipedia articles
- Use AI to create meaningful questions with answers and explanations
- Store generated quizzes for future reference
- Provide a clean and user-friendly interface
- Demonstrate real-world integration of AI, scraping, backend APIs, databases, and frontend UI


## Features
- Accepts any valid Wikipedia article URL
- Scrapes article content using HTML parsing (no Wikipedia API)
- Generates 5 quiz questions using an AI model
- Each question includes:
  - Question text
  - Four options
  - Correct answer
  - Difficulty level
  - Explanation
- Suggests related Wikipedia topics
- Stores quizzes in a PostgreSQL database
- Prevents duplicate quiz generation for the same URL
- Displays quiz history
- Error-handled and stable end-to-end flow


## Technology Stack

### Frontend
- React.js (Class Components)
- HTML, CSS
- Fetch API for backend communication

### Backend
- Python
- Flask
- Flask-CORS
- Requests
- BeautifulSoup

### AI / LLM
- Gemini free-tier model
- Robust JSON extraction from AI responses

### Database
- PostgreSQL
- SQLAlchemy ORM

### Deployment
- Vercel


## Application Workflow

1. User enters a Wikipedia article URL in the frontend
2. Frontend sends the URL to the Flask backend
3. Backend validates the URL
4. Wikipedia page is scraped using BeautifulSoup
5. Extracted text is sent to the AI model
6. AI generates quiz questions in JSON format
7. JSON is safely parsed and validated
8. Quiz is stored in the PostgreSQL database
9. If the URL already exists, stored quiz is returned
10. Frontend displays the quiz in a structured layout
11. User can revisit quizzes via history


## API Endpoints

### Generate Quiz

**Request**(JSON)

{
  "url": "https://en.wikipedia.org/wiki/Alan_Turing"
}

**Response**(JSON)

{
  "id": 1,
  "url": "...",
  "title": "Alan Turing",
  "summary": "...",
  "quiz": [...],
  "related_topics": [...]
}
