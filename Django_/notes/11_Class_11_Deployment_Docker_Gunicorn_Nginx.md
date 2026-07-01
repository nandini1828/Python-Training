# Class 11: Deployment — Docker, Gunicorn, Nginx

## Learning Objectives

After this class, you will understand:

- How to deploy a Django app using Docker
- What Gunicorn is
- What Nginx does
- Why deployment is different from development

## What is Docker?

Docker packages apps into containers so they run consistently everywhere.
A Docker container includes your code, environment, and dependencies.

## What is Gunicorn?

Gunicorn is a Python WSGI HTTP server.
It is used to serve Django applications in production.

## What is Nginx?

Nginx is a web server and reverse proxy.
It forwards requests to Gunicorn and serves static files.

## Deployment Flow

Browser
↓
Nginx
↓
Gunicorn
↓
Django
↓
Response

## Why Deployment is Different

In development, you use `runserver`.
In production, you use Gunicorn and Nginx.

Production also requires:

- secure settings
- `DEBUG = False`
- allowed hosts
- static file collection
- database configuration

## Summary

This class covered:

- Docker
- Gunicorn
- Nginx
- deployment concepts

## Interview Questions

1. What does Gunicorn do?
2. What is Nginx used for?
3. Why should `DEBUG` be false in production?
4. What is a Docker container?

## Exercises

1. Write a simple Dockerfile for Django.
2. Explain why Nginx is useful in production.
3. List the changes needed to switch from development to production.
