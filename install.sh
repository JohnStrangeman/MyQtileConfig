#!/bin/bash

if [ -d ~/Clone ]
then
    echo "~/Clone directory exists..."
    rm -rf ~/Clone/
fi
mv gtk-2.0 gtk-3.0 kitty neofetch qtile rofi ~/.config/
mv .zshrc .bashrc ~/

mkdir -p ~/Clone/yay-bin
git clone https://aur.archlinux.org/yay-bin.git ~/Clone/yay-bin
cd ~/Clone/yay-bin/
makepkg -si

yay -Syy

yay -S gtk3 gtk2 kitty neofetch qtile qtile-extras rofi python --needed --noconfirm
