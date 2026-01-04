import tkinter as tk
from tkinter import messagebox
import requests
from weather_api import get_weather_data
from utils.output_formatter import format_weather_data

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hava Durumu Uygulaması")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Giriş Alanı
        self.lbl_header = tk.Label(self, text="Şehir Adı Girin:", font=('Arial', 14))
        self.lbl_header.pack(pady=10)
        
        self.entry_city = tk.Entry(self, width=30, font=('Arial', 12))
        self.entry_city.pack(pady=5)
        
        # Buton
        self.btn_get_weather = tk.Button(
            self, 
            text="Hava Durumunu Göster", 
            command=self.fetch_weather,
            bg="#4CAF50",
            fg="white",
            
            font=('Arial', 12)
        )
        self.btn_get_weather.pack(pady=10)
        
        # Sonuç Gösterimi
        self.lbl_result = tk.Label(self, text="", font=('Arial', 12), justify='left')
        self.lbl_result.pack(pady=20)
    
    def fetch_weather(self):
        city = self.entry_city.get().strip()
        if not city:
            messagebox.showwarning("Uyarı", "Lütfen bir şehir adı girin!")
            return
        
        try:
            weather_data = get_weather_data(city)
            formatted = format_weather_data(weather_data)
            self.lbl_result.config(text=formatted)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                messagebox.showerror("Hata", f"'{city}' bulunamadı tekrar deneyin!")
            elif e.response.status_code == 401:
                messagebox.showerror("Hata", "Geçersiz API anahtarı!")
            else:
                messagebox.showerror("API Hatası", str(e))
        except Exception as e:
            messagebox.showerror("Hata", str(e))

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()