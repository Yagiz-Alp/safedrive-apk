import tkinter as tk

class SafeDriveV2App:
    def __init__(self, root):
        self.root = root
        self.root.title("SafeDrive v2 - Masaüstü Simülatörü")
        self.root.geometry("700x550")
        self.root.configure(bg="#121212")

        # Değişkenler
        self.is_driving = False
        self.speed = 0.0
        self.speed_limit = 80.0
        self.drive_score = 100
        self.hard_brakes = 0
        self.speed_violations = 0

        # --- ARAYÜZ TASARIMI ---
        # Başlık ve Puan
        header_frame = tk.Frame(root, bg="#121212")
        header_frame.pack(fill="x", padx=20, pady=15)

        title_label = tk.Label(header_frame, text="SAFEDRIVE v2", font=("Arial", 22, "bold"), fg="#00E676", bg="#121212")
        title_label.pack(side="left")

        self.score_label = tk.Label(header_frame, text="Sürüş Puanı: 100", font=("Arial", 18, "bold"), fg="#FFFFFF", bg="#121212")
        self.score_label.pack(side="right")

        # Gösterge Kartları
        cards_frame = tk.Frame(root, bg="#121212")
        cards_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Hız Card
        self.card_speed = tk.Frame(cards_frame, bg="#1E1E1E", highlightbackground="#29B6F6", highlightthickness=2)
        self.card_speed.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(self.card_speed, text="ANLIK HIZ", font=("Arial", 12), fg="#B0BEC5", bg="#1E1E1E").pack(pady=(15, 5))
        self.val_speed = tk.Label(self.card_speed, text="0 km/s", font=("Arial", 24, "bold"), fg="#29B6F6", bg="#1E1E1E")
        self.val_speed.pack(pady=(0, 15))

        # Limit Card
        self.card_limit = tk.Frame(cards_frame, bg="#1E1E1E", highlightbackground="#FFA726", highlightthickness=2)
        self.card_limit.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(self.card_limit, text="HIZ LİMİTİ", font=("Arial", 12), fg="#B0BEC5", bg="#1E1E1E").pack(pady=(15, 5))
        tk.Label(self.card_limit, text="80 km/s", font=("Arial", 24, "bold"), fg="#FFA726", bg="#1E1E1E").pack(pady=(0, 15))

        # Fren Card
        self.card_brakes = tk.Frame(cards_frame, bg="#1E1E1E", highlightbackground="#424242", highlightthickness=2)
        self.card_brakes.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        tk.Label(self.card_brakes, text="ANİ FREN SAYISI", font=("Arial", 12), fg="#B0BEC5", bg="#1E1E1E").pack(pady=(15, 5))
        self.val_brakes = tk.Label(self.card_brakes, text="0", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#1E1E1E")
        self.val_brakes.pack(pady=(0, 15))

        # İhlal Card
        self.card_violations = tk.Frame(cards_frame, bg="#1E1E1E", highlightbackground="#424242", highlightthickness=2)
        self.card_violations.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        tk.Label(self.card_violations, text="HIZ İHLALİ", font=("Arial", 12), fg="#B0BEC5", bg="#1E1E1E").pack(pady=(15, 5))
        self.val_violations = tk.Label(self.card_violations, text="0", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#1E1E1E")
        self.val_violations.pack(pady=(0, 15))

        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        # Durum Metni
        self.status_label = tk.Label(root, text="Sürüş başlatılmadı.", font=("Arial", 13), fg="#B0BEC5", bg="#121212")
        self.status_label.pack(pady=10)

        # Başlat/Durdur Butonu
        self.toggle_btn = tk.Button(root, text="SÜRÜŞÜ BAŞLAT", font=("Arial", 14, "bold"), fg="#000000", bg="#00E676",
                                    activebackground="#00C853", command=self.toggle_drive, height=2)
        self.toggle_btn.pack(fill="x", padx=30, pady=(0, 10))

        # Klavye Kontrolleri Bilgisi
        info_label = tk.Label(root, text="Kontroller: [Yukarı Ok] Gaza Bas  |  [Aşağı Ok] Ani Fren Yap", font=("Arial", 10), fg="#78909C", bg="#121212")
        info_label.pack(pady=(0, 15))

        # Klavye Bağlantıları
        root.bind("<Up>", self.press_gas)
        root.bind("<Down>", self.press_brake)

        # Döngüyü Başlat
        self.update_loop()

    def toggle_drive(self):
        self.is_driving = not self.is_driving
        if self.is_driving:
            self.drive_score = 100
            self.hard_brakes = 0
            self.speed_violations = 0
            self.speed = 0.0
            self.toggle_btn.config(text="SÜRÜŞÜ BİTİR", bg="#FF5252", fg="#FFFFFF")
            self.status_label.config(text="Sürüş Aktif! Gaza basmak için [Yukarı Ok] tuşunu kullanın.", fg="#00E676")
        else:
            self.toggle_btn.config(text="SÜRÜŞÜ BAŞLAT", bg="#00E676", fg="#000000")
            self.status_label.config(text=f"Sürüş Bitti! Ani Fren: {self.hard_brakes} | Hız İhlali: {self.speed_violations}", fg="#B0BEC5")

    def press_gas(self, event):
        if self.is_driving:
            self.speed += 5.0

    def press_brake(self, event):
        if self.is_driving and self.speed > 15:
            self.speed = max(0.0, self.speed - 25.0)
            self.hard_brakes += 1
            self.drive_score = max(0, self.drive_score - 5)
            self.status_label.config(text="⚠️ ANİ FREN ALGILANDI!", fg="#FF5252")

    def update_loop(self):
        if self.is_driving:
            # Doğal yavaşlama (Sürtünme)
            if self.speed > 0:
                self.speed = max(0.0, self.speed - 0.3)

            # Hız Limiti İhlali
            if self.speed > self.speed_limit:
                self.speed_violations += 1
                self.drive_score = max(0, self.drive_score - 1)
                self.status_label.config(text=f"⚠️ HIZ LİMİTİ AŞILDI! ({int(self.speed)} km/s)", fg="#FF5252")

            # Arayüzü Güncelle
            self.val_speed.config(text=f"{int(self.speed)} km/s")
            self.val_brakes.config(text=str(self.hard_brakes))
            self.val_violations.config(text=str(self.speed_violations))
            
            # Puan Rengini Güncelle
            score_color = "#00E676" if self.drive_score > 70 else ("#FFA726" if self.drive_score > 40 else "#FF5252")
            self.score_label.config(text=f"Sürüş Puanı: {self.drive_score}", fg=score_color)

        self.root.after(200, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = SafeDriveV2App(root)
    root.mainloop()
    