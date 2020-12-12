# How to scrape :

Scrape only one keyword : `python3 scaper-single.py -q "keyword"`

```
keep_columns = ['id',
 'conversation_id',
 'created_at',
 'date',
 'time',
 'user_id',
 'username',
 'name',
 'tweet',
 'language',
 'mentions',
 'urls',
 'photos',
 'replies_count',
 'retweets_count',
 'likes_count',
 'hashtags',
 'link',
 'retweet',
 'video',
 'thumbnail',
 'reply_to']
 
 defined_types = {'id': 'int64',
 'conversation_id': 'int64',
 'date': 'str',
 'time': 'str',
 'user_id': 'int64',
 'username': 'str',
 'name': 'str',
 'tweet': 'str',
 'language': 'category',
 'mentions': 'str', # maybe get rid of
 'urls': 'str',
 'photos': 'str',
 'replies_count': 'int64',
 'retweets_count': 'int64',
 'likes_count': 'int64',
 'hashtags': 'str',
 'link': 'str',
 'retweet': 'bool', # is it a retweet ?
 'video': 'bool',
 'thumbnail': 'str',
 'reply_to': 'str'}
 
 df = pd.read_csv(file, usecols=keep_columns, dtype=defined_types)
  # ou
 df = pd.read_csv(file, usecols=keep_columns, dtype=defined_types, parse_dates=['created_at'])
 # pour parser les dates de la colone created_at qui indique la date de création du tweet (prends plus de temps)
```

Keywords :
- abu sayyaf
- afghanistan
- agro
- al-qaeda
- al-qaeda in the arabian peninsula
- al-qaeda in the islamic maghreb
- al-shabaab
- ammonium nitrate
- attack
- biological weapon
- car bomb
- chemical weapon
- conventional weapon
- dirty bomb
- eco-terrorism
- environmental terrorism
- euskadi ta askatasuna
- extremism
- farc
- fundamentalism
- hamas
- hezbollah
- improvised explosive device
- iran
- iraq
- irish republican army
- islamist
- jihad
- nationalism
- nigeria
- nuclear
- nuclear enrichment
- pakistan
- palestine liberation front
- pirates
- plo
- political radicalism
- recruitment
- somalia
- suicide attack
- suicide bomber
- taliban
- tamil tigers
- tehrik-i-taliban pakistan
- terror
- terrorism
- weapons-grade
- yemen
