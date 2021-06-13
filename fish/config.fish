set fish_greeting

set -l abcd (random 0 6)

if [ $abcd = 0 ]
   # tty-clock -s -D -C 0
   neofetch
end
if [ $abcd = 1 ]
   figlet Arch Linux | lolcat -a -d 2
end
if [ $abcd = 2 ]
   neofetch
end
if [ $abcd = 3 ]
   pfetch
end
if [ $abcd = 4 ]
   archey3
end
if [ $abcd = 5 ]
   pfetch
end
if [ $abcd = 6 ]
   ufetch
end


function fish_prompt
      set_color green
      echo (pwd) '»' (set_color normal)
end

alias v="nvim"
alias y="paru -S"
alias p="sudo pacman -S"
alias lisp="rlwrap sbcl"
alias hie="/home/nld/.local/bin/hie"
# ghcup-env
set -q GHCUP_INSTALL_BASE_PREFIX[1]; or set GHCUP_INSTALL_BASE_PREFIX $HOME
test -f /home/nld/.ghcup/env ; and set -gx PATH $HOME/.cabal/bin /home/nld/.ghcup/bin $PATH
