### loyalty app: API

### docs (~requests~)

- auth
/GET
<root>/?password=<password>&username=<username>&email=<email>

- customer
/POST
<root>/customer/?name=<name>&family_name=<family_name>&email=<email>

- balance
/GET
(retrieve balance by `customer_id`)
<root>/customer/balance/?customer_id=<customer_id>
/POST
(create customer balance tx)
<root>/customer/balance/?customer_id=<customer_id>&is_accrual=<is_accrual_tx>&count=<count_to_be_changed>

### pre-install
pip install -r requirements.txt

### run
python manage.py runserver

- you can use <options> if you feel with

### comments
(REQUIRED)
to run this app on PROD env on the server you must follow next steps:
- update variable ALLOWED_HOSTS in the settings.py file
  change 2 array string to <yourorg@mail.com> for allow cors fetch to your resource
