# Django REST Framework and Docker



### PR for this file: https://github.com/kimmyd70/django_models/pull/1

This is Lab 27 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 5 March 2021
____________________

### Feature Tasks

1. Create `snack_tracker_project` in Django with 2 pages: snack list and snack details

2. Create views/urls/templates as needed 

3. Details page should include snack name, purchaser, and description

4. Should be built the “Django way” aka match the structure of in-class demo


__________________

### Server and Client

- Server: running on local server
- Client: Django

____________________

### Testing

Used integrated Django testing.  NOTE: make sure test extends TestCase instead of SimpleTestCase used in previous class.

1. Test Snack pages
    - verify status code
    - verify correct template use
    - use url name instead of hard coded path
TIP: django.urls.reverse will help with that.