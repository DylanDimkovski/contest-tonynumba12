#! /bin/bash

git tag -d testing
git push origin :testing
git tag testing
git push --tags