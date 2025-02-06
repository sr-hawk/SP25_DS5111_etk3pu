#!/bin/bash
# install_chrome.sh
# This script installs Google Chrome Stable by adding the official Google repository,
# and then verifies that headless mode is working by dumping the DOM of https://example.com.
# It uses apt-get to perform the installation, which can be more resource-efficient than
# manually downloading and installing the .deb package.

set -e

# Function to add Google Chrome repository if not already added
add_chrome_repo() {
  echo "Adding Google Chrome repository..."
  # Import the Google public key
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  
  # Add the repository to apt sources if it doesn't exist
  if [ ! -f /etc/apt/sources.list.d/google-chrome.list ]; then
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
  fi
}

# Check if Google Chrome is installed
if ! command -v google-chrome >/dev/null 2>&1; then
  echo "Google Chrome is not installed. Installing now..."
  add_chrome_repo
  sudo apt-get update
  sudo apt-get install -y google-chrome-stable
else
  echo "Google Chrome is already installed."
fi

# Verify that Google Chrome is now installed
if ! command -v google-chrome >/dev/null 2>&1; then
  echo "Google Chrome installation failed."
  exit 1
fi

echo "Google Chrome installed successfully."

# Run a headless test to verify Chrome's headless mode.
# This dumps the DOM of https://example.com to a temporary file and then checks for the expected <title> tag.
echo "Running headless test on https://example.com..."
OUTPUT_FILE="/tmp/example_dom.html"
google-chrome --headless --disable-gpu --dump-dom https://example.com > "$OUTPUT_FILE"

# Check for the expected page title in the dumped HTML
if grep -q "<title>Example Domain</title>" "$OUTPUT_FILE"; then
  echo "Headless test successful: Expected page title found."
  rm "$OUTPUT_FILE"
else
  echo "Headless test failed: Expected page title not found."
  exit 1
fi

echo "Chrome headless test completed successfully."
