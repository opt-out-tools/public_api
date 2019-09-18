Opt Out Public Api
==========


Add a short description here!


Description
===========

You can get latest version of stable docker image using
`docker pull softerrific/opt_out_api:0.1.3`

Also If you want to just get entire project running so you can test how it works
easiest solution would be to just run
`docker-compose run`
Which will provide you with running application on port 8000

API
===
All requests are POST
In case of a error they will return status code 400 
with a json dictionary containing field `errors` which value is list of fields along with errors detected in them

***

/submit_urls
 - urls (array of urls)
 - self_submission (boolean)
 - is_part_of_larger_attack (boolean)

Returns (status 201)
 - submission_id  (id which will be used in submit_further_details)

***

/submit_further_details
 - identify (text, max_size=100)
 - age (positive integer)
 - job (text, max_size=160)
 - perpetrator
 - interaction
 - reaction_type
 - experienced (array of texts, max_text_size=300)
 - feeling (text, max_size=300)
 - submission (id of previously created submission)
 
 Returns (status 201)
 *** 
 
/predict 
 - texts (array of texts, max_size=400)  
 
Returns (status 200): 
 - predictions (array of booleans)

Development
===========

Run `poetry install`
and after that `pre-commit install`

You can test your commit checks by running
`pre-commit run`

You will also need to specify django configuration in .env file (which is not committed to repository)
Example
```

DB_NAME=database_name
DB_USER=db_user
PASSWORD=data_base_password
SECRET_KEY=super_secret_password
DEBUG=TRUE
DB_HOST=database_host
TF_XLA_FLAGS=--tf_xla_cpu_global_jit
```

Note
====

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
