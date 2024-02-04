[app]
# (str) Title of your application
title = GitHubCommitApp

# (str) Package name
package.name = github_commit_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,github3.py

[buildozer]
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas
