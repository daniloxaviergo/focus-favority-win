### Objetivo

Encontrar uma janela específica com o mínimo de esforço possível. Para isso, seleciono a janela e adiciono um atalho para acessá-la.

<img src="https://github.com/daniloxaviergo/focus-favority-win/blob/master/screen/app.png" height="150">

```
s1 -> super+1
s2 -> super+2
...
ss1 -> super+shift+1
ss2 -> super+shift+2
...
```

### Dependências:

```
x11-utils
wmctrl
xbindkeys
```

### Configuração

Adicionar os atalhos para salvar uma janela e acessá-la.

_/home/danilo/.xbindkeysrc_
```ruby
# super+enter numérico
"/home/danilo/scripts/save_window_id.py"
  Mod2+Mod4 + KP_Enter

# super+1(teclado numérico)
"/home/danilo/scripts/goto_saved_window.py s1"
  Mod2+Mod4 + KP_End

# super+2(teclado numérico)
"/home/danilo/scripts/goto_saved_window.py s2"
  Mod2+Mod4 + KP_Down

# super+3(teclado numérico)
"/home/danilo/scripts/goto_saved_window.py s3"
  Mod2+Mod4 + KP_Next

# ...
"/home/danilo/scripts/goto_saved_window.py s4"
  Mod2+Mod4 + KP_Left

"/home/danilo/scripts/goto_saved_window.py s5"
  Mod2+Mod4 + KP_Begin

"/home/danilo/scripts/goto_saved_window.py s6"
  Mod2+Mod4 + KP_Right

"/home/danilo/scripts/goto_saved_window.py s7"
  Mod2+Mod4 + KP_Home

"/home/danilo/scripts/goto_saved_window.py s8"
  Mod2+Mod4 + KP_Up

"/home/danilo/scripts/goto_saved_window.py s9"
  Mod2+Mod4 + KP_Prior

#
# super+shift+1(teclado numérico)
#
"/home/danilo/scripts/goto_saved_window.py ss1"
  Shift+Mod2+Mod4 + KP_End

# super+shift+2(teclado numérico)
"/home/danilo/scripts/goto_saved_window.py ss2"
  Shift+Mod2+Mod4 + KP_Down

# super+shift+3(teclado numérico)
"/home/danilo/scripts/goto_saved_window.py ss3"
  Shift+Mod2+Mod4 + KP_Next

# ...
"/home/danilo/scripts/goto_saved_window.py ss4"
  Shift+Mod2+Mod4 + KP_Left

"/home/danilo/scripts/goto_saved_window.py ss5"
  Shift+Mod2+Mod4 + KP_Begin

"/home/danilo/scripts/goto_saved_window.py ss6"
  Shift+Mod2+Mod4 + KP_Right

"/home/danilo/scripts/goto_saved_window.py ss7"
  Shift+Mod2+Mod4 + KP_Home

"/home/danilo/scripts/goto_saved_window.py ss8"
  Shift+Mod2+Mod4 + KP_Up

"/home/danilo/scripts/goto_saved_window.py ss9"
  Shift+Mod2+Mod4 + KP_Prior
```

No código altere `/home/danilo/scripts` para o caminho correto, inicialize o xbindkeys.
Para saber qual é o código de uma determinada combinação de teclas `xbindkeys -k`
