# Google Calendar Integration for Django REST API

This project demonstrates how to integrate Google Calendar with a Django REST API using the OAuth2 mechanism. The project includes two views for handling the initial step of the OAuth process and handling the redirect request from Google. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 3.x
- Google developer console account
- A google calendar

### Installing

1. Clone the repository
`git clone https://github.com/<your-username>/google-calendar-oauth2--django.git`

2. Create a virtual environment and activate it
`python3 -m venv myenv
source myenv/bin/activate`

3. Install the dependencies
`pip install -r requirements.txt`

4. Create a project in the [Google developer console](https://console.developers.google.com/) and enable the Google Calendar API.

5. In the developer console, navigate to the `Credentials` page, create a new OAuth client ID, and specify authorized redirect URIs.

6. Set the client_id, client_secret, and redirect_uri in the `settings.py` file.

7. Set the url for the views in your `urls.py` file.

8. Start the development server
`python3 manage.py runserver`

### Testing the integration

You can test the integration by sending GET requests to the URLs that trigger the views and checking the responses.

1. Open a web browser and navigate to the URL for the GoogleCalendarInitView. For example, if the URL for this view is `/rest/v1/calendar/init/`, you would navigate to `http://localhost:8000/rest/v1/calendar/init/`

2. The browser should redirect you to the Google authorization endpoint, where you will be prompted to enter your Google credentials and grant access to your calendar.

3. After granting access, the browser will redirect you to the URL for the GoogleCalendarRedirectView.

4. The view will handle the redirect request, get the access_token, and get the list of events in the user's calendar. The view will return the list of events in the response in json format.

  
### Built With
[Django](https://www.djangoproject.com/) - The web framework used

[Python](https://www.python.org/) - Programming language

[Google Calendar API](https://console.cloud.google.com/marketplace/product/google/calendar-json.googleapis.com?q=search&referrer=search&project=calendarapi-375408&supportedpurview=project) - API used  

### Screenshots
  <img width="1470" alt="Screenshot 2023-01-21 at 5 22 03 PM" src="https://user-images.githubusercontent.com/110348583/213865666-9c280780-af5b-492d-8429-a2e5e1241245.png">

  
  <img width="1470" alt="Screenshot 2023-01-21 at 5 22 15 PM" src="https://user-images.githubusercontent.com/110348583/213865673-2bfe039a-5ba2-4b5a-aa6a-a12347452a77.png">

 
  
<img width="1470" alt="Screenshot 2023-01-21 at 5 22 26 PM" src="https://user-images.githubusercontent.com/110348583/213865679-0acce7c4-0f77-464c-9ebc-487971aa1b41.png">

Events in JSON format.

### Demo


https://user-images.githubusercontent.com/110348583/213901391-c687d8bc-e435-4291-ac5c-6efe1395e6f6.mp4

