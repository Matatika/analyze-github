#!/bin/bash

# Exit on error
set -e

# Run the elt, and dbt commands and tests
meltano elt "$EXTRACTOR" "$LOADER" --transform=skip
meltano invoke dbt deps
meltano invoke dbt snapshot --select tap_github
meltano invoke dbt run -m tap_github
