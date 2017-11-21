from waitress import serve

from iflix import App

serve(App.api, listen='*:8080')