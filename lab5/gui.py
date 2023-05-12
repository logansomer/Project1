import csv
from tkinter import *
import csv
import re
import os.path
import gui
import main

class GUI:
    def __init__(self, window: None) -> None:
        """
        :param window: allows Window application to run
        :return: None
        """
        self.window = window
        #name
        self.frame_input = Frame(self.window,background='green')
        self.label_input = Label(self.frame_input, text='input')
        self.entry_input = Entry(self.frame_input)
        self.label_input.pack(padx=15, side='left')
        self.entry_input.pack(padx=5, side='left')
        self.frame_input.pack(anchor='w', pady=10)
        #age
        self.frame_output = Frame(self.window,background='green')
        self.label_output = Label(self.frame_output, text='output')
        self.entry_output = Entry(self.frame_output)
        self.label_output.pack(padx=5, side='left')
        self.entry_output.pack(padx=16, side='left')
        self.frame_output.pack(anchor='w', pady=10)
        #Y/N
        self.frame_status = Frame(self.window,background='green')
        self.label_status = Label(self.frame_status, text='Does this file exist already?')
        self.choice = IntVar()
        self.choice.set(0)
        self.button_yes = Radiobutton(self.frame_status, text='Yes',variable=self.choice, value=1)
        self.button_no = Radiobutton(self.frame_status, text='No',variable=self.choice, value=2)
        self.label_status.pack(padx=5,side='left')
        self.button_yes.pack(padx=5, side='left')
        self.button_no.pack(padx=5, side='left')
        self.frame_status.pack(anchor='w', pady=10)
        #save
        self.frame_save = Frame(self.window,background='green')
        self.button_save = Button(self.frame_save,width=25,height=2, text= 'SAVE', command=self.clicked,background='red')
        self.button_save.pack()
        self.frame_save.pack()
        #text box
        self.frame_text = Frame(self.window,background='green')
        self.label_text = Label(self.frame_text,font= (0,18), text='Make Sure you include \n file types!',background='green')
        self.label_text.pack(padx=10, side='bottom')
        self.frame_text.pack(anchor='w', pady=10)
    def clicked(self)-> None:
        """
        :param input1: Recives users input
        :param output1: Recives users output
        :return: None
        """
        input1 = self.entry_input.get()
        output1 = self.entry_output.get()
        status = self.choice.get()
        if input1 == '' or output1 == '':
            self.entry_output.delete(0, END)
            self.entry_input.delete(0, END)
            self.choice.set(0)
            self.entry_input.focus()
            self.label_text.config(text='Try again')

        else:
            GUI.main1(self)
            self.entry_input.delete(0, END)
            self.entry_output.delete(0, END)
            self.label_text.config(text='Data Stored!')

    def input_fun(self)-> str:
        """
        :param file_name: used to check for file based of user input
        :return: File Location ('Files/' + file_name)
        """
        file_name = self.entry_input.get()
        while True:
            try:
                with open('Files/' + file_name) as file:
                    break
            except Exception:
                self.label_text.config(text='File does not exist please try again')
                self.entry_input.delete(0, END)
                break
        return 'Files/' + file_name

    def output_fun(self) -> str:
        """
        :param file_name: used to check for file based of user input
        :param response: numeric value 0, 1 ,or 2
        :return: File Location ('Files/' + file_name)
        """
        file_name = self.entry_output.get()
        response = self.choice.get()
        while os.path.isfile('Files/' + file_name):
            while response != 1 and response != 2:
                self.label_status.config = Label(text='TRY AGAIN')
            if response == 1:
                self.label_status.config = Label(text='TRY AGAIN')
                self.entry_output.delete(0, END)

            if response == 2:
                return 'Files/' + file_name
        return 'Files/' + file_name
    def main1(self)-> None:
        """
        :param input_file: calls input_fun funtion
        :param output_file: calls output_fun funtion
        """
        input_file = GUI.input_fun(self)
        output_file = GUI.output_fun(self)
        with open(input_file, 'r') as input:
            with open(output_file, 'w', newline='') as output:
                writer = csv.writer(output)
                writer.writerow(['Email', 'Subject', 'Confidence'])
                for line in input:
                    if re.search(r'^From:', line):
                        email = line.rstrip().split()[1]
                    if re.search(r'^Subject:', line):
                        subject = line.rstrip().split()[4]
                    if re.search(r'^X-DSPAM-Confidence:', line):
                        number = (line.split()[1])
                        writer.writerow([email, subject, number])




        if __name__ == '__main__':
            main()


