import twint
from tqdm import tqdm

searches = [
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
 "suicide attack" ,
 "terrorism"]


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

for search in tqdm(searches):
    print(f'Search : {search} ------------------------------')
    config.Search = search
    config.Output = "_".join([search, start_date, end_date, 'Basile']) + ".csv"
    # make search
    twint.run.Search(config)

print('--------------finished-------------')
