c = int('8f14c50f968c43fe3d40ce2692b95fb4e94c17a5dda5eee162fde77a3d0ceb7012a8b367a134194f2d3975def1adfef62657ad456fa527614218c06debaa9348011f3456fa276080e8630f2cbc806273452f4991fd269b97ca158f0264d16f1c76083f3444c6f866b5dcadebddb0687a63a9836380f750be41d423fb07dd595201af564d592a4bf4c2abac822e7d4380a5f795c022a9b2d22d43c129a159d0c5f1b957df94321e10df7c50af3f1dea36808bfa5f164a6a9a65dddee13133fe19ece35f75a969b0f8cff773c32f97cb99e759a6c5f6560c44f0bf6170b4b56c2663ca0d352cf3bb424ee059d375c78fd1ea623c44aaf307bad822f48b8ff881e27c49219d821edadd9e5de82ce9f2ff2eddf76d006adbf16a25e957b692db7c1fe40a2b2d8836039d499893c20aff7d550680c7d3d6bbe0f79dc51676215f1271d7f04ab756ae990f80e1225637ddf5c090a8c446a3a01e3c96368e2ae6b1509e22a6a8c1cf8e120b0c221eeb8fb088460b9177dc52804149504620ecb1c966d44bb6c29eb3c4a4106c486dc9da1562092dc82786628650aea5726f0742d61a40be1a7eb998450a4936bc0d99e3655735532f61c2589c535a77e10a3ae0bea0d8a01aad62e10765190593b2e09f13a6d5bc73b36a5f822542f37115ece855d087232a6d4198b7d1dbdfedf71516199fd5694a1d24993156263f0cb3fb574e491f',16)
e = 13337
p = 167945946509710528501147140850136444757936485900233494350920365296618466491038783888459340376962572176658471433672446105042569166930066764067458760954444551181379291048040552484392012079612125237961930510490682072102514499883651342766510399652317335461788686135874608722851478273373669551946245262568601067289
q = 167945946509710528501147140850136444757936485900233494350920365296618466491038783888459340376962572176658471433672446105042569166930066764067458760954444542315723029727275896055594485064790247910216515269672809063208736956951590237500845779868099616110730494457247861971337900144361732424961936041908032639503
n = 795569463642685540507503580717531982215679866156448758181874864294322245115046429295501396806569726084791213843313411985306755767933614251017259685360119715465741448841742926933764058184678978561438979554324014291467144646477238464467422645352253054043072408503415623126059018449111807300294890437634529289983603557882115343971407081044050231310858245171002149317227947666679143716043142141154344524386085333349328691743473103727587822968025700198172293605188589348169121979328380110985341428872278372426313622759225108517531628814853640680656657769539723198346005032762702856464738405070059566116940640592020837592563966093405895649052241416909627641069000138027201809936286028443581259045590752809132011594533609186039058798304319124598876514669458750171121861029071117458575853963148168447032328126766812085206373608016609150982512467597800331177524543178311636877811255184421602626713179220562081413985985692847372669113031244726086691179028200044542399429299315486513734144695492816493025225952668485937918985944213972980220480476191347009337324778384697829597183756976186825413917475597248616769321954150777672675555280228376126308362907381766363071890237458517881243184612898247096962136202978853341989193954815333784856612689

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(e, p*(p-1)*q*(q-1))


import codecs
print( codecs.decode( hex(pow(c,d,n))[2:], 'hex'))
