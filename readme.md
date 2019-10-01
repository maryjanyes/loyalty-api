### loyalty app: API

### DOCS (REQUESTS/REQUIRED)

<b> - auth </b> </br>
:/GET </br>
root/?password=<password>&username=<username>&email=<email>
(!IMPORTANT)
for create new user use short <a target="_self" href="https://github.com/maryjanyes/loyalty-api/blob/master/how-to-manage-account.md">doc</a>

<b> - customer </b> </br>
:/POST </br>
root/customer/?name=<name>&family_name=<family_name>&email=<email>

<b> - balance </b> </br>
:/GET </br>
(retrieve balance by `customer_id`) </br>
root/customer/balance/?customer_id=<customer_id> </br>
-- </br>
:/POST </br>
(create customer balance tx) </br>
root/customer/balance/?customer_id=<customer_id>&is_accrual=<is_accrual_tx>&count=<count_to_be_changed>
- you can got next result:
<img src="./tx-response-example.png" alt="tx response" />

### pre-install
- `pip install -r requirements.txt`
- `python -m ./balance/clickhouse.py True`

### services
run redis! </br>
run clickhouse! </br>
(or use Docker container)

### run
- `python manage.py runserver`
- separate processes: </br>
`python -m celery -A balance worker -l info --pool=solo` </br>
`python -m celery -A balance beat -l info` </br>
(you can use `options` args)

### db
(credentials)
- initial login: `admin`
- initial password: `0000`

### comments (REQUIRED)
to run this app on PROD env on the server you must follow next steps:
- update variable ALLOWED_HOSTS in the settings.py file
  change 2 array string to <yourorg@mail.com> for allow cors fetch to your resource
