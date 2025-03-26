import phonenumbers
import tkinter as tk
from phonenumbers import geocoder, carrier, timezone, region_code_for_number

def get_phone_info():
    number = entry.get().strip()
    
    if not number:
        result_label.config(text="⚠ Please enter a phone number!", fg="red")
        return
    
    try:
        # Parse phone number for any country
        ch_number = phonenumbers.parse(number)
        
        # Get location, carrier, and time zone
        location = geocoder.description_for_number(ch_number, "en")
        service_provider = carrier.name_for_number(ch_number, "en")
        time_zones = timezone.time_zones_for_number(ch_number)
        country_code = region_code_for_number(ch_number)
        
        # Display results
        result_label.config(
            text=(
                f"🌍 Country: {location} ({country_code})\n"
                f"📶 Carrier: {service_provider}\n"
                f"⏰ Time Zone: {', '.join(time_zones)}"
            ), 
            fg="#333"
        )
    except Exception:
        result_label.config(text="❌ Invalid phone number format!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("🌎 International Phone Tracker")
root.geometry("420x350")
root.configure(bg="#e3f2fd")  # Soft gradient-like blue background

# Title Label
tk.Label(root, text="📱 Phone Number Tracker", font=("Arial", 15, "bold"), bg="#e3f2fd", fg="#1e3a8a").pack(pady=10)

# Entry Field
entry = tk.Entry(root, width=35, font=("Arial", 12), fg="#333", justify="center", relief="solid", bd=2)
entry.insert(0, "Enter phone number with + (e.g., +1XXXXXX)")
entry.pack(pady=5, ipady=5)

# Clear default text on click
def clear_placeholder(event):
    if entry.get() == "Enter phone number with + (e.g., +1XXXXXX)":
        entry.delete(0, tk.END)
entry.bind("<FocusIn>", clear_placeholder)

# Button with Hover Effect
def on_enter(e):
    button.config(bg="#0056b3")

def on_leave(e):
    button.config(bg="#007BFF")

button = tk.Button(root, text="🔍 Get Info", command=get_phone_info, font=("Arial", 12, "bold"), bg="#007BFF", fg="white", padx=10, pady=5, relief="raised", borderwidth=3)
button.pack(pady=10)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e3f2fd")
result_label.pack(pady=10)

root.mainloop()
