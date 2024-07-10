import win32clipboard
import keyboard
import opencc
import time
import webbrowser


def on_key_press(event):    
    if event.name == 'alt' and keyboard.is_pressed('ctrl'):
        try:
            original_text = ""
            modified_text = ""
            
            # copy text
            time.sleep(0.2)
            keyboard.press_and_release('ctrl+c')
            time.sleep(0.02)

            # get clipboard data
            win32clipboard.OpenClipboard()
            original_text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
            print(f"original_text:{original_text}")

            # modify text
            modified_text = opencc.OpenCC('t2s.json').convert(original_text)
            print(f"modified_text:{modified_text}")

            # set clipboard data
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(modified_text, win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()

            if len(original_text)==1:
                bytetemp = original_text.encode('big5')
                # print(bytetemp)
                combined = hex(bytetemp[0]<<8 | bytetemp[1])[2:len(hex(bytetemp[0]<<8 | bytetemp[1]))]
                webbrowser.open("https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%"+combined[0].capitalize()+combined[1].capitalize()+"%"+combined[2].capitalize()+combined[3].capitalize())

            # paste text
            time.sleep(0.02)
            keyboard.press_and_release('ctrl+v')

        except TypeError:
            win32clipboard.CloseClipboard()
            raise TypeError("Specified clipboard format is not available")
        except:
            print("Something else went wrong")
        finally:
            print('\nTranslate: alt + ctrl')
            print('Terminate: alt + x') 


if __name__ == "__main__":
    print('Translate: alt + ctrl')
    print('Terminate: alt + x')
    keyboard.on_press(on_key_press)
    keyboard.wait('alt+x') # 按下 Alt及x 键停止程序
    print('Terminated')