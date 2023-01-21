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
git clone https://github.com/<your-username>/google-calendar-django-rest-api.git

Copy code

2. Create a virtual environment and activate it
python -m venv myenv
source myenv/bin/activate

Copy code

3. Install the dependencies
pip install -r requirements.txt

Copy code

4. Create a project in the [Google developer console](https://console.developers.google.com/) and enable the Google Calendar API.

5. In the developer console, navigate to the `Credentials` page, create a new OAuth client ID, and specify authorized redirect URIs.

6. Set the client_id, client_secret, and redirect_uri in the settings.py file.

7. Set the url for the views in your urls.py file.

8. Start the development server
python manage.py runserver

Copy code

### Testing the integration

You can test the integration by sending GET requests to the URLs that trigger the views and checking the responses.

1. Open a web browser and navigate to the URL for the GoogleCalendarInitView. For example, if the URL for this view is `/rest/v1/calendar/init/`, you would navigate to `http://localhost:8000/rest/v1/calendar/init/`

2. The browser should redirect you to the Google authorization endpoint, where you will be prompted to enter your Google credentials and grant access to your calendar.

3. After granting access, the browser will redirect you to the URL for the GoogleCalendarRedirectView.

4. The view will handle the redirect request, get the access_token, and get the list of events in the user's calendar. The view will return the list of events in the response in json format.

5. You can use a tool like `curl` or `httpie` to test the endpoint and check the response. for example:
curl -X GET http://localhost:8000/rest/v1/calendar/redirect/

Copy code

6. You can also test this by using `postman` by sending the GET request to the above url
