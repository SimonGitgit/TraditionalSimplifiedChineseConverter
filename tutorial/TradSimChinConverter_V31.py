import keyboard
import pyperclip
import webbrowser
import opencc

# Version 3.1
def modify_clipboard():
    # 修改剪贴板的文本为大写

    original_text = pyperclip.paste()
    # print(original_text)
    # modified_text = text.upper()

    modified_text = opencc.OpenCC('t2s.json').convert(original_text)
    # print(modified_text)
    pyperclip.copy(modified_text)

    # 将修改后的文本粘贴回剪贴板

    if len(original_text)==1:
        bytetemp = original_text.encode('big5')
        # print(bytetemp)
        combined = hex(bytetemp[0]<<8 | bytetemp[1])[2:len(hex(bytetemp[0]<<8 | bytetemp[1]))]
        webbrowser.open("https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%"+combined[0].capitalize()+combined[1].capitalize()+"%"+combined[2].capitalize()+combined[3].capitalize())

    keyboard.press_and_release('ctrl+v')

def on_key_press(event):
    if event.name == 'd' and keyboard.is_pressed('ctrl'):
        modify_clipboard()

keyboard.on_press(on_key_press)

keyboard.wait('esc')  # 按下ESC键停止程序