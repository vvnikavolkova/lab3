import tkinter as tk
import threading
from chat import send_msg, read_msgs, reader, conn


MSG_HEIGHT = 2


def init_frames(root):
    frame_main = tk.Frame(root)
    frame_main.pack(fill=tk.BOTH, expand=True)

    frame_msgs = tk.Frame(frame_main)
    frame_msgs.pack(side=tk.RIGHT)

    frame_input = tk.Frame(frame_main)
    frame_input.pack(fill=tk.X, side=tk.BOTTOM)

    frame_nickname = tk.Frame(frame_main)
    frame_nickname.pack(fill=tk.X, side=tk.BOTTOM)

    lbl = tk.Label(frame_main, 
                   height=MSG_HEIGHT,
                   text='Chat started...')
    lbl.pack(side=tk.TOP)

    init_input(frame_nickname, frame_input, frame_msgs)
    return frame_main, frame_input, frame_msgs, frame_nickname


def init_input(frame_nickname, frame_input, frame_msgs):
    name_entry = tk.Entry(frame_nickname)
    name_entry.insert(0, 'Anonymous')

    lbl_nick = tk.Label(frame_nickname, text='Никнейм')

    txt_entry = tk.Entry(frame_input)

    def click(txt_entry):
        text = txt_entry.get()
        #add_msg_label(frame_msgs, text)
        msg = {'text': text, 
               'nickname': name_entry.get()
               }
        send_msg(msg, conn)
        txt_entry.delete(0, tk.END)
        
    btn = tk.Button(frame_input,
              text='Отправить',
              command=lambda: click(txt_entry))
    
    txt_entry.pack(fill=tk.X, side=tk.LEFT, expand=True)
    btn.pack(side=tk.LEFT)

    lbl_nick.pack(side=tk.LEFT)
    name_entry.pack(side=tk.LEFT)


def add_msg_label(frame_msgs, text):
    msg_lbl = tk.Label(frame_msgs,
             height=MSG_HEIGHT,
             background='#92c2f2',
             text=text)
    msg_lbl.pack(side=tk.TOP,
                 anchor=tk.NE,
                 padx=MSG_HEIGHT,
                 pady=MSG_HEIGHT)


def init_gui():
    root = tk.Tk()
    root.geometry('500x500')
    root.title('Max')
    frames = init_frames(root)
    return root, frames


if __name__ == '__main__':
    root, frames = init_gui()

    msgs_frame = frames[2]
    th = threading.Thread(target=read_msgs, 
                     args=(add_msg_label, reader,  msgs_frame),
                     daemon=True)
    th.start()
    root.mainloop()




