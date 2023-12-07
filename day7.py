def part1():
    f = open('inputs/day7.txt', 'r')

    rankings = [[] for i in range(7)]

    cards = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"J":10,"Q":11,"K":12,"A":13}
    mapping = {}

    for x in f:
        pair = x.strip().split(" ")

        score = 0
        ct = [0 for i in range(13)]
        pairs = 0
        triple = False
        for i in range(5):
            character = pair[0][i]
            score = score*100 + cards[character]
            ct[cards[character]-1] += 1

        mapping[score] = int(pair[1])
        skip = False
        for i in range(13):
            if ct[i] == 5:
                rankings[6].append(score)
                skip = True
            elif ct[i] == 4:
                rankings[5].append(score)
                skip = True
            elif ct[i] == 3:
                triple = True
            elif ct[i] == 2:
                pairs += 1
        if skip:
            continue
        if triple and pairs == 1:
            rankings[4].append(score)
        elif triple:
            rankings[3].append(score)
        elif pairs == 2:
            rankings[2].append(score)
        elif pairs == 1:
            rankings[1].append(score)
        else:
            rankings[0].append(score)

    rank = 1
    total = 0
    for row in rankings:
        row.sort()
        for i in range(len(row)):
            total += mapping[row[i]]*rank
            rank += 1
    return total

def part2():
    f = open('inputs/day7.txt', 'r')

    rows = [[] for i in range(7)]

    cards = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"Q":11,"K":12,"A":13}
    mapping = {}

    def options(hand, pos):
        if pos == 4:
            if hand[pos] == "J":
                return cards.keys()
            else:
                return [hand[pos]]
        endings = options(hand, pos+1)
        res = []
        if hand[pos] == "J":
            for card in cards.keys():
                for ending in endings:
                    res.append(card + ending)
        else:
            for ending in endings:
                res.append(hand[pos]+ending)
        return res
    
    for x in f:
        pair = x.strip().split(" ")

        possible_hands = options(pair[0], 0)
        local_rows = [[] for i in range(7)]

        for hand in possible_hands:
            score = 0
            ct = [0 for i in range(13)]
            for i in range(5):
                ct[cards[hand[i]]-1] += 1
                score = score * 100 + cards[hand[i]]

            pairs = 0
            triple = False
            skip = False
            for i in range(13):
                if ct[i] == 5:
                    local_rows[0].append(score)
                    skip = True
                elif ct[i] == 4:
                    local_rows[1].append(score)
                    skip = True
                elif ct[i] == 3:
                    triple = True
                elif ct[i] == 2:
                    pairs += 1
            if skip:
                continue
            if triple and pairs == 1:
                local_rows[2].append(score)
            elif triple:
                local_rows[3].append(score)
            elif pairs == 2:
                local_rows[4].append(score)
            elif pairs == 1:
                local_rows[5].append(score)
            else:
                local_rows[6].append(score)
    
        for i in range(len(local_rows)):
            row = local_rows[i]
            if len(row) > 0:
                row.sort(reverse=True)
                actual_score = 0
                for x in range(5):
                    actual_score *= 100
                    if pair[0][x] != "J":
                        actual_score += cards[pair[0][x]]
                rows[6-i].append(actual_score)
                mapping[actual_score] = int(pair[1])
                break
    rank = 1
    total = 0
    for row in rows:
        row.sort()
        for score in row:
            total += rank*mapping[score]
            rank += 1
    return total

if __name__ == '__main__':
    print(part1())
    print(part2())