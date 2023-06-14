# -*- coding: utf-8 -*-
pip install bardapi>=0.1.8
# simple usage
import bardapi
from bardapi import Bard
import os
## set your __Secure-1PSID value to key
token='YOUR-SECURE-1PSID-HERE'
input_text = "Hello Bard!"
response = bardapi.core.Bard(token).get_answer(input_text)['content']
print(response)
