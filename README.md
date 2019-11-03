# T13 Activity Web

Website to help organizations &amp; clubs coordinate activities amongst their members, especially my local karting club.

Developed by [Marcus Sonestedt](https://www.github.com/marcusl) under the [Affero GPL license](https://en.wikipedia.org/wiki/Affero_General_Public_License).

## Data model

* EventTypes - race day, training week, track work day or club barbequeue
* Events - a specific race or similar time-bound event of some type
* ActivityType - a role that has to be filled during an event, flag marshal, pre-grid controller or technical scrutineer for races, carpenter or painter for work days or grillmeister and saucemaster for barbequeues.
* Activity - a specific activity of given type for an event, which can be assigned to a user
* Member - person able to perform an Activity, possible linked to a web site User

## Development

* Any OS should work, although it has been devleoped on Windows with the goal to support running on Linux in production.
* Visual Studio Code is an free and excellent editor.
* Visual Studio Community/Professional is also usable.

### Architecture Overview

This project was set-up with inspiration from [this blog](https://www.valentinog.com/blog/drf/) but using  Typescript instead of Javascript for the React frontend for type safety.

Currently, the React-based frontend is served via the Django web server but it could be moved to a fast, static website/CDN in the future.

The end-user part of the front-end is written in React to
work as a single-page web application, putting most of the
work on the client and leaving the server with only delivering
data and answering terse api-calls.

For administrators, a classic render-html-on-server approach
via the regular Django framework is used, mostly because we
want to use Django's great autogenerated admin-site to enter
and adjust the backing data

### FrontEnd

Uses [React](https://reactjs.org), TypeScript and Bootstrap.

* Install [Node.js](https://nodejs.org)
* Install packages:

```bash
npm install
```

* Start development server
```
npm start
```

### Backend

Uses [Django](https://www.djangoproject.com) & [Django REST Framework](https://www.django-rest-framework.org/).

By default, uses the [SQLite](https://www.sqlite.org/) db during development, which runs in-process against a single file.

* Install [Python](https://www.python.org)

* Create and activate a virtual python environment
```bash
python -m venv env
env/scripts/activate
```

* Instlal packages
```bash
python -m pip install -r requirements.txt
```

* Init database and populate tables
```bash
python manage.py createsuperuser
python manage.py loaddata testdata
```

* Start development server
```bash
python manage.py runserver
```
