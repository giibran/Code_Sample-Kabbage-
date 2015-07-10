# Code_Sample-Kabbage

## Performance

#### Searching "python"

- My Django View: 345 ms
- Twitter Api: 577 ms
- Wikipedia Api: 202 ms

#### Searching "python django"

- My Django View: 344 ms
- Twitter Api: 677 ms
- Wikipedia Api: 260 ms

#### Searching "the lord of the rings"

- My Django View: 320 ms
- Twitter Api: 808 ms
- Wikipedia Api: 441 ms

## Instalation

1. Clone repository with:
```
git clone https://github.com/giibran/Code_Sample-Kabbage-.git
```

2. Go to new directory of project and run migrations:
```
python manage.py migrate
```

3. Now create a super user:
```
python manage.py createsuperuser
```

4. Open the browser and go to [localhost:8000/admin](localhost:8000/admin)

5. Login with credentials of user created in step 3

6. In admin view click the sites link, open the site already created and set the values with the next data:
- Domain name: localhost
- Display name: twitter

7. Return to admin home [localhost:8000/admin](localhost:8000/admin)

8. In "Social Accounts" click the add option of "Social applications"

9. In new social application view set the values with next data:
- Provider: chose "twitter"
- Name: twitter
- Clien Id: "Consumer Key (API Key)" this key is provider by twitter
- Secret key: "Consumer Secret (API Secret)" this key is provider by twitter
- Move "localhost" site from available sites to chosen sites

10. Done, now go to [localhost:8000](localhost:8000) and test the app
