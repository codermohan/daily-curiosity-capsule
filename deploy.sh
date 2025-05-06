#!/bin/bash
echo "Building Docker image..."
docker build -t curiosity-capsule .

echo "Running app locally..."
docker run -d -p 5000:5000 curiosity-capsule
