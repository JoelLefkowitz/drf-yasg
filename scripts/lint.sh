#!/bin/bash
set -ev

TARGETS='src/drf_yasg2 testproj tests setup.py'
IGNORE='E230,E231,E501,F405,W504'
EXCLUDE='**/migrations/*'

echo $TARGETS --ignore $IGNORE --exclude $EXCLUDE --count
flake8 $TARGETS --ignore $IGNORE --exclude $EXCLUDE --count
