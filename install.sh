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

yay -S gtk3 gtk2 kitty neofetch qtile qtile-extras lightdm lightdm-gtk-greeter rofi python eza oh-my-zsh-git zsh-theme-powerlevel10k-git pokemon-colorscripts-git --needed --noconfirm
systemctl enable lightdm.service 
cd $ZSH_CUSTOM/plugins && git clone https://github.com/chrissicool/zsh-256color
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
cd $clonePath
mv .zshrc .bashrc ~/
mv gtk-2.0 gtk-3.0 kitty neofetch qtile rofi ~/.config/
systemctl start lightdm.service
echo "greeter-session=lightdm-gtk3-greeter" > /etc/lightdm/lightdm.conf

echo "Reboot the pc after instalation using reboot command"
