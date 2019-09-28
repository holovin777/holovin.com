# [holovin.com](https://www.holovin.com)

## Quick installation

```bash
git clone https://github.com/holovin777/holovin.com.git
cd holovin.com
virtualenv venv
source venv/bin/activate
python holovin/manage.py migrate
python holovin/manage.py createsuperuser
python holovin/manage.py runserver
```

### Initial data

The default checkout process requires a shipping address with a country. Oscar uses a model for countries with flags that indicate which are valid shipping countries and so the country database table must be populated before a customer can check out.
The easiest way to achieve this is to use country data from the pycountry package. Oscar ships with a management command to parse that data:
```bash
pip install pycountry
python manage.py oscar_populate_countries
```
By default, this command will mark all countries as a shipping country. Call it with the --no-shipping option to prevent that. You then need to manually mark at least one country as a shipping country.

#### License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)
