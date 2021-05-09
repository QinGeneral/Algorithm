class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def findS(word, index, i, j, visited):
            print(word, word[index] if index < len(word) else None, i, j)
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                if word not in result:
                    result.append(word)
                return True
            visited[i][j] = True
            isSuccess = False

            for di, dj in direction:
                newI = i + di
                newJ = j + dj
                if newI < 0 or newI >= m or newJ < 0 or newJ >= n:
                    continue
                if visited[newI][newJ]:
                    continue
                isSuccess = findS(word, index + 1, newI, newJ, visited)
                if isSuccess:
                    break
            visited[i][j] = False
            return isSuccess

        def findWord(word, i, visited):
            for i in range(m):
                for j in range(n):
                    if findS(word, 0, i, j, visited):
                        break

        for w in words:
            findWord(w, 0, visited)
        return result


class Solution2:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []

        def findS(word, index, i, j, visited):
            # print(word, word[index] if index < len(word) else None, i, j)
            if index == len(word):
                if word not in result:
                    result.append(word)
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            isSuccess = False
            if i - 1 >= 0 and not visited[i - 1][j] and board[i - 1][j] == word[index]:
                visited[i - 1][j] = True
                isSuccess = findS(word, index + 1, i - 1, j, visited)
                visited[i - 1][j] = False
            if j - 1 >= 0 and not visited[i][j - 1] and board[i][j - 1] == word[index]:
                visited[i][j - 1] = True
                isSuccess = findS(word, index + 1, i, j - 1, visited)
                visited[i][j - 1] = False
            if i + 1 < m and not visited[i + 1][j] and board[i + 1][j] == word[index]:
                visited[i + 1][j] = True
                isSuccess = findS(word, index + 1, i + 1, j, visited)
                visited[i + 1][j] = False
            if j + 1 < n and not visited[i][j + 1] and board[i][j + 1] == word[index]:
                visited[i][j + 1] = True
                isSuccess = findS(word, index + 1, i, j + 1, visited)
                visited[i][j + 1] = False
            return isSuccess

        def findWord(word, i, visited):
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        # print(word, i, j)
                        visited[i][j] = True
                        isSuccess = findS(word, 1, i, j, visited)
                        visited[i][j] = False
                        if isSuccess:
                            break

        for w in words:
            findWord(w, 0, visited)
        return result


class Solution3:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []

        end = "_end"

        trie = dict()
        for word in words:
            current_dict = trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[end] = end

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def findS(trie, curWord, i, j, visited):
            curWord += board[i][j]
            trie = trie[board[i][j]]
            if end in trie:
                if curWord not in result:
                    result.append(curWord)

            visited[i][j] = True
            for di, dj in direction:
                newI = i + di
                newJ = j + dj
                if newI < 0 or newI >= m or newJ < 0 or newJ >= n:
                    continue
                if visited[newI][newJ]:
                    continue
                if board[newI][newJ] not in trie:
                    continue
                findS(trie, curWord, newI, newJ, visited)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    findS(trie, "", i, j, visited)

        return result


class Solution4:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        result = []

        end = "_end"

        trie = dict()
        for word in words:
            current_dict = trie
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[end] = end

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def findS(trie, curWord, i, j, visited):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if visited[i][j]:
                return
            if board[i][j] not in trie:
                return
            curWord += board[i][j]
            trie = trie[board[i][j]]
            if end in trie:
                if curWord not in result:
                    result.append(curWord)

            visited[i][j] = True
            for di, dj in direction:
                newI = i + di
                newJ = j + dj

                findS(trie, curWord, newI, newJ, visited)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                findS(trie, "", i, j, visited)

        return result


print(
    Solution4().findWords(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain"],
    )
)


print(
    Solution4().findWords(
        [
            ["o", "a", "b", "n"],
            ["o", "t", "a", "e"],
            ["a", "h", "k", "r"],
            ["a", "f", "l", "v"],
        ],
        ["oa", "oaa"],
    )
)

