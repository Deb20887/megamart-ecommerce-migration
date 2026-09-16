#!/bin/bash

# MegaMart Catalog Service load test
# Usage:
#   ./catalog-load-test.sh <catalog-service-url>

URL="${1:-http://localhost:8000}"

echo "MegaMart Catalog Service Load Test"
echo "Target: $URL"
echo

for i in {1..20}
do
    curl -s -o /dev/null -w "Request $i: HTTP %{http_code}\n" "$URL/products"
done

echo
echo "Load test completed."
