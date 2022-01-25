import csv
import random
from tkinter import *

def main():
    root = Tk()

    #root.geometry('600x400')

    frm_main = Frame(root)
    frm_main.master.title("Journalling Prompt Generator")
    frm_main.pack(padx=30, pady=20, fill=BOTH, expand=1)

    populate_window(frm_main)

    root.mainloop()

def populate_window(frm_main):
    lbl_title = Label(frm_main, text="JOURNAL PROMPT GENERATOR")
    lbl_add_prompt = Label(frm_main, text="Add a prompt to the pile:")
    lbl_gen_prompts = Label(frm_main, text="Generate a random prompt from the pile")
    lbl_num_prompts = Label(frm_main, text="Number prompts would you like to generate (1-10):")
    lbl_print_prompts = Label(frm_main)
    lbl_remove = Label(frm_main)

    ent_add_prompt = Entry(frm_main, width=30)
    #ent_gen_prompts = IntEntry(frm_main, 1, 10, width=5)

    btn_add = Button(frm_main, text="ADD")
    btn_gen = Button(frm_main, text="GENERATE")
    btn_remove = Button(frm_main, text="REMOVE")
    
    lbl_title.grid(  row=0, column=0, padx=3, pady=3)
    lbl_add_prompt.grid(  row=3, column=0, padx=3, pady=3)
    ent_add_prompt.grid(  row=4, column=0, padx=3, pady=3)
    btn_add.grid(row=5, column=0, padx=135, pady=3, sticky="W")
    lbl_gen_prompts.grid(  row=6, column=0, padx=3, pady=3)
    lbl_num_prompts.grid(  row=7, column=0, padx=3, pady=3)
    #ent_gen_prompts.grid(   row=8, column=0, padx=3, pady=3)
    btn_gen.grid(row=9, column=0, padx=120, pady=3, sticky="W")

    def add_prompt():
        #print("Test successful?")
        pt_to_add = ent_add_prompt.get()
        print(pt_to_add)
        #lbl_slow.config(text=f"{slow:.0f}")
        with open("journaling.csv", "at", newline='') as jour_csv:
            writer = csv.writer(jour_csv)
            writer.writerow([pt_to_add])
        ent_add_prompt.delete(0, END)
        ent_add_prompt.focus()
    
    def gen_prompt():
        #print("Generated successfully")
        prompts_list = []
        #print(prompts_list)
        with open("journaling.csv", "rt") as jour_csv:
            reader = csv.reader(jour_csv)
            for row in reader:
                prompts_list.append(row)
        random_prompt_og = random.choice(prompts_list)
        #print(prompts_list)
        #print(random_prompt_og)
        random_prompt = str(random_prompt_og)
        random_prompt = random_prompt[2:]
        lbl_print_prompts.config(text=random_prompt[:-2])
        lbl_remove.config(text="Would you like to remove this prompt from "
                               "the pile?")
        lbl_print_prompts.grid(  row=10, column=0, padx=3, pady=3)
        lbl_remove.grid(  row=11, column=0, padx=3, pady=3)
        btn_remove.grid(  row=12, column=0, padx=3, pady=3)
        return random_prompt

    def remove_prompt():
        with open("journaling.csv", "wt") as jour_csv:
            writer = csv.writer(jour_csv)
        print("Prompt removed!")
        pass

    btn_gen.config(command=gen_prompt)
    btn_remove.config(command=remove_prompt)
    btn_add.config(command=add_prompt)
    



if __name__ == "__main__":
    main()