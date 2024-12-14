
# cgminer Avalon741 Controller - Updated and Compiled

This repository contains an updated and compiled version of the original [cgminer](https://github.com/Canaan-Creative/cgminer) by [Canaan](https://canaan.io), tailored for the Avalon741 Bitcoin ASIC miner.

---

## About This Project

The **cgminer Avalon741 Controller** project is based on the original open-source **cgminer** software created by **Canaan**. This repository includes updates and a compiled version of the software for ease of use with the Avalon741 hardware.

### Key Updates:
- Updated dependencies for compatibility with modern systems.
- Minor adjustments to build scripts for streamlined compilation on [specific OS/platform].
- Precompiled binary included for quick deployment on Avalon741.

For the original source code, visit the [Canaan cgminer repository](https://github.com/Canaan-Creative/cgminer).

---

## Features
- Bitcoin mining with Avalon741 ASIC miner.
- Support for multiple pools and failover configurations.
- Monitoring and control via command line interface.

---

## Installation

### Precompiled Binary:
1. Download the precompiled binary from the [Releases](https://github.com/dibend/cgminer-avalon741-controller/releases) section.
2. Transfer the binary to your Avalon741 controller device.
3. Run the binary:
   ```bash
   ./cgminer
   ```

---

## How to Build from Source

1. Clone this repository:
   ```bash
   git clone https://github.com/dibend/cgminer-avalon741-controller.git
   cd cgminer-avalon741-controller
   ```

2. Install dependencies:
   ```bash
   sudo apt-get install build-essential libcurl4-openssl-dev
   ```

3. Compile the source code:
   ```bash
   make
   ```

4. Run the compiled binary:
   ```bash
   ./cgminer
   ```

---

## Acknowledgements

This project is based on the original [cgminer](https://github.com/Canaan-Creative/cgminer) by [Canaan](https://canaan.io). All rights and credits for the original software go to its respective authors and maintainers.
