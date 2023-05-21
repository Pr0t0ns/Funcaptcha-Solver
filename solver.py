import tls_client, random, urllib, time, requests, os, json
import speech_recognition as sr
from bda import get_bda as bda

# MADE BY Pr0t0n
# AUDIO replacement dict taken from useragents


class Funcap:

  def __init__(self,
               host: str = 'https://client-demo.arkoselabs.com',
               site_key: str = "029EF0D3-41DE-03E1-6971-466539B47725", ua: str="Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
               proxy: str = None, retries: int=5):
    self.host = host
    self.site_key = site_key
    self.ua = ua
    self.uav = self.ua.split("Chrome/")[1].split(".")[0]
    self.rnd = random.uniform(0.21263337817840222, 0.31263337817840222)
    self.session = tls_client.Session(client_identifier=f"chrome_{self.uav}",
                                      random_tls_extension_order=True)
    if proxy != None:
      self.session.proxies = {
        'https': f'http://{proxy}',
        'http': f'http://{proxy}'
      }
    self.bda = bda(self.ua)
    self.attempts = 0
    self.retries = retries
  def skey_request(self):
    try:
      url = f'https://client-api.arkoselabs.com/fc/gt2/public_key/{self.site_key}'
  
      self.session.headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': self.host,
        'referer': self.host,
        'sec-ch-ua':
        f'"Google Chrome";v="{self.uav}", "Chromium";v="{self.uav}", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Chrome OS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': self.ua
      }
      
      payload = f'bda={urllib.parse.quote(self.bda, safe="")}&public_key={self.site_key}&site={urllib.parse.quote(self.host,safe="")}&userbrowser={urllib.parse.quote(self.ua, safe="")}&rnd={self.rnd}'
      response = self.session.post(url, data=payload)
      self.session.cookies = response.cookies
      print("[DEBUG]: Fetched Challenge Token")
      return response.json()['token']
    except:
      self.attempts += 1
      return self.solve()
  def log(self):
    try:
      url = 'https://client-api.arkoselabs.com/fc/a/'
  
      self.session.headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'cache-control': 'no-cache',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'origin': self.host,
          'referer': self.host,
          'sec-ch-ua': f'"Google Chrome";v="{self.uav}", "Chromium";v="{self.uav}", "Not-A.Brand";v="24"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Chrome OS"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': self.ua
      }
      data = f"sid={self.region}&session_token={self.token}&render_type=canvas&category=Site+URL&action={urllib.parse.quote(self.host, safe='')}F&analytics_tier={self.at}"
      self.session.post(url, data=data)
      print("[DEBUG]: Logged Site Session")
      return
    except:
      self.attempts += 1
      return self.solve()


  def get_challenge(self):
    try:
      url = 'https://client-api.arkoselabs.com/fc/gfct/'
  
      data = f"token={self.token}&sid={self.region}&lang=&render_type=canvas&analytics_tier={self.at}&data%5Bstatus%5D=init"
  
      response = self.session.post(url, data=data).json()
      self.challenge_id = response['challengeID']
      print("[DEBUG]: Requested Picture Challenge")
      return
    except:
      self.attempts += 1 
      return self.solve()

  def get_audio_challenge(self):
      try:
        url = f'https://client-api.arkoselabs.com/fc/get_audio/?session_token={self.token}&analytics_tier={self.at}&r={self.region}&game=0&language=en'
        print("[DEBUG]: Fetched Audio Challenge")
        return self.session.get(url).headers['Location']
      except:
        self.attempts += 1 
        return self.solve()
    
  def game_loaded(self):
    try:
      url = "https://client-api.arkoselabs.com/fc/a/"
  
      data = f'sid={self.region}&game_token={self.challenge_id}&session_token={self.token}&game_type=1&render_type=canvas&category=loaded&action=game+loaded&analytics_tier={self.at}'
  
      self.session.post(url, data=data)
      print("[DEBUG]: Logged Canvas Loaded")
      return
    except:
      self.attempts += 1
      return self.solve()
  
  def switch_audio(self):
    try:
      url = 'https://client-api.arkoselabs.com/fc/a/'
  
      data = f"sid={self.region}&game_token={self.challenge_id}&session_token={self.token}&game_type=1&render_type=canvas&category=audio+captcha&action=user+clicked+audio&label=swapped+to+audio+captcha&analytics_tier={self.at}"
      self.session.post(url, data=data)
      print("[DEBUG]: Switched to Audio")
      return
    except:
      self.attempts += 1
      return self.solve()

  def download_challenge(self):
    try:
      response = requests.get(self.challenge).content
      with open(f"{os.getcwd()}/challenges/{self.challenge_id}.wav", "wb") as f:
        f.write(response)
      print(f"[DEBUG]: Downloaded Challenge --> ({self.challenge_id}.wav)")
      return
    except:
      self.attempts += 1 
      return self.solve()
    
  def replace_resp(self, resp: str): 
        resp = resp.lower() 
        replacements = {
            "one": "1",
            "to": "2",
            "two": "2",
            "tree": "3",
            "three": "3",
            "four": "4",
            "for": "4",
            "or": "4",
            "zero": "0",
            "do": "5",
            "right": "5",
            "hero": "4",
            "five": "5",
            "six": "6",
            "nine": "9",
            "white": "1",
            "whine": "1",
            "dial": "69",
            "wine": "1",
            "guys": "9",
            "sides": "9",
            "store": "44",
            "door": "04",
            "side": "9",
            "buy": "55",
            "rightly": "53",
            "rightfully": "53",
            "lee": "53",
            "now": "9",
            "eight": "8",
            "soon": "2",
            "wireless": "8",
            "find": "5",
            "rise": "1",
            "italy": "34",
            "ice": "0",
            "lights": "9",
            "light": "9",
            "sites": "9",
            "pwell": "9",
            "well": "9",
            "size": "9",
            "by": "1",
            "knights": "9",
            "knight": "9",
            "nights": "9",
            "night": "9",
            "-": "",
            " ": "",
            "r": "9",
            "l": "2",
            "a": "4"
        }
        for key in replacements:
            if key in resp:
                resp = resp.replace(key, replacements[key])
        return resp
      
  def solve_audio_challenge(self):
    try:
      path = f"{os.getcwd()}/challenges/{self.challenge_id}.wav"
      try:
          possible_solutions = []
          reformed_solutions = []
          r = sr.Recognizer()
          with sr.WavFile(path) as s:
              #r.adjust_for_ambient_noise(s)
              audio = r.record(s)
              response = r.recognize_google(audio, show_all=True)
              for transcript in response["alternative"]:
                transcript = transcript['transcript']
                resp = self.replace_resp(transcript)
                possible_solutions.append(resp)
              for solution in possible_solutions:
                reform_solution = ""
                for digit in solution:
                  try:
                    digit = int(digit)
                    reform_solution += str(digit)
                  except:
                    pass
                if len(reform_solution) < 4:
                  pass
                else:
                  reformed_solutions.append(reform_solution)
              if len(reformed_solutions) == 0:
                self.attempts += 1
                return self.solve()
              reformed_solutions.sort(key=len)
              return reformed_solutions[len(reformed_solutions) - 1]
      except LookupError:
              pass
    except:
      self.attempts += 1
      return self.solve()
  
  def sumbit_answer(self):
    try:
      url = 'https://client-api.arkoselabs.com/fc/audio/'
  
      data = f'r={self.region}&session_token={self.token}&response={self.solution}&analytics_tier={self.at}&audio_type=2&language=en&bio='
  
      response = self.session.post(url, data=data).json()['response']
      if response == "correct":
        print("[SOLVED]: Solved Captcha")
        return
      elif response == "incorrect":
        print("[INCORRECT]: Captcha Solved Incorrectly!")
        self.attempts += 1
      else:
        print("[FAILED]: Unexpected Error Sumbitting Captcha Solution")
        self.attempts += 1
      if self.retries == self.attempts:
        self.token = None
        return
      return self.solve()
    except:
      self.attempts += 1
      return self.solve()
  
  def solve(self):
    if self.retries == self.attempts:
        return None
    print(f"[DEBUG]: Attempt #{self.attempts + 1}")
    token = self.skey_request()
    self.origin_token = token
    parsed_token = token.split("|")
    try:
      self.token = parsed_token[0]
      self.region = parsed_token[1].split("=")[1]
      self.meta = parsed_token[2].split("=")[1]
      self.at = parsed_token[7].split("=")[1]
      self.atp = parsed_token[8].split("=")[1]
    except:
      pass
    self.log()
    self.get_challenge()
    self.game_loaded()
    self.switch_audio()
    self.challenge = self.get_audio_challenge()
    self.download_challenge()
    self.solve_audio_challenge()
    self.solution = self.solve_audio_challenge()
    print(f"[ANSWER]: Possible Answer --> ({self.solution})")
    self.sumbit_answer()
    if self.token != None:
      return token
    else:
      return None
if __name__ == "__main__":
  token = Funcap().solve()
  print(token)
