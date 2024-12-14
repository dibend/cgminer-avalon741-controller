# CGMiner for AvalonMiner 741

This repository provides a **precompiled CGMiner binary** specifically configured for the AvalonMiner 741. Follow the instructions below to download, set up, and run the miner.

---

## Prerequisites

1. **Hardware**:
   - AvalonMiner 741 or compatible device.
   - USB connection to the miner's controller or directly to a PC.
2. **Software**:
   - Ubuntu or another Linux distribution.
   - Access to a terminal or SSH.
3. **Dependencies**:
   - Ensure the following libraries are installed on your system:
     ```bash
     sudo apt update
     sudo apt install -y libcurl4 libusb-1.0-0
     ```

---

## Download the Precompiled Binary

1. Visit the [Releases Page](https://github.com/dibend/cgminer-avalon741-controller/releases/tag/cgminer).
2. Download the precompiled binary file:
   - **File Name**: `cgminer`
3. Make the binary executable:
   ```bash
   chmod +x cgminer