git checkout heroku
git rebase master
git push -f
git push heroku heroku:master -f
heroku run python manage.py migrate
