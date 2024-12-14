
# CGMiner for AvalonMiner 741

This repository contains the compiled CGMiner binary for use with the AvalonMiner 741. Follow the instructions below to configure and run the miner effectively.

## Prerequisites

1. **Hardware**: AvalonMiner 741 or compatible device.
2. **Software**: 
   - A Linux distribution (e.g., Ubuntu Server).
   - SSH access to the machine where the miner is running.
3. **Dependencies**: Ensure the required libraries and tools are installed.

## Installing Dependencies on Ubuntu (Latest)

Run the following commands to install all the required dependencies:

```bash
sudo apt update
sudo apt install -y build-essential autoconf libtool libcurl4-openssl-dev libudev-dev libusb-1.0-0-dev pkg-config
```

These packages include:
- `build-essential`: Compilers and tools for building software.
- `autoconf` and `libtool`: Tools required for configuration and build processes.
- `libcurl4-openssl-dev`: Provides support for HTTPS pool communication.
- `libudev-dev`: For interacting with USB devices.
- `libusb-1.0-0-dev`: Required for USB communication with mining hardware.
- `pkg-config`: Helper tool for configuring library paths.

---

## Usage Instructions

### 1. Download and Setup

1. Clone the repository and navigate into the directory:
   ```bash
   git clone https://github.com/your-repo-url/cgminer
   cd cgminer
   ```

2. Make the binary executable:
   ```bash
   chmod +x cgminer
   ```

### 2. Configure the Miner

Create or modify the `cgminer.conf` file for your mining pool and hardware. Here's an example configuration:

```json
{
    "pools": [
        {
            "url": "stratum+tcp://your-mining-pool-url:port",
            "user": "your-wallet-address.worker-name",
            "pass": "your-password"
        }
    ],
    "api-listen": true,
    "api-network": true,
    "avalon7-voltage-level": 1,
    "avalon7-freq": 350,
    "avalon7-fan": "10-40"
}
```

- Replace `your-mining-pool-url`, `your-wallet-address`, and other placeholders with your specific details.

### 3. Run the Miner

Start the miner using the following command:

```bash
./cgminer --config cgminer.conf
```

### 4. Monitor the Miner

Use the CGMiner console to monitor the hashrate, pool connection, and temperature. You can also access the API if configured.

### 5. Adjust Settings

- **Voltage**: Use `--avalon7-voltage-level` to adjust power usage.
- **Frequency**: Use `--avalon7-freq` to balance hashing speed and power consumption.
- **Fan Speed**: Use `--avalon7-fan` to control cooling and noise.

Example command:
```bash
./cgminer --api-listen --api-network --avalon7-voltage-level 1 --avalon7-freq 350 --avalon7-fan 10-40
```

---

## Troubleshooting

- **USB Permission Issues**: Ensure the correct permissions for USB devices:
  ```bash
  sudo chmod 666 /dev/bus/usb/*/*
  ```
- **No Devices Found**: Check connections and power supply for the miner.
- **Pool Connectivity Issues**: Verify the pool URL and credentials in your `cgminer.conf`.

---

## Donations

If you find this project helpful, consider donating:

- **Bitcoin (BTC)**: `your-btc-address-placeholder`
- **Bitcoin Legacy (BTC Legacy)**: `your-btc-legacy-address-placeholder`

Thank you for your support!
