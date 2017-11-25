from django.shortcuts import render
from linkedin import linkedin
from secret import API_KEY, API_SECRET

def index(request):
    return render(request, 'index.html')

def sign_in(request):
    # Authenticate using the API key and Secret
    RETURN_URL = "http://localhost:8000/sign_in/"
    authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    authentication.authorization_code = request.GET.get('code')
    application = linkedin.LinkedInApplication(authentication)
    
    # Get the API access token
    tok = authentication.get_access_token()
    application = linkedin.LinkedInApplication(token=tok)

    # Render the user's profile data as JSON
    return render(request, 'sign_in.html', {'profile': application.get_profile()})
