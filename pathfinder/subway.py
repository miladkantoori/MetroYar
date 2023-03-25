from pathfinder.backend import SubwaySystem, Station

subway = SubwaySystem()

# Create station objects

a1 = Station('تجریش', ['l1'])
a2 = Station('قیطریه', ['l1'])
a3 = Station('شهید صدر', ['l1'])
a4 = Station('قلهک', ['l1'])
a5 = Station('دکتر شریعتی', ['l1'])
a6 = Station('میرداماد', ['l1'])
a7 = Station('شهید حقانی', ['l1'])
a8 = Station('شهید همت', ['l1'])
a9 = Station('مصلی امام خمینی', ['l1'])
a10 = Station('شهید بهشتی', ['l1', 'l3'])
a11 = Station('شهید مفتح', ['l1'])
a12 = Station('شهدای هفت تیر', ['l1'])
a13 = Station('طالقانی', ['l1'])
a14 = Station('دروازه دولت', ['l1', 'l4'])
a15 = Station('سعدی', ['l1'])
a16 = Station('امام خمینی', ['l1', 'l2'])
a17 = Station('پانزده خرداد', ['l1'])
a18 = Station('خیام', ['l1'])
a19 = Station('میدان محمدیه', ['l1', 'l7'])
a20 = Station('شوش', ['l1'])
a21 = Station('پایانه جنوب', ['l1'])
a22 = Station('شهید بخارائی', ['l1'])
a23 = Station('علی آباد', ['l1'])
a24 = Station('جوانمرد قصاب', ['l1'])
a25 = Station('شهرری', ['l1'])
a26 = Station('پالایشگاه', ['l1'])
a27 = Station('شاهد', ['l1', 'l1w'])
a28 = Station('حرم مطهر امام خمینی', ['l1'])
a29 = Station('کهریزک', ['l1'])
#l1w
aw1 = Station('شهر آفتاب', ['l1w'])
aw2 = Station('فرودگاه امام خمینی', ['l1w'])
#l2
b1 = Station('تهران (صادقیه)', ['l2', 'l5'])
b2 = Station('طرشت', ['l2'])
b3 = Station('دانشگاه شریف', ['l2'])
b4 = Station('شادمان', ['l2', 'l4'])
b5 = Station('شهید نواب صفوی', ['l2', 'l7'])
b6 = Station('میدان حر', ['l2'])
b7 = Station('دانشگاه امام علی', ['l2'])
b8 = Station('حسن آباد', ['l2'])
b9 = Station('ملت', ['l2'])
b10 = Station('بهارستان', ['l2'])
b11 = Station('دروازه شمیران', ['l2','l4'])
b12 = Station('امام حسین', ['l2', 'l6e'])
b13 = Station('شهید مدنی', ['l2'])
b14 = Station('سبلان', ['l2'])
b15 = Station('فدک', ['l2'])
b16 = Station('جانبازان', ['l2'])
b17 = Station('سرسبز', ['l2'])
b18 = Station('دانشگاه علم و صنعت', ['l2'])
b19 = Station('شهید باقری', ['l2'])
b20 = Station('تهرانپارس', ['l2'])
b21 = Station('فرهنگسرا', ['l2'])
#l3
c1 = Station('آزادگان', ['l3'])
c2 = Station('نعمت آباد', ['l3'])
c3 = Station('عبدل آباد', ['l3'])
c4 = Station('شهرک شریعتی', ['l3'])
c5 = Station('زمزم', ['l3'])
c6 = Station('جوادیه', ['l3'])
c7 = Station('راه آهن', ['l3'])
c8 = Station('مهدیه', ['l3', 'l7'])
c9 = Station('منیریه', ['l3'])
c10 = Station('تئاتر شهر', ['l3', 'l4'])
c11 = Station('میدان ولیعصر', ['l3'])
c12 = Station('میدان جهاد', ['l3'])
c13 = Station('میرزای شیرازی', ['l3'])
c14 = Station('سهروردی', ['l3'])
c15 = Station('شهید قدوسی', ['l3'])
c16 = Station('شهید صیاد شیرازی', ['l3'])
c17 = Station('خواجه عبدالله انصاری', ['l3'])
c18 = Station('شهید زین الدین', ['l3'])
c19 = Station('میدان هروی', ['l3'])
c20 = Station('حسین آباد', ['l3'])
c21 = Station('نوبنیاد', ['l3'])
c22 = Station('اقدسیه', ['l3'])
c23 = Station('شهید محلاتی', ['l3'])
c24 = Station('قائم', ['l3'])
#l4
d1 = Station('ارم سبز', ['l4', 'l5'])
d2 = Station('شهرک اکباتان', ['l4'])
d3 = Station('بیمه', ['l4', 'l4s'])
d4 = Station('میدان آزادی', ['l4'])
d5 = Station('استاد معین', ['l4'])
d6 = Station('دکتر حبیب اله', ['l4'])
d7 = Station('توحید', ['l4', 'l7'])
d8 = Station('میدان انقلاب اسلامی', ['l4'])
d9 = Station('فردوسی', ['l4'])
d10 = Station('میدان شهدا', ['l4', 'l6e'])
d11 = Station('ابن سینا', ['l4'])
d12 = Station('پیروزی', ['l4'])
d13 = Station('نبرد', ['l4'])
d14 = Station('نیروی هوایی', ['l4'])
d15 = Station('شهید کلاهدوز', ['l4'])
#l4s
ds1 = Station('پایانه 1و2 فرودگاه مهرآباد', ['l4s'])
ds2 = Station('پایانه 4و6 فرودگاه مهرآباد', ['l4s'])
#l5
e1 = Station('گلشهر', ['l5', 'l5w'])
e2 = Station('محمدشهر', ['l5'])
e3 = Station('کرج', ['l5'])
e4 = Station('اتمسفر', ['l5'])
e5 = Station('گرمدره', ['l5'])
e6 = Station('وردآورد', ['l5'])
e7 = Station('ایران خودرو', ['l5'])
e8 = Station('چیتگر', ['l5'])
e9 = Station('ورزشگاه آزادی', ['l5'])
#l5w
ew1 = Station('شهید سپهبد سلیمانی', ['l5w'])
#l6e
fe1 = Station('امیرکبیر', ['l6e'])
fe2 = Station('شهید رضایی', ['l6e'])
fe3 = Station('بعثت', ['l6e'])
fe4 = Station('کیانشهر', ['l6e'])
fe5 = Station('دولت آباد', ['l6e'])
#l6w
fw1 = Station('شهید ستاری', ['l6w'])
fw2 = Station('شهید اشرفی اصفهانی', ['l6w'])
fw3 = Station('یادگار امام', ['l6w'])
fw4 = Station('مرزداران', ['l6w'])
fw5 = Station('شهرک آزمایش', ['l6w'])
fw6 = Station('دانشگاه تربیت مدرس', ['l6w', 'l7'])
#l7
g1 = Station('میدان صنعت', ['l7'])
g2 = Station('برج میلاد', ['l7'])
g3 = Station('بوستان گفتگو', ['l7'])
g4 = Station('مدافعان سلامت', ['l7'])
g5 = Station('رودکی', ['l7'])
g6 = Station('کمیل', ['l7'])
g7 = Station('بریانک', ['l7'])
g8 = Station('هلال احمر', ['l7'])
g9 = Station('مولوی', ['l7'])
g10 = Station('میدان قیام', ['l7'])
g11 = Station('شهدای 17 شهریور', ['l7'])
g12 = Station('چهل تن دولاب', ['l7'])
g13 = Station('آهنگ', ['l7'])
g14 = Station('بسیج', ['l7'])


