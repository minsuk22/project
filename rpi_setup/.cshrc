


set prompt="[`whoami`] `pwd` > "
set history = 50
set filec
set autolist
set autoexpand
set path = ($path .)

alias ls 'ls --color'
alias ll 'ls -al'
alias cd 'cd \!*;set prompt="[`whoami`] `pwd` > "; ls'
alias h  'history'
alias gv 'vi'
