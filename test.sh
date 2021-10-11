#!/bin/env bash
set -euo pipefail

pytest -vv
dinject README.md
