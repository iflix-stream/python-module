from waitress import serve
import App
serve(App.api,listen='*:8080')