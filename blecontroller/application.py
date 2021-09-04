import tkinter as tk
from .view import FirstView

class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs);
        self.title("BLE Scanner");
        self.geometry("800x600")
        FirstView(self);

