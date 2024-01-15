#!/bin/bash

clonePath = ${pwd}
if [ -d ~/Clone ]
then
    echo "~/Clone directory exists..."
    rm -rf ~/Clone/
fi

mkdir -p ~/Clone/yay-bin
git clone https://aur.archlinux.org/yay-bin.git ~/Clone/yay-bin
cd ~/Clone/yay-bin/
makepkg -si

yay -Syy

yay -S gtk3 gtk2 kitty neofetch qtile qtile-extras lightdm lightdm-gtk-greeter rofi python eza oh-my-zsh-git zsh-theme-powerlevel10k-git pokemon-colorscripts-git alsa-utils alsa-lib alsa-capabilities --needed --noconfirm
systemctl enable lightdm.service 

mkdir $ZSH_CUSTOM/plugins
cd $ZSH_CUSTOM/plugins && git clone https://github.com/chrissicool/zsh-256color
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

cd $clonePath
mv .zshrc .bashrc .icons ~/
mv gtk-2.0 gtk-3.0 kitty neofetch qtile rofi ~/.config/
mv fonts/ ~/.local/share/

yay -S neovim
git clone https://github.com/NvChad/NvChad.git --depth 1 ~/.config/nvim/

yay -S qemu-desktop virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat --needed --noconfirm
yay -S ebtables iptables --needed --noconfirm

systemctl enable libvirtd.service
systemctl start libvirtd.service
usermod -a -G libvirt $(whoami)
systemctl restart libvirtd.service

echo "greeter-session=lightdm-gtk3-greeter" > /etc/lightdm/lightdm.conf
systemctl start lightdm.service
