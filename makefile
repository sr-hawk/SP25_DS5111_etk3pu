default:
	@cat Makefile

# Create the virtual environment and upgrade pip.
env:
	python3 -m venv env && env/bin/pip install --upgrade pip

# Install the Python dependencies into the virtual environment.
update: env
	env/bin/pip install -r requirements.txt

.PHONY: ygainers.html
.PHONY: wjsgainers.html

sample_data:
	mkdir -p sample_data

# Download the HTML for Yahoo! Finance gainers using headless Chrome.
ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=15000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > timed_data/ygainers.html

# Convert the downloaded HTML to CSV using a Python one-liner.
ygainers.csv: ygainers.html
	env/bin/python3 -c "import pandas as pd; raw = pd.read_html('timed_data/ygainers.html'); raw[0].to_csv('$@', index=False)"

# Download the HTML for WSJ gainers using headless Chrome.
wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > timed_data/wsjgainers.html

# Convert the downloaded WSJ HTML to CSV.
wsjgainers.csv: wsjgainers.html
	env/bin/python3 -c "import pandas as pd; raw = pd.read_html('timed_data/wsjgainers.html'); raw[0].to_csv('$@', index=False)"

#Pylint normalize_csv.py
lint:
	-env/bin/python3 -m pylint bin
	-env/bin/python3 -m pylint tests

#Pytest normalize_csv.py
test:
	env/bin/python3 -m pytest tests

gainers:
	. env/bin/activate; python get_gainer.py $(SRC)