# Add stations to subway system
subway.add_station(a1)
subway.add_station(a2)
subway.add_station(a3)
subway.add_station(a4)
subway.add_station(a5)
subway.add_station(a6)
subway.add_station(a7)
subway.add_station(a8)
subway.add_station(a9)
subway.add_station(a10)
subway.add_station(a11)
subway.add_station(a12)
subway.add_station(a13)
subway.add_station(a14)
subway.add_station(a15)
subway.add_station(a16)
subway.add_station(a17)
subway.add_station(a18)
subway.add_station(a19)
subway.add_station(a20)
subway.add_station(a21)
subway.add_station(a22)
subway.add_station(a23)
subway.add_station(a24)
subway.add_station(a25)
subway.add_station(a26)
subway.add_station(a27)
subway.add_station(a28)
subway.add_station(a29)
subway.add_station(aw1)
subway.add_station(aw2)
subway.add_station(b1)
subway.add_station(b2)
subway.add_station(b3)
subway.add_station(b4)
subway.add_station(b5)
subway.add_station(b6)
subway.add_station(b7)
subway.add_station(b8)
subway.add_station(b9)
subway.add_station(b10)
subway.add_station(b11)
subway.add_station(b12)
subway.add_station(b13)
subway.add_station(b14)
subway.add_station(b15)
subway.add_station(b16)
subway.add_station(b17)
subway.add_station(b18)
subway.add_station(b19)
subway.add_station(b20)
subway.add_station(b21)
subway.add_station(c1)
subway.add_station(c2)
subway.add_station(c3)
subway.add_station(c4)
subway.add_station(c5)
subway.add_station(c6)
subway.add_station(c7)
subway.add_station(c8)
subway.add_station(c9)
subway.add_station(c10)
subway.add_station(c11)
subway.add_station(c12)
subway.add_station(c13)
subway.add_station(c14)
subway.add_station(c15)
subway.add_station(c16)
subway.add_station(c17)
subway.add_station(c18)
subway.add_station(c19)
subway.add_station(c20)
subway.add_station(c21)
subway.add_station(c22)
subway.add_station(c23)
subway.add_station(c24)
subway.add_station(d1)
subway.add_station(d2)
subway.add_station(d3)
subway.add_station(d4)
subway.add_station(d5)
subway.add_station(d6)
subway.add_station(d7)
subway.add_station(d8)
subway.add_station(d9)
subway.add_station(d10)
subway.add_station(d11)
subway.add_station(d12)
subway.add_station(d13)
subway.add_station(d14)
subway.add_station(d15)
subway.add_station(ds1)
subway.add_station(ds2)
subway.add_station(e1)
subway.add_station(e2)
subway.add_station(e3)
subway.add_station(e4)
subway.add_station(e5)
subway.add_station(e6)
subway.add_station(e7)
subway.add_station(e8)
subway.add_station(e9)
subway.add_station(ew1)
subway.add_station(fe1)
subway.add_station(fe2)
subway.add_station(fe3)
subway.add_station(fe4)
subway.add_station(fe5)
subway.add_station(fw1)
subway.add_station(fw2)
subway.add_station(fw3)
subway.add_station(fw4)
subway.add_station(fw5)
subway.add_station(fw6)
subway.add_station(g1)
subway.add_station(g2)
subway.add_station(g3)
subway.add_station(g4)
subway.add_station(g5)
subway.add_station(g6)
subway.add_station(g7)
subway.add_station(g8)
subway.add_station(g9)
subway.add_station(g10)
subway.add_station(g11)
subway.add_station(g12)
subway.add_station(g13)
subway.add_station(g14)









