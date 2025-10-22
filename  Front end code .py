import tkinter as tk
from tkinter import Button, Label, Frame, Toplevel, Entry, StringVar
from backend import SmartHome, SmartPlug, SmartLight, SmartAirFryer

class SmartHomeApp:
    def __init__(self, master):
        self.master = master
        master.title("Smart Home App")
        master.config(bg="lightgray")

        self.home = SmartHome()
        self.home.add_device(SmartPlug(consumption_rate=45))
        self.home.add_device(SmartLight(brightness=50))
        self.home.add_device(SmartAirFryer(cook_mode="Healthy"))

        self.main_frame = Frame(master, bg="lightgray")
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        Button(self.main_frame, text="Turn all on", width=15, bg="lightblue",
               command=self.turn_all_on).grid(row=0, column=0, pady=5, padx=5)
        Button(self.main_frame, text="Turn all off", width=15, bg="lightcoral",
               command=self.turn_all_off).grid(row=0, column=1, pady=5, padx=5)

        for idx, device in enumerate(self.home.devices, start=1):
            color = "green" if device.switched_on else "red"
            Label(self.main_frame, text=str(device), fg=color, bg="lightgray").grid(row=idx, column=0, sticky="w")

            Button(self.main_frame, text="Toggle", width=10, bg="lightyellow",
                   command=lambda i=idx-1: self.toggle_device(i)).grid(row=idx, column=1, padx=5)
            Button(self.main_frame, text="Edit", width=10, bg="lightgreen",
                   command=lambda i=idx-1: self.edit_device(i)).grid(row=idx, column=2, padx=5)
            Button(self.main_frame, text="Delete", width=10, bg="lightcoral",
                   command=lambda i=idx-1: self.delete_device(i)).grid(row=idx, column=3, padx=5)

        Button(self.main_frame, text="Add", width=10, bg="orange",
               command=self.add_device_popup).grid(row=len(self.home.devices)+1, column=0, pady=10, sticky="w")

    def refresh_gui(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.create_widgets()

    def toggle_device(self, index):
        self.home.toggle_device(index)
        self.refresh_gui()

    def delete_device(self, index):
        del self.home.devices[index]
        self.refresh_gui()

    def turn_all_on(self):
        self.home.switch_all_on()
        self.refresh_gui()

    def turn_all_off(self):
        self.home.switch_all_off()
        self.refresh_gui()

    def edit_device(self, index):
        edit_win = Toplevel(self.master)
        device = self.home.devices[index]
        edit_win.title(f"Edit {device.__class__.__name__}")

        if isinstance(device, SmartPlug):
            Label(edit_win, text="Consumption rate:").pack(pady=5)
            rate_entry = Entry(edit_win)
            rate_entry.insert(0, str(device.consumption_rate))
            rate_entry.pack(pady=5)
            Button(edit_win, text="Save", command=lambda: self.save_plug(index, rate=int(rate_entry.get()),window=edit_win)).pack(pady=5)

        elif isinstance(device, SmartLight):
            Label(edit_win, text="Brightness (1-100):").pack(pady=5)
            brightness_entry = Entry(edit_win)
            brightness_entry.pack()
            brightness_entry.insert(0, str(device.brightness))
            Button(edit_win, text="Save", command=lambda: self.save_light(index, int(brightness_entry.get()), edit_win)).pack(pady=5)

        elif isinstance(device, SmartAirFryer):
            Label(edit_win, text="Cook Mode (Healthy, Defrost, Crispy):").pack(pady=5)
            mode_entry = Entry(edit_win)
            mode_entry.pack()
            mode_entry.insert(0, device.cook_mode)
            Button(edit_win, text="Save", command=lambda: self.save_airfryer_mode(index, mode_entry.get(), edit_win)).pack(pady=5)

    def save_airfryer_mode(self, index, mode, window):
        device = self.home.devices[index]
        try:
            device.set_cook_mode(mode)
            window.destroy()
            self.refresh_gui()
        except ValueError as e:
            print(e)

    def save_airfryer_mode(self, index, new_mode, window):
        device = self.home.devices[index]
        try:
            device.set_cook_mode(new_mode)
            window.destroy()
            self.refresh_gui()
        except ValueError as e:
            print(e)

    def save_plug(self, index, rate, window):
        device = self.home.devices[index]
        try:
            device.consumption_rate = rate
            window.destroy()
            self.refresh_gui()
        except ValueError as e:
            print(e)

    def save_light(self, index, brightness, window):
        device = self.home.devices[index]
        try:
            device.set_brightness(brightness)
            window.destroy()
            self.refresh_gui()
        except ValueError as e:
            print(e)

    def add_device_popup(self):
        popup = Toplevel(self.master)
        popup.title("Add Device")

        Label(popup, text="Select device to add:").pack(pady=10)

        # SmartPlug addition (clearly working)
        Button(popup, text="Add SmartPlug",
            command=lambda: [self.home.add_device(SmartPlug(consumption_rate=45)), popup.destroy(), self.refresh_gui()]
            ).pack(pady=5)

        Button(popup, text="Add SmartLight",
            command=lambda: [self.home.add_device(SmartLight(brightness=50)), popup.destroy(), self.refresh_gui()]
            ).pack(pady=5)
        

        # AirFryer (already works, unchanged)
        Button(popup, text="Add SmartAirFryer",
            command=lambda: [self.home.add_device(SmartAirFryer(cook_mode="Healthy")), popup.destroy(), self.refresh_gui()]
            ).pack(pady=5)

def add_light_device(self, brightness, popup):
    try:
        brightness = int(brightness)
        if 1 <= brightness <= 100:
            self.home.add_device(SmartLight(brightness))
            popup.destroy()
            self.refresh_gui()
        else:
            print("Error: Brightness must be 1-100.")
    except ValueError:
        print("Error: Invalid brightness value entered.")


    def add_device(self):
        self.home.add_device(SmartPlug(consumption_rate=30))
        self.refresh_gui()

def main():
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
