import logging
import tkinter as tk
from tkinter import ttk
from typing import Callable, Any, Optional
import os.path
import sys


_warn_pi: tk.PhotoImage = None


def _get_resource_path(resource_path: str) -> str:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # in a pyinstaller bundle
        assets_path = os.path.join(sys._MEIPASS, 'assets')
    else:
        assets_path = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(assets_path, resource_path))
    return full_path


def _get_warn_image() -> tk.PhotoImage:
    global _warn_pi
    if _warn_pi is None:
        _warn_pi = tk.PhotoImage(file=_get_resource_path('warning.png'))
    return _warn_pi


class ModalBox(tk.Toplevel):
    def __init__(self, master, text: str, title: Optional[str], default_focus: Optional[int], *choices):
        if len(choices) < 1:
            choices = ['OK']
    
        super().__init__(master)
        if title is not None:
            self.title(title)
        
        self._master_widget = master
        self._default_focus_btn: Optional[tk.Button] = None
        
        internal_frame = tk.Frame(self)
        internal_frame.pack(padx=15, pady=15, fill=tk.X)
        
        message_frame = tk.Frame(master=internal_frame)
        message_frame.pack(side=tk.TOP, fill=tk.X)
        
        image_label = tk.Label(message_frame, image=_get_warn_image())
        image_label.pack(side=tk.LEFT, anchor="n")
        
        spacer_frame = tk.Frame(master=message_frame)
        spacer_frame.pack(side=tk.LEFT, padx=5)
        
        text_label = tk.Label(message_frame, text=text, anchor="e", justify=tk.LEFT)
        text_label.pack(side=tk.LEFT)
        
        spacer_frame = tk.Frame(master=internal_frame)
        spacer_frame.pack(side=tk.TOP, pady=2)
        
        button_frame = tk.Frame(master=internal_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X)
    
        def last_choice_func():
            self._on_command(len(choices)-1, choices[-1])
        btn = tk.Button(master=button_frame, text=choices[-1], command=last_choice_func)
        btn.pack(side=tk.RIGHT)
        btn.config(width=10)
        if default_focus == len(choices)-1:
            self._default_focus_btn = btn
        idx = len(choices)-1
        for ch in reversed(choices[:-1]):
            idx -= 1
            def choice_func():
                self._on_command(idx, ch)
                
            btn = tk.Button(master=button_frame, text=ch, command=choice_func)
            btn.pack(side=tk.RIGHT)
            btn.config(width=10)
            
            if default_focus == idx:
                self._default_focus_btn = btn

        self.update()
        self.resizable(0, 0)
        self.attributes("-toolwindow", 1)
        self.minsize(max(self.winfo_width(), 300), self.winfo_height())
        self.maxsize(self.winfo_width(), self.winfo_height())
        
        
    def make_modal(self):
        self.focus_set()
        self.grab_set()
        
        if self._default_focus_btn is not None:
            self._default_focus_btn.focus_set()
        
        self.transient(self._master_widget)
        self.wait_window(self)
        
    def _on_command(self, index: int, choice: str):        
        cmd_func = self._on_button_click
        self.destroy()
        cmd_func(index, choice)
        
    def _on_button_click(self, index: int, choice: str):
        pass
        
    
class ConfirmBox(ModalBox):
    def __init__(
        self,
        master,
        text: str,
        bind: Optional[Callable[[bool], Any]] = None,
        title: Optional[str] = None,
        yes: str = 'Yes',
        no: str = 'No',
        default_no: bool = False
    ):
        focus = 0
        if default_no:
            focus = 1
        super().__init__(master, text, title, focus, yes, no)
        
        if bind is None:
            self._select_func = lambda x: 0
        else:
            self._select_func = bind
        
    def _no(self):
        self._select_func(False)
        
    def _yes(self):
        self._select_func(True)
        
    def _on_button_click(self, index: int, choice: str):
        if index == 0:
            self._yes()
        else:
            self._no()
    
    
def message(
    title: str,
    text: str,
    button_text: str = "OK"
):
    msg_box = ModalBox(master=None, text=text, title=title, default_focus=0)
    msg_box.make_modal()

        
def confirm(
    title: str,
    text: str,
    yes: str = 'Yes',
    no: str = 'No',
    default_no: bool = False
) -> bool:
    result = False
    
    def on_select(value):
        nonlocal result
        result = value
        
    conf_box = ConfirmBox(
        master=None, text=text, title=title, yes=yes, no=no, default_no=default_no, bind=on_select
    )
    
    conf_box.make_modal()
    return result