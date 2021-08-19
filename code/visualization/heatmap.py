#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json
import pandas as pd
import numpy as np
import plotly.express as px
import folium


# In[13]:


import webbrowser


# In[14]:


import plotly.io as pio
pio.renderers.default = 'png'


# In[15]:


#인도 주 json파일
india_states = json.load(open(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\states_india.geojson"))
india_states['features'][0].keys()
india_states['features'][7]['properties']


# In[16]:


#딕셔너리 형태의 주 이름:코드번호
state_id_map ={}

for feature in india_states['features']:
    feature['id'] = feature['properties']['state_code']
    state_id_map[feature['properties']['st_nm']] = feature['id']


# In[17]:


state_id_map


# In[18]:


india_states['features'][1]['properties']
state_id_map.keys()
state_id_map.values()


# In[48]:


import collections

#csv data  _clinic
clinic_final = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\GeocodingData\merge\Clinic_final2.csv")

clinic_final= collections.Counter(clinic_final['State'])
clinic_final = pd.DataFrame(list(clinic_final.items()), columns=['State','No'])
print(clinic_final)

clinic_final['State'][0] = 'Arunanchal Pradesh'
clinic_final['State'][9] = 'NCT of Delhi'
clinic_final['State'][12] = 'Jammu & Kashmir'

clinic_final['id'] = clinic_final['State'].apply(lambda x: state_id_map[x])
clinic_final

# clinic_final= collections.Counter(clinic_final['State'])
# clinic_final = pd.DataFrame(list(clinic_final.items()), columns=['State','No'])
# clinic_final
# clinic_final['State'][1] = 'Arunanchal Pradesh'

# clinic_final['State'][4] = 'NCT of Delhi'
# clinic_final['State'][9] = 'Jammu & Kashmir'
# clinic_final


# In[67]:


import collections

#csv data  _clinic
hospital_final = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\GeocodingData\merge\Hospital_final2.csv")

hospital_final= collections.Counter(hospital_final['State'])
hospital_final = pd.DataFrame(list(hospital_final.items()), columns=['State','No'])
print(hospital_final)

hospital_final['State'][0] = 'Arunanchal Pradesh'
hospital_final['State'][9] = 'NCT of Delhi'
hospital_final['State'][12] = 'Jammu & Kashmir'

hospital_final['id'] = hospital_final['State'].apply(lambda x: state_id_map[x])



hospital_final


# In[62]:


hospital_final = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\GeocodingData\merge\Hospital_final2.csv")

hospital_final= collections.Counter(hospital_final['State'])
hospital_final = pd.DataFrame(list(hospital_final.items()), columns=['State','No'])
print(hospital_final)

hospital_final['State'][0] = 'Arunanchal Pradesh'
hospital_final['State'][9] = 'NCT of Delhi'
hospital_final['State'][12] = 'Jammu & Kashmir'

hospital_final['id'] = hospital_final['State'].apply(lambda x: state_id_map[x])
hospital_final


# In[44]:


import collections

fitness_final = pd.read_csv(r"C:\Users\Lenovo\PycharmProjects\new_cleansing\resource\GeocodingData\merge\Fitness_final2.csv")

fitness_final= collections.Counter(fitness_final['State'])
fitness_final = pd.DataFrame(list(fitness_final.items()), columns=['State','No'])
print(fitness_final)

fitness_final['State'][0] = 'Arunanchal Pradesh'
fitness_final['State'][9] = 'NCT of Delhi'
fitness_final['State'][12] = 'Jammu & Kashmir'

fitness_final['id'] = fitness_final['State'].apply(lambda x: state_id_map[x])
fitness_final


# In[ ]:





# In[49]:


#plotly clinic
fig = px.choropleth(clinic_final, locations = 'id' , geojson=india_states, color= 'No', scope='asia', title = '지역별 clinic 기관 밀도' )
fig.update_geos(fitbounds='locations', visible = False)
fig.show()


# In[68]:


#plotly hospital
fig = px.choropleth(hospital_final, locations = 'id' , geojson=india_states, color= 'No', scope='asia', title = '지역별 hospital 기관 밀도' )
fig.update_geos(fitbounds='locations', visible = False)
fig.show()


# In[45]:


#plotly fitness
fig = px.choropleth(fitness_final, locations = 'id' , geojson=india_states, color= 'No', scope='asia', title = '지역별 fitness 기관 밀도' )
fig.update_geos(fitbounds='locations', visible = False)
fig.show()

