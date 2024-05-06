from sec_api import RenderApi 
from sec_api import QueryApi
import pandas as pd
import numpy as np
import csv
import sqlite3
from sec_api import XbrlApi
from sec_api import ExtractorApi

extractorApi = ExtractorApi("d26ded3e0bab10bba3857deaf9a482e6e497e258fd6b4f40096defb753e5e9de")

#
# 10-K example
#
# Tesla 10-K filing
filing_url_10k = "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"

# get the standardized and cleaned text of section 1A "Risk Factors"
# section1A_text = extractorApi.get_section(filing_url_10k, "1A", "text")
# print(section1A_text)

# section6_text = extractorApi.get_section(filing_url_10k, "6", "text")
# print(section6_text)

section8_text = extractorApi.get_section(filing_url_10k, "8", "text")  


from sec_api import RenderApi

renderApi = RenderApi(api_key="d26ded3e0bab10bba3857deaf9a482e6e497e258fd6b4f40096defb753e5e9de")

url = "https://www.sec.gov/Archives/edgar/data/1662684/000110465921082303/tm2119986d1_8k.htm"

filing = renderApi.get_filing(url)

print(filing)