import matplotlib.colors as mcol
import matplotlib.cm as cm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#%matplotlib notebook


gdp = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_9984786.csv',skiprows=4)
life_expectancy = pd.read_csv("API_SP.DYN.LE00.IN_DS2_en_csv_v2_9984885.csv",skiprows=4)
population = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_9984924.csv',skiprows=4)
pop_densety = pd.read_csv('API_EN.POP.DNST_DS2_en_csv_v2_9987064.csv',skiprows=4)
industry_pres = pd.read_csv('API_NV.IND.TOTL.ZS_DS2_en_csv_v2_9988031.csv',skiprows=4)


gdp=gdp.set_index('Country Name')
life_expectancy = life_expectancy.set_index('Country Name')
population = population.set_index('Country Name')
pop_densety=pop_densety.set_index('Country Name')
industry_pres = industry_pres.set_index('Country Name')


gdp['gdp']=gdp['2016']
life_expectancy['life_expectancy']=life_expectancy['2016']
pop_densety['pop_densety']=pop_densety['2016']
industry_pres['industry_pres'] = industry_pres['2016']


population = population['2016']
gdp=gdp['gdp']
life_expectancy=life_expectancy['life_expectancy']
pop_densety=pop_densety['pop_densety']
industry_pres = industry_pres['industry_pres']


gdp_per_perspn = gdp/population
gdp_per_perspn = gdp_per_perspn.dropna()
data=pd.DataFrame([gdp_per_perspn,life_expectancy,pop_densety,industry_pres],index=['gdp_per_capita','life_expectancy','pop_densety','industry_pres']).transpose().dropna()


'''print(gdp.shape)
print(life_expectancy.shape)
print(population.shape)
print(gdp_per_perspn)
#data=data[data['2016'] < data['2016'].max()]
print((data.shape))'''
print((data).loc['China'])

fig = plt.figure(figsize=[7,5])
cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b", "green", "red"])
cpick = cm.ScalarMappable(cmap=cm1)
cpick.set_array([])
cpick.to_rgba(data['industry_pres'])

sc = plt.scatter(data['life_expectancy'],data['gdp_per_capita'],s=data['pop_densety']/5,alpha=.7,c=data['industry_pres'],cmap=cm1)
#plt.axes([data['life_expectancy'].min(),data['life_expectancy'].max(),data['gdp_per_capita'].min(),data['gdp_per_capita'].max()])
#plt.axes([1,2,3,4])
cbar = plt.colorbar(ticks=[0, 20, 40, 60, 80, 100])
cbar.ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
plt.yticks(np.arange(data['gdp_per_capita'].min(),data['gdp_per_capita'].max(),10000))
plt.xticks(np.arange(55,95,5))
'''fig=sns.jointplot(data['life_expectancy'],data['2016'])
fig.ax_marg_y.set_yticks(np.arange(5000,100000,5000))'''
plt.xlabel('life_expectancy (years)')
plt.ylabel('GDP per capita (usd $)')
plt.title('relation between GDP per capita and life expectancy and population\ndensity as a size of bubble and industry percentage of GDP in color\n(each bubble represent a country)')
plt.show()

# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
#Population density (people per sq. km of land area)