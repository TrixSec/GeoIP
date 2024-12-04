**Current Version**: 1.0
**Author**: Trix Cyrus  
**Copyright**: © 2024 Trixsec Org  
**Maintained**: Yes

# GeoIP Lookup Tool

A Python script that fetches and displays geolocation information for an IP address. The information includes details such as country, city, latitude, longitude, timezone, and connection data. The results are displayed with bold and colored formatting for easy readability.

## Features

- Fetches geolocation data for a given IP address using the IPWho API.
- Displays information like country, city, region, continent, timezone, and more.
- Connection details such as ASN, ISP, and domain.
- Bold and colored terminal output for better visibility.

## Installation

### Prerequisites

- Python 3.6 or later.
- `requests` library for making HTTP requests.
- `termcolor` library for terminal color output.

### Installing Dependencies

1. Clone the repository:

```bash
git clone https://github.com/TrixSec/GeoIP.git
cd GeoIP
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or manually install the required libraries:

```bash
pip install requests termcolor
```

## Usage

Run the script from the terminal with the `--ip` argument to specify the IP address you want to look up.

```bash
python geoip.py --ip <IP_ADDRESS>
```

### Example

```bash
python geoip.py --ip 1.1.1.1
```

### Test run

![GeoIP](https://github.com/TrixSec/GeoIP/blob/main/testrun/testrun.jpg?raw=true)]


### Explanation of Fields:

- **Ip**: The IP address being looked up.
- **Success**: Whether the query was successful.
- **Type**: The type of IP address (IPv4 or IPv6).
- **Continent**: The continent where the IP is located.
- **Country**: The country of the IP address.
- **City**: The city of the IP address.
- **Latitude / Longitude**: Geolocation coordinates.
- **Connection**: Details about the IP's ASN (Autonomous System Number), organization, ISP (Internet Service Provider), and domain.
- **Timezone**: Timezone information, including UTC offset and current time.

