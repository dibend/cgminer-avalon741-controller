
# CGMiner for AvalonMiner 741

This repository provides a **precompiled CGMiner binary** specifically configured for the AvalonMiner 741. Follow the instructions below to set up and start mining.

---

## Prerequisites

1. **Hardware**:
   - AvalonMiner 741 or compatible device.
   - USB connection to the miner's controller or directly to a PC.
2. **Software**:
   - Ubuntu or another Linux distribution.
   - Access to a terminal or SSH.
3. **Dependencies**:
   - Install the following libraries:
     ```bash
     sudo apt update
     sudo apt install -y libcurl4 libusb-1.0-0
     ```

---

## Download the Precompiled Binary

1. Visit the [Releases Page](https://github.com/dibend/cgminer-avalon741-controller/releases/tag/cgminer).
2. Download the precompiled binary:
   - **File Name**: `cgminer`
3. Make the binary executable:
   ```bash
   chmod +x cgminer
   ```

---

## Configuration

### Option 1: Using `cgminer.conf`

Create a `cgminer.conf` file to specify your mining pool and hardware settings. Here's an example:

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

Place this file in the same directory as the binary.

### Option 2: Command-Line Options

Instead of using a configuration file, you can directly pass your settings as command-line arguments:

```bash
./cgminer --api-listen --api-network   --avalon7-voltage-level 1 --avalon7-freq 350 --avalon7-fan 10-40   -o stratum+tcp://your-mining-pool-url:port   -u your-wallet-address.worker-name   -p your-password
```

Replace the placeholders with:
- `your-mining-pool-url`: Your pool's URL (e.g., `stratum+tcp://sha256.unmineable.com:3333`).
- `your-wallet-address`: Your wallet address for receiving rewards.
- `worker-name`: Your worker's identifier (e.g., `741`).
- `your-password`: The password for your pool (optional; leave empty if not required).

---

## Starting Mining

### With `cgminer.conf` File
Run the miner using the configuration file:

```bash
./cgminer --config cgminer.conf
```

### With Command-Line Arguments
Run the miner with specific arguments:

```bash
./cgminer --api-listen --api-network   --avalon7-voltage-level 1 --avalon7-freq 350 --avalon7-fan 10-40   -o stratum+tcp://your-mining-pool-url:port   -u your-wallet-address.worker-name   -p your-password
```

---

## Mining Usage Instructions

### Key Options
- **Mining Pool URL**: The pool's address where the miner connects.
- **Wallet Address**: The BTC address where rewards are credited.
- **Worker Name**: A unique identifier for your miner (e.g., `741`).
- **Voltage Level**: Use `--avalon7-voltage-level` to adjust power consumption (1 for lowest power, 8 for moderate performance).
- **Frequency**: Set with `--avalon7-freq`. For quiet operation, start with 350 MHz.
- **Fan Speed**: Use `--avalon7-fan` to control cooling and noise (e.g., `10-40` for quieter operation).

### Example Usage
1. **Silent Operation**:
   ```bash
   ./cgminer --api-listen --api-network      --avalon7-voltage-level 1 --avalon7-freq 350 --avalon7-fan 10-40      -o stratum+tcp://sha256.unmineable.com:3333      -u LTC:MX4sa3cmLVgEUFKYQaeexaqYCSFCJW8n9v.741 -p ""
   ```

2. **Max Hashrate**:
   ```bash
   ./cgminer --api-listen --api-network      --avalon7-voltage-level 8 --avalon7-freq 650 --avalon7-fan 60-100      -o stratum+tcp://your-mining-pool-url:port      -u your-wallet-address.worker-name      -p ""
   ```

---

## Monitoring the Miner

- **Real-Time Stats**:
  - Hashrate
  - Device temperature
  - Pool connection status
- **API Access**:
  - Enable with `--api-listen`.
  - Access via port `4028` (default).

---

## Troubleshooting

1. **USB Permissions**:
   If you encounter USB access issues:
   ```bash
   sudo chmod 666 /dev/bus/usb/*/*
   ```

2. **No Devices Found**:
   - Check USB connections and power supply.
   - Ensure the miner is properly detected.

3. **Pool Connectivity Issues**:
   - Verify the pool URL and credentials.
   - Ensure the network connection is stable.

---

## Donations

If you find this project helpful, consider donating:

- **Bitcoin (BTC)**: `your-btc-address-placeholder`
- **Bitcoin Legacy (BTC Legacy)**: `your-btc-legacy-address-placeholder`

Thank you for your support!
