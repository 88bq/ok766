import requests
from time import sleep
r1 = requests.session()

username = 'just.akoky'
password = 'koky200'
login_url = 'https://www.instagram.com/accounts/login/ajax/'
login_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '318',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'mid=YvPCiQALAAEWSeJvmuuZSGIAQMVH; ig_did=01D115A7-9D0E-4315-ACEF-F76B63093F98; ig_nrcb=1; shbid="949\05449740966681\0541691678257:01f7581447096928500d0e9b5a6c1dcccc0f9e4a76cbde2d2f3a4d5800a55bd89d467f7e"; shbts="1660142257\05449740966681\0541691678257:01f79ef02b5960fa5beb33182ab76070805358ed55f610a7c007de2826ff1eee77aff1dc"; datr=v8LzYnWkegYf9MUDzVDUWrhh; rur="LDC\05417132276117\0541691703540:01f7488c3b8a6f9ef9566fc5dbd229f37860858c877328c1eb54cd03e597bc73d74ce10f"; csrftoken=4BVetVtNHFFGviwKDWic49N22ffQqrXO',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'viewport-width': '748',
    'x-asbd-id': '198387',
    'x-csrftoken': '4BVetVtNHFFGviwKDWic49N22ffQqrXO',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR02oyqqBMyUuLzwVFw_fgnaWAjVsm3aAbOx1sTkKRyYbus9',
    'x-instagram-ajax': '730e073623b1',
    'x-requested-with': 'XMLHttpRequest',}
login_data = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
#login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
sis = "login_to_acc.cookies['sessionid']"
#print(sis)

username = 'p_cr_'
password = 'qqqq1111'

login_url = 'https://www.instagram.com/accounts/login/ajax/'
login_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '324',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=78139217-AA45-4BD2-B5F6-B09B643AA161; mid=YFYfPwALAAFGM1cFn3DQChknqi81; fbm_124024574287414=base_domain=.instagram.com; datr=7WCEYUXxlPyOzXWEzNFbWqNL; ig_nrcb=1; shbid="986\05440585259262\0541680820500:01f749ffe21087158bf9674c72ed668547e1bd1757bb57804eedf707f4e647bd5f23bd0d"; shbts="1649284500\05440585259262\0541680820500:01f70fb1ee5cae92fbc69351084d7b342e7b9525c6d27e5057482dd7e9cb0b508176cb30"; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ; rur="CLN\05440585259262\0541680833423:01f7a23eb734d0c2bf17ae7ee4a809032f3307aee5afece51cf27676da17b66732e09d3b"; csrftoken=P0z6titFtjFSxzo1MwFkWmECGmRKGu3m; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'P0z6titFtjFSxzo1MwFkWmECGmRKGu3m',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3MPcSpz49Ovxjy7OsqBmH0zrFcdFnDJvygH0Y7st6HewA-',
    'x-instagram-ajax': '780586326a8f',
    'x-requested-with': 'XMLHttpRequest',
}
login_data = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
#login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
sis4 = '491278312%3AxhllmCqQz6Mj1O%3A3%3AAYc1CB4c3Rnn1oN29jtb755577465_2ZJ4dTUClGxQ'
print(sis4)

username = 'cv30.zp'
password = 'ahmedcan'

login_url = 'https://www.instagram.com/accounts/login/ajax/'
login_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '324',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=78139217-AA45-4BD2-B5F6-B09B643AA161; mid=YFYfPwALAAFGM1cFn3DQChknqi81; fbm_124024574287414=base_domain=.instagram.com; datr=7WCEYUXxlPyOzXWEzNFbWqNL; ig_nrcb=1; shbid="986\05440585259262\0541680820500:01f749ffe21087158bf9674c72ed668547e1bd1757bb57804eedf707f4e647bd5f23bd0d"; shbts="1649284500\05440585259262\0541680820500:01f70fb1ee5cae92fbc69351084d7b342e7b9525c6d27e5057482dd7e9cb0b508176cb30"; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ; rur="CLN\05440585259262\0541680833423:01f7a23eb734d0c2bf17ae7ee4a809032f3307aee5afece51cf27676da17b66732e09d3b"; csrftoken=P0z6titFtjFSxzo1MwFkWmECGmRKGu3m; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'P0z6titFtjFSxzo1MwFkWmECGmRKGu3m',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3MPcSpz49Ovxjy7OsqBmH0zrFcdFnDJvygH0Y7st6HewA-',
    'x-instagram-ajax': '780586326a8f',
    'x-requested-with': 'XMLHttpRequest',
}
login_data = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
sis3 = 'login_to_acc'

username = 'cw.bc_'
password = '07708142135ss'

