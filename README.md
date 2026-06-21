# Reproducible ML Pipeline — Session 5
A worked example of code, data, experiment and environment versioning.
%%writefile .gitignore
__pycache__/
*.pyc
mlruns/
/data/*.csv
!git add README.md .gitignore
!git commit -m "Project skeleton: README, gitignore, folder layout"
!git log --oneline
