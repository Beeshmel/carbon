import tkinter as tk


def calculate_carbon_footprint():
    period = period_var.get()

    if period == "Месяц":
        transportation = float(public_transport_entry.get())
        car_mileage = float(mileage_entry.get())
        electricity_usage = float(electricity_entry.get())
        water_usage = float(water_entry.get())
        total_carbon_footprint = transportation * 0.5 + car_mileage * 0.3 + (electricity_usage + water_usage) * 0.2
        result_label.config(
            text="Ваш углеродный след за месяц составляет {:.2f} тонн CO2".format(total_carbon_footprint))
    elif period == "Квартал":
        total_carbon_footprint = "Расчеты для квартала в разработке"
        result_label.config(text=total_carbon_footprint)
    elif period == "Год":
        total_carbon_footprint = "Расчеты для года в разработке"
        result_label.config(text=total_carbon_footprint)


# Create GUI window
root = tk.Tk()
root.title("Carbon Footprint Calculator")

# Add period selection
period_label = tk.Label(root , text="Выберите период расчета:")
period_label.pack()
period_options = ["Месяц" , "Квартал" , "Год"]
period_var = tk.StringVar(root)
period_var.set(period_options[0])
period_dropdown = tk.OptionMenu(root , period_var , *period_options)
period_dropdown.pack()

# Add input fields
public_transport_label = tk.Label(root , text="Количество поездок на общественном транспорте:")
public_transport_label.pack()
public_transport_entry = tk.Entry(root)
public_transport_entry.pack()

mileage_label = tk.Label(root , text="Пробег личного автомобиля (км):")
mileage_label.pack()
mileage_entry = tk.Entry(root)
mileage_entry.pack()

electricity_label = tk.Label(root , text="Расход электроэнергии (кВт-ч):")
electricity_label.pack()
electricity_entry = tk.Entry(root)
electricity_entry.pack()

water_label = tk.Label(root , text="Расход воды (м³):")
water_label.pack()
water_entry = tk.Entry(root)
water_entry.pack()

# Add calculate button
calculate_button = tk.Button(root , text="Рассчитать" , command=calculate_carbon_footprint)
calculate_button.pack()

# Add result label
result_label = tk.Label(root , text="")
result_label.pack()

root.mainloop()