login_url = 'https://www.instagram.com/accounts/login/ajax/'
login_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '324',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=78139217-AA45-4BD2-B5F6-B09B643AA161; mid=YFYfPwALAAFGM1cFn3DQChknqi81; fbm_124024574287414=base_domain=.instagram.com; datr=7WCEYUXxlPyOzXWEzNFbWqNL; ig_nrcb=1; shbid="986\05440585259262\0541680820500:01f749ffe21087158bf9674c72ed668547e1bd1757bb57804eedf707f4e647bd5f23bd0d"; shbts="1649284500\05440585259262\0541680820500:01f70fb1ee5cae92fbc69351084d7b342e7b9525c6d27e5057482dd7e9cb0b508176cb30"; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ; rur="CLN\05440585259262\0541680833423:01f7a23eb734d0c2bf17ae7ee4a809032f3307aee5afece51cf27676da17b66732e09d3b"; csrftoken=P0z6titFtjFSxzo1MwFkWmECGmRKGu3m; fbsr_124024574287414=qApR9SAnVwsms5w22xIRjmRsLveFZ4siDeMvtNEoyXM.eyJ1c2VyX2lkIjoiMTAwMDY1NDQ0MzUyNzgyIiwiY29kZSI6IkFRQll2RndwVWpuNDNvQnNGTjFGZHFpQkY3dWdpWVo4Q3hyTlJZdGVuaTlyV1YyTUR1VzVwMmFPcEJPZmk5SG12TkpEbWI0M0pDUUFHSTNHRXVXekdqZGM0Um1iVExJR1BUMDBLVndQd0Q3ZE16eGR0Z1RydVlnc19PTmYtSllzQVNueDJaSlNQR0R3Q3VYNjdIMnl3a0dkZEJ2a3U4cUJPSXREYjVQdklxcVVlYmR5aWZQbHlrVldCVFVnVGV0T0dIQXNPV1dzOFRDOFFNZHA4ZWxtbGwyRW1NZ2VadnRMUW5pODU2SWh3MG8xaWtEUHhQUWFMdjFRZ00yc3ZXMy0wREhkdGdQT1ZuNjlLeHAydjJmTkJScVFCS1k5ZEJ4a2kzaWExZU5MSzMwRks4cG9IY1Nnc3k5U2RQX2htVVBJTU5vbFBCbndGSC1zY3lSQ2s4UXQ1NFRsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFBWHJXMXFDc0pCcVpBYzZCWXU3S3I3c1pDMW5yY1BaQXJ0Q2JaQTNaQnRGV2RDVFNWbTVvOWx2WWZvNlBER0RWVGFwWXFBdkRaQXUyc0d1ZkNVMVpBSG9PMHRXcnU1QlpBR0VLcHVKbFpDT01DQ2VreWNCSkZaQ3ZjMmFDSFdMaUVsNGIxdHYydU9obDJoWTFBQkd4Snl3djFXNEpBRUtuYlN1UmpjOE02cEdsc25KSFg1dmlCTnNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQ5Mjk3NDIyfQ',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'x-asbd-id': '198387',
    'x-csrftoken': 'P0z6titFtjFSxzo1MwFkWmECGmRKGu3m',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3MPcSpz49Ovxjy7OsqBmH0zrFcdFnDJvygH0Y7st6HewA-',
    'x-instagram-ajax': '780586326a8f',
    'x-requested-with': 'XMLHttpRequest',
}
login_data = {
    'username': f'{username}',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)
sis2 = 'login_to_acc.'


def edit(msg, msgid):
    r1.get(f'https://api.telegram.org/bot5104020480:AAFjvjRzZGLgRZ0vaOwsJu-ramNiuZs1KRI/editMessageText?chat_id=1382680308&text=%{msg}&message_id={msgid}')


x = r1.get(
        f'https://api.telegram.org/bot5104020480:AAFjvjRzZGLgRZ0vaOwsJu-ramNiuZs1KRI/sendMessage?chat_id=1382680308&text=Bot Working Now ....').json()[
        'result']['message_id']
