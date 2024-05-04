# middleware.py
from django.http import Http404
from django.shortcuts import render
from django.urls import resolve


class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            # Check if the URL matches any known patterns
            try:
                resolve(request.path)
            except Http404:
                # If URL doesn't match any patterns, render custom 404 page
                return render(request, '404.html', status=404)
