# Phish Proof
The Phish Proof web app is designed to teach corporations and their employees how to practice proper security hygiene. Phish Proof consists of various rooms that are designed to educate about the various ways that attackers attempt to social engineer employees, exploit insecure passwords, and exploit excessive permissions to move laterally within a network or gain access to sensitive data. Each user will have their own login and be able to move through the material at their own pace.
Practicing proper security hygiene is very important for corporations especially ones that deal with Personally Identifiable Information (PII). Informing your employee base of best security practices will not only keep them from being exploited, but it makes your company more secure overall. The number one weakness in security is humans, but the number one strength in security is well informed humans.

## Installation
```bash
pip install django
pip install bleach
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run Phish Proof, simply,
```bash
python manage.py runserver
```
In order to create a class or challenge via the admin portal, navigate to:
```bash
/admin/
```
and login with the superuser you created.
Additionally, here you can create/modify users.

# License
The MIT License

Copyright (c) 2025 Mason Wagner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.