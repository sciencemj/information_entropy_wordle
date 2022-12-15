import string
import math

words = ['about', 'above', 'abuse', 'actor', 'acute', 'admit', 'adopt', 'adult', 'after', 'again', 'agent', 'agree', 'ahead', 'alarm', 'album', 'alert', 'alike', 'alive', 'allow', 'alone', 'along', 'alter', 'among', 'anger', 'angle', 'angry', 'apart', 'apple', 'apply', 'arena', 'argue', 'arise', 'array', 'aside', 'asset', 'audio', 'audit', 'avoid', 'award', 'aware', 'badly', 'baker', 'bases', 'basic', 'basis', 'beach', 'began', 'begin', 'begun', 'being', 'below', 'bench', 'billy', 'birth', 'black', 'blame', 'blind', 'block', 'blood', 'board', 'boost', 'booth', 'bound', 'brain', 'brand', 'bread', 'break', 'breed', 'brief', 'bring', 'broad', 'broke', 'brown', 'build', 'built', 'buyer', 'cable', 'calif', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'chase', 'cheap', 'check', 'chest', 'chief', 'child', 'china', 'chose', 'civil', 'claim', 'class', 'clean', 'clear', 'click', 'clock', 'close', 'coach', 'coast', 'could', 'count', 'court', 'cover', 'craft', 'crash', 'cream', 'crime', 'cross', 'crowd', 'crown', 'curve', 'cycle', 'daily', 'dance', 'dated', 'dealt', 'death', 'debut', 'delay', 'depth', 'doing', 'doubt', 'dozen', 'draft', 'drama', 'drawn', 'dream', 'dress', 'drill', 'drink', 'drive', 'drove', 'dying', 'eager', 'early', 'earth', 'eight', 'elite', 'empty', 'enemy', 'enjoy', 'enter', 'entry', 'equal', 'error', 'event', 'every', 'exact', 'exist', 'extra', 'faith', 'false', 'fault', 'fiber', 'field', 'fifth', 'fifty', 'fight', 'final', 'first', 'fixed', 'flash', 'fleet', 'floor', 'fluid', 'focus', 'force', 'forth', 'forty', 'forum', 'found', 'frame', 'frank', 'fraud', 'fresh', 'front', 'fruit', 'fully', 'funny', 'giant', 'given', 'glass', 'globe', 'going', 'grace', 'grade', 'grand', 'grant', 'grass', 'great', 'green', 'gross', 'group', 'grown', 'guard', 'guess', 'guest', 'guide', 'happy', 'harry', 'heart', 'heavy', 'hence', 'henry', 'horse', 'hotel', 'house', 'human', 'ideal', 'image', 'index', 'inner', 'input', 'issue', 'japan', 'jimmy', 'joint', 'jones', 'judge', 'known', 'label', 'large', 'laser', 'later', 'laugh', 'layer', 'learn', 'lease', 'least', 'leave', 'legal', 'level', 'lewis', 'light', 'limit', 'links', 'lives', 'local', 'logic', 'loose', 'lower', 'lucky', 'lunch', 'lying', 'magic', 'major', 'maker', 'march', 'maria', 'match', 'maybe', 'mayor', 'meant', 'media', 'metal', 'might', 'minor', 'minus', 'mixed', 'model', 'money', 'month', 'moral', 'motor', 'mount', 'mouse', 'mouth', 'movie', 'music', 'needs', 'never', 'newly', 'night', 'noise', 'north', 'noted', 'novel', 'nurse', 'occur', 'ocean', 'offer', 'often', 'order', 'other', 'ought', 'paint', 'panel', 'paper', 'party', 'peace', 'peter', 'phase', 'phone', 'photo', 'piece', 'pilot', 'pitch', 'place', 'plain', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prime', 'print', 'prior', 'prize', 'proof', 'proud', 'prove', 'queen', 'quick', 'quiet', 'quite', 'radio', 'raise', 'range', 'rapid', 'ratio', 'reach', 'ready', 'refer', 'right', 'rival', 'river', 'robin', 'roger', 'roman', 'rough', 'round', 'route', 'royal', 'rural', 'scale', 'scene', 'scope', 'score', 'sense', 'serve', 'seven', 'shall', 'shape', 'share', 'sharp', 'sheet', 'shelf', 'shell', 'shift', 'shirt', 'shock', 'shoot', 'short', 'shown', 'sight', 'since', 'sixth', 'sixty', 'sized', 'skill', 'sleep', 'slide', 'small', 'smart', 'smile', 'smith', 'smoke', 'solid', 'solve', 'sorry', 'sound', 'south', 'space', 'spare', 'speak', 'speed', 'spend', 'spent', 'split', 'spoke', 'sport', 'staff', 'stage', 'stake', 'stand', 'start', 'state', 'steam', 'steel', 'stick', 'still', 'stock', 'stone', 'stood', 'store', 'storm', 'story', 'strip', 'stuck', 'study', 'stuff', 'style', 'sugar', 'suite', 'super', 'sweet', 'table', 'taken', 'taste', 'taxes', 'teach', 'teeth', 'terry', 'texas', 'thank', 'theft', 'their', 'theme', 'there', 'these', 'thick', 'thing', 'think', 'third', 'those', 'three', 'threw', 'throw', 'tight', 'times', 'tired', 'title', 'today', 'topic', 'total', 'touch', 'tough', 'tower', 'track', 'trade', 'train', 'treat', 'trend', 'trial', 'tried', 'tries', 'truck', 'truly', 'trust', 'truth', 'twice', 'under', 'undue', 'union', 'unity', 'until', 'upper', 'upset', 'urban', 'usage', 'usual', 'valid', 'value', 'video', 'virus', 'visit', 'vital', 'voice', 'waste', 'watch', 'water', 'wheel', 'where', 'which', 'while', 'white', 'whole', 'whose', 'woman', 'women', 'world', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'write', 'wrong', 'wrote', 'yield', 'young', 'youth']

def getDecision(a_ent:dict):
    best = -1
    best_word = "*"
    best_index = -1
    for x in string.ascii_lowercase:
        for i in range(5):
            if (a_ent[x][i]) > best:
                best = a_ent[x][i]
                best_word = x
                best_index = i
    return best_word, best_index

def getWordListAd(words_:list, pred:str):
    new_words = [x for x in words_]
    for w in words_:
        for i in range(5):
            if pred[i] != '*':
                if pred[i] != w[i]:
                    new_words.remove(w)
    return new_words

def getWordListRm(words_:list, pred:str):
    new_words = [x for x in words_]
    for w in words_:
        for i in range(5):
            if pred[i] != '*':
                if pred[i] == w[i]:
                    new_words.remove(w)
    return new_words


def getNewInfo(words_):
    count = {x : [0 for i in range(5)] for x in string.ascii_lowercase}
    for w in words_:
        for x in string.ascii_lowercase:
            for i in range(5):
                if w[i] == x:
                    count[x][i] += 1
    p = {x : [0 for i in range(5)] for x in string.ascii_lowercase}
    for x in string.ascii_lowercase:
        for i in range(5):
            p[x][i] = count[x][i] / len(words_)
    s = {x : [0 for i in range(5)] for x in string.ascii_lowercase}
    for x in string.ascii_lowercase:
        for i in range(5):
            if p[x][i] != 0:
                s[x][i] = -p[x][i] * math.log2(p[x][i])
            else:
                s[x][i] = -1

    return s

answer = "*****"
ent = getNewInfo(words)
#print(ent) # p * log2p 높은 것 선택
w, index = getDecision(ent)
answer = answer[:index] + w + answer[index + 1:]
#print(answer)
new_words = getWordListAd(words, answer)
for i in range(4):
    ent = getNewInfo(new_words)
    w, index = getDecision(ent)
    answer = answer[:index] + w + answer[index + 1:]
    new_words = getWordListAd(new_words, answer)
print(f"first word is {answer}")

while True:
    result = input("your result?: ")
    if result == 'correct':
        print("👍")
        break
    for i in range(5):
        k = '*****'[:i] + answer[i] + '*****'[i+1:]
        #print(k)
        if result[i] == '*':
            words = getWordListRm(words, k)
        else:
            words = getWordListAd(words, k)
    # word list refresh
    new_words = [x for x in words]
    answer = result
    for i in range(5):
        ent = getNewInfo(new_words)
        w, index = getDecision(ent)
        answer = answer[:index] + w + answer[index + 1:]
        new_words = getWordListAd(new_words, answer)
        if len(new_words) == 1:
            answer = new_words[0]
            break
    print(f"next word is {answer}")