w = 1
f = 0
unf = 0
while True:
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'mid=YvPCiQALAAEWSeJvmuuZSGIAQMVH; ig_did=01D115A7-9D0E-4315-ACEF-F76B63093F98; ig_nrcb=1; datr=v8LzYnWkegYf9MUDzVDUWrhh; shbid="6103\054542435544\0541692247115:01f7e84a7402214adafcb477c48104000e282f4463439aadab55a2a4888527fb62650400"; shbts="1660711115\054542435544\0541692247115:01f70ac54c96500c43e98fbc2678e7abb7cee9ce9b107f269cc2a765c9b05d7f79f7e4d9"; csrftoken=RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn; ds_user_id=44024702280; sessionid={sis}; rur="RVA\05444024702280\0541692394506:01f7ddcce74f6340f16267746cf06acb43726d91689bb80e9a890e77423bf9efaec51b04"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/sollaf5/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'viewport-width': '705',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR02oyqqBMyUuLzwVFw_fgnaWAjVsm3aAbOx1sTkKRyYbvvt',
        'x-instagram-ajax': '1006052345',
        'x-requested-with': 'XMLHttpRequest',
    }
    headers2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'mid=YvPCiQALAAEWSeJvmuuZSGIAQMVH; ig_did=01D115A7-9D0E-4315-ACEF-F76B63093F98; ig_nrcb=1; datr=v8LzYnWkegYf9MUDzVDUWrhh; shbid="6103\054542435544\0541692247115:01f7e84a7402214adafcb477c48104000e282f4463439aadab55a2a4888527fb62650400"; shbts="1660711115\054542435544\0541692247115:01f70ac54c96500c43e98fbc2678e7abb7cee9ce9b107f269cc2a765c9b05d7f79f7e4d9"; csrftoken=RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn; ds_user_id=44024702280; sessionid={sis2}; rur="RVA\05444024702280\0541692394506:01f7ddcce74f6340f16267746cf06acb43726d91689bb80e9a890e77423bf9efaec51b04"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/sollaf5/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'viewport-width': '705',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR02oyqqBMyUuLzwVFw_fgnaWAjVsm3aAbOx1sTkKRyYbvvt',
        'x-instagram-ajax': '1006052345',
        'x-requested-with': 'XMLHttpRequest',
    }
    headers3 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'mid=YvPCiQALAAEWSeJvmuuZSGIAQMVH; ig_did=01D115A7-9D0E-4315-ACEF-F76B63093F98; ig_nrcb=1; datr=v8LzYnWkegYf9MUDzVDUWrhh; shbid="6103\054542435544\0541692247115:01f7e84a7402214adafcb477c48104000e282f4463439aadab55a2a4888527fb62650400"; shbts="1660711115\054542435544\0541692247115:01f70ac54c96500c43e98fbc2678e7abb7cee9ce9b107f269cc2a765c9b05d7f79f7e4d9"; csrftoken=RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn; ds_user_id=44024702280; sessionid={sis3}; rur="RVA\05444024702280\0541692394506:01f7ddcce74f6340f16267746cf06acb43726d91689bb80e9a890e77423bf9efaec51b04"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/sollaf5/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'viewport-width': '705',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR02oyqqBMyUuLzwVFw_fgnaWAjVsm3aAbOx1sTkKRyYbvvt',
        'x-instagram-ajax': '1006052345',
        'x-requested-with': 'XMLHttpRequest',
    }
    headers4 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': f'mid=YvPCiQALAAEWSeJvmuuZSGIAQMVH; ig_did=01D115A7-9D0E-4315-ACEF-F76B63093F98; ig_nrcb=1; datr=v8LzYnWkegYf9MUDzVDUWrhh; shbid="6103\054542435544\0541692247115:01f7e84a7402214adafcb477c48104000e282f4463439aadab55a2a4888527fb62650400"; shbts="1660711115\054542435544\0541692247115:01f70ac54c96500c43e98fbc2678e7abb7cee9ce9b107f269cc2a765c9b05d7f79f7e4d9"; csrftoken=RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn; ds_user_id=44024702280; sessionid={sis4}; rur="RVA\05444024702280\0541692394506:01f7ddcce74f6340f16267746cf06acb43726d91689bb80e9a890e77423bf9efaec51b04"',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/sollaf5/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'viewport-width': '705',
        'x-asbd-id': '198387',
        'x-csrftoken': 'RwfmNGKm2lb1H5nQrq0bikMrEvU0ChQn',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR02oyqqBMyUuLzwVFw_fgnaWAjVsm3aAbOx1sTkKRyYbvvt',
        'x-instagram-ajax': '1006052345',
        'x-requested-with': 'XMLHttpRequest',
    }


    try:
        #########################################story
        url = 'https://www.instagram.com/web/friendships/1782581874/follow/'
        print(r1.post(url, headers=headers).text)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
        url = 'https://www.instagram.com/web/friendships/1782581874/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
        url = 'https://www.instagram.com/web/friendships/1093863445/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
        url = 'https://www.instagram.com/web/friendships/311258768/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/1399429282/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)
        sleep(35)

        url = 'https://www.instagram.com/web/friendships/407474340/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/7709124619/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/1782327804/follow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        f += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
    except:
        pass
    z = 0
    while z < 2000:
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}
Time => {z}''', x)
        sleep(1)
        z += 1

    try:
        #########################################story
        url = 'https://www.instagram.com/web/friendships/1782327804/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/7709124619/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/407474340/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/309511113/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/1782581874/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/1093863445/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
        url = 'https://www.instagram.com/web/friendships/311258768/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)

        url = 'https://www.instagram.com/web/friendships/1399429282/unfollow/'
        r1.post(url, headers=headers)
        #r1.post(url, headers=headers2)
        #r1.post(url, headers=headers3)
        r1.post(url, headers=headers4)
        unf += 1
        edit(f'''Follo = {f}
Unfollo => {unf}
Cycle => {w}''', x)

        sleep(35)
    except:
        pass
    w += 1

