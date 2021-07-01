pays = []
region = []
dpt = []
ville = []

id_algo = ' [x]'

x = 0
while x <= df.shape[0]-1:
    target = df['details'][x]
    
    v = re.findall('hénin beaumont|hénin-beaumont|bengaluru|mexico|huntington beach|chengdu|suzano|waltham|bologna|fecamp|fécamp|dieppe|allston|shenzhen|chevilly-larue|vannes|villeurbanne|la queue-en-brie|magny-les-hameaux|reims|london|la rochelle|cwmbran|canton|chorzów|vitry-sur-seine|barcelona|barcelone|bangkok|buenos aires|johannesbourg|midrand|atlanta|torino|prague|lisbonne|stuttgart|sydney|nur-sultan|budapest|détroit|henin beaumont|amiens|wissous|waterford|djeddah|hengelo|bayonne|saint-sébastien-sur-loire|austin|méxico|singapour|madrid|new york|ocoyoacac|zeralda|saint-chamond|karlstein|thonon-les-bains|charlotte|blackburn|rydalmere|barcelone|coblence|charleroi|francfort-sur-le-main|oslo|berlin|melbourne|toronto|münchen|cairo|bucarest|singapore|savigliano|copenhagen|swiftwater|framingham|moscow|temara|pôrto alegre|bridgewater|noida|cambridge|chorzow|brea|cleveland|bucuresti|bangalore|shanghai|lille|marseille|saint nazaire|saint-nazaire|portet sur garonne|st brieuc|wattrelos|compiègne|bouguenais|dampierre en burly|dampierre-en-burly|angers|albertville|massy|libourne|pau|saumur|saint-denis|grenoble|dhari|rungis|gardanne|lens|ollioules|bagneux|nevers|mérignac|montréal|montreal|saint-ouen|saint ouen|epinal|soliman|carquefou|bordes|rouen|pontarlier|velizy|gennevilliers|montpellier|eyguières|saint lô|tulle|le havre|lannion|niort|saint brieuc|lorient|arras|auxerre|colombelles|pont-audemer|feyzin|issy-les-moulineaux|palaiseau|cholet|limours|puilboreau|mantes la jolie|alençon|st maximin|pierrelatte|bourg en bresse|metz|laval|granville|avranches|toulon|beauvais|gignac|langueux|beaucouzé|la chapelle saint ursin|roanne|st sebastien|saint denis|abbeville|domerat|la défense|la defense|nanterre|lisieux|bagnolet|bourges|haguenau|saran|nantes|brive-la-gaillarde|menton|charleville-mézières|saint-dizier|versailles|toulouse|thionville|chauny|le caire|valenciennes|pantin|avignon|rians|aubervilliers|caen|rennes|courbevoie|annecy|la courneuve|le plessis-robinson|orléans|ivry sur seine|brest|eragny|cherbourg|paris|lyon|vélizy-villacoublay|élancourt', target.lower())
    if not v:
        ville.append('')
        dpt.append('')
        region.append('')
        pays.append('')
    else:
        if v[0].title() == 'Paris':
            temp = geo.loc[geo['ville'] == f'Paris{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cherbourg':
            temp = geo.loc[geo['ville'] == f'Cherbourg{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Le Plessis-Robinson':
            temp = geo.loc[geo['ville'] == f'Le Plessis-Robinson{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Versailles':
            temp = geo.loc[geo['ville'] == f'Versailles{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bangalore' or v[0].title() == 'Bengaluru':
            temp = geo.loc[geo['ville'] == f'Bangalore{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bourges':
            temp = geo.loc[geo['ville'] == f'Bourges{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cairo' or v[0].title() == 'Le Caire':
            temp = geo.loc[geo['ville'] == f'Le Caire{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Ouen' or v[0].title() == 'Saint Ouen' or v[0].title() == 'Saint- Ouen':
            temp = geo.loc[geo['ville'] == f'Saint-Ouen{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Brest':
            temp = geo.loc[geo['ville'] == f'Brest{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Vitry-sur-Seine':
            temp = geo.loc[geo['ville'] == f'Vitry-sur-Seine{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bangkok':
            temp = geo.loc[geo['ville'] == f'Bangkok{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Henin Beaumont' or v[0].title() == 'Henin-Beaumont' or v[0].title() == 'Hénin-Beaumont':
            temp = geo.loc[geo['ville'] == f'Henin Beaumont{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Amiens':
            temp = geo.loc[geo['ville'] == f'Amiens{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Wissous':
            temp = geo.loc[geo['ville'] == f'Wissous{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bayonne':
            temp = geo.loc[geo['ville'] == f'Bayonne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Sébastien-Sur-Loire':
            temp = geo.loc[geo['ville'] == f'Saint-Sébastien-Sur-Loire{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Chamond':
            temp = geo.loc[geo['ville'] == f'Saint-Chamond{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Nazaire' or v[0].title() == 'Saint Nazaire':
            temp = geo.loc[geo['ville'] == f'Saint-Nazaire{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lille':
            temp = geo.loc[geo['ville'] == f'Lille{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Marseille':
            temp = geo.loc[geo['ville'] == f'Marseille{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Velizy' or v[0].title() == 'Vélizy-Villacoublay':
            temp = geo.loc[geo['ville'] == f'Vélizy-Villacoublay{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Élancourt' or v[0].title() == 'Elancourt':
            temp = geo.loc[geo['ville'] == f'Élancourt{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Brea':
            temp = geo.loc[geo['ville'] == f'Brea{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Nantes':
            temp = geo.loc[geo['ville'] == f'Nantes{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Toulouse':
            temp = geo.loc[geo['ville'] == f'Toulouse{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lorient':
            temp = geo.loc[geo['ville'] == f'Lorient{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Gennevilliers':
            temp = geo.loc[geo['ville'] == f'Gennevilliers{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Roanne':
            temp = geo.loc[geo['ville'] == f'Roanne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Shanghai':
            temp = geo.loc[geo['ville'] == f'Shanghai{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Valenciennes':
            temp = geo.loc[geo['ville'] == f'Valenciennes{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Charleroi':
            temp = geo.loc[geo['ville'] == f'Charleroi{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Issy-Les-Moulineaux' or v[0].title() == 'Issy Les Moulineaux':
            temp = geo.loc[geo['ville'] == f'Issy-Les-Moulineaux{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Toronto':
            temp = geo.loc[geo['ville'] == f'Toronto{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Chorzow' or v[0].title() == 'Chorzów':
            temp = geo.loc[geo['ville'] == f'Chorzow{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bucarest' or v[0].title() == 'Bucuresti' or v[0].title() == 'Bucaresti':
            temp = geo.loc[geo['ville'] == f'Bucarest{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pau':
            temp = geo.loc[geo['ville'] == f'Pau{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lyon':
            temp = geo.loc[geo['ville'] == f'Lyon{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Hengelo':
            temp = geo.loc[geo['ville'] == f'Hengelo{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Montreal' or v[0].title() == 'Montréal':
            temp = geo.loc[geo['ville'] == f'Montreal{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cambridge':
            temp = geo.loc[geo['ville'] == f'Cambridge{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Noida':
            temp = geo.loc[geo['ville'] == f'Noida{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Ivry Sur Seine' or v[0].title() == 'Ivry':
            temp = geo.loc[geo['ville'] == f'Ivry Sur Seine{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Denis' or v[0].title() == 'Saint Denis':
            temp = geo.loc[geo['ville'] == f'Saint-Denis{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Toulon':
            temp = geo.loc[geo['ville'] == f'Toulon{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bridgewater':
            temp = geo.loc[geo['ville'] == f'Bridgewater{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Annecy':
            temp = geo.loc[geo['ville'] == f'Annecy{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Arras':
            temp = geo.loc[geo['ville'] == f'Arras{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Nanterre':
            temp = geo.loc[geo['ville'] == f'Nanterre{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Madrid':
            temp = geo.loc[geo['ville'] == f'Madrid{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Berlin':
            temp = geo.loc[geo['ville'] == f'Berlin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Singapore' or v[0].title() == 'Singapour':
            temp = geo.loc[geo['ville'] == f'Singapour{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Massy':
            temp = geo.loc[geo['ville'] == f'Massy{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cholet':
            temp = geo.loc[geo['ville'] == f'Cholet{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Framingham':
            temp = geo.loc[geo['ville'] == f'Framingham{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Ollioules':
            temp = geo.loc[geo['ville'] == f'Ollioules{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Portet Sur Garonne':
            temp = geo.loc[geo['ville'] == f'Portet Sur Garonne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Orléans':
            temp = geo.loc[geo['ville'] == f'Orléans{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'México' or v[0].title() == 'Mexico':
            temp = geo.loc[geo['ville'] == f'Mexico{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Rydalmere':
            temp = geo.loc[geo['ville'] == f'Rydalmere{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Melbourne':
            temp = geo.loc[geo['ville'] == f'Melbourne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Grenoble':
            temp = geo.loc[geo['ville'] == f'Grenoble{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Sydney':
            temp = geo.loc[geo['ville'] == f'Sydney{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Savigliano':
            temp = geo.loc[geo['ville'] == f'Savigliano{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Karlstein':
            temp = geo.loc[geo['ville'] == f'Karlstein{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Stuttgart':
            temp = geo.loc[geo['ville'] == f'Stuttgart{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Rennes':
            temp = geo.loc[geo['ville'] == f'Rennes{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Le Havre':
            temp = geo.loc[geo['ville'] == f'Le Havre{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Montpellier':
            temp = geo.loc[geo['ville'] == f'Montpellier{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Auxerre':
            temp = geo.loc[geo['ville'] == f'Auxerre{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Niort':
            temp = geo.loc[geo['ville'] == f'Niort{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Tulle':
            temp = geo.loc[geo['ville'] == f'Tulle{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Colombelles':
            temp = geo.loc[geo['ville'] == f'Colombelles{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'La Chapelle Saint Ursin' or v[0].title() == 'La-Chapelle-Saint-Ursin':
            temp = geo.loc[geo['ville'] == f'La Chapelle Saint Ursin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Angers':
            temp = geo.loc[geo['ville'] == f'Angers{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Rungis':
            temp = geo.loc[geo['ville'] == f'Rungis{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Caen':
            temp = geo.loc[geo['ville'] == f'Caen{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Rouen':
            temp = geo.loc[geo['ville'] == f'Rouen{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Nur-Sultan':
            temp = geo.loc[geo['ville'] == f'Nur-Sultan{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Prague':
            temp = geo.loc[geo['ville'] == f'Prague{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Temara':
            temp = geo.loc[geo['ville'] == f'Temara{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Oslo':
            temp = geo.loc[geo['ville'] == f'Oslo{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Swiftwater':
            temp = geo.loc[geo['ville'] == f'Swiftwater{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Atlanta':
            temp = geo.loc[geo['ville'] == f'Atlanta{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Laval':
            temp = geo.loc[geo['ville'] == f'Laval{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Barcelona' or v[0].title() == 'Barcelone':
            temp = geo.loc[geo['ville'] == f'Barcelone{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Soliman':
            temp = geo.loc[geo['ville'] == f'Soliman{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Limours':
            temp = geo.loc[geo['ville'] == f'Limours{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'New York':
            temp = geo.loc[geo['ville'] == f'New York{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lisbonne':
            temp = geo.loc[geo['ville'] == f'Lisbonne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Torino' or v[0].title() == 'Turin':
            temp = geo.loc[geo['ville'] == f'Torino{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Moscow' or v[0].title() == 'Moscou':
            temp = geo.loc[geo['ville'] == f'Moscou{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Francfort-Sur-Le-Main' or v[0].title() == 'Francfort Sur Le Main':
            temp = geo.loc[geo['ville'] == f'Francfort-Sur-Le-Main{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lisieux':
            temp = geo.loc[geo['ville'] == f'Lisieux{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Eragny':
            temp = geo.loc[geo['ville'] == f'Eragny{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Blackburn':
            temp = geo.loc[geo['ville'] == f'Blackburn{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Courbevoie':
            temp = geo.loc[geo['ville'] == f'Courbevoie{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Ocoyoacac':
            temp = geo.loc[geo['ville'] == f'Ocoyoacac{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Copenhagen' or v[0].title() == 'Copenhague':
            temp = geo.loc[geo['ville'] == f'Copenhagen{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Puilboreau':
            temp = geo.loc[geo['ville'] == f'Puilboreau{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Zeralda':
            temp = geo.loc[geo['ville'] == f'Zeralda{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint Brieuc' or v[0].title() == 'Saint-Brieuc' or v[0].title() == 'St Brieuc':
            temp = geo.loc[geo['ville'] == f'Saint Brieuc{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bagnolet':
            temp = geo.loc[geo['ville'] == f'Bagnolet{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bagneux':
            temp = geo.loc[geo['ville'] == f'Bagneux{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Budapest':
            temp = geo.loc[geo['ville'] == f'Budapest{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bordes':
            temp = geo.loc[geo['ville'] == f'Bordes{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Alençon':
            temp = geo.loc[geo['ville'] == f'Alençon{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cleveland':
            temp = geo.loc[geo['ville'] == f'Cleveland{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Metz':
            temp = geo.loc[geo['ville'] == f'Metz{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Mantes La Jolie' or v[0].title() == 'Mantes-La-Jolie':
            temp = geo.loc[geo['ville'] == f'Mantes La Jolie{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Dampierre-En-Burly' or v[0].title() == 'Dampierre En Burly':
            temp = geo.loc[geo['ville'] == f'Dampierre-En-Burly{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'La Défense' or v[0].title() == 'La Defense':
            temp = geo.loc[geo['ville'] == f'La Défense{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Epinal' or v[0].title() == 'Épinal':
            temp = geo.loc[geo['ville'] == f'Epinal{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Aubervilliers':
            temp = geo.loc[geo['ville'] == f'Aubervilliers{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Détroit' or v[0].title() == 'Detroit':
            temp = geo.loc[geo['ville'] == f'Détroit{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saran':
            temp = geo.loc[geo['ville'] == f'Saran{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Thionville':
            temp = geo.loc[geo['ville'] == f'Thionville{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Beauvais':
            temp = geo.loc[geo['ville'] == f'Beauvais{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Albertville':
            temp = geo.loc[geo['ville'] == f'Albertville{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bourg En Bresse'or v[0].title() == 'Bourg-En-Bresse':
            temp = geo.loc[geo['ville'] == f'Bourg En Bresse{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Mérignac':
            temp = geo.loc[geo['ville'] == f'Mérignac{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Buenos Aires':
            temp = geo.loc[geo['ville'] == f'Buenos Aires{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Granville':
            temp = geo.loc[geo['ville'] == f'Granville{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Feyzin':
            temp = geo.loc[geo['ville'] == f'Feyzin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Beaucouzé':
            temp = geo.loc[geo['ville'] == f'Beaucouzé{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Menton':
            temp = geo.loc[geo['ville'] == f'Menton{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Palaiseau':
            temp = geo.loc[geo['ville'] == f'Palaiseau{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lannion':
            temp = geo.loc[geo['ville'] == f'Lannion{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Djeddah':
            temp = geo.loc[geo['ville'] == f'Djeddah{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pierrelatte':
            temp = geo.loc[geo['ville'] == f'Pierrelatte{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Midrand':
            temp = geo.loc[geo['ville'] == f'Midrand{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Brive-La-Gaillarde' or v[0].title() == 'Brive La Gaillarde':
            temp = geo.loc[geo['ville'] == f'Brive-La-Gaillarde{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Coblence':
            temp = geo.loc[geo['ville'] == f'Coblence{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Langueux':
            temp = geo.loc[geo['ville'] == f'Langueux{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Nevers':
            temp = geo.loc[geo['ville'] == f'Nevers{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Johannesbourg':
            temp = geo.loc[geo['ville'] == f'Johannesbourg{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Rians':
            temp = geo.loc[geo['ville'] == f'Rians{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'St Sebastien':
            temp = geo.loc[geo['ville'] == f'St Sebastien{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Compiègne':
            temp = geo.loc[geo['ville'] == f'Compiègne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Gignac':
            temp = geo.loc[geo['ville'] == f'Gignac{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Haguenau':
            temp = geo.loc[geo['ville'] == f'Haguenau{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Thonon-Les-Bains' or v[0].title() == 'Thonon Les Bains':
            temp = geo.loc[geo['ville'] == f'Thonon-Les-Bains{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saumur':
            temp = geo.loc[geo['ville'] == f'Saumur{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Avignon':
            temp = geo.loc[geo['ville'] == f'Avignon{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'La Courneuve':
            temp = geo.loc[geo['ville'] == f'La Courneuve{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Eyguières':
            temp = geo.loc[geo['ville'] == f'Eyguières{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'St Maximin' or v[0].title() == 'Saint Maximin':
            temp = geo.loc[geo['ville'] == f'St Maximin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Avranches':
            temp = geo.loc[geo['ville'] == f'Avranches{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bouguenais':
            temp = geo.loc[geo['ville'] == f'Bouguenais{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pantin':
            temp = geo.loc[geo['ville'] == f'Pantin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Lens':
            temp = geo.loc[geo['ville'] == f'Lens{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint Dizier' or v[0].title() == 'Saint-Dizier':
            temp = geo.loc[geo['ville'] == f'Saint-Dizier{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Chauny':
            temp = geo.loc[geo['ville'] == f'Chauny{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pont-Audemer' or v[0].title() == 'Pont Audemer':
            temp = geo.loc[geo['ville'] == f'Pont-Audemer{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Libourne':
            temp = geo.loc[geo['ville'] == f'Libourne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Gardanne':
            temp = geo.loc[geo['ville'] == f'Gardanne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Domerat':
            temp = geo.loc[geo['ville'] == f'Domerat{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pôrto Alegre' or v[0].title() == 'Porto Alegre':
            temp = geo.loc[geo['ville'] == f'Pôrto Alegre{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Pontarlier':
            temp = geo.loc[geo['ville'] == f'Pontarlier{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Wattrelos':
            temp = geo.loc[geo['ville'] == f'Wattrelos{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Charleville-Mézières' or v[0].title() == 'Charleville-Mezieres' or v[0].title() == 'Charleville Mézières' or v[0].title() == 'Charleville Mezieres':
            temp = geo.loc[geo['ville'] == f'Charleville-Mézières{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Charlotte':
            temp = geo.loc[geo['ville'] == f'Charlotte{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Abbeville':
            temp = geo.loc[geo['ville'] == f'Abbeville{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'München' or v[0].title() == 'Munich':
            temp = geo.loc[geo['ville'] == f'München{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Saint-Lô' or v[0].title() == 'Saint-Lo' or v[0].title() == 'Saint Lô' or v[0].title() == 'Saint Lo':
            temp = geo.loc[geo['ville'] == f'Saint Lô{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Carquefou':
            temp = geo.loc[geo['ville'] == f'Carquefou{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Austin':
            temp = geo.loc[geo['ville'] == f'Austin{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Dhari':
            temp = geo.loc[geo['ville'] == f'Soliman{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Canton':
            temp = geo.loc[geo['ville'] == f'Canton{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Cwmbran':
            temp = geo.loc[geo['ville'] == f'Cwmbran{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'La Rochelle':
            temp = geo.loc[geo['ville'] == f'La Rochelle{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'London':
            temp = geo.loc[geo['ville'] == f'London{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Reims':
            temp = geo.loc[geo['ville'] == f'Reims{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Magny-Les-Hameaux':
            temp = geo.loc[geo['ville'] == f'Magny-Les-Hameaux{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'La Queue-En-Brie':
            temp = geo.loc[geo['ville'] == f'La Queue-En-Brie{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Villeurbanne':
            temp = geo.loc[geo['ville'] == f'Villeurbanne{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Chevilly-Larue':
            temp = geo.loc[geo['ville'] == f'Chevilly-Larue{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Shenzhen':
            temp = geo.loc[geo['ville'] == f'Shenzhen{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Allston':
            temp = geo.loc[geo['ville'] == f'Allston{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Dieppe':
            temp = geo.loc[geo['ville'] == f'Dieppe{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Fécamp' or v[0].title() == 'Fecamp':
            temp = geo.loc[geo['ville'] == f'Fécamp{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Bologna':
            temp = geo.loc[geo['ville'] == f'Bologna{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Waltham':
            temp = geo.loc[geo['ville'] == f'Waltham{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Suzano':
            temp = geo.loc[geo['ville'] == f'Suzano{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Chengdu':
            temp = geo.loc[geo['ville'] == f'Chengdu{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        elif v[0].title() == 'Huntington Beach':
            temp = geo.loc[geo['ville'] == f'Huntington Beach{id_algo}']
            ville.append(temp['ville'].values[0]), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
        else:
            t = re.findall('drome|drôme|gironde|gard|manche|eure|hauts-de-seine|seine et marne|savoie|haute savoie|isère|rhône|loire atlantique|saône et loire|bouches du rhône|hérault', target.lower())
            if not t:
                ville.append('')
                dpt.append('')
                region.append('TBD1')
                pays.append('TBD1')
            elif t[0].title() == 'Gironde':
                temp = geo.loc[geo['ville'] == f'Gironde{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Drome' or t[0].title() == 'Drôme':
                temp = geo.loc[geo['ville'] == f'Drôme{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Gard':
                temp = geo.loc[geo['ville'] == f'Gard{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Manche':
                temp = geo.loc[geo['ville'] == f'Manche{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Eure':
                temp = geo.loc[geo['ville'] == f'Eure{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Hauts-De-Seine' or t[0].title() == 'Hauts De Seine' or t[0].title() == 'Hauts-de-Seine' or t[0].title() == 'Hauts de Seine':
                temp = geo.loc[geo['ville'] == f'Hauts-de-Seine{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Seine-Et-Marne' or t[0].title() == 'Seine Et Marne' or t[0].title() == 'Seine-et-Marne' or t[0].title() == 'Seine et Marne':
                temp = geo.loc[geo['ville'] == f'Seine-et-Marne{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Savoie':
                temp = geo.loc[geo['ville'] == f'Savoie{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Haute Savoie' or t[0].title() == 'Haute-Savoie':
                temp = geo.loc[geo['ville'] == f'Haute-Savoie{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Isère' or t[0].title() == 'Isere':
                temp = geo.loc[geo['ville'] == f'Isère{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Rhone' or t[0].title() == 'Rhône':
                temp = geo.loc[geo['ville'] == f'Rhône{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Loire-Atlantique' or t[0].title() == 'Loire Atlantique':
                temp = geo.loc[geo['ville'] == f'Loire Atlantique{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Saône et Loire':
                temp = geo.loc[geo['ville'] == f'Saône et Loire{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            elif t[0].title() == 'Bouches du Rhône':
                temp = geo.loc[geo['ville'] == f'Bouches du Rhône{id_algo}']
                ville.append(''), dpt.append(temp['dpt'].values[0]), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
            else:
                r = re.findall("géorgie|bade-wurtemberg|michigan|overijssel|new york|caroline du nord|lancashire|nouvelle-galles du sud|thessaloniki|rhénanie-palatinat|
                	californie|ontario|rio grande do sul|new jersey|uttar pradesh|massachusetts|wallonie|île-de-france|normandie|bretagne|ile de france|hauts de france|
                	centre val de loire|provence/alps|hauts-de-france|quebec|québec|auvergne-rhône-alpes|bourgogne franche comte|pays de la loire|
                	provence-alpes-côte d'azur|grand est|nouvelle-aquitaine|occitanie", target.lower())
                if not r:
                    ville.append('')
                    dpt.append('')
                    region.append('')
                    pays.append('TBD2')
                elif r[0].title() == 'Michigan':
                    temp = geo.loc[geo['region'] == f'Michigan{id_algo}']
                    ville.append(''), dpt.append(''), region.append(temp['region'].values[0]), pays.append(temp['pays'].values[0])
                else:
                    c = re.findall('pologne|argentine|thaïlande|afrique du sud|sweden|ecosse|germany|australia|kazakhstan|irlande|hongrie|arabie saoudite|mexico|singapour|
                    	spain|algérie|mexique|england|angleterre|espagne|greece|belgium|united kingdom|allemagne|royaume-uni|norway|deutschland|egypt|singapore|italy|denmark|
                    	russie|morocco|brazil|france|canada|tunisia|chine|china|india|romania|états-unis|united states|poland', target.lower())
                    if not r:
                        pays.append('TBD3')
                    elif r[0].title() == 'Pologne':
                        temp = geo.loc[geo['region'] == f'Pologne{id_algo}']
                        ville.append(''), dpt.append(''), region.append(''), pays.append(temp['pays'].values[0])
                    else:
                        dpt.append('No Info')
                        region.append('No Info')
                        pays.append('No Info')
    x = x + 1

df['country'] = pays
df['region'] = region
df['departement'] = dpt
df['ville'] = ville