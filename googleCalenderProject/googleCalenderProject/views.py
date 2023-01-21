import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View

class GoogleCalendarInitView(View):
    def get(self, request):
        # Set the necessary parameters for the OAuth process
        client_id = settings.GOOGLE_CLIENT_ID
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        scope = 'https://www.googleapis.com/auth/calendar'
        
        # Redirect the user to the Google authorization endpoint
        auth_url = f'https://accounts.google.com/o/oauth2/auth?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code'
        return redirect(auth_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        # Get the code from the request
        code = request.GET.get('code')
        
        # Set the necessary parameters for getting the access_token
        client_id = settings.GOOGLE_CLIENT_ID
        client_secret = settings.GOOGLE_CLIENT_SECRET
        redirect_uri = settings.GOOGLE_REDIRECT_URI
        grant_type = 'authorization_code'
        
        # Make a POST request to the Google token endpoint
        token_url = 'https://accounts.google.com/o/oauth2/token'
        data = {
            'code': code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': redirect_uri,
            'grant_type': grant_type
        }
        response = requests.post(token_url, data=data)
        access_token = response.json().get('access_token')
        
        # Use the access_token to get the list of events in the user's calendar
        calendar_url = 'https://www.googleapis.com/calendar/v3/calendars/primary/events'
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        events_response = requests.get(calendar_url, headers=headers)
        events = events_response.json().get('items', [])
        
        # Return the list of events in the response
        return JsonResponse(events, safe=False)        
