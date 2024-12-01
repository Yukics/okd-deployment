# Installation & setup

1. Install lm-sensors package

```bash
apt install lm-sensors
```

2. Setup sensors

```bash
sensors-detect
# yes to all & Enter
```

3. List sensors

```bash
sensors
```

Output:

```bash
tg3-pci-0303
Adapter: PCI adapter
temp1:        +68.0°C  (high = +100.0°C, crit = +110.0°C)

tg3-pci-0300
Adapter: PCI adapter
temp1:        +68.0°C  (high = +100.0°C, crit = +110.0°C)

coretemp-isa-0000
Adapter: ISA adapter
Package id 0:  +57.0°C  (high = +81.0°C, crit = +91.0°C)
Core 0:        +57.0°C  (high = +81.0°C, crit = +91.0°C)
Core 1:        +56.0°C  (high = +81.0°C, crit = +91.0°C)
Core 2:        +53.0°C  (high = +81.0°C, crit = +91.0°C)
Core 3:        +55.0°C  (high = +81.0°C, crit = +91.0°C)
Core 4:        +55.0°C  (high = +81.0°C, crit = +91.0°C)
Core 5:        +55.0°C  (high = +81.0°C, crit = +91.0°C)

be2net-pci-0701
Adapter: PCI adapter
temp1:        +59.0°C  

acpitz-acpi-0
Adapter: ACPI interface
temp1:         +8.3°C  

tg3-pci-0302
Adapter: PCI adapter
temp1:        +68.0°C  (high = +100.0°C, crit = +110.0°C)

coretemp-isa-0001
Adapter: ISA adapter
Package id 1:  +67.0°C  (high = +81.0°C, crit = +91.0°C)
Core 0:        +67.0°C  (high = +81.0°C, crit = +91.0°C)
Core 1:        +64.0°C  (high = +81.0°C, crit = +91.0°C)
Core 2:        +64.0°C  (high = +81.0°C, crit = +91.0°C)
Core 3:        +67.0°C  (high = +81.0°C, crit = +91.0°C)
Core 4:        +66.0°C  (high = +81.0°C, crit = +91.0°C)
Core 5:        +66.0°C  (high = +81.0°C, crit = +91.0°C)

power_meter-acpi-0
Adapter: ACPI interface
power1:      242.00 W  (interval = 300.00 s)

be2net-pci-0700
Adapter: PCI adapter
temp1:        +59.0°C  
```
