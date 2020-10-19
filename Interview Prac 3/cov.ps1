coverage run test.py
coverage report -m
coverage html 

git add -A
git commit -m "continuous testing view"
git push 