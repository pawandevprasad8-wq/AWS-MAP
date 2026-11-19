import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

AWS_REGION = os.environ.get("AWS_REGION", "ap-south-1")
AWS_LOCATION_API_KEY = os.environ.get(
    "AWS_LOCATION_API_KEY",
    "v1.public.eyJqdGkiOiIzYTBkODM0Yy1lN2E5LTRmZGItYTkxMS0yMDI1OTc4ZGExNWUifWy-fXLUhxq1O8pGpPZwqRt1kiucnUjiurjhg7n-j_9Kc3Hy8m1vmBAPWzJWwoZ4FFsvaBuPk7GJQYX3n_tORSoylFSH4tYUlaptpEExVgMNpZ_xmiNRCETWhzbGc8zkjAd5J1BuUF7K-F6WL3aqA5cvKCOMT_pOGqs8qg2--MBkBpRJasI1gheJsUae9xQdUl5CG1LBA4XdAZ6oj-hLqOEzU3f-telO6vSrwG_W2gaekLiOHnUnqlhIRbGk8hKDfcM0slxEAwlmlRFgUWiYDZoUzIqIji12iX2HPGs4JvHkSx50L3ZbJsStlTLFowf9MvZfULA30ce0gYACeZXRHrg.Njg1MGZlZTUtYTI2ZS00MDdlLWJjNDktMDNmZDlkNzVmMjQ0",
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "region": AWS_REGION,
            "api_key": AWS_LOCATION_API_KEY,
        },
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )
  
