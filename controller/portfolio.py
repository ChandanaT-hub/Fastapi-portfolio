from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, JSONResponse
from models.models import Portfolio, Experience

router = APIRouter()
# templates = Jinja2Templates(directory="templates")
import os
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates")
)

portfolio_data = Portfolio(
    name="Chandana T",
    role="Python Backend Engineer",
    about="Backend Engineer with 2+ years experience in fintech systems using FastAPI, PostgreSQL, and AWS.",
    skills=[
        "Python", "FastAPI", "PostgreSQL", "AWS", "Redis", "Celery",
        "SQLAlchemy", "Python", "Nginx"
    ],
    experience=[
        Experience(
            company="Evoqins",
            role="Software Engineer",
            description=[
                "Took ownership of a live fintech backend system without formal knowledge transfer and ensured continued development and stability",
                "Designed and maintained REST APIs using FastAPI and PostgreSQL for financial transaction workflows.",
                "Handled production bug fixes, feature development, and API version upgrades for live services.",
                "Built asynchronous processing pipelines using Celery and Redis for background jobs including report generation and notifications.",
                "Implemented automated investment report generation using Jinja2 templates and wkhtmltopdf." 
                "Deployed and maintained backend services on AWS EC2 using Nginx and Systemd.", 
                "Monitored and debugged production systems using AWS CloudWatch logs.", 
                "Assisted the client directly with technical clarifications, bug investigations, and production issues.",
                "Automated scheduled backend operations by implementing cron jobs for time-based status updates and recurring processes."  
                "Leveraged AI-powered tools like Cursor and Claude to accelerate development, optimize code quality, and improve debugging efficiency."
            ]
        ),
        Experience(
            company="Payrup",
            role="Software Engineer Intern",
            description=[
                "Developed UI using React.js",
                "Improved frontend usability"
            ]
        )
    ]
)

# @router.get("/")
# def home(request: Request):
#    return JSONResponse(
#         content={
#             "message": "Hey there",
#             "data": portfolio_data.dict()
#         }
#     )
@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={
            "data": portfolio_data.dict()
        }
    )

# Resume download route
@router.get("/download-resume")
def download_resume():
    return FileResponse(
        path="static/resume/RESUME_CHANDANA_T.pdf",
        filename="RESUME_CHANDANA_T.pdf",
        media_type='application/pdf'
    )