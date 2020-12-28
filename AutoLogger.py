import re
import tkinter as tk
from tkinter import filedialog, scrolledtext, Scrollbar, font

root = tk.Tk()
root.title('AutoLogging') # set the title for the application
display_text = tk.StringVar() #  dynamic variable, on change it will reflect to all places
default_lable_text = 'Entered file is : '
display_text.set(default_lable_text)
filename = '' # global filename variable

def changeColorOfTrace():
    # get string to look for (if empty, no searching)
    s = entry.get()
    if s:
        # start from the beginning (and when we come to the end, stop)
        idx = '1.0'
        while 1:
            # print('inside while')
            # find next occurrence, exit loop if no more
            idx = stext2.search(s, idx, nocase=1, stopindex='end')
            if not idx: break
            # index right after the end of the occurrence
            lastidx = '%s+%dc' % (idx, len(s))
            # tag the whole occurrence (start included, stop excluded)
            stext2.tag_add('found', idx, lastidx)
            # prepare to search for next occurrence
            idx = lastidx
        # use a red foreground for all the tagged occurrences
        stext2.tag_config('found', foreground='red')

'''
    This function reads the file and add traces in the file.
    Simultanously set the file contained in testboxes
    left scrolledText - without Trace (original file)
    right scrolledText - with Trace
'''
def logEnable(file_ch):
    # change the state of scrolledTest 
    stext1.configure(state ='normal')
    stext2.configure(state ='normal')
    # flush the text form textbox
    stext1.delete(0.0,'end')
    stext2.delete(0.0,'end')
    # set empty string at textbox
    stext1.insert(1.0, '')
    stext2.insert(1.0, '')

    fr = open(file_ch,'r')
    text1 = fr.read()
    fw = open('output.log','w')
	# according to your requirment you can change regex 
    reg = re.compile(r'^\s*(int|void|byte|word|static|inline|float)[\s\/\*\w]*\([\s\/,\*\w]*\)(?!;)[\s\/\*\w]*(\{)$',re.MULTILINE)
    fw.write(reg.sub(lambda m : m.group() +'\n'+entry.get(),text1))
    fr.close()
    fw.close()
    fr1 = open('output.log','r')
    text2 = fr1.read()
    fr1.close()
    stext1.insert(1.0, text1)
    stext2.insert(1.0, text2)
    changeColorOfTrace()
    stext2.configure(state ='disabled')
    stext1.configure(state ='disabled')

'''
Open file Dialog box
And set filename in global variable
'''
def fileUpload():
    global filename
    filelist = (('C','*.c'),('C++','*.cpp'),('Python','*.py'),('All','*.*'))
    filename = filedialog.askopenfilename(initialdir='./',title="select a file",filetypes=filelist)
    print(filename)
    display_text.set(default_lable_text + filename)
    logEnable(filename)


cheight = root.winfo_screenheight() 
cwidth = root.winfo_screenwidth()
cv = tk.Canvas(root, height =cheight, width=cwidth,bg='#084353', bd=20)
cv.pack()

myFont = font.Font(family='Helvetica',size=9)
frame2 = tk.Frame(root, bg='#535b7c')
frame2.place(relx=0.0,rely=0.96,relwidth=1.0,relheight=0.05)
label2 = tk.Label(frame2,text='@kunal kumar',bg='#e6e7ed')
label2.place(relx=0.0,rely=0.0,relwidth=1.0,relheight=0.8)
label2['font']=myFont

frame1 = tk.Frame(root, bg='#535b7c')
frame1.place(relx=0.0,rely=0.0,relwidth=1,relheight=0.15)
label = tk.Label(frame1,text='Auto Logger',bg='#e6e7ed',font=30)
label.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)


frame = tk.Frame(root, bg='#b4a19c')
frame.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.8)

myFont = font.Font(family='Helvetica',size=12)
button = tk.Button(frame,text="Choose file",bg='#106f0c',command=lambda : fileUpload())
# button.pack(side='left',fill='both',expand=True)
button.place(relx=0,rely=0,relwidth=0.25,relheight=0.1)
button['font']=myFont

label1 = tk.Label(frame,textvariable=display_text,bg='#f4f59f')
# label.pack(side='left',fill='both',expand=True)
label1.place(relx=0.3,rely=0,relwidth=0.75,relheight=0.1)
label1['font']=myFont

label = tk.Label(frame,text="Enter Trace : ",bg='#f4f59f')
label.place(relx=0,rely=0.1,relwidth=0.25,relheight=0.06)
entry = tk.Entry(frame, bg='#f8f9f9')
entry.place(relx=0.3,rely=0.1,relwidth=0.75,relheight=0.06)

hint = 'TRACE_TXT(TRCE_NUM, TRCE_NUM_CTSIP, TRCE_DEV, "  %s  line no = %d ",__FUNCTION__,__LINE__);'
var = tk.StringVar()
var.set('Example : '+hint)
label = tk.Entry(frame,readonlybackground='#084353',fg='white',state='readonly',justify='center')
label.config(textvariable=var, relief='flat')
label.place(relx=0,rely=0.16,relwidth=1,relheight=0.03)


# TRACE_TXT(TRCE_NUM, TRCE_NUM_CTSIP, TRCE_DEV, "  %s  line no = %d ",__FUNCTION__,__LINE__);
# entry = tk.Entry(frame, bg='grey')
# # entry.pack(side='left',fill='both',expand=True)
# entry.place(relx=0.8,rely=0,relwidth=0.25,relheight=0.1)

'''
ScrolledText used for storing large text 
'''

stext1 = tk.scrolledtext.ScrolledText(frame, undo=True, wrap='word',borderwidth=3,fg='green',padx=5,pady=5)
stext1['font'] = ('consolas', '10')
stext1['bg'] = '#f8f9f9'
stext1.place(relx=0.01,rely=0.2,relwidth=0.49,relheight=0.77)
stext2 = tk.scrolledtext.ScrolledText(frame, undo=True, wrap='word',borderwidth=3,fg='blue',padx=5,pady=5)
stext2['font'] = ('consolas', '10')
stext2['bg'] = '#f8f9f9'
stext2.place(relx=0.51,rely=0.2,relwidth=0.48,relheight=0.77)

#  used to retain window
root.mainloop()