# Add connections between stations
subway.add_connection(a1, a2, 2)
subway.add_connection(a2, a3, 2)
subway.add_connection(a3, a4, 2)
subway.add_connection(a4, a5, 3)
subway.add_connection(a5, a6, 2)
subway.add_connection(a6, a7, 3)
subway.add_connection(a7, a8, 2)
subway.add_connection(a8, a9, 2)
subway.add_connection(a9, a10, 2)
subway.add_connection(a10, a11, 2)
subway.add_connection(a11, a12, 2)
subway.add_connection(a12, a13, 3)
subway.add_connection(a13, a14, 2)
subway.add_connection(a14, a15, 2)
subway.add_connection(a15, a16, 2)
subway.add_connection(a16, a17, 2)
subway.add_connection(a17, a18, 2)
subway.add_connection(a18, a19, 3)
subway.add_connection(a19, a20, 2)
subway.add_connection(a20, a21, 2)
subway.add_connection(a21, a22, 2)
subway.add_connection(a22, a23, 3)
subway.add_connection(a23, a24, 2)
subway.add_connection(a24, a25, 4)
subway.add_connection(a25, a26, 5)
subway.add_connection(a26, a27, 3)
subway.add_connection(a27, a28, 3)
subway.add_connection(a28, a29, 4)

subway.add_connection(a27, aw1, 7)
subway.add_connection(aw1, aw2, 33)

