from random import randint

def proxy():

	p1 = "185.53.179.29:80" #netherlands
        p2 = "162.255.119.250:80" #US
	p3 = "193.111.63.208:80" #netherlands
      	p4 = "104.28.20.2:80" #US
	p5 = "62.210.105.242:80" #FR
	p6 = "162.255.119.250:80" #US
	p7 = "103.224.212.222:80" #UK
	p8 = "104.28.20.2:80" #US
	p9 = "93.191.169.211:80" #UK
	p10 = "69.64.147.10:80" #US
	p11 = "62.149.128.160:80" #netherlands
	p12 = "46.4.207.219:80" #FR

	proxys = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
	randproxy = proxys[randint(0,11)]
	return randproxy
