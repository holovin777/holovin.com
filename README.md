# holovin.com


Initial data

The default checkout process requires a shipping address with a country. Oscar uses a model for countries with flags that indicate which are valid shipping countries and so the country database table must be populated before a customer can check out.

The easiest way to achieve this is to use country data from the pycountry package. Oscar ships with a management command to parse that data:

$ pip install pycountry
[...]
$ python manage.py oscar_populate_countries

By default, this command will mark all countries as a shipping country. Call it with the --no-shipping option to prevent that. You then need to manually mark at least one country as a shipping country.

