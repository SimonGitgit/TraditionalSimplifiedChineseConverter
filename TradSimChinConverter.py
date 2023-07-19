from tkinter import Label, Button, Entry, Tk, END
import webbrowser
import opencc

# t2s - 繁体转简体
# s2t - 简体转繁体
# mix2t - 混合体转繁体
# mix2s - 混合体转简体

# $ echo '繁体' | opencc -c t2s
# $ opencc -i zhwiki_raw.txt -o zhwiki_converted.txt -c t2s.json

# converter = opencc.OpenCC('s2t.json')
# print(converter.convert('汉字'))

# converter2 = opencc.OpenCC('t2s.json')
# print(converter2.convert("難寫"))
main_win = Tk()
main_win.title("繁簡轉換器 版權所有© 2022 Simon Tam. All rights reserved.")
width = 500
height = 51
main_win.geometry(f'{width}x{height}')
instantiateRight = int(main_win.winfo_screenwidth()-width)
instantiateBottom = int(main_win.winfo_screenheight()-height-120)
main_win.geometry("+{}+{}".format(instantiateRight,instantiateBottom))

def toSimplified():
    strtemp = e1.get()
    converter2 = opencc.OpenCC('t2s.json')
    newstr = converter2.convert(strtemp)
    #pc.copy(str(newstr))
    main_win.clipboard_clear()
    main_win.clipboard_append(newstr)
    e2.delete(0,END)
    e2.insert(0, newstr)

    
    # Version 1
    # if len(strtemp)==1:
    #     #print(strtemp.encode('big5'))
    #     bytetemp = strtemp.encode('big5')
    #     #print(bytetemp)
    #     combined =  hex(bytetemp[0]<<8 | bytetemp[1])[2:len(hex(bytetemp[0]<<8 | bytetemp[1]))]
    #     combinedstr = ""
    #     for ele in combined:
    #         combinedstr += ele.capitalize()
    #     #webbrowser.open("http://input.foruto.com/cjdict/" + str(int(combined)) + ".php")
    #     webbrowser.open("http://input.foruto.com/cjdict/Images/CJZD_JPG/"+combinedstr+".JPG")

    # Version 2
    if len(strtemp)==1:
        bytetemp = strtemp.encode('big5')
        # print(bytetemp)
        combined = hex(bytetemp[0]<<8 | bytetemp[1])[2:len(hex(bytetemp[0]<<8 | bytetemp[1]))]
        webbrowser.open("https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%"+combined[0].capitalize()+combined[1].capitalize()+"%"+combined[2].capitalize()+combined[3].capitalize())
        # print("https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/search.php?q=%"+combined[0].capitalize()+combined[1].capitalize()+"%"+combined[2].capitalize()+combined[3].capitalize())   #  %D7%F0")

def toTraditional():
    strtemp = e2.get()
    converter1 = opencc.OpenCC('s2t.json')
    newstr = converter1.convert(strtemp)
    #pc.copy(str(newstr))
    main_win.clipboard_clear()
    main_win.clipboard_append(newstr)
    e1.delete(0,END)
    e1.insert(0, newstr)
    
l1 = Label(main_win, text="繁", fg='black')
l1.place(x=0,y=3)
l2 = Label(main_win, text="簡", fg='black')
l2.place(x=0,y=28)

e1 = Entry(main_win,width=70)
e1.place(x=20,y=3)
e2 = Entry(main_win,width=70)
e2.place(x=20,y=28)

b1 = Button(main_win, text="繁轉簡", fg = 'black', command=toSimplified)
b1.place(x=450,y=0)
b2 = Button(main_win, text="簡轉繁", fg = 'black', command=toTraditional)
b2.place(x=450,y=25)

main_win.mainloop()

