import twint
from tqdm import tqdm

searches = ["abu sayyaf" ,
 "afghanistan" ,
 "agro" ,
 "al-qaeda" ,
 "al-qaeda in the arabian peninsula" ,
 "al-qaeda in the islamic maghreb" ,
 "al-shabaab" ,
 "ammonium nitrate" ,
 "attack" ,
 "biological weapon" ,
 "car bomb" ,
 "chemical weapon" ,
 "conventional weapon" ,
 "dirty bomb" ,
 "eco-terrorism" ,
 "environmental terrorism" ,
 "euskadi ta askatasuna" ,
 "extremism" ,
 "farc" ,
 "fundamentalism" ,
 "hamas" ,
 "hezbollah" ,
 "improvised explosive device" ,
 "iran" ,
 "iraq" ,
 "irish republican army" ,
 "islamist" ,
 "jihad" ,
 "nationalism" ,
 "nigeria" ,
 "nuclear" ,
 "nuclear enrichment" ,
 "pakistan" ,
 "palestine liberation front" ,
 "pirates" ,
 "plo" ,
 "political radicalism" ,
 "recruitment" ,
 "somalia" ,
 "suicide attack" ,
 "suicide bomber" ,
 "taliban" ,
 "tamil tigers" ,
 "tehrik-i-taliban pakistan" ,
 "terror" ,
 "terrorism" ,
 "weapons-grade" ,
 "yemen"]


start_date = '2012-01-01'
end_date = '2014-09-01'
search_term = 'Trump'

config = twint.Config()
# config.Search = search_term
# config.Limit = 100
config.Hide_output = True
config.Lang = "en"
config.Since = start_date
config.Until = end_date
config.Store_csv = True
config.Output = "_".join([search_term, start_date, end_date, 'Basile']) + ".csv"

for search in searches[1:]:
    print(f'Search : {search} ------------------------------')
    config.Search = search
    config.Output = "_".join([search, start_date, end_date, 'Basile']) + ".csv"
    # make search
    twint.run.Search(config)