subway.add_connection(b1, b2, 2)
subway.add_connection(b2, b3, 2)
subway.add_connection(b3, b4, 2)
subway.add_connection(b4, b5, 3)
subway.add_connection(b5, b6, 3)
subway.add_connection(b6, b7, 2)
subway.add_connection(b7, b8, 3)
subway.add_connection(b8, a16, 2)
subway.add_connection(a16, b9, 3)
subway.add_connection(b9, b10, 2)
subway.add_connection(b10, b11, 2)
subway.add_connection(b11, b12, 2)
subway.add_connection(b12, b13, 3)
subway.add_connection(b13, b14, 2)
subway.add_connection(b14, b15, 2)
subway.add_connection(b15, b16, 2)
subway.add_connection(b16, b17, 3)
subway.add_connection(b17, b18, 2)
subway.add_connection(b18, b19, 2)
subway.add_connection(b19, b20, 2)
subway.add_connection(b20, b21, 2)
subway.add_connection(c1, c2, 1)
subway.add_connection(c2, c3, 2)
subway.add_connection(c3, c4, 2)
subway.add_connection(c4, c5, 2)
subway.add_connection(c5, c6, 2)
subway.add_connection(c6, c7, 2)
subway.add_connection(c7, c8, 3)
subway.add_connection(c8, c9, 2)
subway.add_connection(c9, c10, 3)
subway.add_connection(c10, c11, 4)
subway.add_connection(c11, c12, 3)
subway.add_connection(c12, c13, 3)
subway.add_connection(c13, a10, 3)
subway.add_connection(a10, c14, 2)
subway.add_connection(c14, c15, 2)
subway.add_connection(c15, c16, 2)
subway.add_connection(c16, c17, 3)
subway.add_connection(c17, c18, 3)
subway.add_connection(c18, c19, 2)
subway.add_connection(c19, c20, 2)
subway.add_connection(c20, c21, 2)
subway.add_connection(c21, c22, 2)
subway.add_connection(c22, c23, 4)
subway.add_connection(c23, c24, 5)
subway.add_connection(d1, d2, 2)
subway.add_connection(d2, d3, 3)
subway.add_connection(d3, d4, 2)
subway.add_connection(d4, d5, 2)
subway.add_connection(d5, d6, 2)
subway.add_connection(d6, b4, 3)
subway.add_connection(b4, d7, 2)
subway.add_connection(d7, d8, 2)
subway.add_connection(d8, c10, 3)
subway.add_connection(c10, d9, 3)
subway.add_connection(d9, a14, 2)
subway.add_connection(a14, b11, 3)
subway.add_connection(b11, d10, 3)
subway.add_connection(d10, d11, 2)
subway.add_connection(d11, d12, 2)
subway.add_connection(d12, d13, 2)
subway.add_connection(d13, d14, 2)
subway.add_connection(d14, d15, 2)
subway.add_connection(d3, ds1, 2)
subway.add_connection(ds1, ds2, 2)
subway.add_connection(e1, e2, 5)
subway.add_connection(e2, e3, 6)
subway.add_connection(e3, e4, 7)
subway.add_connection(e4, e5, 4)
subway.add_connection(e5, e6, 12)
subway.add_connection(e6, e7, 6)
subway.add_connection(e7, e8, 6)
subway.add_connection(e8, e9, 5)
subway.add_connection(e9, d1, 4)
subway.add_connection(d1, b1, 6)

subway.add_connection(ew1, e1, 40)

subway.add_connection(b12, d10, 2)
subway.add_connection(d10, fe1, 2)
subway.add_connection(fe1, fe2, 4)
subway.add_connection(fe2, fe3, 2)
subway.add_connection(fe3, fe4, 3)
subway.add_connection(fe4, fe5, 5)

subway.add_connection(fw1, fw2, 1)
subway.add_connection(fw2, fw3, 2)
subway.add_connection(fw3, fw4, 2)
subway.add_connection(fw4, fw5, 2)
subway.add_connection(fw5, fw6, 6)
subway.add_connection(g1, g2, 2)
subway.add_connection(g2, g3, 3)
subway.add_connection(g3, fw6, 2)
subway.add_connection(fw6, g4, 3)
subway.add_connection(g4, d7, 2)
subway.add_connection(d7, b5, 2)
subway.add_connection(b5, g5, 2)
subway.add_connection(g5, g6, 2)
subway.add_connection(g6, g7, 2)
subway.add_connection(g7, g8, 2)
subway.add_connection(g8, c8, 2)
subway.add_connection(c8, a19, 3)
subway.add_connection(a19, g9, 2)
subway.add_connection(g9, g10, 2)
subway.add_connection(g10, g11, 2)
subway.add_connection(g11, g12, 3)
subway.add_connection(g12, g13, 3)
subway.add_connection(g13, g14, 3)













