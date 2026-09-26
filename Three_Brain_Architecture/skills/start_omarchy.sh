#!/bin/bash
exec qemu-system-x86_64 -enable-kvm -machine q35 -cpu host -smp 4 -m 8192 \
-drive if=pflash,format=raw,readonly=on,file=/usr/share/OVMF/OVMF_CODE_4M.fd \
-drive if=pflash,format=raw,file="$HOME/Destiny-Omarchy/OVMF_VARS_4M.fd" \
-drive file="$HOME/Destiny-Omarchy/omarchy.qcow2",format=qcow2,if=virtio \
-vga std -display gtk \
-nic user,model=virtio-net-pci,hostfwd=tcp:127.0.0.1:2222-:22
