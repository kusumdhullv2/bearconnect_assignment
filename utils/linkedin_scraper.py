from linkedin_api import Linkedin
from datetime import datetime
import os


def fetch_linkedin_details(linkedin_url):

    result = {}
    print(f"Fetching linked in profile information...")

    # Authenticate using any Linkedin user account credentials
    username = os.environ['ASSIGNMENT_USERNAME']
    password = os.environ['ASSIGNMENT_PASSWORD']
    api = Linkedin(username, password)
    #   print(f"api : {api}")

    # GET a profile
    profile_name = linkedin_url.split("/")[-1]
    #print(f"profile_name : {profile_name}")
    profile = api.get_profile(profile_name)
    #print(f"profile : {profile.items()}")
    print(f"linked in profile information fetched for profile {profile_name}.")

    if(profile["student"] == "True"):
        result["student"] = True
        # get education from profile
        profile_education = profile["education"]
        #print(f"profile education : {profile_education}")
        latest_education = profile_education[0]
        school_name = latest_education.get('schoolName', None)
        #print(f"school name : {school_name}")
        result["student_college_name"] = school_name
    else:
        result["student"] = False        
        # get experience from profile
        profile_experience = profile["experience"]
        #print(f"profile experience : {profile_experience}")
        latest_experience = profile_experience[0]
        # get company name
        company_name = latest_experience.get('companyName', 'Unknown')
        result["current_company_name"] = company_name

        # get company experience
        start_date = latest_experience.get('timePeriod', {}).get('startDate', {})
        start_year = start_date.get('year')
        start_month = start_date.get('month')

        experience_years = 0  # Default to 0 if start date is not available
        if start_year and start_month:
            start_date_obj = datetime(start_year, start_month, 1)
            current_date = datetime.now()
            experience_years = (current_date.year - start_date_obj.year) + ((current_date.month - start_date_obj.month) / 12)
            experience_years = round(experience_years, 1)  # Round to 1 decimal place
            result["current_company_tenure"] = experience_years

        result["current_company_tenure"] = experience_years
            
        # get job title
        # Determine if the person is a founder
        title = latest_experience.get('title', '').lower()
        if 'founder' in title or 'co-founder' in title:
            result["founder"] = True
            result["founding_company_name"] = company_name
        else:
            result["founder"] = False

        print(f"result : {result}")
    return result