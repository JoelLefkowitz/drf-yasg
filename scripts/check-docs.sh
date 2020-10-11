#!/bin/bash
set -ev

twine check .tox/dist/*
