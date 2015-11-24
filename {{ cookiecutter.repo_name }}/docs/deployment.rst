**********
Deployment
**********

Describe how to deploy your project here.


The configuration uses `envdir <https://pypi.python.org/pypi/envdir>`_.
There are some settings that need to be completed or changed on the
first deployment. Each of them is an environment variable set in an
envdir:

If you are using Mailgun:

``DJANGO_MAILGUN_ACCESS_KEY``
    `Mailgun <https://www.mailgun.com/>`_ secret API key. You can find the
    secret API key on the `Mailgun dashboard <https://mailgun.com/app/dashboard>`_.

``DJANGO_MAILGUN_SERVER_NAME``
    Specifies your subdomain where the email are sent from. More
    information about domains can be found in the
    `Mailgun User Manual <https://documentation.mailgun.com/user_manual.html#verifying-your-domain>`_.

