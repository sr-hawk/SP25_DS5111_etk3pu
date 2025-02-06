#!/bin/bash
set -e

echo "Updating package list..."
sudo apt update

echo "Installing make..."
sudo apt install make -y

echo "Installing python3.12-venv..."
sudo apt install python3.12-venv -y

echo "Installing tree..."
sudo apt install tree -y

echo "Base VM setup complete."
