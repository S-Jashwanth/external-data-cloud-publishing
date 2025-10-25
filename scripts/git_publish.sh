#!/usr/bin/env bash
set -e
if [ -z "$1" ]; then
  echo 'Usage: ./scripts/git_publish.sh <git-repo-https-url>'
  exit 1
fi
git init
git add .
git commit -m "Initial commit: External Data Cloud Publishing (Extended)"
git branch -M main
git remote add origin "$1"
git push -u origin main
