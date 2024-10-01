from math import gcd

def kasiski(texte : str, longueur: int) -> int:
    sous_chaines : dict[str, list[int]]
    sous_chaine : str

    sous_chaines_pairs : dict[str, list[int]]
    positions : list[int]

    distances : list[int]

    pgcd : int

    sous_chaines = {}
    for i in range(len(texte) - longueur):
        sous_chaine = texte[i:i+longueur]
        if sous_chaine in sous_chaines:
            sous_chaines[sous_chaine].append(i)
        else:
            sous_chaines[sous_chaine] = [i]

    
    sous_chaines_pairs = {}
    for sous_chaine in sous_chaines:
        positions = sous_chaines[sous_chaine]
        if len(positions) > 1:
            sous_chaines_pairs[sous_chaine] = positions


    distances = []
    for sous_chaine in sous_chaines_pairs:
        positions = sous_chaines_pairs[sous_chaine]
        distances.append(abs(positions[0] - positions[1]))

        
    distances = list(dict.fromkeys(distances))
    pgcd = gcd(*distances)

    return pgcd
    


if __name__ == "__main__":
    res = kasiski("SBGZPLPSLAOZRLLDHAZTTSKUGGURHIUEFPGZCECAWBGOZSKHDBJACOKTDZMQIWVANVKEHEJIQBNQRRPPWWMDPPYIFIRSDRZTKUYFWEDSHTBQHBLTLVYFTAUEAXRAXTNEDSTQHSVSLVZTTIIIPXRQBEETDBOACEMEQBNAJGYTKMMAPLYAVJKQCTYEVISQIHVMHBNASSRNGBKOWNZQXMYAUCIYSBGZPLPSLANMKETHDVMQSDIAVBOOPLCYWPXAJGYTKMNUHTFRBWLOGYGTROXMEHPAGIVFXNXTRQTOGERSLVMOGYGTROXMEHZCFWSBAEOIWGXMCGZNJNXABTYESMTMCDGASMXYTTYOGAURIHVPDAZFWRFUJPSMRHZNHARUZEKHHJXUIIJHEWSNTSRNGKUXDSJUVKUYEUKEUAGFQLVTFPRQNPRRNQTIDRCDZIXUXTFTKMSMIHVMDBOOPLCYDLBMCCVDFWSBJTVRLHKPHCYEPMYAUTYESZKETNKMHBNASSWOUJXQPKZNJUUPTRECUGVFDSPSWMSEDFKEQQTHDLMEVWRHXNXCDZKRJLCYFWTEIRLCWMJBGOSLHUYUCPLRHUGFWEDAWQIEIHVBHAZWCONNEMOZTTRZOLPTZOQXNRDGQZUDNKOPIZTTMRTLKGXPNRLBAOEDFTRBXZAVRRPKQIMAGFRLBNYHCIY" 
            , 4)
    print(res)