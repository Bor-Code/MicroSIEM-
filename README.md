🛡️ MicroSIEM - Sade ve Etkili Güvenlik İzleme Sistemi
MicroSIEM, ağınızdaki güvenlik olaylarını gerçek zamanlı takip etmenize, analiz etmenize ve görselleştirmenize yardımcı olan kullanıcı dostu bir araç. Python ile yazılmış bu sistem, hem Windows hem Linux'ta rahatlıkla çalışıyor ve ağ güvenliğinizi izlemeyi oldukça kolaylaştırıyor.
Sistemin temel mantığı şu şekilde: Syslog trafiğinizi sürekli dinliyor, şüpheli aktiviteleri tespit ediyor ve size anlamlı bilgiler sunuyor. Özellikle kaba kuvvet (brute force) saldırılarını yakalamada oldukça başarılı. Saldırganların nereden geldiğini harita üzerinde görebilir, hangi sistemlerinizin hedef alındığını anlık takip edebilirsiniz. Tüm bunları da modern ve anlaşılır bir web arayüzünde görüyorsunuz.

🚀 Neler Yapabilir?
Platform Desteği->Windows, Linux ve MacOS üzerinde çalışıyor. Hangi işletim sistemini kullanırsanız kullanın, kurulum ve kullanım aynı kolaylıkta.
Gerçek Zamanlı İzleme->UDP 5140 portu üzerinden gelen Syslog paketlerini anlık olarak yakalar ve işler. Ağınızda olan biteni saniye saniye takip edebilirsiniz. Gecikme yok, her şey gerçek zamanlı.
Akıllı Saldırı Tespiti->Başarısız giriş denemelerini özel algoritmalarla analiz eder. Tekrarlayan başarısız denemeler, kısa sürede çok sayıda istek gibi anormal davranışları tespit edip size uyarı verir. Böylece bir saldırı başlamadan önlem alabilirsiniz.
Coğrafi Konum Belirleme->Saldırgan IP adreslerinin nereden geldiğini otomatik olarak bulur. Hangi ülkeden, hangi internet servis sağlayıcısından geldiğini görürsünüz. Bu bilgi sayesinde gerekirse belirli bölgelerden gelen trafiği engelleyebilirsiniz.
Canlı Dashboard->Web tabanlı modern bir arayüz üzerinden tüm verileri görselleştirir. Grafikler, tablolar ve haritalar sayesinde karmaşık verileri kolayca anlayabilirsiniz. Saldırı trendlerini, en çok hedef alınan sistemlerinizi ve tehdit haritanızı canlı olarak izleyebilirsiniz.
Güvenli Admin Paneli->Dashboard'a erişim şifre korumalı. Sadece yetkili kişiler sisteme giriş yapabilir ve güvenlik verilerinizi görebilir.

🛠️ Nasıl Kurulur?
1. Ön Hazırlık
Bilgisayarınızda Python 3 kurulu olmalı. Python'un güncel bir sürümünü (tercihen 3.8 veya üzeri) kullanmanızı öneririz.
2. Projeyi İndirin
Terminal veya komut satırını açın ve aşağıdaki komutları sırasıyla çalıştırın:
bashgit clone https://github.com/Bor-Code/MicroSIEM.git
cd MicroSIEM
Bu komutlar projeyi GitHub'dan bilgisayarınıza indirir ve proje klasörüne giriş yapar.
3. Gerekli Kütüphaneleri Yükleyin
Proje klasöründeyken şu komutu çalıştırın:
bashpip install -r requirements.txt
Bu komut, MicroSIEM'in çalışması için gerekli tüm Python kütüphanelerini otomatik olarak yükler.
4. Sistemi Başlatın
Kurulum tamamlandıktan sonra programı başlatmak için:
bashpython microsiem.py
Program başladığında konsol üzerinden size bir web adresi verecek (genellikle http://localhost:5000). Bu adresi tarayıcınızda açarak dashboard'a erişebilirsiniz.

Keyifli kullanımlar! [Bor-Code]

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛡️ MicroSIEM - Simple and Effective Security Monitoring System
MicroSIEM is a user-friendly tool that helps you monitor, analyze, and visualize security events on your network in real time. Written in Python, this system runs smoothly on both Windows and Linux, making it very easy to monitor your network security.
The system works as follows: It continuously monitors your syslog traffic, detects suspicious activity, and provides you with meaningful information. It is particularly effective at catching brute force attacks. You can see where attackers are coming from on a map and instantly track which of your systems are being targeted. All of this is displayed in a modern and intuitive web interface.

🚀 What Can It Do?
Platform Support->Works on Windows, Linux, and MacOS. No matter which operating system you use, installation and usage are equally easy.
Real-Time Monitoring->Instantly captures and processes Syslog packets coming through UDP port 5140. You can track what's happening on your network second by second. No delay, everything is real-time.
Smart Attack Detection->Analyzes failed login attempts using specialized algorithms. It detects abnormal behavior such as repeated failed attempts or a large number of requests in a short time and alerts you. This allows you to take action before an attack begins.
Geolocation->Automatically finds where attacker IP addresses are coming from. You can see which country and which internet service provider they are coming from. With this information, you can block traffic from specific regions if necessary.
Live Dashboard->Visualizes all data through a modern web-based interface. You can easily understand complex data through graphs, tables, and maps. You can monitor attack trends, your most targeted systems, and your threat map live.
Secure Admin Panel->Access to the Dashboard is password protected. Only authorized persons can log into the system and view your security data.

🛠️ How to Install?
1. Prerequisites
Python 3 must be installed on your computer. We recommend using a recent version of Python (preferably 3.8 or higher).
2. Download the Project
Open the terminal or command line and run the following commands in order:
bashgit clone https://github.com/Bor-Code/MicroSIEM.git
cd MicroSIEM
These commands download the project from GitHub to your computer and enter the project folder.
3. Install the Required Libraries
While in the project folder, run the following command:
bashpip install -r requirements.txt
This command automatically installs all the Python libraries required for MicroSIEM to work.
4. Start the System
Once the installation is complete, start the program with:
bashpython microsiem.py
When the program starts, it will provide you with a web address via the console (usually http://localhost:5000). You can access the dashboard by opening this address in your browser.

Enjoy! [Bor-Code]
