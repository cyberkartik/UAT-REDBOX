line = 'SymbolNULSOHSTXETXEOTENQACKBELBSHTLFVTFFCRSOSIDLEDC1DC2DC3DC4NAKSYNETBCANEMSUBESCFSGSRSUS!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
n = 10
var = [line[i:i + n] for i in range(0, len(line), n)]
print(var)
