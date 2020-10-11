#!/bin/bash
set -ev

sphinx-build -WnEa -b html docs docs/_build/html