print(
    Solution4().findWords(
        [
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
            ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
            ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
        ],
        [
            "ababababaa",
            "ababababab",
            "ababababac",
            "ababababad",
            "ababababae",
            "ababababaf",
            "ababababag",
            "ababababah",
            "ababababai",
            "ababababaj",
            "ababababak",
            "ababababal",
            "ababababam",
            "ababababan",
            "ababababao",
            "ababababap",
            "ababababaq",
            "ababababar",
            "ababababas",
            "ababababat",
            "ababababau",
            "ababababav",
            "ababababaw",
            "ababababax",
            "ababababay",
            "ababababaz",
            "ababababba",
            "ababababbb",
            "ababababbc",
            "ababababbd",
            "ababababbe",
            "ababababbf",
            "ababababbg",
            "ababababbh",
            "ababababbi",
            "ababababbj",
            "ababababbk",
            "ababababbl",
            "ababababbm",
            "ababababbn",
            "ababababbo",
            "ababababbp",
            "ababababbq",
            "ababababbr",
            "ababababbs",
            "ababababbt",
            "ababababbu",
            "ababababbv",
            "ababababbw",
            "ababababbx",
            "ababababby",
            "ababababbz",
            "ababababca",
            "ababababcb",
            "ababababcc",
            "ababababcd",
            "ababababce",
            "ababababcf",
            "ababababcg",
            "ababababch",
            "ababababci",
            "ababababcj",
            "ababababck",
            "ababababcl",
            "ababababcm",
            "ababababcn",
            "ababababco",
            "ababababcp",
            "ababababcq",
            "ababababcr",
            "ababababcs",
            "ababababct",
            "ababababcu",
            "ababababcv",
            "ababababcw",
            "ababababcx",
            "ababababcy",
            "ababababcz",
            "ababababda",
            "ababababdb",
            "ababababdc",
            "ababababdd",
            "ababababde",
            "ababababdf",
            "ababababdg",
            "ababababdh",
            "ababababdi",
            "ababababdj",
            "ababababdk",
            "ababababdl",
            "ababababdm",
            "ababababdn",
            "ababababdo",
            "ababababdp",
            "ababababdq",
            "ababababdr",
            "ababababds",
            "ababababdt",
            "ababababdu",
            "ababababdv",
            "ababababdw",
            "ababababdx",
            "ababababdy",
            "ababababdz",
            "ababababea",
            "ababababeb",
            "ababababec",
            "ababababed",
            "ababababee",
            "ababababef",
            "ababababeg",
            "ababababeh",
            "ababababei",
            "ababababej",
            "ababababek",
            "ababababel",
            "ababababem",
            "ababababen",
            "ababababeo",
            "ababababep",
            "ababababeq",
            "ababababer",
            "ababababes",
            "ababababet",
            "ababababeu",
            "ababababev",
            "ababababew",
            "ababababex",
            "ababababey",
            "ababababez",
            "ababababfa",
            "ababababfb",
            "ababababfc",
            "ababababfd",
            "ababababfe",
            "ababababff",
            "ababababfg",
            "ababababfh",
            "ababababfi",
            "ababababfj",
            "ababababfk",
            "ababababfl",
            "ababababfm",
            "ababababfn",
            "ababababfo",
            "ababababfp",
            "ababababfq",
            "ababababfr",
            "ababababfs",
            "ababababft",
            "ababababfu",
            "ababababfv",
            "ababababfw",
            "ababababfx",
            "ababababfy",
            "ababababfz",
            "ababababga",
            "ababababgb",
            "ababababgc",
            "ababababgd",
            "ababababge",
            "ababababgf",
            "ababababgg",
            "ababababgh",
            "ababababgi",
            "ababababgj",
            "ababababgk",
            "ababababgl",
            "ababababgm",
            "ababababgn",
            "ababababgo",
            "ababababgp",
            "ababababgq",
            "ababababgr",
            "ababababgs",
            "ababababgt",
            "ababababgu",
            "ababababgv",
            "ababababgw",
            "ababababgx",
            "ababababgy",
            "ababababgz",
            "ababababha",
            "ababababhb",
            "ababababhc",
            "ababababhd",
            "ababababhe",
            "ababababhf",
            "ababababhg",
            "ababababhh",
            "ababababhi",
            "ababababhj",
            "ababababhk",
            "ababababhl",
            "ababababhm",
            "ababababhn",
            "ababababho",
            "ababababhp",
            "ababababhq",
            "ababababhr",
            "ababababhs",
            "ababababht",
            "ababababhu",
            "ababababhv",
            "ababababhw",
            "ababababhx",
            "ababababhy",
            "ababababhz",
            "ababababia",
            "ababababib",
            "ababababic",
            "ababababid",
            "ababababie",
            "ababababif",
            "ababababig",
            "ababababih",
            "ababababii",
            "ababababij",
            "ababababik",
            "ababababil",
            "ababababim",
            "ababababin",
            "ababababio",
            "ababababip",
            "ababababiq",
            "ababababir",
            "ababababis",
            "ababababit",
            "ababababiu",
            "ababababiv",
            "ababababiw",
            "ababababix",
            "ababababiy",
            "ababababiz",
            "ababababja",
            "ababababjb",
            "ababababjc",
            "ababababjd",
            "ababababje",
            "ababababjf",
            "ababababjg",
            "ababababjh",
            "ababababji",
            "ababababjj",
            "ababababjk",
            "ababababjl",
            "ababababjm",
            "ababababjn",
            "ababababjo",
            "ababababjp",
            "ababababjq",
            "ababababjr",
            "ababababjs",
            "ababababjt",
            "ababababju",
            "ababababjv",
            "ababababjw",
            "ababababjx",
            "ababababjy",
            "ababababjz",
            "ababababka",
            "ababababkb",
            "ababababkc",
            "ababababkd",
            "ababababke",
            "ababababkf",
            "ababababkg",
            "ababababkh",
            "ababababki",
            "ababababkj",
            "ababababkk",
            "ababababkl",
            "ababababkm",
            "ababababkn",
            "ababababko",
            "ababababkp",
            "ababababkq",
            "ababababkr",
            "ababababks",
            "ababababkt",
            "ababababku",
            "ababababkv",
            "ababababkw",
            "ababababkx",
            "ababababky",
            "ababababkz",
            "ababababla",
            "abababablb",
            "abababablc",
            "ababababld",
            "abababable",
            "abababablf",
            "abababablg",
            "abababablh",
            "ababababli",
            "abababablj",
            "abababablk",
            "ababababll",
            "abababablm",
            "ababababln",
            "abababablo",
            "abababablp",
            "abababablq",
            "abababablr",
            "ababababls",
            "abababablt",
            "abababablu",
            "abababablv",
            "abababablw",
            "abababablx",
            "abababably",
            "abababablz",
            "ababababma",
            "ababababmb",
            "ababababmc",
            "ababababmd",
            "ababababme",
            "ababababmf",
            "ababababmg",
            "ababababmh",
            "ababababmi",
            "ababababmj",
            "ababababmk",
            "ababababml",
            "ababababmm",
            "ababababmn",
            "ababababmo",
            "ababababmp",
            "ababababmq",
            "ababababmr",
            "ababababms",
            "ababababmt",
            "ababababmu",
            "ababababmv",
            "ababababmw",
            "ababababmx",
            "ababababmy",
            "ababababmz",
            "ababababna",
            "ababababnb",
            "ababababnc",
            "ababababnd",
            "ababababne",
            "ababababnf",
            "ababababng",
            "ababababnh",
            "ababababni",
            "ababababnj",
            "ababababnk",
            "ababababnl",
            "ababababnm",
            "ababababnn",
            "ababababno",
            "ababababnp",
            "ababababnq",
            "ababababnr",
            "ababababns",
            "ababababnt",
            "ababababnu",
            "ababababnv",
            "ababababnw",
            "ababababnx",
            "ababababny",
            "ababababnz",
            "ababababoa",
            "ababababob",
            "ababababoc",
            "ababababod",
            "ababababoe",
            "ababababof",
            "ababababog",
            "ababababoh",
            "ababababoi",
            "ababababoj",
            "ababababok",
            "ababababol",
            "ababababom",
            "ababababon",
            "ababababoo",
            "ababababop",
            "ababababoq",
            "ababababor",
            "ababababos",
            "ababababot",
            "ababababou",
            "ababababov",
            "ababababow",
            "ababababox",
            "ababababoy",
            "ababababoz",
            "ababababpa",
            "ababababpb",
            "ababababpc",
            "ababababpd",
            "ababababpe",
            "ababababpf",
            "ababababpg",
            "ababababph",
            "ababababpi",
            "ababababpj",
            "ababababpk",
            "ababababpl",
            "ababababpm",
            "ababababpn",
            "ababababpo",
            "ababababpp",
            "ababababpq",
            "ababababpr",
            "ababababps",
            "ababababpt",
            "ababababpu",
            "ababababpv",
            "ababababpw",
            "ababababpx",
            "ababababpy",
            "ababababpz",
            "ababababqa",
            "ababababqb",
            "ababababqc",
            "ababababqd",
            "ababababqe",
            "ababababqf",
            "ababababqg",
            "ababababqh",
            "ababababqi",
            "ababababqj",
            "ababababqk",
            "ababababql",
            "ababababqm",
            "ababababqn",
            "ababababqo",
            "ababababqp",
            "ababababqq",
            "ababababqr",
            "ababababqs",
            "ababababqt",
            "ababababqu",
            "ababababqv",
            "ababababqw",
            "ababababqx",
            "ababababqy",
            "ababababqz",
            "ababababra",
            "ababababrb",
            "ababababrc",
            "ababababrd",
            "ababababre",
            "ababababrf",
            "ababababrg",
            "ababababrh",
            "ababababri",
            "ababababrj",
            "ababababrk",
            "ababababrl",
            "ababababrm",
            "ababababrn",
            "ababababro",
            "ababababrp",
            "ababababrq",
            "ababababrr",
            "ababababrs",
            "ababababrt",
            "ababababru",
            "ababababrv",
            "ababababrw",
            "ababababrx",
            "ababababry",
            "ababababrz",
            "ababababsa",
            "ababababsb",
            "ababababsc",
            "ababababsd",
            "ababababse",
            "ababababsf",
            "ababababsg",
            "ababababsh",
            "ababababsi",
            "ababababsj",
            "ababababsk",
            "ababababsl",
            "ababababsm",
            "ababababsn",
            "ababababso",
            "ababababsp",
            "ababababsq",
            "ababababsr",
            "ababababss",
            "ababababst",
            "ababababsu",
            "ababababsv",
            "ababababsw",
            "ababababsx",
            "ababababsy",
            "ababababsz",
            "ababababta",
            "ababababtb",
            "ababababtc",
            "ababababtd",
            "ababababte",
            "ababababtf",
            "ababababtg",
            "ababababth",
            "ababababti",
            "ababababtj",
            "ababababtk",
            "ababababtl",
            "ababababtm",
            "ababababtn",
            "ababababto",
            "ababababtp",
            "ababababtq",
            "ababababtr",
            "ababababts",
            "ababababtt",
            "ababababtu",
            "ababababtv",
            "ababababtw",
            "ababababtx",
            "ababababty",
            "ababababtz",
            "ababababua",
            "ababababub",
            "ababababuc",
            "ababababud",
            "ababababue",
            "ababababuf",
            "ababababug",
            "ababababuh",
            "ababababui",
            "ababababuj",
            "ababababuk",
            "ababababul",
            "ababababum",
            "ababababun",
            "ababababuo",
            "ababababup",
            "ababababuq",
            "ababababur",
            "ababababus",
            "ababababut",
            "ababababuu",
            "ababababuv",
            "ababababuw",
            "ababababux",
            "ababababuy",
            "ababababuz",
            "ababababva",
            "ababababvb",
            "ababababvc",
            "ababababvd",
            "ababababve",
            "ababababvf",
            "ababababvg",
            "ababababvh",
            "ababababvi",
            "ababababvj",
            "ababababvk",
            "ababababvl",
            "ababababvm",
            "ababababvn",
            "ababababvo",
            "ababababvp",
            "ababababvq",
            "ababababvr",
            "ababababvs",
            "ababababvt",
            "ababababvu",
            "ababababvv",
            "ababababvw",
            "ababababvx",
            "ababababvy",
            "ababababvz",
            "ababababwa",
            "ababababwb",
            "ababababwc",
            "ababababwd",
            "ababababwe",
            "ababababwf",
            "ababababwg",
            "ababababwh",
            "ababababwi",
            "ababababwj",
            "ababababwk",
            "ababababwl",
            "ababababwm",
            "ababababwn",
            "ababababwo",
            "ababababwp",
            "ababababwq",
            "ababababwr",
            "ababababws",
            "ababababwt",
            "ababababwu",
            "ababababwv",
            "ababababww",
            "ababababwx",
            "ababababwy",
            "ababababwz",
            "ababababxa",
            "ababababxb",
            "ababababxc",
            "ababababxd",
            "ababababxe",
            "ababababxf",
            "ababababxg",
            "ababababxh",
            "ababababxi",
            "ababababxj",
            "ababababxk",
            "ababababxl",
            "ababababxm",
            "ababababxn",
            "ababababxo",
            "ababababxp",
            "ababababxq",
            "ababababxr",
            "ababababxs",
            "ababababxt",
            "ababababxu",
            "ababababxv",
            "ababababxw",
            "ababababxx",
            "ababababxy",
            "ababababxz",
            "ababababya",
            "ababababyb",
            "ababababyc",
            "ababababyd",
            "ababababye",
            "ababababyf",
            "ababababyg",
            "ababababyh",
            "ababababyi",
            "ababababyj",
            "ababababyk",
            "ababababyl",
            "ababababym",
            "ababababyn",
            "ababababyo",
            "ababababyp",
            "ababababyq",
            "ababababyr",
            "ababababys",
            "ababababyt",
            "ababababyu",
            "ababababyv",
            "ababababyw",
            "ababababyx",
            "ababababyy",
            "ababababyz",
            "ababababza",
            "ababababzb",
            "ababababzc",
            "ababababzd",
            "ababababze",
            "ababababzf",
            "ababababzg",
            "ababababzh",
            "ababababzi",
            "ababababzj",
            "ababababzk",
            "ababababzl",
            "ababababzm",
            "ababababzn",
            "ababababzo",
            "ababababzp",
            "ababababzq",
            "ababababzr",
            "ababababzs",
            "ababababzt",
            "ababababzu",
            "ababababzv",
            "ababababzw",
            "ababababzx",
            "ababababzy",
            "ababababzz",
        ],
    )
)