#include <Wire.h>                // Library untuk I2C
#include <LiquidCrystal_I2C.h>   // Library untuk LCD I2C

LiquidCrystal_I2C lcd(0x27, 16, 2);  // LCD dengan alamat 0x27, ukuran 16x2

#define alarm 11
#define sensor 2

// Variabel dan data sensor
int nilai = 0, jumlah = 0;
float set_panjang = 0;
byte set_priode = 0;
float nilai_waktu = 0, T, T2, g;

void setup() {
  Serial.begin(9600);        // Serial monitor
  lcd.init();                // Inisialisasi LCD
  lcd.backlight();           // Nyalakan backlight
  pinMode(alarm, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(sensor), hitungAyunan, FALLING);

  tampilkanPesan("BANDUL", "MATEMATIS");
  alarmSingkat();
}

void loop() {
  if (Serial.available() > 0) {
    // Membaca panjang tali dan periode dari Python
    set_panjang = Serial.parseFloat();
    set_priode = Serial.parseInt();
    
    // Menghitung gravitasi
    hitungGravitasi();
  }
}

void hitungGravitasi() {
  tampilkanPesan("Proses", "Menghitung...");

  nilai = 0; jumlah = 0; nilai_waktu = 0;
  while (jumlah < set_priode) {
    if (nilai >= 2) {
      jumlah++;
      nilai = 0;
    }
    nilai_waktu++;
    delay(1);
  }

  nilai_waktu /= 1000;  // Konversi ke detik
  T = nilai_waktu / set_priode;
  T2 = T * T;
  g = (39.43 * set_panjang / 100) / T2;

  Serial.println("L=" + String(set_panjang) + ",T=" + String(T) + ",g=" + String(g));
  alarmSingkat();
}

void hitungAyunan() {
  if (digitalRead(sensor) == LOW) {
    nilai++;
    alarmSingkat();
  }
}

void tampilkanPesan(String baris1, String baris2) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(baris1);
  lcd.setCursor(0, 1);
  lcd.print(baris2);
  delay(2000);
}

void alarmSingkat() {
  digitalWrite(alarm, HIGH);
  delay(100);
  digitalWrite(alarm, LOW);
}
