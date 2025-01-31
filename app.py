from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from utils.linkedin_scraper import fetch_linkedin_details
from utils.message_formatter import generate_message
from utils.message_selector import select_welcome_message


app = FastAPI()

@app.post("/process/")
async def process(file: UploadFile):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="File must be a CSV")
    print(f"Request Received...")
    try:
        # Read CSV content
        data = pd.read_csv(file.file)
        
        # Check mandatory fields
        mandatory_fields = {'name', 'email', 'linkedin_profile'}
        if not mandatory_fields.issubset(data.columns):
            raise HTTPException(status_code=400, detail=f"CSV must contain columns: {mandatory_fields}")
        print(f"Request is valid!!!")
        # result to send back to clients
        results = []

        for _, row in data.iterrows():
            name = row['name']
            email = row['email']
            linkedin_url = row['linkedin_profile']
            
            # Get additional details from LinkedIn URL
            profile_details = fetch_linkedin_details(linkedin_url)
            
            # get welcome message for the main message
            welcome_message = select_welcome_message(profile_details)

            # data for the template
            profile_data = {
                "name": name,
                "welcome_message": welcome_message
            }

            # get main message
            message = generate_message(profile_data)
            
            # Append result
            results.append({
                "name": name,
                "email": email,
                "linkedin_profile": linkedin_url,
                "message": message
            })
        
        print(f"Request processing complete!!!")
        # Return results as JSON
        return JSONResponse(content={"profiles": results})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
