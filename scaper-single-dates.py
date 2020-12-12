import twint
import argparse

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

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query', type=str, required=True)
parser.add_argument('-s', '--start', type=str)
parser.add_argument('-e', '--end', type=str)

args = parser.parse_args()
print(f'Start : {args.start}, End : {args.end}\n')
print(f'Launching the querry for {args.query}\n\n')

if args.start:
    start_date = args.start
else:
    start_date = '2012-01-01'
    
if args.end:
    end_date = args.end
else:
    end_date = '2014-09-01'

config = twint.Config()
# config.Search = search_term
# config.Limit = 100
config.Hide_output = False
config.Lang = "en"
config.Since = start_date
config.Until = end_date
config.Store_csv = True
config.Search = args.query
config.Output = "_".join([args.query, start_date, end_date, 'Basile']) + ".csv"
# make search
twint.run.Search(config)

