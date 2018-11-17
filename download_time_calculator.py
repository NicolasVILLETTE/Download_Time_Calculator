import datetime
import speedtest
import tkinter
from tkinter import *
from tkinter import ttk

class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("Download Time Calculator")

        FILE_SIZES = ["Bytes", "KiloBytes", "MegaBytes", "GigaBytes"]
        DL_SPEED = ["Kbps", "Mbps", "Gbps"]

        self.file_size_label = Label(master, text = "File Size:")
        self.file_size_label.grid(row = 0, column = 0) 

        self.file_size_spinbox = Spinbox(master, from_ = 0.0, to = 9999.99, increment = 0.01) 
        self.file_size_spinbox.grid(row = 0, column = 1)
        
        self.file_size_combobox = ttk.Combobox(master, values = FILE_SIZES, state = "readonly")
        self.file_size_combobox.grid(row = 0, column = 2)

        self.download_speed_label = Label(master, text = "Download Speed:")
        self.download_speed_label.grid(row = 1, column = 0) 

        self.download_speed_spinbox = Spinbox(master, from_ = 0.0, to = 9999.99, increment = 0.01) 
        self.download_speed_spinbox.grid(row = 1, column = 1)

        self.download_speed_combobox = ttk.Combobox(master, values = DL_SPEED, state = "readonly")
        self.download_speed_combobox.grid(row = 1, column = 2)

        self.calculate_button = Button(master, text = "Calculate", command=self.calculate)
        self.calculate_button.grid(row = 2, column = 0)

        self.file_size_label = Label(master, text = "Download Time:")
        self.file_size_label.grid(row = 2, column = 1) 

        self.result = Text(master, height=1, width=20)
        self.result.grid(row = 2, column = 2)

        self.speed_calculate = Button(master, text = "Speed Test", command=self.speed_test)
        self.speed_calculate.grid(row = 3, column = 0)

        self.download_speed_label = Label(master, text = "Download Speed:")
        self.download_speed_label.grid(row = 3, column = 1)

        self.download_speed_result = Text(master, height=1, width=20)
        self.download_speed_result.grid(row = 3, column = 2)

    def get_file_size(self):

        if self.file_size_combobox.get() == "Bytes":
            file_size = float(self.file_size_spinbox.get()) 
        elif self.file_size_combobox.get() == "KiloBytes":
            file_size = float(self.file_size_spinbox.get()) * 10 ** 3
        elif self.file_size_combobox.get() == "MegaBytes":
            file_size = float(self.file_size_spinbox.get()) * 10 ** 6 
        elif self.file_size_combobox.get() == "GigaBytes":
            file_size = float(self.file_size_spinbox.get()) * 10 ** 9

        return file_size

    def get_download_speed(self):

        if self.download_speed_combobox.get() == "Kbps":
            download_speed = float(self.download_speed_spinbox.get()) * 10 ** 3
        elif self.download_speed_combobox.get() == "Mbps":
            download_speed = float(self.download_speed_spinbox.get()) * 10 ** 6 
        elif self.download_speed_combobox.get() == "Gbps":
            download_speed = float(self.download_speed_spinbox.get()) * 10 ** 9

        return download_speed

    def calculate(self):

        self.result.delete(1.0,END)
        self.result.insert(INSERT, (str(datetime.timedelta(seconds= self.get_file_size() / self.get_download_speed())*8)))
    
    def speed_test(self):

       st = speedtest.Speedtest()
       st.get_best_server()
       download_speed = st.download()

       self.download_speed_result.delete(1.0,END)
       self.download_speed_result.insert(INSERT, download_speed * 10 ** -6)

       self.result.delete(1.0,END)
       self.result.insert(INSERT, str(datetime.timedelta(seconds = self.get_file_size() / download_speed)*8))

def main():

    root = Tk()
    main_app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':

    main()
