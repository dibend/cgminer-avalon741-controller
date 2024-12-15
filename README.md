
# cgminer Avalon741 Controller

This repository provides a modified version of `cgminer` that enables any 64-bit Linux PC to function as a USB controller for the AvalonMiner 741. It simplifies the setup process and removes the need for a dedicated Avalon controller.

---

## Features

- Turns any 64-bit Linux PC into a USB controller for the AvalonMiner 741.
- Supports multiple pools with failover configurations.
- Command-line interface for easy monitoring and control.
- Precompiled binary for quick setup.

---

## Prerequisites

### Hardware
- **AvalonMiner 741** unit.
- **AvalonMiner USB Converter 3 (AUC3)**.
- **AUC3 I2C 5PIN Cable**.
- **Micro-USB Cable**.
- **Server-grade Power Supply Unit (PSU)** with at least six PCI-E 6-pin connectors.
- A 64-bit Linux PC with a free USB port.

### Software
- A 64-bit Linux distribution (e.g., Ubuntu, Debian, CentOS).
- The precompiled `cgminer` binary from this repository.

---

## Installation

### 1. Download the Precompiled Binary
1. Navigate to the [Releases](https://github.com/dibend/cgminer-avalon741-controller/releases) section of this repository.
2. Download the latest `cgminer` binary for 64-bit Linux.

### 2. Set Up Permissions
1. Move the binary to a location in your system's `PATH` (e.g., `/usr/local/bin`):
   ```bash
   sudo mv cgminer /usr/local/bin/
   ```
2. Ensure the binary is executable:
   ```bash
   sudo chmod +x /usr/local/bin/cgminer
   ```

---

## Usage

### 1. Connect the Hardware
1. Plug the **AvalonMiner USB Converter 3 (AUC3)** into your Linux PC using the Micro-USB cable.
2. Connect the AUC3 to the AvalonMiner 741 using the AUC3 I2C 5PIN cable.
3. Power on the AvalonMiner 741 by connecting the PSU.

### 2. Start cgminer
Run the `cgminer` binary with the appropriate options to start mining:
```bash
cgminer --avalon7-freq <frequency> --avalon7-voltage <voltage> -o <pool_url> -u <username> -p <password>
```

### Example Command
```bash
cgminer --avalon7-freq 500 --avalon7-voltage 800 -o stratum+tcp://pool.example.com:3333 -u worker_name -p worker_password
```

---

## Advanced Configuration

To customize your mining setup:
1. Create a configuration file named `cgminer.conf` in the same directory as the binary.
2. Add your desired settings. Example:
   ```json
   {
       "pools": [
           {
               "url": "stratum+tcp://pool.example.com:3333",
               "user": "worker_name",
               "pass": "worker_password"
           }
       ],
       "avalon7-freq": "500",
       "avalon7-voltage": "800"
   }
   ```
3. Start `cgminer` without any command-line arguments:
   ```bash
   cgminer
   ```

---

## Donations

If you find this software useful, please consider donating to support further development:

- **Bitcoin (BTC):** `bc1q8jwd2qayh9tlzl9vkdltf8c7dv4wr4j69flhl7`
- **Bitcoin Legacy (BTC Legacy):** `16XVRPsGkvfi5tYowoJXkeqvbuZWmv7gW2`
- **Litecoin (LTC):** `ltc1qtxvy57u89tphvnaj6drruj8cqj4xssykv3z6f4`

Your contributions are greatly appreciated and help keep this project alive!

---

## Acknowledgements

This project is based on the original [cgminer](https://github.com/Canaan-Creative/cgminer) by [Canaan](https://canaan.io). All credit for the original software goes to its respective authors and maintainers.

---

By following this guide, you can turn any 64-bit Linux PC into an Avalon 741 USB controller, enabling efficient cryptocurrency mining.
