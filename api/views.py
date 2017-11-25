from django.shortcuts import render
from django.http import JsonResponse
from linkedin import linkedin
from secret import API_KEY, API_SECRET

def sign_in(request):
    # Get the authorization URL from Linkedin
    RETURN_URL = "http://localhost:8000/sign_in/"
    authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    application = linkedin.LinkedInApplication(authentication)
    return JsonResponse({'auth_url': authentication.authorization_url})
